---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lorawan.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# LoRaWAN
<a name="lorawan"></a>

 The LoRaWAN is an LPWAN standard specified by the LoRa Alliance. The LoRa Alliance describes LoRaWAN as “a Low Power, Wide Area networking protocol designed to wirelessly connect battery operated ‘things’ to the internet in regional, national or global networks, and targets key Internet of Things (IoT) requirements such as bi-directional communication, end-to-end security, mobility and localization services”.

 When using LoRaWAN, both public and private deployment modes are supported. In a public deployment mode, IoT devices can access a public LoRaWAN network, operated by the LoRaWAN network provider and shared by several customers. In private deployment mode, you can build and operate your own LoRaWAN network.

## Range and coverage
<a name="range-and-coverage-2"></a>

 LoRaWAN specification is based on LoRa radio frequency modulation technique, which is patented by Semtech Corporation. LoRa is operated in license free ISM (industrial, scientific, and medical) frequency bands, for example 433 MHz/868 MHz in Europe, or 915 MHz in US. LoRa uses modulation technique based on Chirp Spread Spectrum, allowing transmission range of up to 20 km in line of sight, and up to five km in urban areas. The actual range depends on environment (for example, existence of obstacle for the radio signal), transmission configuration (for example, transmission power), and positioning of gateways.

 LoRa radio frequency modulation technique is suitable for use cases that require indoor and underground coverage, because the radio signal can penetrate physical barriers such as walls or ceilings.

## Data rate
<a name="data-rate-2"></a>

 When using LoRaWAN, the data rate is limited to 0,3 Kbit/s to 27 Kbit/s. The effective maximum data rate depends the spread factor used by the device.

## Mobility
<a name="mobility-2"></a>

 LoRaWAN can be used for use cases requiring stationary and moving devices, assuming availability of network coverage on the device location. When using LoRaWAN protocol, a device payload will be received by all the gateways within reach. Each of gateways receiving payload from the device will forward this payload to the LoRaWAN network server. The LoRaWAN network server will perform a deduplication of the message.

## Battery life
<a name="battery-life-1"></a>

 A battery can last several years without replacement. However, note that long battery duration is only possible when operating LoRaWAN devices as Class A and B (for example, devices that are sleeping most of the time).

## Spectrum licensing
<a name="spectrum-licensing-2"></a>

 LoRaWAN operates in a license-free spectrum; however, region-specific regulations apply. For example, duty cycle regulations in the EU define the maximum air time for a LoRaWAN device.

## Application payload size
<a name="application-payload-size"></a>

 LoRaWAN maximum application payload size depends both on the LoRaWAN frequency plan (for example, EU868 or US915) and the LoRaWAN data rate (for example, 0 or 7) the device is using for the transmission. Consult the [LoRaWAN Regional Parameters](https://lora-alliance.org/resource_hub/rp2-102-lorawan-regional-parameters/) for a detailed description of the maximum payload size for each country. Note that the term *LoRaWAN data rate,* in this and the next section, is LoRaWAN-specific and is used to describe a combination of Spreading Factor (for example, SF7) and bandwidth (125 Khz).

 An application payload size of 11 bytes is supported in most frequency plans (for example, EU868 and US915) with any of the LoRaWAN data rates. If your application requires larger payload sizes, a thorough research is recommended. For example, according to the chapter 2.4.6 “EU863-870 Maximum payloads size” of [RP2-1.0.2 LoRaWAN Regional Parameters](https://lora-alliance.org/resource_hub/rp2-102-lorawan-regional-parameters/), the maximum payload size when using Data Rate 0 is 51 bytes, assuming the fields of proficiency testing (FOpt) field is used.

## Latency and reachability
<a name="latency-and-reachability"></a>

 When using LoRaWAN, typical latency is in the order of magnitude of seconds. Reachability depends on device class.

 Class A devices are in energy-efficient power saving mode most of the time and listen for downlink messages only for a short period of time after transmitting. Because of this energy-saving mechanism they also have the longest reachability. These devices are battery-powered sensors.

 Class B devices can receive downlink messages in scheduled downlink slots, so that they have improved reachability compared to Class A devices. Class B devices are battery-powered actuators.

 Class C devices continuously listen for the incoming messages. Because of this they have the better (shorter) reachability in order of magnitude of seconds.

## Further considerations
<a name="further-considerations-2"></a>

 Although out of scope for this whitepaper, other important considerations for LoRaWAN are security, device, and operation and subscription costs and local regulatory requirements.
