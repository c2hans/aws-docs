---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lte-m.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# LTE-M
<a name="lte-m"></a>

 LTE-M is an LPWAN technology developed by 3rd Generation Partnership Project (3GPP). LTE-M standard LTE Cat M1 was first specified as part of 3GPP Release 13, and then updated as standard LTE Cat M2 as part of 3GPP Release 14. For simplicity, this whitepaper will further use LTE-M synonymous with LTE Cat M1.

 When using LTE-M, devices communicate by IP protocol, although non–IP based communication is technically possible.

## LTE-M compared to NB-IoT
<a name="lte-m-compared-to-nb-iot"></a>

 Although LTE-M has many similar characteristics as NB-IoT, there are differences. Compared to NB-IoT, LTE-M tends to offer higher data rates, lower latency, better energy efficiency for big payloads, and is better suited for mobile applications than NB-IoT. LTE-M devices tend to have higher power consumption for small payloads and higher end device costs compared to NB-IoT devices.

## Range and coverage
<a name="range-and-coverage-1"></a>

 LTE-M transmission range in terms of maximum distance between the tower and the IoT device is approximately one km in urban areas, and approximately 10 km in rural areas. LTE-M supports indoor coverage.

## Data rate
<a name="data-rate-1"></a>

 For LTE Cat M1, peak data rate is 1 MBps both in uplink and downlink.

## Mobility
<a name="mobility-1"></a>

 LTE-M technologies can be used for use cases with fixed and mobile assets (for example, mobile fleet management or mobile asset tracking), assuming availability of network coverage on device location. Compared to NB-IoT, LTE-M is better suited for use cases requiring asset mobility. The first reason is handover support. When an LTE-M device is moving from one cell tower to another, it can seamlessly switch the connection to the new cell tower while staying attached to the network. Avoiding a need to detach from an old cell tower and perform a reattachment to the new cell tower results in increased energy efficiency and continuous connectivity.

## Battery life
<a name="battery-life"></a>

 A battery can last several years without replacement, given appropriate engineering and configuration of the IoT device. For example, reduction of uplink frequency and using battery saving features, PSM and eDRX, can be helpful to increase energy efficiency.

 The principles behind PSM and eDRX for LTE-M are similar to those for NB-IoT as described in the previous section. However, note that differences in the implementation between LTE-M and NB-IoT apply, for example for eDRX cycle durations and other parameters.

## Latency
<a name="latency"></a>

 When using LTE Cat M1, typical latency is between 10 and 20 ms.

## Spectrum licensing
<a name="spectrum-licensing-1"></a>

 LTE-M uses licensed spectrum. 3GPP Release 13 defines 19 frequency bands for LTE-M, with two additional bands added in 3GPP Release 14.

## Payload size
<a name="payload-size-1"></a>

 The exact maximum payload size when using NB-IoT depends on used connectivity module, used mobile network, and chosen approach for integration with your cloud application. For example, a message packet (including IP header) greater than 1,280 bytes risks being truncated and undeliverable. Because of these dependencies, AWS recommends consulting both your connectivity module manufacturer and network operator in that matter.

## Further considerations
<a name="further-considerations-1"></a>

 Although out of scope for this whitepaper, other important considerations for LTE-M are security, device and subscription cost, and carrier roaming agreements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
