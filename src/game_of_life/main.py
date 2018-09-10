import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# TODO: Add Game of life logic.

interval = 10  # Time in milliseconds betwwen frames
dpi = 5  # Points per inch
map_size = (20, 20)

# Initial Data, Build game board
x = np.zeros(map_size)
x = x.astype(bool) # Array type

# Germs patterns
blinker = [1, 1, 1]

# populate the land with the selections
x[2, 2:5] = blinker

def go_down(X):
    """Game of life step using generator expressions"""
    return np.roll(np.roll(X, 1, 0), 1, 1)

# Build the figure.
# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xticks([])  # ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_yticks([])  # ax.set_ylim(0, 1), ax.set_yticks([])
im = ax.imshow(x, cmap=plt.cm.binary, interpolation='nearest')
# im.set_clim(-0.05, 1)   # Background color (Gray)

def init():
    initial_map = np.zeros(map_size) # Or np.zeros_like(X)
    im.set_data(initial_map)
    return im,


def update(frame):
    # Update the image before update the state
    im.set_data(update.x)
    update.x = go_down(update.x)
    if frame == 4:
      animate.event_source.stop()

    return im,
update.x = x


animate = animation.FuncAnimation(
    fig, update, init_func=init, interval=2, blit=True, frames=12, repeat=False)

# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=interval,
#                               repeat=False, init_func=init)
plt.show()