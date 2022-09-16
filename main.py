import random, pygame
import particle_physics as pp
from pygame import time
from particle_physics import *



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (125, 125, 125)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

Delta_T = 100
particles_list = []
particles_attributes = {}
j = 1

for i in range(1, 3001):
    random_pos_x, random_pos_y, random_velocity_x, random_velocity_y = random.randint(100, 1400), random.randint(100, 650), random.random(), random.random()
    velocity_negator_x, velocity_negator_y = random.randint(-1, 1), random.randint(-1, 1)
    if velocity_negator_x == -1:
        random_velocity_x = -(random_velocity_x)
    if velocity_negator_y == -1:
        random_velocity_y = -(random_velocity_y)
    random_mass = random.randint(1, 10)

    particle_name = "particle_{}".format(i)

    particles_attributes.update({f"{particle_name}" : {
    "position_x" : f"{random_pos_x}",
    "position_y" : f"{random_pos_y}",
    "velocity_x" : f"{random_velocity_x}",
    "velocity_y" : f"{random_velocity_y}"
}})

    particles_def = particle_phyisics(particle_name, random_pos_x, random_pos_y, random_velocity_x, random_velocity_y, mass = random_mass)
    particles_list.append(particles_def)

    j += 1


pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Arial", 18)


def fps_counter():
    fps = str(round(float(clock.get_fps()), 2))
    fps_text = font.render(fps, 1, pygame.Color("green"))
    return fps_text

def particle_count():
    particle_num = str(len(particles_list))
    particle_num_text = font.render(particle_num, 1, pygame.Color("blue"))
    return particle_num_text
 
# Set the width and height of the screen [width, height]
size = (1500, 750)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Particle Physics")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here'

        mouse_presses = pygame.mouse.get_pressed()
 
        if mouse_presses[2]:
            mouse_position = pygame.mouse.get_pos()
            random_velocity_x, random_velocity_y = random.random(), random.random()
            velocity_negator_x, velocity_negator_y = random.randint(-1, 1), random.randint(-1, 1)
            if velocity_negator_x == -1:
                random_velocity_x = -(random_velocity_x)
            if velocity_negator_y == -1:
                random_velocity_y = -(random_velocity_y)

            random_mass = random.randint(1, 10)
            
            random_pos_x = mouse_position[0]
            random_pos_y = mouse_position[1]


            particle_name = "particle_{}".format(j)

            particles_attributes.update({f"{particle_name}" : {
            "position_x" : f"{random_pos_x}",
            "position_y" : f"{random_pos_y}",
            "velocity_x" : f"{random_velocity_x}",
            "velocity_y" : f"{random_velocity_y}"
        }})

            particles_def = particle_phyisics(particle_name, random_pos_x, random_pos_y, random_velocity_x, random_velocity_y, mass = random_mass)
            particles_list.append(particles_def)

            j += 1


    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY)
 
    # --- Drawing code should go here
 


    fps =  float(clock.get_fps())
    if fps == 0:
        fps = 60
    time_factor = Delta_T / fps

    for particle in particles_list:
        particle.update_physics(time_factor, particles_attributes)
        particle.update_screen(screen, BLACK)

    screen.blit(fps_counter(), (10, 0))
    screen.blit(particle_count(), (10, 20))

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()