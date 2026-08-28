---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-create-resources.html
---

# Create network analyzer configuration and add resources
<a name="network-analyzer-create-resources"></a>

Before you can stream trace messages, create a network analyzer configuration and add the resources you want to monitor to this configuration. A LoRaWAN network analyzer configuration is a set of settings and rules that define how network analyzer should capture and analyze traffic in a LoRaWAN network. It specifies the types of information and messages that should be included in the network trace, and any filtering or processing rules that should be applied.

a LoRaWAN network analyzer configuration providesvisibility into the communication between LoRaWAN devices and the network server. This enables troubleshooting, performance monitoring, and security analysis of the LoRaWAN network.

When you create a configuration, you can:
+ Specify a configuration name and optional description.
+ Customize the configuration settings such as frame info and level of detail for your log messages.
+ Add the resources that you want to monitor. The resources can be wireless devices or wireless gateways, or both.

The configuration settings that you specify will determine the trace messaging information that you'll receive for resources you add to the configuration. You may also want to create multiple configurations depending on your monitoring use case.

The following shows how to create a configuration and add resources.

**Topics**
+ [Create a network analyzer configuration](network-analyzer-create.md)
+ [Add resources and update the network analyzer configuration](network-analyzer-resources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
