---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-solutions-with-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing Low-Power Wide-Area Network (LPWAN) Solutions with AWS IoT
<a name="implementing-lpwan-solutions-with-aws"></a>

Publication date: **December 17, 2021** ([Document history](document-revisions.md))

 This whitepaper helps Amazon Web Services (AWS) customers to implement their Internet of Things (IoT) solutions with low-power wide-area network (LPWAN) connectivity technologies. First, this paper provides customers with a decision framework, to help them decide if LPWAN is the right choice for their IoT use case. Then, it provides an overview of LPWAN connectivity technologies and their capabilities, as well as implementation guidelines for implementing Narrowband Internet of Things (NB IoT), [LTE-M](https://en.wikipedia.org/wiki/LTE-M), Long Range Wide Area Network (LoRaWAN), and [Sigfox](https://www.sigfox.com/en) connectivity for the IoT applications. Finally, a detailed description of NB-IoT, LTE-M, LoRaWAN, and Sigfox technologies is provided in the appendix.

 This whitepaper is intended for technical architects, IoT cloud engineers, IoT security architects, and embedded engineers.

## Introduction
<a name="introduction"></a>

 When building Internet of Things (IoT) solutions on AWS, you have a broad choice of wired and wireless connectivity options. For example, in the area of wireless connectivity, you can choose from short range connectivity (for example, Bluetooth Low Energy (BLE), Zigbee, or Z-Wave), a low-power wide-area network (LPWAN) (for example, LoRaWAN, Narrowband Internet of Things (NB-IoT), LTE-M, or Sigfox), cellular (for example, LTE Cat 4), and satellite. This broad range of choices allows you to address specific requirements of individual use cases. It also introduces a certain complexity in the selection process. Because choosing a specific connectivity option can be costly to reverse (due to the impact on hardware design and procurement), a special diligence is required when selecting connectivity technology.

 This whitepaper focuses on LPWAN connectivity technologies. First, it will help you to decide if LPWAN connectivity technologies are appropriate for a specific use case. Next, it provides you with information about the differences between individual LPWAN technologies, allowing you to make better trade-off decisions. Finally, it provides you with guidelines for implementing individual LPWAN technologies using AWS. The scope of this whitepaper is illustrated in the following diagram:

![Diagram showing various connectivity technologies, such as near field, short range, WiFi, cellular networks, and satellite networks.](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/connectivity-tech.png)

 When building IoT solutions, a decision for any connectivity technology shall be based on the requirements of the use cases and applications. The next section explores a framework you can use to evaluate these requirements.
