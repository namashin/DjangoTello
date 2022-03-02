import logging

from django.http import JsonResponse
from django.shortcuts import render

from .dronemanager import DroneManager

logger = logging.getLogger(__name__)


def get_drone():
    return DroneManager()


def index(request):
    """

    /indexのurlの時

    """
    return render(request, 'index.html')


def controller(request):
    """

    /controllerのurlの時

    """
    return render(request, 'controller.html')


def command(request):
    """

    /api/commandでPOSTリクエストが来た時

    """

    if "command" in request.POST:
        cmd = request.POST["command"]
        logger.info({'action': 'command', 'cmd': cmd})
        drone = get_drone()
        if cmd == 'takeOff':
            drone.takeoff()
        if cmd == 'land':
            drone.land()
        if cmd == 'speed':
            speed = request.form.get('speed')
            logger.info({'action': 'command', 'cmd': cmd, 'speed': speed})
            if speed:
                drone.set_speed(int(speed))

        if cmd == 'up':
            drone.up()
        if cmd == 'down':
            drone.down()
        if cmd == 'forward':
            drone.forward()
        if cmd == 'back':
            drone.back()
        if cmd == 'clockwise':
            drone.clockwise()
        if cmd == 'counterClockwise':
            drone.counter_clockwise()
        if cmd == 'left':
            drone.left()
        if cmd == 'right':
            drone.right()
        if cmd == 'flipFront':
            drone.flip_front()
        if cmd == 'flipBack':
            drone.flip_back()
        if cmd == 'flipLeft':
            drone.flip_left()
        if cmd == 'flipRight':
            drone.flip_right()
        if cmd == 'patrol':
            drone.patrol()
        if cmd == 'stopPatrol':
            drone.stop_patrol()
        if cmd == 'faceDetectAndTrack':
            drone.enable_face_detect()
        if cmd == 'stopFaceDetectAndTrack':
            drone.disable_face_detect()
        if cmd == 'snapshot':
            if drone.snapshot():
                return JsonResponse({'status': 'success'}), 200
            else:
                return JsonResponse({'status': 'fail'}), 400

        return JsonResponse({'status': 'success'}), 200
