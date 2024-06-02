from roku import Roku; 
import sys;
import time; 

roku: Roku = None
continuing = False


semantic_commands = {
    'click' : 'select',
    'tap' : 'select',
    'move right' : 'right',
    'move left' : 'left',
    'move down' : 'down',
    'move up' : 'up',
    'wait' : 'sleep',
}

def roku_init(ip):
    global roku
    roku=Roku(ip, '8060'); 
    roku.poweron()

def app_roku_init(ip, app):
    global roku
    global continuing
    roku = Roku(ip, '8060')
    continuing = app.lower() in roku.active_app.name.lower()
    roku.poweron()
    [elem for i, elem in enumerate(roku.apps) if app.lower() in elem.name.lower()][0].launch()

def app_search(ip, app, query):
    app_roku_init(ip, app)
    if(continuing):
        print("running from inside app; assuming preparation for text input complete")

    select = False

    if('netflix' in app.lower()): 
        time.sleep(2)
        if not continuing:
            print("navigating")
            time.sleep(6)
            roku.select()
            time.sleep(1.0)
            roku.left()
            time.sleep(0.2)
            roku.up()
            time.sleep(0.2)
            roku.select()
            time.sleep(2)
        print("searching")
        roku.literal(query)
        time.sleep(0.2 * len(query))
        [roku.right() for _ in range(6 - (ord(query[len(query) - 1]) - ord('a')) % 6)]
        if select:
            roku.select()
            time.sleep(0.2)
            roku.select()
    elif('youtube' in app.lower()): 
        time.sleep(20)
        print("navigating")
        roku.back() # for occasional startup modal
        time.sleep(2)
        roku.left()
        time.sleep(1)
        roku.up()
        time.sleep(0.5)
        roku.select()
        time.sleep(2)
        roku.right() 
        print("searching")
        roku.literal(query)
        time.sleep(0.2 * len(query))
        roku.left()
        [roku.down() for _ in range(5)]
        roku.right() # in case of sponsored/ad videos
        if select:
            roku.select()
    elif('prime' in app.lower()): 
        time.sleep(6 if continuing else 20)
        time.sleep(6.0)
        print("navigating")
        roku.select()
        time.sleep(2)
        roku.down()
        time.sleep(0.8)
        roku.left()
        time.sleep(0.8)
        roku.up()
        time.sleep(0.8)
        roku.select()
        time.sleep(2)
        
        print("searching")
        curr_x = 0
        curr_y = 0
        move_delay = 0.01
        result_delay = 2
        print(f"typing {query.lower()}")
        for character in query.lower():
            target_x = (ord(character) - ord('a') ) % 6
            target_y = (ord(character) - ord('a')) // 6
            if character == ' ':
                target_x = 0
                target_y = 6
            if character.isdecimal():
                # TODO
                pass

            diff_x = target_x - curr_x
            diff_y = target_y - curr_y

            print(f"target ({target_x}, {target_y}), diff ({diff_x}, {diff_y})")

            for _ in range(abs(diff_x)):
                if diff_x > 0:
                    roku.right()
                    time.sleep(move_delay)
                else:
                    roku.left()
                    time.sleep(move_delay)
            
            for _ in range(abs(diff_y)):
                if diff_y > 0:
                    roku.down()
                    time.sleep(move_delay)
                else:
                    roku.up()
                    time.sleep(move_delay)
            
            print(character, end=' ')
            roku.select()

            curr_x = target_x
            curr_y = target_y

            if character == ' ':
                roku.up()
                time.sleep(move_delay)
                curr_y -= 1
        print('\n')

        [roku.up() for _ in range(curr_y)]
        [roku.right() for _ in range( 6 - curr_x)]
        time.sleep(result_delay)
        roku.right()
        if select:
            roku.select()
    elif('Plex' in app): 
        time.sleep(2)
        if not continuing:
            print("navigating")
            time.sleep(3)
            roku.select()
            time.sleep(0.4)
            roku.left()
            time.sleep(0.4)
            roku.up()
            time.sleep(0.2)
            roku.select()
            time.sleep(0.2)
        print("searching")
        roku.literal(query)
        time.sleep(0.5 * len(query))
        [roku.right() for _ in range(6 - (ord(query[len(query) - 1]) - ord('a')) % 6)]
    
    print("complete")

def up(ip):
    roku_init(ip)
    roku.up()

def down(ip):
    roku_init(ip)
    roku.down()

def left(ip):
    roku_init(ip)
    roku.left()

def right(ip):
    roku_init(ip)
    roku.right()

def type(ip, text):
    roku_init(ip)
    roku.literal(text)

def vol_up(ip):
    roku_init(ip)
    roku.volume_up()

def vol_down(ip):
    roku_init(ip)
    roku.volume_down()

def vol_mute(ip):
    roku_init(ip)
    roku.volume_mute()

def poweroff(ip):
    roku = Roku(ip, '8060')
    roku.poweroff()

def poweron(ip):
    roku_init(ip)

def click(ip):
    roku_init(ip)
    roku.select()

def execute(ip, actions):
    action_array = actions.split(' ')
    it = enumerate(action_array)
    for i, word in it:
        if 'time' in word and i >= 2:
            count = text2int(action_array[i - 1])
            print(f"performing {count} {action_array[i - 2]} actions")
            thismodule = sys.modules[__name__]
            operation = getattr(thismodule, action_array[i - 2])
            for i in range(count):
                operation(ip)
            next(it, None)
            next(it, None)
        else:
            thismodule = sys.modules[__name__]
            operation = getattr(thismodule, action_array[i])
            operation(ip)
            print(action_array[i])
        time.sleep(0.5)



# https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split('-'):
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current