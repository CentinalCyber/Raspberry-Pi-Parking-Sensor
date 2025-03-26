# Raspberry-Pi-Parking-Sensor
Ultrasonic parking sensor using Raspberry Pi, HC-SR04, LCD, and Buzzer


# Raspberry Pi Parking Sensor

This project uses an **HC-SR04 ultrasonic sensor**, **LCD1602 I2C display**, and a **buzzer** to simulate a real-time parking assist system using a **Raspberry Pi**.

## 🛠️ Features
- Measures distance using ultrasonic sensor
- Displays live distance data on LCD
- Activates buzzer with varying alerts (buzzing speed) based on proximity
- LCD warnings like "SAFE", "CAUTION", "TOO CLOSE" depening on distance


## 📷 Hardware Used
- Raspberry Pi 4 Model B
- HC-SR04 Ultrasonic Sensor
- LCD1602 I2C Display
- Buzzer
- Jumper Wires & Breadboard

## 🧠 How It Works
The ultrasonic sensor detects the distance to an object and sends the result to the LCD. Based on how close the object is, the buzzer will activate with different beep speeds or stay silent if the path is clear.

## 📁 File
- `parking_sensor.raspberrypi.py`: Main Python script for running the parking sensor system.

## ✅ To Run
Make sure you have the `RPLCD` library installed:
