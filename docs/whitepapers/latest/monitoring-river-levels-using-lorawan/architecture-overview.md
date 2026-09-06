---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/architecture-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture overview
<a name="architecture-overview"></a>

## LoRaWAN gateway
<a name="lorawan-gateway"></a>

 To facilitate LoRaWAN connectivity, deploy a Laird Connectivity Sentrius RG1xx LoRaWAN gateway, which is a gateway device qualified for use with AWS IoT Core, and provides a range of up to ten miles for connecting devices. This gateway is registered in AWS IoT Core for LoRaWAN, and configured to receive data payloads from the remote IoT device wirelessly.

 Once configured and registered, the gateway communicates with AWS IoT Core for LoRaWAN over a fixed internet connection using two distinct protocols: Configuration and Update Service (CUPS) and WebSocket Secure (WSS).

 The CUPS protocol allows a supported LoRaWAN gateway to periodically retrieve configuration and software updates from a remote CUPS server. Although optional, its use is highly recommended, as it simplifies the management of LoRaWAN gateways. The LoRaWAN Basics Station software running on the gateway leverages CUPS to securely communicate with the managed CUPS server running in AWS over HTTPS, and retrieve endpoint information and certificates for the data plane.

 Thereafter, actual data transfer is facilitated over the data plane using the LoRaWAN Network Server (LNS) protocol based on WebSocket Secure (WSS).

## LoRaWAN device
<a name="lorawan-device"></a>

 To simulate a low-cost, low-power microcontroller monitoring a designated river level, a Pycom LoPy4 ESP32 development board equipped with a built-in Semtech SX1276 LoRa transceiver is used to upload data to the gateway. You will use an HC-SR04 ultrasonic distance sensor to approximate the distance to the water surface, and to send this measurement as a lean, two-byte payload. This paper provides a [MicroPython application example](source-code.md#micropython-application-example) which illustrates the distance capture and its subsequent transmission as a valid LoRaWAN payload.

## AWS IoT Core for LoRaWAN
<a name="aws-iot-core-for-lorawan"></a>

 With a goal of building an end-to-end application, service and wireless device profiles are configured in AWS IoT Core for LoRaWAN, and the microcontroller registered as a wireless device. To facilitate onward connectivity to additional AWS services, a destination accompanied by an AWS IoT rule is configured.

## AWS Lambda decoder
<a name="aws-lambda-decoder"></a>

 Payloads received by LoRaWAN are base64 encoded. As such, you will use a decoder function deployed to AWS Lambda to decode the payload, construct a meaningful JSON payload, and republish this back to AWS IoT Core from where it can be forwarded to AWS services. This paper provides a [Lambda decoder function example](source-code.md#lambda-decoder-function-example) to demonstrate this conversion.

 The Lambda decoder function allows other applications and devices to subscribe to messages arriving via LoRaWAN through the use of the [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) protocol and a designated topic. Depending on the precise use case, the Lambda function could be modified to undertake alternative tasks, such as directly invoking an [AWS SDK API](https://aws.amazon.com/tools/) call to forward data to other AWS services, or updating the device shadow.

![Diagram showing solution overview](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/solution-overview.png)
