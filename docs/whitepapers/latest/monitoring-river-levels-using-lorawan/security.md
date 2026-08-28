---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

 LoRaWAN devices encrypt their binary messages using [AES128 CTR](https://xilinx.github.io/Vitis_Libraries/security/2020.1/guide_L1/internals/ctr.html) mode before they are transmitted over the air. Transport Layer Security (TLS) encryption is used further upstream between the LoRaWAN gateway and AWS IoT Core.

 Refer to [Data Security with AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-security.html) for details on how data security is addressed between each component.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
