---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-iot-solutions-on-aws-using-lorawan.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing LPWAN IoT solutions on AWS using LoRaWAN
<a name="implementing-lpwan-iot-solutions-on-aws-using-lorawan"></a>

 LoRa Alliance specifies the LoRaWAN protocol in documents called LoRaWAN specifications. Although LoRaWAN operates in the unlicensed radio spectrum, manufacturers and operators of LoRaWAN devices still have to fulfill various country-specific regulations. To account for this, LoRa Alliance also publishes regional parameters documents specify a common denominator per country as a recommendation (but not specification) for device manufacturers and operators.

 *Table 2 – LoRaWAN specifications*

|  Version  |  Year  |  Major changes  |   |  Download specification  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|  1.0  |  2015  |  Initial release  |   |   |   |   |
|  1.0.1  |  2016  |  Clarifications / corrections  |   |   |   |   |
|  1.0.2  |  2016  |  Separation of regional parameters  |   |   |   |   |
|  1.1  |  2017  |  Roaming added, security features added  |   |   |  [1.1](https://lora-alliance.org/resource_hub/lorawan-specification-v1-1/)  |   |
|  1.0.3  |  2018  |  Class B added as normative  |   |   |  [1.0.3](https://lora-alliance.org/resource_hub/lorawan-specification-v1-0-3/)  |   |
|  1.0.4  |  2020  |  Class B improved, security improved, clarifications  |   |   |  [1.0.4](https://lora-alliance.org/resource_hub/lorawan-104-specification-package/)  |   |

 The LoRaWAN Regional Parameters document describes the recommended configurations and parameters for different regions worldwide. They are separated from the protocol specification to allow the addition of new regions without impacting the LoRaWAN specification. You can download the most recent version (RP2-1.0.2) of the [LoRaWAN Regional Parameters](https://lora-alliance.org/resource_hub/rp2-102-lorawan-regional-parameters/).

**Topics**
+ [LoRaWAN network architecture](lorawan-network-architecture.md)
+ [LoRaWAN networks](lorawan-networks.md)
+ [Building a private LoRaWAN network](building-a-private-lorawan-network.md)
+ [Public LoRaWAN networks](public-lorawan-networks-1.md)
