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
decoded = np.transpose(scrambled_square)  # transpose
decoded = decoded[::-1, ::-1]             # reverse both rows and columns

# Rotate the image by 180 degrees
decoded = np.rot90(decoded, 2)  # rotate by 180 degrees

# Display the final image
plt.imshow(decoded, cmap='gray')  # use 'gray' instead of 'grey'
plt.title("Decoded Hidden Image (Fixed Orientation)")
plt.axis('off')
plt.show()



