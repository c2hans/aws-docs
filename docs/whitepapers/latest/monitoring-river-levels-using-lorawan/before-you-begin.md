---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/before-you-begin.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Before you begin
<a name="before-you-begin"></a>
+  **Long range** (**LoRa**) is a wireless radio communication technology which operates in the license-free, sub-gigahertz radio frequency band. Due to the technology’s focus on achieving longer range and lower power consumption compared to other wireless connectivity standards such as Bluetooth, Wi-Fi or mobile broadband, LoRa has found widespread use to meet a variety of Internet of Things (IoT) use cases where there is a compelling requirement to implement an LPWAN. In such deployments, the LPWAN is often used to facilitate communication between geographically distributed, low-cost, power-constrained devices such as battery-operated sensor units that are positioned in remote locations with challenges in access.
+  **Long range wide-area network** (**LoRaWAN**) provides the protocols for the upper layers of the LPWAN. It builds on the lower physical foundations provided by LoRa technology, including its hardware, to manage end-to-end communication between devices that participate in the overall network. Additionally, LoRaWAN allows data payloads to wirelessly flow between devices participating in the network and centralized gateways responsible for routing the traffic.
+  [**AWS IoT Core for LoRaWAN**](https://aws.amazon.com/iot-core/lorawan/) is a fully managed feature that removes the undifferentiated heavy-lifting of instantiating and operating a private LoRaWAN network by enabling customers to build a fully serverless, scalable, and secure LoRaWAN-based application that tightly integrates with AWS services, including [AWS IoT Core](https://aws.amazon.com/iot-core/).

![Diagram showing AWS IoT Core for LoRaWAN overview](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/iot-core-for-lorawan-overview.jpg)
