---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/gateways.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Gateways
<a name="gateways"></a>

 Amazon Monitron uses gateways to transfer the data collected by the Amazon Monitron Sensors to the AWS Cloud. Gateways are positioned in factories within 20 to 30 meters of the sensors. They communicate with the sensors over Bluetooth Low Energy (BLE), and with the AWS Cloud using either Wi-Fi or Ethernet.

This topic explains how to install your Ethernet and Wi-Fi gateways. It also explains how to delete an unnecessary gateways.

**Note**
Once you've added a gateway to your project, you can edit the gateway's name to help you find it fast.

**Topics**
+ [Ethernet gateways](setting-up-ethernet-gateways.md)
+ [Wi-Fi gateways](setting-up-Wi-Fi-gateways.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
