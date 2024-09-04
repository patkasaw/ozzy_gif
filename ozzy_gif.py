import imageio.v3 as iio

filenames = ['ozzy1.png', 'ozzy2.png', 'ozzy3.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('ozzy.gif', images, duration = 200, loop = 0)
