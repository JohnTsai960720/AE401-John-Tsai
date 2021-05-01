from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x-3,y+18,z-3,x+2,y+22,z+2,161)
mc.setBlocks(x-3,y+8,z-3,x+2,y+12,z+2,161)
mc.setBlocks(x-1,y,z-1,x,y+20,z,17)