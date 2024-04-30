import matplotlib.pyplot as plt

# Dummy data for the graph
epochs = [i for i in range(1, 16)]
val_loss = [0.2810, 0.2768, 0.2673, 0.2557, 0.2401, 0.2196, 0.1943, 0.1643, 0.1303, 0.0940, 0.0579, 0.0257, 0.0020, 0.0124, 0.0014]
val_acc = [0.86, 0.91, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 0.99, 0.99, 1.00, 1.00, 1.00, 0.99]

# Plot the graph
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 8))
ax1.plot(epochs, val_loss, color='blue')
ax1.set_title('Validation Loss')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Loss')

ax2.plot(epochs, val_acc, color='green')
ax2.set_title('Validation Accuracy')
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Accuracy')

plt.tight_layout()
plt.show()
