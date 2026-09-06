---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-iot-solutions-with-mqtt.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing LPWAN IoT solutions with MQTT
<a name="implementing-lpwan-iot-solutions-with-mqtt"></a>

 Using UDP and CoAP on MCU devices is recommended to improve power efficiency and ensure longer battery life. However, for use cases with a non-constrained devices or devices without long battery lifetime requirements, also MQTT and HTTP protocols should be considered, as described in the following sections.

## Device telemetry ingestion
<a name="device-telemetry-ingestion"></a>

 To ingest telemetry with MQTT and HTTP, customers can use FreeRTOS libraries and OS-independent AWS IoT Device SDK for Embedded C. For customers who use FreeRTOS, AWS recommends using FreeRTOS libraries ingest telemetry through JSON (using [coreJSON](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-corejson.html) library), HTTP(S) (using [coreHTTP](https://docs.aws.amazon.com/freertos/latest/userguide/core-http.html) library), MQTT (using [coreMQTT](https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt.html) library), and TCP sockets (using [Secure Sockets](https://docs.aws.amazon.com/freertos/latest/userguide/secure-sockets.html) library). If using other operating system then FreeRTOS, customers can also use [AWS IoT Device SDK for Embedded C](https://github.com/aws/aws-iot-device-sdk-embedded-C), which also provides [coreJSON](https://github.com/aws/aws-iot-device-sdk-embedded-C#corejson), [coreHTTP,](https://github.com/aws/aws-iot-device-sdk-embedded-C#corehttp) and [coreMQTT](https://github.com/aws/aws-iot-device-sdk-embedded-C#coremqtt) libraries.

## Device commands
<a name="device-commands"></a>

 To send commands to the device, customers can use [AWS IoT Device Shadow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html). Interaction with AWS IoT Device Shadow is supported in FreeRTOS (refer to [AWS IoT Device Shadow library](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-cloud-shadows.html)) and OS-independent [AWS IoT Device SDK for Embedded C](https://github.com/aws/aws-iot-device-sdk-embedded-C#aws-iot-device-shadow).

## Firmware updates
<a name="firmware-updates"></a>

 Device provisioning relates to the application workflow that provides unique identity and configuration data to the device. The provisioning layer is also involved with ongoing maintenance and eventual decommissioning of devices over time.

 Firmware and over-the-air (OTA) updates without human intervention is critical for security, scalability, and delivering new capabilities to the IoT devices.

 Customers using FreeRTOS can use [OTA Agent library](https://docs.aws.amazon.com/freertos/latest/userguide/ota-agent-library.html) to perform firmware upgrades on the FreeRTOS devices. If using operating systems other than FreeRTOS, customers can use [AWS IoT Over-the-air Update library](https://github.com/aws/aws-iot-device-sdk-embedded-C#aws-iot-over-the-air-update) included in the [AWS IoT Device SDK for Embedded C](https://github.com/aws/aws-iot-device-sdk-embedded-C#aws-iot-device-shadow).

## Implementing device provisioning
<a name="implementing-device-provisioning"></a>

 When you use AWS IoT fleet provisioning, AWS IoT can generate and securely deliver device certificates and private keys to your devices when they connect to AWS IoT for the first time. You can find the guidelines for implementing fleet provisioning on your MCU device in the [Fleet Provisioning Documentation](https://docs.aws.amazon.com/freertos/latest/lib-ref/c-sdk/provisioning/index.html).
