from OSC import OSCClient, OSCMessage
import random


OSC_OUT_HOST = "localhost"
OSC_OUT_PORT = 57121

if __name__ == "__main__":
    mOscClient = OSCClient()
    mOscClient.connect( (OSC_OUT_HOST,OSC_OUT_PORT) )
    mOscMessage = OSCMessage()


    try:
                    mOscMessage.setAddress("/direccion")
                    mOscMessage.append(random.random())
                    mOscMessage.append('/valor')
                    mOscMessage.append('/nombre')
                    mOscClient.send(mOscMessage)

    except KeyboardInterrupt:
        mOscClient.close()
    finally:
        mOscClient.close()