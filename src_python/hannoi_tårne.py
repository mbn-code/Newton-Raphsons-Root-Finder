import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    disks = [plt.Rectangle((0, 0), 0.5, 0.1, edgecolor='black', facecolor='white') for _ in range(3)]
    for i, disk in enumerate(disks):
        disk.set_xy((0.75 * i, 0))
        ax.add_patch(disk)
        ax.annotate(f'Disk {i+1}', (0.75 * i, 0), xytext=(0.75 * i, -0.5), ha='center')

    peg_heights = {'A': 0, 'B': 0, 'C': 0}

    def animate(frame):
        # Use the frame argument to determine the state of the animation
        # For example, if you're moving a disk every frame:
        disk_to_move = frame % len(disks)
        # Calculate the new position of the disk
        new_x = 0.75 * (frame // len(disks))
        new_y = 0.1 * peg_heights[chr(ord('A') + (frame // len(disks)) % 3)]
        # Move the disk
        disks[disk_to_move].set_xy((new_x, new_y))
        # Update the peg heights
        peg_heights[chr(ord('A') + (frame // len(disks)) % 3)] += 1
        peg_heights[chr(ord('A') + (disk_to_move // len(disks)) % 3)] -= 1
        def hanoi(n, source, target, auxiliary):
            if n > 0:
                hanoi(n-1, source, auxiliary, target)
                print(f"Move disk {n} from {source} to {target}")
                disks[n-1].set_xy((0.75 * (ord(target) - ord('A')), 0.1 * peg_heights[target]))
                peg_heights[target] += 1
                peg_heights[source] -= 1
                hanoi(n-1, auxiliary, target, source)

        hanoi(3, 'A', 'C', 'B')

    _ = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=False)
    plt.show()

main()