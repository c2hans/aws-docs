---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/nb-iot.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# NB-IoT
<a name="nb-iot"></a>

 Narrowband Internet of Thing (NB-IoT) is an LPWAN technology developed by 3rd Generation Partnership Project (3GPP). NB-IoT standard LTE Cat NB1 was first specified as part of 3GPP Release 13 and then updated as LTE Cat NB2 as part of 3GPP Release 14. For simplicity, this whitepaper will use NB-IoT synonymous with LTE Cat NB1.

 The design principles of NB-IoT are long device battery life, low device complexity, support for massive number of devices, and support for high coverage to reach devices in wide areas as well as in challenging locations. When using NB-IoT, devices communicate by IP protocol, although non–IP based communication is technically possible.

 NB-IoT is a wireless cellular network technology. A *cell* is a geographical area in which the IoT device can communicate over radio with the transceiver station. The transceiver station is called a *base station* or *cell tower*.

## Range and coverage
<a name="range-and-coverage"></a>

 NB-IoT transmission range, in terms of distances between cell tower and the IoT device, is approximately one km in urban areas, and approximately 10 km in rural areas. NB-IoT supports indoor coverage.

## Data rate
<a name="data-rate"></a>

 For NB-IoT, peak data rate is approximately 26 Kbps in downlink and approximately 66 Kbps in uplink when using multi-tone uplink mode, and approximately 20 Kbps when using single-tone uplink mode.

## Mobility
<a name="mobility"></a>

 NB-IoT is frequently used in applications and use cases with stationary assets (for example, smart metering or smart parking). LTE-M technologies such as LTE Cat M1 are more frequently used for use cases with mobile assets. This is mostly because LTE Cat NB1 technology has limited support for handover between cells. Without handover support, energy-consuming detach and reattach procedures, and related intermittent connectivity are necessary on each cell change.

 **Latency**

 When using NB-IoT, latency is from 1.6 seconds to 10 seconds.

 **Battery life**

 A battery can last several years without replacement, given appropriate engineering and configuration of the IoT device. For example, reduction of uplink frequency and using battery saving features, Power Saving Mode (PSM) and Extended Discontinuous Reception Mode (eDRX), can help increase energy efficiency.

 By using PSM, device engineers can set a device in an energy-efficient extended power saving model for up to 14 days. During extended sleep, the device remains registered in the network, but network is not paging the device. The device can wake up when it needs to send data, and is reachable for downlink for a brief time interval after each data transfer. Because the device remains registered in the network, it does not need to perform an energy-consuming reattach procedure after waking up. By not paging the device during extended sleep, additional energy saving can be achieved.

 By using eDRX, device software engineers can adjust device low-power sleep time, which is defined by the network and is often approximately 10 seconds by default. By using eDRX, this wakeup period can be extended to up to approximately 175 minutes. By using eDRX, device software engineers can adjust a tradeoff between energy efficiency and device reaction times. For example, if the application for smart street lights sets eDRX interval of approximately 2.7 min, it can take up to 2.7 minutes until the command from the cloud application to turn on the lights arrives at the device.

 Although eDRX does not provide the same level of energy efficiency as PSM, it offers significantly shorter wake-up times than PSM. Also note that both support and upper limits for PSM and eDRX depend on network operator and used device. AWS suggests you contact your network operators and device vendors for further information.

## Spectrum licensing
<a name="spectrum-licensing"></a>

 NB-IoT uses licensed spectrum. 3GPP Release 13 defines 14 frequency bands for NB-IoT, with four additional bands added in 3GPP Release 14, and four more bands added in 3GPP Release 15.

## Payload size
<a name="payload-size"></a>

 LTE-M supports payloads up to 1,280 bytes when using IP protocol. However, the exact maximum payload size depends on connectivity module and mobile network used, and chosen approach for integration with your cloud application (for example, by IPsec). Because of these dependencies, AWS recommends that you consult both your connectivity module manufacturer and network operator.

## Further considerations
<a name="further-considerations"></a>

 Although out of scope for this whitepaper, other important considerations for LTE-M are security, device, and subscription cost and carrier roaming agreements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
