import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 120

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class Car:
    def __init__(self, x, y):
        """
        🚗 CAR CLASS - Our main character!
        
        What we're learning:
        - Basic physics simulation
        - Object-oriented programming
        - Game coordinates and movement
        """
        # Position
        self.x = x
        self.y = y
        
        # Movement properties
        self.angle = 0          # Which direction car faces (0 = right, 90 = down)
        self.speed = 0          # Current speed
        self.max_speed = 20      # Top speed limit
        
        # Physics constants (experiment with these!)
        self.acceleration = 0.3  # How quickly car speeds up
        self.deceleration = 0.3     # How quickly car slows down
        self.turn_speed = 3         # How fast car turns
        
        # Car size
        self.width = 20
        self.height = 12
        
        # Status
        self.crashed = True
        
    def update(self, keys_pressed):
        """
        🔄 UPDATE CAR PHYSICS
        
        This is where the magic happens! We simulate realistic car movement.
        Key concepts:
        - Acceleration and deceleration
        - Turning only when moving (like real cars)
        - Converting angle to movement using trigonometry
        """
        
        # STEP 1: Handle speed changes
        if keys_pressed[pygame.K_UP]:
            # Accelerate (but don't exceed max speed)
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys_pressed[pygame.K_DOWN]:
            # Brake/reverse
            self.speed = max(self.speed - self.deceleration, 0)
        else:
            # Natural slowdown when no input (friction)
            self.speed = max(self.speed - self.deceleration * 0.5, 0)
            
        # STEP 2: Handle turning (only when moving!)
        if self.speed > 0:
            if keys_pressed[pygame.K_LEFT]:
                self.angle -= self.turn_speed
            elif keys_pressed[pygame.K_RIGHT]:
                self.angle += self.turn_speed
                
        # STEP 3: Convert angle and speed to actual movement
        # This is TRIGONOMETRY in action!
        # cos(angle) = how much to move in X direction
        # sin(angle) = how much to move in Y direction
        move_x = math.cos(math.radians(self.angle)) * self.speed
        move_y = math.sin(math.radians(self.angle)) * self.speed
        
        # Update position
        self.x += move_x
        self.y += move_y
        
        # Keep car on screen (simple boundary)
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))
        
    def get_corners(self):
        """
        📐 CALCULATE CAR CORNERS
        
        Why do we need this?
        - Cars are rectangles, not just points
        - We need corners for drawing and collision detection
        - We need to ROTATE the rectangle based on car angle
        
        This is ROTATION MATHEMATICS!
        """
        corners = []
        half_width = self.width // 2
        half_height = self.height // 2
        
        # Define the 4 corners relative to car center
        local_corners = [
            (-half_width, -half_height),  # Top-left
            (half_width, -half_height),   # Top-right
            (half_width, half_height),    # Bottom-right
            (-half_width, half_height)    # Bottom-left
        ]
        
        # Rotate each corner around car center
        for local_x, local_y in local_corners:
            # Rotation formula (rotation matrix):
            # new_x = old_x * cos(angle) - old_y * sin(angle)
            # new_y = old_x * sin(angle) + old_y * cos(angle)
            
            cos_angle = math.cos(math.radians(self.angle))
            sin_angle = math.sin(math.radians(self.angle))
            
            # Apply rotation
            rotated_x = local_x * cos_angle - local_y * sin_angle
            rotated_y = local_x * sin_angle + local_y * cos_angle
            
            # Convert to world coordinates
            world_x = self.x + rotated_x
            world_y = self.y + rotated_y
            
            corners.append((world_x, world_y))
            
        return corners
        
    def draw(self, screen):
        """
        🎨 DRAW THE CAR
        
        We draw the car as a polygon (4-sided shape) using its corners
        """
        corners = self.get_corners()
        color = RED if self.crashed else BLUE
        
        # Draw car body
        pygame.draw.polygon(screen, color, corners)
        
        # Draw car center point (helpful for debugging)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 3)
        
        # Draw direction indicator (small line showing where car faces)
        end_x = self.x + math.cos(math.radians(self.angle)) * 15
        end_y = self.y + math.sin(math.radians(self.angle)) * 15
        pygame.draw.line(screen, WHITE, (self.x, self.y), (end_x, end_y), 2)

class Track:
    def __init__(self):
        """
        🏁 TRACK CLASS - The driving environment
        
        What we're learning:
        - Environment design
        - Simple collision detection setup
        - Creating interesting layouts
        """
        self.walls = []
        self.create_simple_track()
        
    def create_simple_track(self):
        """
        🛠️ CREATE A SIMPLE TRACK
        
        Each wall is defined as (x1, y1, x2, y2) - a rectangle
        Try modifying these to create different track layouts!
        """
        
        # Outer boundary walls
        self.walls.extend([
            (50, 50, 850, 50),    # Top wall
            (50, 650, 850, 650),  # Bottom wall
            (50, 50, 50, 650),    # Left wall
            (850, 50, 850, 650)   # Right wall
        ])
        
        # Inner track walls (creates a driving corridor)
        self.walls.extend([
            (150, 150, 750, 150),  # Inner top wall
            (150, 550, 750, 550),  # Inner bottom wall
            (150, 150, 150, 550),  # Inner left wall
            (750, 150, 750, 550)   # Inner right wall
        ])
        
        # Add some obstacles to make it interesting
        self.walls.extend([
            (250, 250, 270, 350),  # Obstacle 1
            (450, 200, 470, 300),  # Obstacle 2
            (650, 300, 670, 400)   # Obstacle 3
        ])
        
    def draw(self, screen):
        """
        🎨 DRAW THE TRACK
        
        Draw all walls as black rectangles
        """
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            width = x2 - x1
            height = y2 - y1
            pygame.draw.rect(screen, BLACK, (x1, y1, width, height))

class Game:
    def __init__(self):
        """
        🎮 GAME CLASS - Manages everything
        
        What we're learning:
        - Game loop structure
        - Event handling
        - Organizing code into classes
        """
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Part 1: Car Physics and Control")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Create our game objects
        self.car = Car(100, 100)  # Start car at position (100, 100)
        self.track = Track()
        
        # Font for displaying information
        self.font = pygame.font.Font(None, 28)
        
    def handle_events(self):
        """
        ⌨️ HANDLE KEYBOARD AND WINDOW EVENTS
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    # Reset car to starting position
                    self.car = Car(100, 100)
                    print("Car reset!")
                    
    def draw_info(self):
        """
        📊 DRAW USEFUL INFORMATION ON SCREEN
        """
        info_lines = [
            "🚗 CAR PHYSICS DEMO",
            "",
            "Controls:",
            "↑ = Accelerate",
            "↓ = Brake",
            "← → = Turn (only when moving!)",
            "R = Reset car",
            "ESC = Exit",
            "",
            "Car Info:",
            f"Position: ({self.car.x:.0f}, {self.car.y:.0f})",
            f"Speed: {self.car.speed:.2f}",
            f"Angle: {self.car.angle:.0f}°",
            "",
            "🔧 Try This:",
            "- Notice how you can only turn when moving",
            "- Watch the white line show car direction",
            "- Try different speeds and turning",
            "- Car has momentum - doesn't stop instantly!"
        ]
        
        for i, line in enumerate(info_lines):
            if line:  # Skip empty lines
                surface = self.font.render(line, True, BLACK)
                self.screen.blit(surface, (10, 10 + i * 25))
                
    def run(self):
        """
        🔄 MAIN GAME LOOP
        
        This is the heart of any game:
        1. Handle input
        2. Update game state
        3. Draw everything
        4. Repeat!
        """
        print("🚗 Part 1: Car Physics and Control")
        print("Use arrow keys to drive around!")
        print("Notice the realistic car physics - momentum, turning, etc.")
        print("Press R to reset, ESC to exit")
        
        while self.running:
            # 1. Handle input
            self.handle_events()
            
            # 2. Update game state
            keys_pressed = pygame.key.get_pressed()
            self.car.update(keys_pressed)
            
            # 3. Draw everything
            self.screen.fill(WHITE)          # Clear screen
            self.track.draw(self.screen)     # Draw track
            self.car.draw(self.screen)       # Draw car
            self.draw_info()                 # Draw UI
            
            pygame.display.flip()            # Show everything
            self.clock.tick(FPS)            # Control frame rate
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()