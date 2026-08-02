---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/cost.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost
<a name="cost"></a>

 All AWS services included in this implementation guide have a pay-as-you-go pricing model, which scales relative to the demand placed on the application. There are no upfront or monthly commitments.

 There are no additional charges for using AWS IoT Core for LoRaWAN, beyond AWS IoT Core charges incurred from messaging. However, if additional AWS IoT Core features are used in conjunction with the deployment, connectivity, [device shadow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html), registry, and [rules engine](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html), charges may apply.

 The cost of [AWS Lambda](https://aws.amazon.com/lambda/), used in the solution to decode LoRaWAN payloads, is based on the number of times the function is run, and the duration it runs for.
