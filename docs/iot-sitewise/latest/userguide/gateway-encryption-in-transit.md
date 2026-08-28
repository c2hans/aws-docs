---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-encryption-in-transit.html
---

# Data in transit between local components on SiteWise Edge
<a name="gateway-encryption-in-transit"></a>

SiteWise Edge gateways run on AWS IoT Greengrass, which doesn't encrypt data exchanged locally on the AWS IoT Greengrass core because the data doesn't leave the device. This includes communication between AWS IoT Greengrass components such as the AWS IoT SiteWise connector. For more information, see [Data on the core device](https://docs.aws.amazon.com/greengrass/v1/developerguide/encryption-in-transit.html#data-in-transit-locally) in the *AWS IoT Greengrass Version 1 Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
