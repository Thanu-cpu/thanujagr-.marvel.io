import numpy as np
import matplotlib.pyplot as plt

# Load the scrambled matrix
scrambled = np.load("encoded_array.npy")
print("Original Shape:", scrambled.shape)
print("Total Elements:", scrambled.size)

# Reshape into a square
size = int(np.sqrt(scrambled.size))
scrambled_square = scrambled.reshape(size, size)
print("Reshaped Shape:", scrambled_square.shape)

# Fix orientation
decoded = np.transpose(scrambled_square)   # transpose
decoded = decoded[::-1, ::-1]              # reverse both rows and columns

# Display the final image
plt.imshow(decoded, cmap='grey')
plt.title("Decoded Hidden Image")
plt.axis('off')
plt.show()
