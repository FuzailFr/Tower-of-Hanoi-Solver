def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> None:
    """
    Menyelesaikan masalah Tower of Hanoi secara rekursif.
    
    Args:
        n: Jumlah disk
        source: Tiang asal (Start)
        destination: Tiang tujuan (Finish)
        auxiliary: Tiang bantu
    """
    if n == 1:
        print(f"Pindahkan disk 1 dari tiang {source} ke tiang {destination}")
        return
    
    # Pindahkan n-1 disk dari source ke auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Pindahkan disk terbesar dari source ke destination
    print(f"Pindahkan disk {n} dari tiang {source} ke tiang {destination}")
    
    # Pindahkan n-1 disk dari auxiliary ke destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

if __name__ == "__main__":
    # Berdasarkan referensi image_e60164.png, terdapat 3 disk pada start state di tiang A.
    total_disks = 3
    print(f"Langkah penyelesaian Tower of Hanoi untuk {total_disks} disk:\n")
    tower_of_hanoi(total_disks, 'A', 'C', 'B')
