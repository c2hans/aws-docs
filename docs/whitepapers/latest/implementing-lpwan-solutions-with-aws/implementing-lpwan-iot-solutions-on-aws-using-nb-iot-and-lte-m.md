---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-iot-solutions-on-aws-using-nb-iot-and-lte-m.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing LPWAN IoT solutions on AWS using NB-IoT and LTE-M
<a name="implementing-lpwan-iot-solutions-on-aws-using-nb-iot-and-lte-m"></a>

 IoT solutions using NB-IoT and LTE-M technologies often use resource-constrained battery-operated devices. For such devices, use of connection-based protocols such as MQTT and HTTP might unnecessarily decrease battery life or increase implementation complexity.

 As opposed to MQTT and HTTP, connectionless protocols such as Constrained Application Protocol (CoAP) or User Datagram Protocol (UDP) offer higher energy efficiency and can reduce implementation complexity on the IoT device. Because of these benefits, telemetry ingestion and device commands for resource-constrained battery-operated NB-IoT and LTE-M devices are often implemented using UDP and CoAP protocols. You will find a detailed description for various implementation approaches in the [Implementing LPWAN IoT solutions with UDP](implementing-lpwan-iot-solutions-with-udp.md) and [Implementing LPWAN IoT solutions with CoAP](implementing-lpwan-iot-solutions-with-coap.md) sections of this document.

 When using LTE-M with a non-constrained device or a device without long battery lifetime requirements, also MQTT and HTTP protocols shall be considered. You will find further information about using MQTT and HTTP protocols in the [Implementing LPWAN IoT solutions with MQTT](implementing-lpwan-iot-solutions-with-mqtt.md) section of this document.

 The following sections introduce User Datagram Protocol (UDP) and Constrained Application Protocol (CoAP) and then provide guidelines for their implementation with AWS IoT.

**Topics**
+ [Implementing LPWAN IoT solutions with UDP](implementing-lpwan-iot-solutions-with-udp.md)
+ [Implementing LPWAN IoT solutions with CoAP](implementing-lpwan-iot-solutions-with-coap.md)
+ [Implementing LPWAN IoT solutions with MQTT](implementing-lpwan-iot-solutions-with-mqtt.md)
+ [Managing cellular connectivity](managing-cellular-connectivity.md)
