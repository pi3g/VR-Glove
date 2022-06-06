def main():
    import busio
    import digitalio
    import board
    import adafruit_mcp3xxx.mcp3008 as MCP
    from adafruit_mcp3xxx.analog_in import AnalogIn
    from time import sleep

    sleep(1)

    # SCK = GP2
    # MISO = GP4
    # MOSI = GP3
    # CS = GP5

    # create the spi bus
    spi = busio.SPI(clock=board.GP2, MISO=board.GP4, MOSI=board.GP3)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.GP5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channels on pins 0-4
    chan0 = AnalogIn(mcp, MCP.P0)
    chan1 = AnalogIn(mcp, MCP.P1)
    chan2 = AnalogIn(mcp, MCP.P2)
    chan3 = AnalogIn(mcp, MCP.P3)
    chan4 = AnalogIn(mcp, MCP.P4)
    channels = [chan0, chan1, chan2, chan3, chan4]

    while True:
        values = [chan.voltage for chan in channels]
        print(values)
        sleep(0.1)

if __name__ == '__main__':
    main()