import pygame
import asyncio
import i18n
import json
from collections import deque
from Scene.opening import Open

mapping = { }
args =  {}

def check(object, events):
    return object.check(events)
def process(results, queue:deque,object):
    if results:
        #points.check(object.screen)
        object.display.update()
       
    if isinstance(results, list):
        for item in results:
            if item in mapping.keys():
                queue.append(mapping[item])

        


# pygbag --archive winter-gamejam-2025-pirate\sword



# Initialize pygame
pygame.init()

clock = pygame.time.Clock()



async def main():
    display = pygame.display
    queue =  deque([Open])
    object =  queue.pop()(display)
    display = object.display 




    while queue or object.running:
        await asyncio.sleep(0)
        if not object.running:
            object = queue.pop()
            pass_args = args.get(object, {})
            object =  object(display,**pass_args)if args else object(display)
            display = object.display
        
        events = pygame.event.get()
        
        results = check(object, events)
        process(results,queue,object)
                

        


        

# This is the program entry point
asyncio.run(main())