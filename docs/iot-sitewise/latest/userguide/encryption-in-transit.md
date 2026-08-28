---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/encryption-in-transit.html
---

# Data encryption in transit for AWS IoT SiteWise
<a name="encryption-in-transit"></a>

AWS IoT SiteWise uses encryption in transit to secure the data transmitted between your devices, gateways, and the AWS Cloud. Communication with AWS IoT SiteWise is encrypted using HTTPS and TLS 1.2, ensuring that your data remains confidential and protected from unauthorized access or interception.

There are three modes of communication where data is in transit:
+ [Over the internet](internet-encryption-in-transit.md) – Communication between local devices (including SiteWise Edge gateways) and AWS IoT SiteWise is encrypted.
+ [Over the local network](local-encryption-in-transit.md) – Communication between OpsHub for SiteWise application and SiteWise Edge gateways is always encrypted. Communication between the SiteWise monitor application running within your browser and SiteWise Edge gateways is always encrypted. Communication between SiteWise Edge gateways and OPC UA sources can be encrypted.
+ [Between components on SiteWise Edge gateways](gateway-encryption-in-transit.md) – Communication between AWS IoT Greengrass components on SiteWise Edge gateways isn't encrypted.

**Topics**
+ [Data in transit over the internet](internet-encryption-in-transit.md)
+ [Data in transit over the local network](local-encryption-in-transit.md)
+ [Data in transit between local components on SiteWise Edge](gateway-encryption-in-transit.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
