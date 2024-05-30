from roku import Roku; 
import requests; 
import time; 

roku: Roku = None
continuing = False

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

    if(app =='Netflix'): 
        time.sleep(2)
        if not continuing:
            time.sleep(6)
            roku.select()
            time.sleep(1.0)
            roku.left()
            time.sleep(0.2)
            roku.up()
            time.sleep(0.2)
            roku.select()
            time.sleep(2)
        roku.literal(query)
        time.sleep(0.2 * len(query))
        [roku.right() for _ in range(6 - (ord(query[len(query) - 1]) - ord('a')) % 6)]
        if select:
            roku.select()
            time.sleep(0.2)
            roku.select()
    elif(app =='YouTube'): 
        time.sleep(20)
        roku.back() # for occasional startup modal
        time.sleep(2)
        roku.left()
        time.sleep(1)
        roku.up()
        time.sleep(0.5)
        roku.select()
        time.sleep(2)
        roku.right() 
        roku.literal(query)
        time.sleep(0.2 * len(query))
        roku.left()
        [roku.down() for _ in range(5)]
        roku.right() # in case of sponsored/ad videos
        if select:
            roku.select()
    elif(app =='Prime Video'): 
        time.sleep(6 if continuing else 20)
        roku.select()
        time.sleep(6.0)
        roku.down()
        time.sleep(0.8)
        roku.left()
        time.sleep(0.8)
        roku.up()
        time.sleep(0.8)
        roku.select()
        time.sleep(2)

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
            time.sleep(3)
            roku.select()
            time.sleep(0.4)
            roku.left()
            time.sleep(0.4)
            roku.up()
            time.sleep(0.2)
            roku.select()
            time.sleep(0.2)
        roku.literal(query)
        time.sleep(0.5 * len(query))
        [roku.right() for _ in range(6 - (ord(query[len(query) - 1]) - ord('a')) % 6)]

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
    roku.poewroff()

def poweron(ip):
    roku_init(ip)

def click(ip):
    roku_init(ip)
    roku.select()
