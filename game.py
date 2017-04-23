import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 14)
text_colour = (255, 255, 255)

rooms = {
    "Room 1": {
        'description': "Room 1 description",
        'image': pygame.image.load("image1.png"),
        'paths': {"west": "Room 2"}
    },
    "Room 2": {
        'description': "Room 2 description",
        'image': pygame.image.load("image2.png"),
        'paths': {"east": "Room 1"}
    }
}

room_name = "Room 1"
done = False
clock = pygame.time.Clock()

while not done:

    # Clear the screen
    screen.fill((0, 0, 0))

    room = rooms[room_name]

    screen.blit(room['image'], (20, 20))
    text = "You are in {}. {}.".format(room_name, room['description'])
    textsurface = myfont.render(text, False, text_colour)
    screen.blit(textsurface, (20, 300))

    # Create a list of options
    options = []
    for p in room['paths']:
        options.append('Go {}'.format(p))
    options.append('Quit')

    # Display the options on screen
    text_areas = []
    x_pos, y_pos = (20, 320)
    for i, option in enumerate(options):
        ts = myfont.render(option, False, text_colour)
        text_areas.append(screen.blit(ts, (x_pos, y_pos)))
        x_pos += text_areas[-1].width + 10

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # get a list of objects that are under the mouse cursor
            clicked_objects = [r for r in text_areas if r.collidepoint(pos)]

            if len(clicked_objects) > 0:
                selected_option = options[text_areas.index(clicked_objects[0])]
                if selected_option == 'Quit':
                    done = True
                elif selected_option.startswith('Go '):
                    room_name = room['paths'][selected_option[3:]]
                print selected_option

    # Update the screen
    clock.tick()
    pygame.display.flip()