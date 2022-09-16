import pygame
import numpy as np

attraction_radius = 1500
reppeling_radius = 3

attracting_strength = 1
reppeling_strength = 2

world_gravity = np.array([0, -0.05])

world_friction = np.array([0.0025, 0.0025])

class particle_phyisics():
    def __init__(self, particle_name, position_x = 0, position_y = 0, velocity_x = 0, velocity_y = 0, acceleration_x = 0, acceleration_y = 0, mass = 1):

        self.particle_name = particle_name

        self.mass = np.array([mass, mass])
        self.position = np.array([position_x, position_y])
        self.velocity = np.array([velocity_x, velocity_y])
        self.acceleration = np.array([acceleration_x, acceleration_y])

    def update_physics(self, Delta_T, particles_attributes):

        Delta_T = np.array([Delta_T, Delta_T])

        def collisions(particles_attributes):
            pass

        def friction():
            friction = -1 * world_friction * self.velocity
            self.velocity = self.velocity + friction * Delta_T

        def wall_bounce():
            if not (100 < self.position[0] < 1400):
                self.velocity[0] = -(self.velocity[0])
            if not (100 < self.position[1] < 650):
                self.velocity[1] = -(self.velocity[1])
            

        def gravity():

            self.acceleration = self.acceleration - world_gravity
            self.velocity = self.velocity - self.acceleration * Delta_T

            self.acceleration = np.array([0, 0])
            
        
        
        wall_bounce()
        gravity()
        friction()

        self.velocity = self.velocity - self.acceleration * Delta_T
        self.position = self.position - self.velocity * Delta_T

    def update_screen(self, screen, particle_color):
        pygame.draw.circle(screen, particle_color, self.position, 2, 0)