-- ============================================================================
-- SIMONA — Setup Supabase (jalankan sekali di SQL Editor Supabase)
-- ============================================================================
-- Ini BUKAN skema relasional penuh (tabel per entitas). Untuk mempercepat
-- migrasi dari versi prototipe (in-memory dict) tanpa menulis ulang semua
-- logic, seluruh data (unit, periode, assessment, evidence, dst) disimpan
-- sebagai SATU baris JSONB di tabel ini. App akan otomatis load/save ke
-- tabel ini setiap ada perubahan data.
--
-- Ini cukup untuk kebutuhan sekarang (prototipe yang dipakai serius, tim
-- kecil-menengah). Kalau nanti butuh query SQL yang lebih canggih (laporan,
-- filter kompleks, dsb), bisa dimigrasikan ke skema relasional penuh
-- (lihat simona_schema.sql yang sudah pernah dibuat sebelumnya).
-- ============================================================================

create table if not exists simona_state (
  id int primary key,
  data jsonb not null,
  updated_at timestamptz not null default now()
);

-- Aktifkan Row Level Security
alter table simona_state enable row level security;

-- Kebijakan akses: karena app ini pakai login sendiri (bukan Supabase Auth)
-- dan anon key dipakai langsung dari browser, tabel ini dibuka penuh untuk
-- baca & tulis lewat anon key. Ini WAJAR untuk prototipe internal dengan
-- akses terbatas (link tidak disebar publik), tapi TIDAK cocok untuk data
-- sensitif berskala luas — untuk itu perlu Supabase Auth per-user + RLS
-- yang membatasi akses per role, seperti pada simona_schema.sql.
create policy "simona_state_allow_all"
  on simona_state
  for all
  using (true)
  with check (true);

-- Baris awal (opsional — app akan otomatis membuatnya sendiri saat pertama
-- kali dijalankan kalau baris ini belum ada, jadi INSERT ini boleh dilewati)
-- insert into simona_state (id, data) values (1, '{}'::jsonb)
-- on conflict (id) do nothing;


-- ============================================================================
-- STORAGE BUCKET UNTUK EVIDENCE (foto/PDF yang diupload unit)
-- ============================================================================
-- PENTING: evidence (foto/PDF) TIDAK disimpan sebagai teks di tabel
-- simona_state lagi (itu bikin ukuran data bengkak & app jadi berat/gampang
-- mati). Sekarang file aslinya disimpan di Supabase Storage, cuma path-nya
-- saja yang dicatat di simona_state.

insert into storage.buckets (id, name, public)
values ('evidences', 'evidences', false)
on conflict (id) do nothing;

-- Kebijakan akses bucket: dibuka untuk baca & tulis lewat anon key, sama
-- alasannya seperti simona_state (app ini pakai login sendiri, bukan
-- Supabase Auth). Untuk internal use ini wajar.
create policy "evidences_allow_all_select"
  on storage.objects for select
  using (bucket_id = 'evidences');

create policy "evidences_allow_all_insert"
  on storage.objects for insert
  with check (bucket_id = 'evidences');

create policy "evidences_allow_all_update"
  on storage.objects for update
  using (bucket_id = 'evidences');

create policy "evidences_allow_all_delete"
  on storage.objects for delete
  using (bucket_id = 'evidences');
