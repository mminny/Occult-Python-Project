import cProfile
import palingrames
import palingrames_optimized
cProfile.run('palingrames.find_palingrams()')
cProfile.run('palingrames_optimized.find_palngrams()')