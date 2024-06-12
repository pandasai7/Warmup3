from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from panda3d.core import CollisionNode, CollisionSphere, CollisionHandlerQueue, CollisionSegment
import math, sys, random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)
        self.parent = self.loader.loadModel("./Assets/cube")
        
        self.parentCnode = self.parent.attachNewNode(CollisionNode('pcnode')) #attach collider 'pcnode' to self.parent and name it parentCnode
        self.parentCnode.node().addSolid(CollisionSphere(0, 0, 0, 1.5)) #make parentCnode collision sphere
        self.fighterCnode = self.fighter.attachNewNode(CollisionNode('fcnode')) #attach collider 'fcnode' to self.fighter and name it parentCnode
        self.fighterCnode.node().addSolid(CollisionSphere(0, 0, 0, 1.5)) #make fighterCnode collision sphere
        self.traverser = CollisionTraverser() #creates traverser to look at all object under a parent
        self.pusher = CollisionHandlerPusher() #Makes collider pusher to push colliders
        self.pusher.addCollider(self.fighterCnode, self.fighter) #tells the pusher object what colliders will push
        self.traverser.addCollider(self.fighterCnode, self.pusher) #tells the traverser to check the fighterCnode collider and how to interact
        self.cTrav = self.traverser #actually does the act of checking for collisions
        self.traverser.showCollisions(self.render) #makes a lil red box to show collisions for debugging purposes and passes it to the camera to make it visible
        self.traverser.traverse(self.render) #makes traverser child of parent camera (self.render)
        
        self.fighterCnode.show()
        self.parentCnode.show()


        x = 0

        for i in range(100):
            theta = x
            cos = 50.0 * math.cos(theta)
            sin = 50.0 * math.sin(theta)
            tan = 0.0 * math.tan(theta)
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(cos, sin, tan)
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)

                                #----------COLLISION----------#

            #creates a collision solid as collision sphere
            ##cs = CollisionSphere(0, 0, 0, 1.4)
            
            #creates a node to attach to the collision solid
            ##cnodePath = self.placeholder2.attachNewNode(CollisionNode('cnode'))

            #attaches the node to the solid
            ##cnodePath.node().addSolid(cs)

            #makes the collisionNode visible for debugging purposes
            ##cnodePath.show()
            
            #CollisionHandler PUSHER - auto pushes object out of walls
            ##cnodePath.node().addSolid(cs)
            
            ##pusher.addCollider(cnodePath, self.fighter)
            ##pusher.addInPattern('fnode-into-cnode')
            
            #traverser
            
            ##traverser.addCollider(cnodePath, pusher)
            
            #makes collisions visible
            ##traverser.showCollisions(self.render)
            
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06
        
        #fighter collider stuffs
        ##fs = CollisionSphere(0, 0, 0, 1.0)
        ##fnodePath = self.fighter.attachNewNode(CollisionNode('fnode'))
        ##fnodePath.node().addSolid(fs)
        ##pusher.addCollider(fnodePath, self.fighter)
        ##fnodePath.show()

        #Mouse Control
        self.disableMouse()
        self.camera.setPos(0.0, 0.0, 250.0)
        self.camera.setHpr(0.0, -90.0, 0.0)

        #----------controls----------#
        #quit
        self.accept('escape', self.quit)
        
        #left
        self.accept('arrow_left', self.negativeX, [1]) #LeftPressed
        self.accept('arrow_left-up', self.negativeX, [0]) #LeftReleased

        #right
        self.accept('arrow_right', self.positiveX, [1]) #RightPressed
        self.accept('arrow_right-up', self.positiveX, [0]) #RightReleased

        #up
        self.accept('arrow_up', self.positiveY, [1]) #RightPressed
        self.accept('arrow_up-up', self.positiveY, [0]) #RightReleased

        #down
        self.accept('arrow_down', self.negativeY, [1]) #RightPressed
        self.accept('arrow_down-up', self.negativeY, [0]) #RightReleased

    def negativeX(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
            else:
                 self.taskMgr.remove('moveNegativeX')
    def positiveX(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.movePositiveX, 'movePositiveX')
            else:
                 self.taskMgr.remove('movePositiveX')
    def negativeY(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
            else:
                 self.taskMgr.remove('moveNegativeY')
    def positiveY(self, keyDown):
            if(keyDown):
                self.taskMgr.add(self.movePositiveY, 'movePositiveY')
            else:
                 self.taskMgr.remove('movePositiveY')

    def quit(self):
         sys.exit() 


    def moveNegativeX(self, task):
         self.fighter.setX(self.fighter, -1)
         return task.cont

    def movePositiveX(self, task):
        self.fighter.setX(self.fighter, 1)
        return task.cont

    def moveNegativeY(self, task):
        self.fighter.setY(self.fighter, -1)
        return task.cont

    def movePositiveY(self, task):
        self.fighter.setY(self.fighter, 1)
        return task.cont

app = MyApp()
app.run()


