---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/evaluating-technical-fit.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Evaluating technical fit
<a name="evaluating-technical-fit"></a>

 The purpose of technical fit evaluation is to ensure that a connectivity technology of your choice fulfills technical requirements of your use-case. AWS recommends you consider both imminent use-cases and also foreseen use-cases, which you expect to arise as your IoT solution evolves. This foresight of future use-cases is important, because choices of connectivity technology typically impact the IoT device hardware design, that may be costly to reverse. This section provides an overview of technical fit requirements.

## Deployment area requirements
<a name="deployment-area-requirements"></a>

 Availability of LPWAN connectivity options can vary significantly depending on the intended locations of your IoT device. If available in the intended location, public LPWAN networks (for example, NB-IoT/LTE-M networks, public LoRaWAN network, or Sigfox) can be a feasible choice. In the areas where public LPWAN networks are not available or are not economically feasible, an option to operate private LPWAN network can be considered, for example using LoRaWAN technology. You will find more information about building private LoRaWAN networks in the *Implementing LPWAN IoT solutions on AWS with LoRaWAN* section of this document.

## Range, indoor, and underground coverage requirements
<a name="range-indoor-and-underground-coverage-requirements"></a>

 Whatever LPWAN connectivity technology you choose, your IoT device will need an intermediary to exchange data with the AWS Cloud or your edge device. For LPWAN technologies, examples of such intermediaries include a network operator cell tower or LoRaWAN gateway. For example, an asset tracking use case might require IoT devices to send and receive data when kilometers away from a cell tower or a gateway. Another example is an indoor IoT solution for food safety, where a few hundred meters of distance to a cell tower or LoRaWAN gateway are sufficient for the purpose of the use case.

 For LPWAN, **range requirements** refer to the ability of your IoT device to send and receive data with an expected quality of service with the specified distance to the cell tower or a gateway. If your use case requires IoT devices to send and receive data with buildings or underground, then **indoor and underground coverage requirements** need to be considered. They refer to the expected ability of your IoT device to send and receive data, when there are obstacles such as walls between device and cell tower, or gateway.

 LPWAN technologies are optimized for long-range transmission and indoor coverage (for example, inside buildings or underground).

 Wi-Fi technology provides standards that support significant transmission ranges and indoor coverage. However, the power consumption of Wi-Fi devices can be higher than power consumption of LPWAN devices. If you consider Wi-Fi for your IoT solution, AWS recommends that you exercise special diligence in the evaluation of battery life and power consumption requirements described in the next section.

## Battery life and power consumption requirements
<a name="battery-life-and-power-consumption-requirements"></a>

 Battery life requirements apply to IoT use cases for device that operate from batteries. For such use cases, it’s important to define a needed duration of operation before battery replacement or recharge is required. The duration of battery-based operation is determined by the device’s power consumption and the battery capacity.

 The device’s power consumption depends on used radio transmission technology and device activity patterns. For example, devices that use LPWAN technologies such as LoRaWAN, NB-IoT, LTE-M, and Sigfox can operate for years on the same low-capacity battery (for example, AA/AAA or CR2032), assuming they only need to send and receive data infrequently and can spend most of the time in an energy-efficient sleep mode.

 However, if your use case requires devices to constantly listen for incoming messages, that would prevent devices from changing into the power saving model. That would significantly reduce the battery life regardless of the used wireless connectivity technology. For example, LoRaWAN Class C devices can constantly listen for incoming and more frequently send outgoing messages, at a price of having an external power source.

## Data rate and communication interval requirements
<a name="data-rate-and-communication-interval-requirements"></a>

 Data rate describes the amount of data per time period an IoT device will need to exchange with your application to fulfill the requirements of your use case. When evaluating data rate, both uplink and downlink data rate requirements are considered. The uplink data rate relates to the data your application is sending to the device for further processing. Examples of uplink data are sensor telemetry or video stream content from a security camera. The downlink data rate relates to the data your application is sending to the device. Examples of downlink data are device commands, device configuration updates, and firmware updates.

 The maximum data rate differs for each LPWAN. Examples include Sigfox with up to 0.1 kilobit/second, LoRaWAN with up to 5,47 kilobit/second, NB-IoT with up to 26 kilobit/second (downlink), and LTE-M (LTE Cat M1) with up to one megabit/second. Consider that use of higher data rates tends to result in higher power consumption, and shorter battery life.

 Communication interval requirements describe how frequently your use case requires the IoT device to send uplink or receive downlink. LPWAN technologies are used in use cases with infrequent communication (for example, few times a day to few times a week), while still maintaining context in the network for reachability. Using less frequent communication improves energy efficiency, allowing low-power operation, and longer battery life.

## Device mobility requirements
<a name="device-mobility-requirements"></a>

 Device mobility requirements describe if your use case requires your IoT devices to be stationary or moving. In the case of IoT devices that are moving, the important consideration is the area in which the devices are moving. If the IoT devices are sending and receiving data during the movement, velocity of movement is also considered.

 In general, LPWAN technologies support both stationary and mobile devices. However, device mobility requirements can have a significant influence to the selection of specific LPWAN technology for your use case. Consult the descriptions of individual LPWAN technologies in [Appendix: Characteristics of LPWAN technologies](appendix-characteristics-of-lpwan-technologies.md) to learn more about their support for device mobility.

 Not only will device mobility impact the specific LPWAN technology used, but it will also influence the decision to use private or public networks, because private networks are usually constrained to relatively small, fixed areas. If an IoT device has high-mobility requirements and will travel outside of a private network’s coverage area, it might need to join a public network.

 Finally, especially for use cases with cross-country mobility requirements, roaming capabilities of the network operator shall be considered. For example, by using roaming features of LTE-M and NB-IoT networks, IoT devices might establish connectivity in cross-country mobility scenarios. Similar concepts are also available for LoRaWAN and Sigfox.

 **Latency and reachability requirements**

 Latency can be defined as an amount of time it takes for a data sent by a device to arrive in a cloud application. For example, after a sensor measurement is performed by an IoT device, it should take no more than 10 seconds until this data can be processed by the cloud application. For LPWAN technologies, latency varies between milliseconds and a few seconds, depending on the selected LPWAN technology.

 Reachability can be defined as the amount of time it takes until data sent by a cloud application arrives at a device. For an example of reachability requirement, assume a use case where an IoT device has an attached actuator (a device that is capable of converting electrical signals into physical action, such as a relay for operating a power switch). The cloud application will be used to activate the actuator (for example, a power switch) on that IoT device. In this example, reachability is a duration until the command from the cloud application arrives at the device and the power switch state is changed. A possible requirement for reachability can be: **the switch change command from the cloud application shall arrive on the IoT device in less than 10 minutes**.

 If LPWAN connectivity is used on a battery-operated device, there is a trade-off between reachability duration and battery lifetime. This tradeoff is caused by the mechanism of energy-efficient power saving mode most LPWAN technologies offer. During power saving mode, power consumption is reduced, but devices are not capable of receiving downlink data. The longer time IoT devices are in listening mode, the lower the reachability and the higher the energy consumption.

 **Cost requirements**

 Cost considerations for individual connectivity technologies are out of scope for this whitepaper. However, AWS suggests that you consider the following costs when evaluating connectivity technologies:
+  Device costs for IoT devices, and possibly necessary gateways
+  Subscription and connectivity costs for network operators
+  Operating costs for software components

 **Security and regulatory**

 AWS recommends that you define security requirements for your use case and evaluate the connectivity technologies, in question, based on these requirements.

**Note**
Security evaluation of individual connectivity technologies is out of scope for this whitepaper.
