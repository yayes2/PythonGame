import time
from src.common.state import State
from src.common.player import Player
import asyncio
import websockets
import json
import os

target_fps = 60.0

frame_interval = 1.0 / target_fps

state = State()


async def process_event(websocket, path):
    """
    Process an event sent to the server from a client

    :param websocket:
    :param path:
    :return:
    """
    event = await websocket.recv()
    event = json.loads(event)
    print(websocket, event)
    # if event['name'] == 'JOIN':
    #     player = Player(websocket, event['player_name'])
    #     state.players.append(player
    #  if event['name'] == 'MOVE':


def load_map(name):
    """
    Loads a map file into memory.

    :param name:
    :return:
    """
    file = open(os.path.join('..', 'maps', name + '.json'))
    state.map = json.loads(file.read())
    for player in state.players:
        player.spectator = False


def frame():
    """
    Process the physics for a frame and send the render command.

    :return:
    """
    print("frame")
    # global state
    # print(state)
    start_time = time.time()
    # for player in state.players:
    #     v_max = 20
    #     if player.velocity[0] < -1 * v_max:
    #         player.velocity[0] = v_max
    #     if player.left and player.velocity[0] > -1 * v_max:
    #         v_max_per_frame = -1
    #         v_max_point = -10
    #         if player.velocity[0] > 0:
    #             v_change = v_max_per_frame
    #         elif player.velocity[0] < v_max_point:
    #             v_change = (player.velocity[0] / v_max_point) * v_max_per_frame
    #         else:
    #             v_change = v_max_per_frame / 5
    #         if v_change < v_max_per_frame / 10:
    #             v_change = v_max_per_frame / 10
    #         player.velocity += v_change
    #     elif player.right and player.velocity[0] < v_max:
    #         v_max_per_frame = 1
    #         v_max_point = 10
    #         if player.velocity[0] < 0:
    #             v_change = v_max_per_frame
    #         elif player.velocity[0] > v_max_point:
    #             v_change = (player.velocity[0] / v_max_point) * v_max_per_frame
    #         else:
    #             v_change = v_max_per_frame / 5
    #         if v_change < v_max_per_frame / 10:
    #             v_change = v_max_per_frame / 10
    #         player.velocity[0] += v_change
    # time.sleep(frame_interval - ((time.time() - start_time) % frame_interval))
    time.sleep(1)

print("INFO > Server starting")

start_server = websockets.serve(process_event, 'localhost', 8080)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.create_task(loop.run_in_executor(None, frame))
loop.run_forever()

os.exit(0)
