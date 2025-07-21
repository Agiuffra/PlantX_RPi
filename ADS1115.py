import smbus
import time

bus_num = 1
dev_addr = 0x48

bus = smbus.SMBus(bus_num)

conv_addr = 0x00
conf_addr = 0x01

bus.write_i2c_block_data(dev_addr, conf_addr, [0b01000100, 0b10000011])
        
while(1):
    try:
        data = bus.read_i2c_block_data(dev_addr, conf_addr, 2)
        print(f"Config: {bin(data[1])}")
        data_raw = bus.read_i2c_block_data(dev_addr, conv_addr, 2)
        data = (data_raw[0]<<8)+data_raw[1]
        data = data*3.3/65535
        print(f"Data: {data_raw}")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(2)
    
    