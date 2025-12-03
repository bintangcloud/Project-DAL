from repositories.pelanggan_rep import pelanggan_rep
repo = pelanggan_rep()

repo.create("P001", "Bintang", "081234")
print(repo.get_all())
