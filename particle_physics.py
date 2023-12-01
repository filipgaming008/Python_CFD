# imports
from turtle import position
import pygame, math
from vector_operations import vector_operation as VOp

# constants
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

        new_particle_attributes = particles_attributes

        # Delta_T
        Delta_T = [Delta_T, Delta_T]


        # collisions update
        def collisions(particles_attributes):
            for particle in particles_attributes:
                
                target_particle_position = [float(particles_attributes[particle]["position_x"]), float(particles_attributes[particle]["position_y"])]

                G = 66.7408

                direction = VOp.sub(target_particle_position, self.position)

                direction = VOp.cart2pol(direction)

                distance = direction[0]

                if (self.position != target_particle_position) and (distance > 8):

                    # print("Dist ", distance)

                    acceleration = G / (distance * distance)

                    # print("Accel ", acceleration)

                    direction = [acceleration, direction[1]]

                    direction = VOp.pol2cart(direction)

                    self.acceleration = VOp.add(direction, self.acceleration)


            return(new_particle_attributes)             


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
        # gravity()
        friction()
        wall_bounce()
        new_particle_attributes = collisions(particles_attributes)


        # position update of particle
        self.velocity = VOp.sub(self.velocity, VOp.mult(self.acceleration, Delta_T))
        self.position = VOp.add(self.position, VOp.mult(self.velocity, Delta_T))
        self.acceleration = [0, 0]

        new_particle_attributes.update({f"{self.particle_name}" : {
            "position_x" : f"{self.position[0]}",
            "position_y" : f"{self.position[1]}",
            "mass" : f"{self.mass[0]}"
        }})

        return(new_particle_attributes)

    # display update
    def update_screen(self, screen, particle_color):
        pygame.draw.circle(screen, particle_color, self.position, 2, 0)