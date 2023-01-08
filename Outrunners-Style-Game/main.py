import genericpath
import math
import random
from math import floor, sqrt, cos, sin

import pygame
import pygame.freetype
import os
import datetime
import json

from pygame import Rect

''' Window settings '''
WIDTH, HEIGHT = 960, 720
BLUE = (81, 116, 240)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PJF: Project Jagged Ferrari")
PYGAME_ICON = pygame.image.load(os.path.join('Assets', 'player_car.png'))
pygame.display.set_icon(PYGAME_ICON)

''' Menu settings and images'''
CAR_SPIN_1 = pygame.image.load(os.path.join('Assets', 'car_spin_1.png'))
CAR_SPIN_2 = pygame.image.load(os.path.join('Assets', 'car_spin_2.png'))
CAR_SPIN_3 = pygame.image.load(os.path.join('Assets', 'car_spin_3.png'))
CAR_SPIN_4 = pygame.image.load(os.path.join('Assets', 'car_spin_4.png'))
CAR_SPIN_5 = pygame.image.load(os.path.join('Assets', 'car_spin_5.png'))
CAR_SPIN_6 = pygame.image.load(os.path.join('Assets', 'car_spin_6.png'))
CAR_SPIN_7 = pygame.image.load(os.path.join('Assets', 'car_spin_7.png'))
CAR_SPIN_8 = pygame.image.load(os.path.join('Assets', 'car_spin_8.png'))
CAR_SPIN_9 = pygame.image.load(os.path.join('Assets', 'car_spin_9.png'))
CAR_SPINNING = [CAR_SPIN_1, CAR_SPIN_2, CAR_SPIN_3, CAR_SPIN_4, CAR_SPIN_5, CAR_SPIN_6, CAR_SPIN_7, CAR_SPIN_8,
                CAR_SPIN_9]

''' Background image '''
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'background.jpg'))
BACKGROUND_SCALE = 0.38
BACKGROUND_IMAGE_WIDTH = BACKGROUND_IMAGE.get_width() * BACKGROUND_SCALE
BACKGROUND_IMAGE_HEIGHT = BACKGROUND_IMAGE.get_height() * BACKGROUND_SCALE
MENU_BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'menu_background.png'))
TRACK_MENU_BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'track_menu_background.png'))

''' Button images '''
start_img = pygame.image.load(os.path.join('Assets', 'start_btn.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('Assets', 'exit_btn.png')).convert_alpha()
BUTTON_PLAY_UNPRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_play_unpressed.png')).convert_alpha()
BUTTON_PLAY_PRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_play_pressed.png')).convert_alpha()
PLAY_BUTTON = [BUTTON_PLAY_UNPRESSED_IMAGE, BUTTON_PLAY_PRESSED_IMAGE]
BUTTON_QUIT_UNPRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_quit_unpressed.png')).convert_alpha()
BUTTON_QUIT_PRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_quit_pressed.png')).convert_alpha()
QUIT_BUTTON = [BUTTON_QUIT_UNPRESSED_IMAGE, BUTTON_QUIT_PRESSED_IMAGE]
BUTTON_SAVE_UNPRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_save_unpressed.png')).convert_alpha()
BUTTON_SAVE_PRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_save_pressed.png')).convert_alpha()
SAVE_BUTTON = [BUTTON_SAVE_UNPRESSED_IMAGE, BUTTON_SAVE_PRESSED_IMAGE]
BUTTON_X_UNPRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_x_unpressed.png')).convert_alpha()
BUTTON_X_PRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_x_pressed.png')).convert_alpha()
X_BUTTON = [BUTTON_X_UNPRESSED_IMAGE, BUTTON_X_PRESSED_IMAGE]
BUTTON_BACK_UNPRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_back_unpressed.png')).convert_alpha()
BUTTON_BACK_PRESSED_IMAGE = pygame.image.load(os.path.join('Assets', 'button_back_pressed.png')).convert_alpha()
BACK_BUTTON = [BUTTON_BACK_UNPRESSED_IMAGE, BUTTON_BACK_PRESSED_IMAGE]

''' Player car image '''
PLAYER_CAR_STRAIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'player_car.png'))
PLAYER_CAR_LEFT_IMAGE = pygame.image.load(os.path.join('Assets', 'player_car_left.png'))
PLAYER_CAR_RIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'player_car_right.png'))
PLAYER_CAR_DRIFT_LEFT_IMAGE = pygame.image.load(os.path.join('Assets', 'player_car_drift_left.png'))
PLAYER_CAR_DRIFT_RIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'player_car_drift_right.png'))
PLAYER_CAR_IMAGE_WIDTH = PLAYER_CAR_STRAIGHT_IMAGE.get_width()
PLAYER_CAR_IMAGE_HEIGHT = PLAYER_CAR_STRAIGHT_IMAGE.get_height()
CAR_SCALE = 2.5
PLAYER_ON_SCREEN_POSITION_X = WIDTH / 2 - (PLAYER_CAR_IMAGE_WIDTH * CAR_SCALE) / 2
PLAYER_ON_SCREEN_POSITION_Y = 550

''' Track settings '''
road_segments = []
render_distance = 300  # visible segments number
NUMBER_OF_SEGMENTS_ON_TRACK = 2500
SEGMENT_LENGTH = 200
ROAD_WIDTH = 2000
RUMBLE_LENGTH = 3
LANES = 3
COLORS = {
    'light': {'road': (120, 120, 120), 'grass': (167, 235, 108), 'rumble': (219, 13, 13), 'lane': (223, 228, 237)},
    # light rumble is red, lane is white
    'dark': {'road': (115, 115, 115), 'grass': (154, 219, 96), 'rumble': (223, 228, 237),
             'lane': (115, 115, 115)}}  # dark rumble is white, lane is road color
START_FINISH_SEGMENT_IMAGE = pygame.image.load(os.path.join('Assets', 'checkered_texture.jpg'))
START_FINISH_SEGMENT = START_FINISH_SEGMENT_IMAGE.get_rect()

VERY_HARD_TURN = 2500
HARD_TURN = 3500
MEDIUM_TURN = 5100
LIGHT_TURN = 10100
VERY_LIGHT_TURN = 20100
TURNS = [VERY_LIGHT_TURN, LIGHT_TURN, MEDIUM_TURN, HARD_TURN, VERY_HARD_TURN]

''' Camera settings '''
camera_x = 0
camera_y = 1000
distance_to_player = 700
distance_to_plane = 1 / (camera_y / distance_to_player)

''' Program settings '''
FPS = 60
dt = 1 / FPS

''' Player settings '''
MAX_SPEED = SEGMENT_LENGTH * FPS
ACCELERATION = MAX_SPEED / 10
BREAKING = -MAX_SPEED / 2
DECELERATION = -MAX_SPEED / 7
DRIFT_DECELERATION = -MAX_SPEED / 5
OFFROAD_DECELERATION = -MAX_SPEED / 2

''' Misc '''
PARTICLE_IMAGE = pygame.image.load(os.path.join('Assets', 'smoke1.png'))
GB_LOGO = pygame.image.load(os.path.join('Assets', 'grupa_badawcza_logo.png'))
MF_LOGO = pygame.image.load(os.path.join('Assets', 'munefrakt_logo.png'))

button_clicked = False


class Button:
    def __init__(self, x, y, images, scale):
        self.images = images
        self.scale = scale
        self.width = images[0].get_width()
        self.height = images[0].get_height()
        self.image = pygame.transform.scale(self.images[0], (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect(center=(x, y))
        self.active = True

    def draw(self, surface):
        global button_clicked

        action = False
        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position) and self.active:
            self.image = pygame.transform.scale(self.images[1],
                                                (int(self.width * self.scale), int(self.height * self.scale)))
            if pygame.mouse.get_pressed()[0] == 1 and not button_clicked:
                button_clicked = True
                action = True
        else:
            self.image = pygame.transform.scale(self.images[0],
                                                (int(self.width * self.scale), int(self.height * self.scale)))
            if not self.active:
                self.image.fill((79, 79, 79), special_flags=pygame.BLEND_RGB_MULT)

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class SmokeParticle:
    def __init__(self, x, y, is_dirt):
        self.x = x
        self.y = y
        self.is_dirt = is_dirt
        self.x_l_or_r = 1
        self.x_vel = 0.3 * random.choice([-1, 1])
        self.scale = 1.5
        self.alive_time = 260
        self.time_rate = 5
        self.k = 0.02 * random.random() * random.choice([-1, 1])
        self.alive = True
        self.image = pygame.transform.scale(PARTICLE_IMAGE, (
            PARTICLE_IMAGE.get_width() * self.scale, PARTICLE_IMAGE.get_height() * self.scale))

    def update_particle(self):
        self.x += self.x_vel
        self.x_vel -= self.k * self.x_l_or_r * (current_speed / MAX_SPEED)
        self.scale += 0.02
        self.alive_time -= self.time_rate
        if self.alive_time < 0:
            self.alive_time = 0
            self.alive = False
        self.time_rate -= 0.05
        if self.time_rate < 3:
            self.time_rate = 3
        self.image = pygame.transform.scale(PARTICLE_IMAGE, (
            PARTICLE_IMAGE.get_width() * self.scale, PARTICLE_IMAGE.get_height() * self.scale))

    def draw(self):
        if self.is_dirt:
            self.image.fill((102, 66, 34), special_flags=pygame.BLEND_RGB_MULT)
        WIN.blit(self.image, self.image.get_rect(center=(self.x, self.y)))


class Smoke:
    def __init__(self, x=PLAYER_ON_SCREEN_POSITION_X + 20,
                 y=PLAYER_ON_SCREEN_POSITION_Y + (PLAYER_CAR_IMAGE_HEIGHT - 3) * CAR_SCALE):
        self.x = x
        self.y = y
        self.left_particles = []
        self.right_particles = []
        self.all_particles = []
        self.frames = 0
        self.is_dirt = False

    def add_particles(self):
        if self.frames % 5 == 0:
            self.frames = 0
            self.left_particles.append(SmokeParticle(self.x, self.y, self.is_dirt))
            self.right_particles.append(
                SmokeParticle(self.x + PLAYER_CAR_IMAGE_WIDTH * CAR_SCALE - 40, self.y, self.is_dirt))
            self.all_particles = self.left_particles + self.right_particles

    def update(self):
        self.all_particles = [i for i in self.all_particles if i.alive]
        self.frames += 1
        for i in self.all_particles:
            i.update_particle()

    def draw(self):
        for i in self.all_particles:
            i.draw()


smoke = Smoke()


class Sprite:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.image = image
        self.scale = scale
        self.sprite_width = image.get_width() * self.scale
        self.sprite_height = image.get_height() * self.scale
        self.image = pygame.transform.scale(self.image, (int(self.sprite_width), int(self.sprite_height)))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        pass

    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))


# def get_last_y(index):
#     if index != 0:
#         return road_segments[index - 1]['p2']['world']['y']
#     else:
#         return road_segments[NUMBER_OF_SEGMENTS_ON_TRACK - 1]['p2']['world']['y']
#
#
# def set_hills(index, length, y_value):
#     for i in range(length):
#         if index != 0:
#             road_segments[index + i]['p2']['world']['y'] += y_value
#             road_segments[index + i]['p1']['world']['y'] = get_last_y(index + i - 1)


def create_section(number_of_segments):
    for i in range(number_of_segments):
        road_segments.append(
            {'index': i,
             'p1': {'world': {'x': 0, 'y': 0, 'z': ((i + 1) * SEGMENT_LENGTH)},
                    'camera': {},
                    'screen': {}},
             'p2': {'world': {'x': 0, 'y': 0, 'z': ((i + 2) * SEGMENT_LENGTH)},
                    'camera': {},
                    'screen': {}},
             'color': COLORS['dark'] if i % 2 != 0 else COLORS['light'],
             'radius': 0
             })

    return len(road_segments) * SEGMENT_LENGTH


def create_turn(index, length, radius):
    for i in range(length):
        road_segments[index + i]['radius'] = radius


def generate_track():
    current_segment = 0
    min_straight_length = 10
    max_straight_length = 150
    min_turn_length = 10
    max_turn_length = 300
    while current_segment < NUMBER_OF_SEGMENTS_ON_TRACK:
        if NUMBER_OF_SEGMENTS_ON_TRACK - current_segment >= max_straight_length:
            straight_length = random.randint(min_straight_length, max_straight_length)
            current_segment += straight_length
        else:
            if NUMBER_OF_SEGMENTS_ON_TRACK - current_segment >= min_straight_length:
                straight_length = random.randint(min_straight_length, NUMBER_OF_SEGMENTS_ON_TRACK - current_segment)
                current_segment += straight_length
            else:
                break
        if NUMBER_OF_SEGMENTS_ON_TRACK - current_segment >= max_turn_length:
            turn_length = random.randint(min_turn_length, max_turn_length)
            turn_radius = random.choice(TURNS) * random.choice([-1, 1])
            create_turn(current_segment, turn_length, turn_radius)
            current_segment += turn_length
        else:
            if NUMBER_OF_SEGMENTS_ON_TRACK - current_segment >= min_turn_length:
                turn_length = random.randint(min_turn_length, NUMBER_OF_SEGMENTS_ON_TRACK - current_segment)
                turn_radius = random.choice(TURNS) * random.choice([-1, 1])
                create_turn(current_segment, turn_length, turn_radius)
                current_segment += turn_length
            else:
                break


''' Returns a segment the car is currently on '''


def find_segment_by_z_value(z_value):
    return road_segments[floor(z_value / SEGMENT_LENGTH) % len(road_segments)]


def calculate_3D_view(p, camera_x, camera_y, camera_z, camera_depth):
    p['camera']['x'] = (p['world']['x'] or 0) - camera_x
    p['camera']['y'] = (p['world']['y'] or 0) - camera_y
    p['camera']['z'] = (p['world']['z'] or 0) - camera_z
    p['screen']['scale'] = camera_depth / p['camera']['z']
    p['screen']['x'] = round((WIDTH / 2) + (p['screen']['scale'] * p['camera']['x'] * WIDTH / 2))
    p['screen']['y'] = round((HEIGHT / 2) - (p['screen']['scale'] * p['camera']['y'] * HEIGHT / 2))
    p['screen']['w'] = round(p['screen']['scale'] * ROAD_WIDTH * WIDTH / 2)


def draw_polygon(x1, y1, x2, y2, x3, y3, x4, y4, color):
    pygame.draw.polygon(WIN, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])


def draw_start_finish_lane(x1, y1, x2, y2, x3, y3, x4, y4, color):
    pygame.draw.polygon(WIN, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
    img = pygame.transform.scale(START_FINISH_SEGMENT_IMAGE, (x2 - x1, y1 - y4))
    start_finish_lane = Rect(x1, y4, x2 - x1, y1 - y4)
    WIN.blit(img, start_finish_lane)
    pygame.draw.rect(WIN, 'white', start_finish_lane, 1)


def draw_segment(index, x1, y1, w1, x2, y2, w2, color):
    r1 = w1 / (2 * LANES)
    r2 = w2 / (2 * LANES)
    l1 = w1 / (8 * LANES)
    l2 = w2 / (8 * LANES)

    pygame.draw.rect(WIN, color['grass'], (0, y2, WIDTH, y1 - y2))

    if index == 3 or index == 2:
        draw_start_finish_lane(x1 - w1, y1, x1 + w1, y1, x2 + w2, y2, x2 - w2, y2, 'white')
    else:
        draw_polygon(x1 - w1, y1, x1 + w1, y1, x2 + w2, y2, x2 - w2, y2, color['road'])

    draw_polygon(x1 - w1 - r1, y1, x1 - w1, y1, x2 - w2, y2, x2 - w2 - r2, y2, color['rumble'])
    draw_polygon(x1 + w1 + r1, y1, x1 + w1, y1, x2 + w2, y2, x2 + w2 + r2, y2, color['rumble'])

    lanew1 = w1 * 2 / LANES
    lanew2 = w2 * 2 / LANES
    lanex1 = x1 - w1 + lanew1
    lanex2 = x2 - w2 + lanew2
    for lane in range(LANES - 1):
        if index != 3 and index != 2:
            draw_polygon(lanex1 - l1 / 2, y1, lanex1 + l1 / 2, y1, lanex2 + l2 / 2, y2, lanex2 - l2 / 2, y2,
                         color['lane'])
            lanex1 += lanew1
            lanex2 += lanew2


''' Setting player's position (z value) on the track '''


def increase_z_position(player_current_position, player_traveled_distance, length_of_track):
    global position
    global last_position

    player_new_position = player_current_position + player_traveled_distance
    while player_new_position >= length_of_track:
        player_new_position -= length_of_track
    while player_new_position < 0:
        player_new_position += length_of_track

    last_position = position
    position = player_new_position


''' Calculate track's x value offset on the screen'''


def calculate_curve_x_value(segment_length, radius):
    # print(f"\rY position: {y}", end=' ')
    if radius == 0:
        return 0
    x_value = round(math.fabs(radius) - sqrt(math.fabs(radius) ** 2 - segment_length ** 2))

    if radius < 0:
        return -x_value
    else:
        return x_value


def percentRemaining(j, total):
    # print(f"\rPosition: {(j % total):3.0f} / {total}", end=' ')
    return (j % total) / total


def render_track():
    global current_curve
    base_segment = find_segment_by_z_value(position)
    maxy = HEIGHT
    curve = 0
    position_on_segment = percentRemaining(position, SEGMENT_LENGTH)
    curve_value = 0
    # print(f"\rPosition X: {position_x}", end=' ')

    for i in range(render_distance):
        segment = road_segments[(base_segment['index'] + i) % len(road_segments)]
        is_road_looping = segment['index'] < base_segment['index']

        calculate_3D_view(segment['p1'], (position_x + curve_value - (curve * position_on_segment)), camera_y,
                          position - (track_length if is_road_looping else 0), distance_to_plane)

        curve += calculate_curve_x_value(SEGMENT_LENGTH, segment['radius'])
        if i == 0:
            current_curve = curve
        curve_value += curve

        calculate_3D_view(segment['p2'], (position_x + curve_value - (curve * position_on_segment)), camera_y,
                          position - (track_length if is_road_looping else 0), distance_to_plane)

        if (segment['p1']['camera']['z'] <= distance_to_plane) or (segment['p2']['screen']['y'] >= maxy):
            continue

        draw_segment(segment['index'],
                     segment['p1']['screen']['x'],
                     segment['p1']['screen']['y'],
                     segment['p1']['screen']['w'],
                     segment['p2']['screen']['x'],
                     segment['p2']['screen']['y'],
                     segment['p2']['screen']['w'],
                     segment['color'])

        maxy = segment['p2']['screen']['y']


''' Controlling player's speed, current z and x position and car animations '''


def car_steering():
    global current_speed
    global position_x
    global current_car_orientation

    base_segment = find_segment_by_z_value(position)
    keys = pygame.key.get_pressed()
    drift_multiplayer = 1
    current_car_orientation = PLAYER_CAR_STRAIGHT_IMAGE
    smoke.is_dirt = False

    if position_x < -ROAD_WIDTH or position_x > ROAD_WIDTH:
        smoke.is_dirt = True
        if current_speed > MAX_SPEED / 3:
            current_speed += OFFROAD_DECELERATION * dt
            smoke.add_particles()
            smoke.update()
            smoke.draw()

    if keys[pygame.K_SPACE] and current_speed > MAX_SPEED / 2:
        drift_multiplayer = 1.7
        smoke.add_particles()
        smoke.update()
        smoke.draw()
        current_speed += DRIFT_DECELERATION * dt

    if keys[pygame.K_LEFT] and position_x > -ROAD_WIDTH * 2:
        position_x -= dt * (current_speed / MAX_SPEED) * WIDTH * 4 * drift_multiplayer
        if current_speed != 0:
            current_car_orientation = PLAYER_CAR_LEFT_IMAGE
            if drift_multiplayer != 1 and current_speed > MAX_SPEED / 3 + 2000:
                current_car_orientation = PLAYER_CAR_DRIFT_LEFT_IMAGE

    if keys[pygame.K_RIGHT] and position_x < ROAD_WIDTH * 2:
        position_x += dt * (current_speed / MAX_SPEED) * WIDTH * 4 * drift_multiplayer
        if current_speed != 0:
            current_car_orientation = PLAYER_CAR_RIGHT_IMAGE
            if drift_multiplayer != 1 and current_speed > MAX_SPEED / 3 + 2000:
                current_car_orientation = PLAYER_CAR_DRIFT_RIGHT_IMAGE

    if keys[pygame.K_UP]:
        if 0 < current_speed < 500:
            smoke.add_particles()
            smoke.update()
            smoke.draw()
        if current_speed < MAX_SPEED:
            current_speed += ACCELERATION * dt
    elif keys[pygame.K_DOWN]:
        current_speed += BREAKING * dt
        if 0 < current_speed < 1000:
            smoke.add_particles()
            smoke.update()
            smoke.draw()
        if current_speed < 0:
            current_speed = 0
    else:
        current_speed += DECELERATION * dt
        if current_speed < 0:
            current_speed = 0

    if base_segment['radius'] != 0:
        position_x += dt * (current_speed / MAX_SPEED) ** 2 * (20000000 / base_segment['radius'])


def check_best_time():
    global best_time
    global last_time
    global timer
    global saved_track_index

    new_time = timer
    last_time = new_time
    if new_time < best_time or best_time == [0, 0, 0]:
        best_time = new_time
        if saved_track_index is not None:
            saved_tracks[saved_track_index]['best time'] = best_time

    timer = [0, 0, 0]


def check_lap_number():
    global lap
    global lap_counted

    # print(f"\rPosition: {round(position)} / {round(last_position)}, {lap_counted}", end=' ')

    if position < last_position and not lap_counted:
        lap += 1
        lap_counted = True
        check_best_time()
    elif position >= last_position:
        lap_counted = False


def render_player():
    player_on_screen_position_x = WIDTH / 2 - (current_car_orientation.get_width() * CAR_SCALE) / 2
    player_car = pygame.transform.scale(current_car_orientation,
                                        (current_car_orientation.get_width() * CAR_SCALE,
                                         current_car_orientation.get_height() * CAR_SCALE))
    WIN.blit(player_car, (player_on_screen_position_x, PLAYER_ON_SCREEN_POSITION_Y))


def draw_gauge(rot_x, rot_y):
    orange_color = (227, 112, 41)
    gauge_radius = 90
    gauge = pygame.Surface((gauge_radius * 2, gauge_radius * 2))
    gauge.set_colorkey((0, 0, 0))
    gauge.set_alpha(200)
    pygame.draw.circle(gauge, (227, 112, 41), (gauge_radius, gauge_radius), gauge_radius)
    pygame.draw.circle(gauge, (1, 1, 1), (gauge_radius, gauge_radius), gauge_radius - 3)
    pygame.draw.circle(gauge, (20, 20, 20), (gauge_radius, gauge_radius), gauge_radius - 15)

    gb_logo = pygame.transform.scale(GB_LOGO, (GB_LOGO.get_width() * 0.6, GB_LOGO.get_height() * 0.6))
    gauge.blit(gb_logo, gb_logo.get_rect(center=(gauge_radius, gauge_radius - 30)))

    digital_speedo = pygame.Rect(gauge_radius / 2, gauge_radius + 35, 80, 30)
    pygame.draw.rect(gauge, (120, 120, 120), digital_speedo)
    pygame.draw.rect(gauge, (1, 1, 1), digital_speedo, 2)

    text_speed = font_speed.render(f"{round(240 * current_speed / MAX_SPEED, 1)}", False, (1, 1, 1))
    gauge.blit(text_speed, (gauge_radius / 2 + 5, gauge_radius + 32))

    speed_num = 0
    for i in range(13):
        line_rot = (2 * math.pi * 60 / 360) + 2 * math.pi * 20 / 360 * i
        new_x1 = cos(line_rot) * (gauge_radius - gauge_radius) - sin(line_rot) * (
                    gauge_radius * 2 - gauge_radius) + gauge_radius
        new_y1 = sin(line_rot) * (gauge_radius - gauge_radius) + cos(line_rot) * (
                    gauge_radius * 2 - gauge_radius) + gauge_radius
        new_x2 = cos(line_rot) * (gauge_radius - gauge_radius) - sin(line_rot) * (
                    (gauge_radius * 2 - 15) - gauge_radius) + gauge_radius
        new_y2 = sin(line_rot) * (gauge_radius - gauge_radius) + cos(line_rot) * (
                    (gauge_radius * 2 - 15) - gauge_radius) + gauge_radius
        pygame.draw.line(gauge, orange_color, (new_x2, new_y2), (new_x1, new_y1), 3)
        text_speed_num = font_speed_num.render(f"{speed_num}", True, orange_color)
        if i < 6:
            gauge.blit(text_speed_num, (new_x2 + 5 - i * 1.5, new_y2 - 10 + i * 2))
        elif i == 6:
            gauge.blit(text_speed_num, (new_x2 - 7, new_y2))
        else:
            gauge.blit(text_speed_num, (new_x2 - (i - 6) * 4.2 - (12 - i) * 1.7, new_y2 - 10 + (12 - i) * 2))
        speed_num += 20

    WIN.blit(gauge, (rot_x - gauge_radius, rot_y - gauge_radius))


angle = 0


def render_speedo():
    global angle
    angle = (2 * math.pi * 60 / 360) + (2 * math.pi * 240 / 360) * (current_speed / MAX_SPEED)
    x = 150
    y = HEIGHT - 50
    rot_x = x
    rot_y = y - 80
    new_x1 = cos(angle) * (x - rot_x) - sin(angle) * (y - rot_y) + rot_x
    new_y1 = sin(angle) * (x - rot_x) + cos(angle) * (y - rot_y) + rot_y
    new_x2 = cos(angle) * (x - rot_x) - sin(angle) * ((y - 95) - rot_y) + rot_x
    new_y2 = sin(angle) * (x - rot_x) + cos(angle) * ((y - 95) - rot_y) + rot_y
    draw_gauge(rot_x, rot_y)
    pygame.draw.line(WIN, 'red', (new_x2, new_y2), (new_x1, new_y1), 4)
    pygame.draw.circle(WIN, 'black', (rot_x, rot_y), 3)


def render_ui():
    text_timer = font_timer.render(f"{timer[0]:02}:{timer[1]:02}:{int(str(timer[2])[:3])}", False, 'white')
    rect_timer = text_timer.get_rect(topleft=(WIDTH / 2 - 75, 10))
    draw_text_outline(text_timer, rect_timer, 2)
    WIN.blit(text_timer, rect_timer)

    text_lap = font_lap.render(f"Lap: {lap}", False, 'white')
    rect_lap = text_timer.get_rect(topleft=(WIDTH - 120, 10))
    draw_text_outline(text_lap, rect_lap, 2)
    WIN.blit(text_lap, rect_lap)

    text_best_time = font_best_time.render(f"Best Time: {best_time[0]:02}:{best_time[1]:02}:{int(str(best_time[2])[:3]):03}", False, 'white')
    rect_best_time = text_timer.get_rect(topleft=(20, 10))
    draw_text_outline(text_best_time, rect_best_time, 2)
    WIN.blit(text_best_time, rect_best_time)

    text_last_time = font_best_time.render(f"Last Time: {last_time[0]:02}:{last_time[1]:02}:{int(str(last_time[2])[:3]):03}", False, 'white')
    rect_last_time = text_timer.get_rect(topleft=(20, 50))
    draw_text_outline(text_last_time, rect_last_time, 2)
    WIN.blit(text_last_time, rect_last_time)

    text_game_info = font_game_info.render(f"Press ESC to pause game", False, 'grey')
    WIN.blit(text_game_info, (WIDTH - 150, HEIGHT - 30))
    render_speedo()


def render_background():
    global background_x_start_position
    WIN.fill(BLUE)
    background = pygame.transform.scale(BACKGROUND_IMAGE, (BACKGROUND_IMAGE_WIDTH, BACKGROUND_IMAGE_HEIGHT))
    if not game_paused:
        background_x_start_position += current_curve * (current_speed / MAX_SPEED)
    # print(f"\rX Value: {round(background_x_start_position)}", end=' ')
    WIN.blit(background, (background_x_start_position, 0))
    WIN.blit(background, (background_x_start_position - BACKGROUND_IMAGE_WIDTH, 0))
    WIN.blit(background, (background_x_start_position + BACKGROUND_IMAGE_WIDTH, 0))
    if background_x_start_position <= -BACKGROUND_IMAGE_WIDTH:
        WIN.blit(background, (background_x_start_position - BACKGROUND_IMAGE_WIDTH, 0))
        background_x_start_position = 0
    if background_x_start_position >= BACKGROUND_IMAGE_WIDTH:
        WIN.blit(background, (background_x_start_position + BACKGROUND_IMAGE_WIDTH, 0))
        background_x_start_position = 0


esc_pressed = False


def draw_game_window():
    global position
    global game_paused
    global esc_pressed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and not game_paused and not esc_pressed:
        esc_pressed = True
        game_paused = True

    if not keys[pygame.K_ESCAPE] and esc_pressed:
        esc_pressed = False

    if keys[pygame.K_ESCAPE] and game_paused and not esc_pressed:
        esc_pressed = True
        game_paused = False

    render_background()
    render_track()
    render_player()
    render_ui()

    if not game_paused:
        increase_z_position(position, dt * current_speed, track_length)
        check_lap_number()
        car_steering()

        if len(smoke.all_particles) != 0:
            smoke.update()
            smoke.draw()

        global start_timer
        if not start_timer:
            start_timer = True
    else:
        esc_pause_menu()

    pygame.display.update()


def esc_pause_menu():
    global window_mode
    global game_paused
    global start_timer
    global saved_tracks
    global saved_track_index

    save_button = Button(WIDTH / 2, 320, SAVE_BUTTON, 4.5)
    quit_button = Button(WIDTH / 2, 420, QUIT_BUTTON, 4.5)
    pause_menu = pygame.Surface((WIDTH, HEIGHT))
    pause_menu.set_colorkey((0, 0, 0))
    pause_menu.set_alpha(150)
    pygame.draw.rect(pause_menu, (10, 10, 10), (0, 0, WIDTH, HEIGHT))
    WIN.blit(pause_menu, (0, 0))
    if quit_button.draw(WIN):
        update_game_settings()
        game_paused = False
        start_timer = False
        set_screen_fade_in(2, 'menu')

    if saved_track_index is not None or len(saved_tracks) == 5:
        save_button.active = False
    else:
        save_button.active = True

    if save_button.draw(WIN) and saved_track_index is None:
        if len(saved_tracks) < 5:
            saved_tracks.append({'name': f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', 'track': road_segments, 'best time': best_time})
            saved_track_index = len(saved_tracks)


fade_in_step = 1
fade_in_next_window_mode = None


def set_screen_fade_in(step, next_window_mode):
    global fade_in_next_window_mode
    global fade_in_step
    global window_mode

    fade_in_step = step
    fade_in_next_window_mode = next_window_mode
    window_mode = 'fade in'


def screen_fade_in():
    global window_mode
    global fade_alpha
    global fade_in_next_window_mode
    window_mode = 'fade in'

    if fade_alpha >= 255 or fade_alpha == 0:
        fade_alpha = 0

    fade_in = pygame.Surface((WIDTH, HEIGHT))
    fade_in.set_colorkey((0, 0, 0))

    fade_in.set_alpha(fade_alpha)
    pygame.draw.rect(fade_in, (1, 1, 1), (0, 0, WIDTH, HEIGHT))
    WIN.blit(fade_in, (0, 0))
    # print(f"\rAlpha value: {alpha}", end=' ')
    pygame.display.update()
    fade_alpha += fade_in_step

    if fade_alpha >= 255:
        window_mode = fade_in_next_window_mode


car_frame = 0
car_spin_image = 0


def menu_car_spinning():
    global car_frame
    global car_spin_image
    car_frame += 1

    car_spin_on_screen_position_x = WIDTH / 2 - (CAR_SPINNING[car_spin_image].get_width() * CAR_SCALE) / 2
    car_spin = pygame.transform.scale(CAR_SPINNING[car_spin_image],
                                      (CAR_SPINNING[car_spin_image].get_width() * CAR_SCALE,
                                       CAR_SPINNING[car_spin_image].get_height() * CAR_SCALE))
    WIN.blit(car_spin, (car_spin_on_screen_position_x, PLAYER_ON_SCREEN_POSITION_Y + 30))
    if car_frame % 10 == 0:
        car_spin_image = (car_spin_image + 1) % 9
        car_frame = 0


def draw_menu_window():
    global window_mode
    global run
    global saved_track_index

    play_button = Button(WIDTH / 2, 370, PLAY_BUTTON, 4.5)
    quit_button = Button(WIDTH / 2, 470, QUIT_BUTTON, 4.5)

    WIN.fill(BLUE)
    WIN.blit(MENU_BACKGROUND_IMAGE, (0, 0))
    menu_car_spinning()

    if play_button.draw(WIN):
        if len(saved_tracks) != 0:
            set_screen_fade_in(buttons_fade_in_value, 'tracks')
        else:
            set_screen_fade_in(buttons_fade_in_value, 'game')
            saved_track_index = None
    if quit_button.draw(WIN):
        run = False

    pygame.display.update()


saved_track_index = None


def load_saved_track(index):
    global road_segments
    global best_time
    global saved_track_index

    road_segments = saved_tracks[index]['track']
    best_time = saved_tracks[index]['best time']
    saved_track_index = index


def show_saved_tracks():
    global window_mode

    for i in range(len(saved_tracks)):
        track_play_button = Button(WIDTH / 2 + 90, 200 + (i * 65), PLAY_BUTTON, 3)
        track_delete_button = Button(WIDTH / 2 + 170, 200 + (i * 65), X_BUTTON, 2)

        text_saved_track = font_saved_track.render(f"{saved_tracks[i]['name']}", False, 'white')
        rect_saved_track = text_saved_track.get_rect(center=(WIDTH / 2 - 100, 200 + (i * 65) - 15))
        draw_text_outline(text_saved_track, rect_saved_track, 2)
        WIN.blit(text_saved_track, rect_saved_track)

        text_saved_best_time = font_saved_track.render(
            f"Best time: {saved_tracks[i]['best time'][0]:02}:{saved_tracks[i]['best time'][1]:02}:{int(str(saved_tracks[i]['best time'][2])[:3]):03}",
            False, 'white')
        rect_saved_best_time = text_saved_best_time.get_rect(center=(WIDTH / 2 - 100, 200 + (i * 65) + 15))
        draw_text_outline(text_saved_best_time, rect_saved_best_time, 2)
        WIN.blit(text_saved_best_time, rect_saved_best_time)

        if track_play_button.draw(WIN):
            set_screen_fade_in(buttons_fade_in_value, 'game')
            load_saved_track(i)
        if track_delete_button.draw(WIN):
            del saved_tracks[i]
            break


def draw_tracks_menu_window():
    global window_mode
    global saved_track_index

    play_button = Button(WIDTH / 2, 650, PLAY_BUTTON, 4.5)
    back_button = Button(100, 650, BACK_BUTTON, 4.5)

    WIN.fill(BLUE)
    WIN.blit(TRACK_MENU_BACKGROUND_IMAGE, (0, 0))

    text_saved_tracks = font_saved_tracks.render(f"Select saved track", False, 'white')
    rect = text_saved_tracks.get_rect(center=(WIDTH / 2, 100))
    draw_text_outline(text_saved_tracks, rect, 3)

    WIN.blit(text_saved_tracks, rect)

    show_saved_tracks()

    if play_button.draw(WIN):
        set_screen_fade_in(buttons_fade_in_value, 'game')
        saved_track_index = None
    if back_button.draw(WIN):
        set_screen_fade_in(buttons_fade_in_value, 'menu')

    pygame.display.update()


def draw_text_outline(text, rect, size):
    mask = pygame.mask.from_surface(text)
    mask_surf = mask.to_surface()
    mask_surf.set_colorkey((0, 0, 0))
    mask_surf.fill((36, 36, 36), special_flags=pygame.BLEND_RGB_MULT)
    WIN.blit(mask_surf, (rect[0] - size, rect[1]))
    WIN.blit(mask_surf, (rect[0] + size, rect[1]))
    WIN.blit(mask_surf, (rect[0], rect[1] - size))
    WIN.blit(mask_surf, (rect[0], rect[1] + size))


fade_alpha = 255


def render_start_screen():
    global fade_alpha
    global window_mode

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        fade_alpha = 0
        window_mode = 'menu'
        return

    WIN.fill((0, 0, 0))
    scale = 3
    mf_logo = pygame.transform.scale(MF_LOGO, (MF_LOGO.get_width() * scale, MF_LOGO.get_height() * scale))
    WIN.blit(mf_logo, mf_logo.get_rect(center=(WIDTH / 2, HEIGHT / 2)))

    fade_out = pygame.Surface((WIDTH, HEIGHT))
    fade_out.set_colorkey((0, 0, 0))

    fade_out.set_alpha(fade_alpha)
    pygame.draw.rect(fade_out, (10, 10, 10), (0, 0, WIDTH, HEIGHT))
    WIN.blit(mf_logo, mf_logo.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
    WIN.blit(fade_out, (0, 0))
    pygame.display.update()
    # print(f"\rAlpha value: {fade_alpha}", end=' ')
    fade_alpha -= 1

    if fade_alpha < 0:
        set_screen_fade_in(3, 'menu')


def update_game_settings():
    global road_segments
    global lap
    global lap_counted
    global track_length
    global position
    global last_position
    global position_x
    global current_speed
    global current_car_orientation
    global timer
    global best_time
    global last_time
    global current_curve
    global background_x_start_position
    global smoke
    global angle

    lap = 1
    lap_counted = False

    road_segments = []
    track_length = create_section(NUMBER_OF_SEGMENTS_ON_TRACK)
    generate_track()

    position = 0
    last_position = position
    position_x = 0
    current_speed = 0
    current_car_orientation = PLAYER_CAR_STRAIGHT_IMAGE

    timer = [0, 0, 0]
    best_time = [0, 0, 0]
    last_time = [0, 0, 0]

    current_curve = 0
    background_x_start_position = 0

    smoke = Smoke()
    angle = 0


def read_saved_tracks():
    global saved_tracks

    if genericpath.exists('saved_tracks_data.json'):
        with open('saved_tracks_data.json') as json_file:
            data = json.load(json_file)

        saved_tracks = data


def save_saved_tracks():
    with open('saved_tracks_data.json', 'w') as out_file:
        json.dump(saved_tracks, out_file)


pygame.font.init()
font_default = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 30)

lap = 1
lap_counted = False
font_lap = font_default

track_length = create_section(NUMBER_OF_SEGMENTS_ON_TRACK)
generate_track()

position = 0
last_position = position
position_x = 0
current_speed = 0
font_speed = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 22)
current_car_orientation = PLAYER_CAR_STRAIGHT_IMAGE

timer = [0, 0, 0]  # minutes, seconds, milliseconds
best_time = [0, 0, 0]
last_time = [0, 0, 0]
start_timer = False
pygame.time.set_timer(pygame.USEREVENT, 1)
font_timer = font_default
font_best_time = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 20)
font_last_time = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 20)

font_speed_num = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 10)

current_curve = 0
background_x_start_position = 0

window_mode = 'start'
run = True
game_paused = False

font_game_info = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 10)

saved_tracks = []

font_saved_tracks = pygame.font.Font(os.path.join('Assets', '8-bit Arcade In.ttf'), 80)
font_saved_track = pygame.font.Font(os.path.join('Assets', 'Grand9K Pixel.ttf'), 20)

buttons_fade_in_value = 4

def main():
    global timer
    global run
    global button_clicked

    pygame.init()
    clock = pygame.time.Clock()

    read_saved_tracks()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and start_timer and not game_paused:
                timer[2] += clock.get_time()
                if timer[2] >= 10000:
                    timer[2] = 0
                    timer[1] += 1
                    if timer[1] >= 60:
                        timer[1] = 0
                        timer[0] += 1
            if event.type == pygame.QUIT:
                run = False

        if window_mode == 'fade in':
            screen_fade_in()
        elif window_mode == 'start':
            render_start_screen()
        elif window_mode == 'menu':
            draw_menu_window()
        elif window_mode == 'tracks':
            draw_tracks_menu_window()
        elif window_mode == 'game':
            draw_game_window()

        # print(f"\rIndex: {saved_track_index}", end=' ')
        # print(f"\rButton pressed: {button_clicked}", end=' ')

        if pygame.mouse.get_pressed()[0] == 0:
            button_clicked = False

    save_saved_tracks()
    pygame.quit()


if __name__ == '__main__':
    main()
