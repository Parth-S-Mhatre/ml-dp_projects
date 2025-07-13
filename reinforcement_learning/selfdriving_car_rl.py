import pygame
import numpy as np
import math
import random
from collections import deque
import pickle

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 5
        self.acceleration = 0.2
        self.deceleration = 0.1
        self.turn_speed = 3
        self.width = 20
        self.height = 12
        self.crashed = False
        self.distance_traveled = 0
        self.last_x = x
        self.last_y = y
        self.sensors = []
        self.sensor_distances = []
        
    def update(self, action):
        if self.crashed:
            return
            
        # Actions: 0=nothing, 1=accelerate, 2=brake, 3=turn left, 4=turn right
        # 5=accel+left, 6=accel+right, 7=brake+left, 8=brake+right
        
        # Handle acceleration/braking
        if action in [1, 5, 6]:  # Accelerate
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif action in [2, 7, 8]:  # Brake
            self.speed = max(self.speed - self.deceleration, 0)
        else:  # Natural deceleration
            self.speed = max(self.speed - self.deceleration * 0.5, 0)
            
        # Handle turning
        if action in [3, 5, 7]:  # Turn left
            if self.speed > 0:
                self.angle -= self.turn_speed
        elif action in [4, 6, 8]:  # Turn right
            if self.speed > 0:
                self.angle += self.turn_speed
                
        # Update position
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed
        
        # Calculate distance traveled
        dx = self.x - self.last_x
        dy = self.y - self.last_y
        self.distance_traveled += math.sqrt(dx*dx + dy*dy)
        self.last_x, self.last_y = self.x, self.y
        
    def get_sensor_data(self, track):
        """Get distance readings from 8 sensors around the car"""
        self.sensor_distances = []
        self.sensors = []
        
        # 8 sensors at different angles
        sensor_angles = [-90, -45, 0, 45, 90, 135, 180, -135]
        sensor_range = 100
        
        for angle_offset in sensor_angles:
            sensor_angle = math.radians(self.angle + angle_offset)
            
            # Cast ray from car center
            for distance in range(1, sensor_range):
                sensor_x = self.x + math.cos(sensor_angle) * distance
                sensor_y = self.y + math.sin(sensor_angle) * distance
                
                # Check if sensor hit track boundary
                if (sensor_x < 0 or sensor_x >= SCREEN_WIDTH or 
                    sensor_y < 0 or sensor_y >= SCREEN_HEIGHT or
                    track.check_collision(sensor_x, sensor_y)):
                    self.sensor_distances.append(distance / sensor_range)  # Normalize
                    self.sensors.append((sensor_x, sensor_y))
                    break
            else:
                # No collision found within range
                self.sensor_distances.append(1.0)
                self.sensors.append((
                    self.x + math.cos(sensor_angle) * sensor_range,
                    self.y + math.sin(sensor_angle) * sensor_range
                ))
        
        return self.sensor_distances + [self.speed / self.max_speed]  # Add speed as input
        
    def check_collision(self, track):
        """Check if car collided with track boundaries"""
        corners = self.get_corners()
        for corner in corners:
            if track.check_collision(corner[0], corner[1]):
                self.crashed = True
                return True
        return False
        
    def get_corners(self):
        """Get the four corners of the car for collision detection"""
        corners = []
        half_width = self.width // 2
        half_height = self.height // 2
        
        # Calculate corners relative to center
        local_corners = [
            (-half_width, -half_height),
            (half_width, -half_height),
            (half_width, half_height),
            (-half_width, half_height)
        ]
        
        # Rotate and translate corners
        for lx, ly in local_corners:
            # Rotate
            cos_a = math.cos(math.radians(self.angle))
            sin_a = math.sin(math.radians(self.angle))
            rx = lx * cos_a - ly * sin_a
            ry = lx * sin_a + ly * cos_a
            
            # Translate
            corners.append((self.x + rx, self.y + ry))
            
        return corners
        
    def draw(self, screen):
        """Draw the car"""
        corners = self.get_corners()
        color = RED if self.crashed else BLUE
        pygame.draw.polygon(screen, color, corners)
        
        # Draw sensors
        for sensor in self.sensors:
            pygame.draw.line(screen, GREEN, (self.x, self.y), sensor, 1)
            pygame.draw.circle(screen, GREEN, (int(sensor[0]), int(sensor[1])), 2)

class Track:
    def __init__(self):
        self.walls = []
        self.checkpoints = []
        self.create_simple_track()
        
    def create_simple_track(self):
        """Create a simple oval track with obstacles"""
        # Outer walls
        self.walls.extend([
            # Top wall
            (100, 100, 800, 100),
            # Bottom wall
            (100, 600, 800, 600),
            # Left wall
            (100, 100, 100, 600),
            # Right wall
            (800, 100, 800, 600)
        ])
        
        # Inner walls (creating a track)
        self.walls.extend([
            # Inner top wall
            (200, 200, 700, 200),
            # Inner bottom wall
            (200, 500, 700, 500),
            # Inner left wall
            (200, 200, 200, 500),
            # Inner right wall
            (700, 200, 700, 500)
        ])
        
        # Add some obstacles
        self.walls.extend([
            # Obstacles
            (300, 300, 320, 400),
            (500, 250, 520, 350),
            (600, 350, 620, 450)
        ])
        
        # Create checkpoints for reward calculation
        self.checkpoints = [
            (150, 150, 30),  # (x, y, radius)
            (450, 150, 30),
            (750, 150, 30),
            (750, 450, 30),
            (450, 450, 30),
            (150, 450, 30)
        ]
        
    def check_collision(self, x, y):
        """Check if point (x, y) collides with any wall"""
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            # Check if point is inside rectangle
            if (min(x1, x2) <= x <= max(x1, x2) and 
                min(y1, y2) <= y <= max(y1, y2)):
                return True
        return False
        
    def draw(self, screen):
        """Draw the track"""
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, BLACK, 
                           (wall[0], wall[1], wall[2]-wall[0], wall[3]-wall[1]))
        
        # Draw checkpoints
        for i, checkpoint in enumerate(self.checkpoints):
            color = YELLOW if i == 0 else PURPLE
            pygame.draw.circle(screen, color, (checkpoint[0], checkpoint[1]), checkpoint[2], 2)

class SimpleQLearningAgent:
    def __init__(self, state_size=9, action_size=9, learning_rate=0.1, 
                 epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = {}
        self.memory = deque(maxlen=2000)
        
    def get_state_key(self, state):
        """Convert continuous state to discrete key for Q-table"""
        # Discretize sensor readings and speed
        discrete_state = []
        for i in range(len(state)):
            if i < 8:  # Sensor readings
                discrete_state.append(int(state[i] * 5))  # 0-5 bins
            else:  # Speed
                discrete_state.append(int(state[i] * 3))  # 0-3 bins
        return tuple(discrete_state)
        
    def act(self, state):
        """Choose action using epsilon-greedy policy"""
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        
        state_key = self.get_state_key(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(self.action_size)
        
        return np.argmax(self.q_table[state_key])
        
    def remember(self, state, action, reward, next_state, done):
        """Store experience in memory"""
        self.memory.append((state, action, reward, next_state, done))
        
    def replay(self, batch_size=32):
        """Train the agent using Q-learning"""
        if len(self.memory) < batch_size:
            return
            
        batch = random.sample(self.memory, batch_size)
        
        for state, action, reward, next_state, done in batch:
            state_key = self.get_state_key(state)
            next_state_key = self.get_state_key(next_state)
            
            if state_key not in self.q_table:
                self.q_table[state_key] = np.zeros(self.action_size)
            if next_state_key not in self.q_table:
                self.q_table[next_state_key] = np.zeros(self.action_size)
                
            target = reward
            if not done:
                target += 0.95 * np.max(self.q_table[next_state_key])
                
            self.q_table[state_key][action] += self.learning_rate * (
                target - self.q_table[state_key][action]
            )
            
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
            
    def save_model(self, filename):
        """Save the Q-table"""
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)
            
    def load_model(self, filename):
        """Load the Q-table"""
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
        except FileNotFoundError:
            print(f"Model file {filename} not found. Starting with empty Q-table.")

class SelfDrivingCarRL:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Self-Driving Car - Reinforcement Learning")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize components
        self.track = Track()
        self.car = Car(150, 150)
        self.agent = SimpleQLearningAgent()
        
        # Training parameters
        self.episode = 0
        self.episode_reward = 0
        self.episode_steps = 0
        self.max_steps = 1000
        self.last_checkpoint = -1
        
        # UI
        self.font = pygame.font.Font(None, 36)
        self.training_mode = True
        self.show_sensors = True
        
    def calculate_reward(self):
        """Calculate reward based on car's performance"""
        reward = 0
        
        # Penalty for crashing
        if self.car.crashed:
            return -100
            
        # Small reward for staying alive
        reward += 0.1
        
        # Reward for forward movement
        reward += self.car.speed * 0.1
        
        # Check checkpoint rewards
        for i, checkpoint in enumerate(self.track.checkpoints):
            cx, cy, radius = checkpoint
            distance = math.sqrt((self.car.x - cx)**2 + (self.car.y - cy)**2)
            
            if distance < radius:
                if i == (self.last_checkpoint + 1) % len(self.track.checkpoints):
                    reward += 50  # Big reward for reaching next checkpoint
                    self.last_checkpoint = i
                    
        # Penalty for going too slow
        if self.car.speed < 1:
            reward -= 0.5
            
        return reward
        
    def reset_episode(self):
        """Reset for new episode"""
        self.car = Car(150, 150)
        self.episode += 1
        self.episode_reward = 0
        self.episode_steps = 0
        self.last_checkpoint = -1
        
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.training_mode = not self.training_mode
                elif event.key == pygame.K_s:
                    self.show_sensors = not self.show_sensors
                elif event.key == pygame.K_r:
                    self.reset_episode()
                elif event.key == pygame.K_RETURN:
                    self.agent.save_model("car_model.pkl")
                    print("Model saved!")
                elif event.key == pygame.K_l:
                    self.agent.load_model("car_model.pkl")
                    print("Model loaded!")
                    
    def draw_ui(self):
        """Draw user interface"""
        info_texts = [
            f"Episode: {self.episode}",
            f"Reward: {self.episode_reward:.1f}",
            f"Steps: {self.episode_steps}",
            f"Epsilon: {self.agent.epsilon:.3f}",
            f"Speed: {self.car.speed:.1f}",
            f"Mode: {'Training' if self.training_mode else 'Testing'}",
            "",
            "Controls:",
            "SPACE - Toggle Training/Testing",
            "S - Toggle Sensors",
            "R - Reset Episode",
            "ENTER - Save Model",
            "L - Load Model",
            "ESC - Exit"
        ]
        
        for i, text in enumerate(info_texts):
            if text:
                color = WHITE if i < 6 else GRAY
                surface = self.font.render(text, True, color)
                self.screen.blit(surface, (10, 10 + i * 25))
                
    def run(self):
        """Main game loop"""
        print("Self-Driving Car RL Training Started!")
        print("Press SPACE to toggle between training and testing modes")
        print("Press S to toggle sensor visualization")
        print("Press R to reset episode")
        print("Press ENTER to save model, L to load model")
        
        while self.running:
            self.handle_events()
            
            # Get current state
            state = self.car.get_sensor_data(self.track)
            
            # Choose action
            if self.training_mode:
                action = self.agent.act(state)
            else:
                # In testing mode, always use best action
                state_key = self.agent.get_state_key(state)
                if state_key in self.agent.q_table:
                    action = np.argmax(self.agent.q_table[state_key])
                else:
                    action = 0
            
            # Execute action
            self.car.update(action)
            
            # Check collision
            self.car.check_collision(self.track)
            
            # Calculate reward
            reward = self.calculate_reward()
            self.episode_reward += reward
            self.episode_steps += 1
            
            # Get next state
            next_state = self.car.get_sensor_data(self.track)
            
            # Check if episode is done
            done = (self.car.crashed or 
                   self.episode_steps >= self.max_steps)
            
            # Store experience and train
            if self.training_mode:
                self.agent.remember(state, action, reward, next_state, done)
                if len(self.agent.memory) > 32:
                    self.agent.replay()
            
            # Reset if episode is done
            if done:
                if self.training_mode:
                    print(f"Episode {self.episode}: Reward = {self.episode_reward:.1f}, "
                          f"Steps = {self.episode_steps}, Epsilon = {self.agent.epsilon:.3f}")
                self.reset_episode()
            
            # Draw everything
            self.screen.fill(WHITE)
            self.track.draw(self.screen)
            
            if self.show_sensors:
                self.car.draw(self.screen)
            else:
                # Draw car without sensors
                corners = self.car.get_corners()
                color = RED if self.car.crashed else BLUE
                pygame.draw.polygon(self.screen, color, corners)
            
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()

if __name__ == "__main__":
    try:
        game = SelfDrivingCarRL()
        game.run()
    except KeyboardInterrupt:
        print("\nTraining interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()