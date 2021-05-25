import spidev
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 15600000

# 读取数据
shuju = spi.readbytes()
#
