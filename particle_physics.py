# imports
import pygame
from vector_operations import vector_operation as VOp

# constants
attraction_radius = 1500
reppeling_radius = 3

attracting_strength = 1
reppeling_strength = 2

world_gravity = [0, -0.05]

world_friction = [0.0025, 0.0025]



# class def
class particle_phyisics():

    # class instantiaction
    def __init__(self, particle_name, position_x = 0, position_y = 0, velocity_x = 0, velocity_y = 0, acceleration_x = 0, acceleration_y = 0, mass = 1):

        self.particle_name = particle_name

        self.mass = [mass, mass]
        self.position = [position_x, position_y]
        self.velocity = [velocity_x, velocity_y]
        self.acceleration = [acceleration_x, acceleration_y]


    # physics update
    def update_physics(self, Delta_T, particles_attributes):


        # Delta_T
        Delta_T = [Delta_T, Delta_T]


        # collisions update
        def collisions(particles_attributes):
            pass

        # friction update
        def friction():
            friction = VOp.mult([-1, -1], VOp.mult(world_friction, self.velocity))
            self.velocity = VOp.add(self.velocity, VOp.mult(friction, Delta_T))

        # wall bounce update
        def wall_bounce():
            if not (100 < self.position[0] < 1400):
                self.velocity[0] = -(self.velocity[0])
            if not (100 < self.position[1] < 650):
                self.velocity[1] = -(self.velocity[1])
            
        # gravity update
        def gravity():

            self.acceleration = VOp.sub(self.acceleration, world_gravity)
            self.velocity = VOp.add(self.velocity, VOp.mult(self.acceleration, Delta_T))

            self.acceleration = [0, 0]
            
        
        # function calls
        wall_bounce()
        gravity()
        friction()


        # position update of particle
        self.velocity = VOp.sub(self.velocity, VOp.mult(self.acceleration, Delta_T))
        self.position = VOp.add(self.position, VOp.mult(self.velocity, Delta_T))


    # display update
    def update_screen(self, screen, particle_color):
        pygame.draw.circle(screen, particle_color, self.position, 2, 0)