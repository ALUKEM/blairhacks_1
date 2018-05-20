import Leap, sys, thread, time, serial, smtplib, math, sqlite3
from setup import start

proximal = []
distal = []
realframeid = 0

class SampleListener(Leap.Listener):
        proximal = []
        distal = []
        finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
        bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

        def on_init(self, controller):
                print "Initialized"

        def on_connect(self, controller):
                print "Connected"

        def on_disconnect(self, controller):
                # Note: not dispatched when running in a debugger.
                print "Disconnected"

        def on_exit(self, controller):
                print "Exited"

        def on_frame(self, controller):
                global realframeid
                global userInput
                global proximal
                global distal

                # Get the most recent frame and report some basic information
                frame = controller.frame()

                print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
                          realframeid, frame.timestamp, len(frame.hands), len(frame.fingers))

                # Get hands
                for hand in frame.hands:
                
                        # Get fingers
                        for finger in hand.fingers:
                                if len(frame.fingers) == 5:
                                        boneValidData = []
                                        for phinger in hand.fingers:
                                                bone1 = phinger.bone(3)
                                                bone2 = phinger.bone(1)
                                                boneValidData.append(bone1.is_valid)
                                                boneValidData.append(bone2.is_valid)
                                        if boneValidData[0] and boneValidData[1] and boneValidData[2] and boneValidData[3] and boneValidData[4] and boneValidData[5] and boneValidData[6] and boneValidData[7] and boneValidData[8] and boneValidData[9]:
                                                print "%s finger, id: %d" % (
                                                                self.finger_names[finger.type],
                                                                finger.id)

                                                bone = finger.bone(1)
                                                print "Bone: %s, start: %s, end: %s, direction: %s,  midpoint: %s" % (
                                                        self.bone_names[bone.type],
                                                        bone.prev_joint,
                                                        bone.next_joint,
                                                        bone.direction,
                                                        bone.center)
                                                if userInput == "record":
                                                        proximal.append(["fingerdata.db", self.finger_names[finger.type], "proximal", converttolist(str(bone.center)), "r"])
                                                        #enterdata("fingerdata.db", self.finger_names[finger.type], "proximal", converttolist(str(bone.center)), "r")
                                                        
                                                else:
                                                        #enterdata("userfingerdata.db", self.finger_names[finger.type], "proximal", converttolist(str(bone.center)), "e")
                                                        proximal.append(["userfingerdata.db", self.finger_names[finger.type], "proximal", converttolist(str(bone.center)), "e"])

                                                bone = finger.bone(3)
                                                print "Bone: %s, start: %s, end: %s, direction: %s,  midpoint: %s" % (
                                                        self.bone_names[bone.type],
                                                        bone.prev_joint,
                                                        bone.next_joint,
                                                        bone.direction,
                                                        bone.center)

                                                if userInput == "record":
                                                        distal.append(["fingerdata.db", self.finger_names[finger.type], "distal", converttolist(str(bone.center)), "r"])
                                                        #enterdata("fingerdata.db", self.finger_names[finger.type], "distal", converttolist(str(bone.center)), "r")
                                                else:
                                                        #enterdata("userfingerdata.db", self.finger_names[finger.type], "distal", converttolist(str(bone.center)), "e")
                                                        distal.append(["userfingerdata.db", self.finger_names[finger.type], "distal", converttolist(str(bone.center)), "e"])
                
                        realframeid += 1
                if not frame.hands.is_empty:
                        print ""
                
def file_len(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                                pass
        return i + 1

def enterdata(dbname, finger, section, l, re, conn, c):
        n = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky'].index(finger) + 1
        name = section + str(n)
        if re == "r":
                name = "f" + name

        c.execute("INSERT INTO %s (`xcoord`, `ycoord`, `zcoord`) VALUES (%f, %f, %f)" % (name, float(l[0]), float(l[1]), float(l[2])))
def converttolist(a):
                a = a.replace(")", "")
                a = a.replace("(", "")
                a = a.replace(" ", "")
                a = a.replace("\n", "")
                #print a
                results = a.split(',')
                #print results
                if len(results) == 3:   
                        result = map(float, results)
                        return result
                else:
                        return None

def enterPass():
        global realframeid
        global proximal
        global distal
        # Create a sample listener and controller
        listener = SampleListener()
        controller = Leap.Controller()
        if(controller.is_connected == False):
                  print("Waiting for controller...");
                  while(not(controller.is_connected)):
                           time.sleep(1);
        print("Controller Connected.")

        # Keep this process running until Enter is pressed
        print "Press Enter to record password."
        print "Tip: Record with large motions for most secure passwords!"
        try:
                sys.stdin.readline()
        except KeyboardInterrupt:
                pass
        # Have the sample listener receive events from the controller
        print "Recording in 3..."
        time.sleep(1)
        print "2..."
        time.sleep(1)
        print "1..."
        time.sleep(1)
        print "Recording..."
        controller.add_listener(listener)

        try:
                sys.stdin.readline()
        except KeyboardInterrupt:
                pass
        finally:
                # Remove the sample listener when done
                controller.remove_listener(listener)
                #upload to database
                if userInput == "record":
                        conn = sqlite3.connect("fingerdata.db")
                else:
                        conn = sqlite3.connect("userfingerdata.db")
                c = conn.cursor()
                #proximal
                for i in proximal:
                        enterdata(i[0], i[1], i[2], i[3], i[4], conn, c)

                #distal
                for j in distal:
                        enterdata(j[0], j[1], j[2], j[3], j[4], conn, c)

                conn.commit()
                conn.close()
                
                print "saved"

start("fingerdata")     
userInput = raw_input("Record Gesture or Enter Gesture?")
while userInput.lower() != "record" and userInput.lower() != "enter":
     print "\nInvalid input!\n"
     userInput = raw_input("Record Gesture or Enter Gesture?")
"""if userInput.lower() == "record":
        conn = sqlite3.connect("fingerdata.db")
        c = conn.cursor()
        c.execute("DROP TABLE fproximal1")
        c.execute("DROP TABLE fproximal2")
        c.execute("DROP TABLE fproximal3")
        c.execute("DROP TABLE fproximal4")
        c.execute("DROP TABLE fproximal5")
        c.execute("DROP TABLE fdistal1")
        c.execute("DROP TABLE fdistal2")
        c.execute("DROP TABLE fdistal3")
        c.execute("DROP TABLE fdistal4")
        c.execute("DROP TABLE fdistal5")
        conn.commit()
        conn.close()

conn2 = sqlite3.connect("userfingerdata.py")
c2 = conn2.cursor()
c.execute("DROP TABLE proximal1")
c.execute("DROP TABLE proximal2")
c.execute("DROP TABLE proximal3")
c.execute("DROP TABLE proximal4")
c.execute("DROP TABLE proximal5")
c.execute("DROP TABLE distal1")
c.execute("DROP TABLE distal2")
c.execute("DROP TABLE distal3")
c.execute("DROP TABLE distal4")
c.execute("DROP TABLE distal5")
conn2.commit()
conn2.close()"""
enterPass()

                
