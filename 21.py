from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

for i in range(21):
    for k in range(3):
    
        mc.setBlock(x+i+k,y-1,z+i,169)
    