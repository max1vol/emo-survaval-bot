# Off-Grid Survival Emotionally Intelligent Bot

I want to build an off grid all in one package which can listens and respond to voice queries.

It'll also have a "face" with motorized eye brows, nose and mouth and use those to express emotions.

It'll be powered from powerbank and will also have a solar panel for full autonomy.

## Diagram

![emo-bot](https://github.com/user-attachments/assets/a9e7d037-9f7b-4a07-a5e5-0a4537610c8a)

## Tech Stack

### Software

The bot will be powered by Raspberry Pi 5 with 8GB RAM.

We will run:
1. Audio in / text out LLM: [Gemma 3n 2B active](https://huggingface.co/google/gemma-3n-E2B-it)
2. Text to speech: [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)

### Model tuning

Initially we will prompt Gemma 3n to focus on survival advice.

LLM will output both text to pronounce by TTS (text to speech) and "emotional state" (one of pre-defined state strings).

Emotion state will be translated into servo angles.

### Motor and wiring design 

To animate mouth and eye brows we will use SG90 servos connected to Raspberry Pi pins.

### Bill of Materials

1. 2x [Adafruit Small 1.2" 8x8 LED Matrix w/I2C Backpack - Red Product ID: 1049](https://thepihut.com/products/adafruit-small-1-2-8x8-led-matrix-w-i2c-backpack-red) - $9.95x = $20

2. 4x [TowerPro Servo Motor - SG90 Digital](https://thepihut.com/products/towerpro-servo-motor-sg90-digital) $5.50x4 = $22

3. 1x [6V 2W Solar Panel - ETFE (Voltaic P126)](https://thepihut.com/products/6v-2w-solar-panel-etfe-voltaic-p126) $35
   
5. [Raspberry Pi 5 8GB](https://shop.pimoroni.com/products/raspberry-pi-5?variant=41044580171859) - $104
   
7. [Active cooler, needed for AI workloads](https://shop.pimoroni.com/products/raspberry-pi-5-active-cooler?variant=41044554580051) - $6.50
   
8. [USB powered Speakers](https://thepihut.com/products/usb-powered-speakers) - $12

9. [USB microphone](https://thepihut.com/products/mini-usb-microphone) - $7.50

------

Total: $206.9 (including taxes)
