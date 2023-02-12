import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the sound file
sound = pygame.mixer.Sound("mixkit-piano-falling-effect-408.wav")

# Play the sound
sound.play()

# Wait for the sound to finish playing
while pygame.mixer.get_busy():
    continue
