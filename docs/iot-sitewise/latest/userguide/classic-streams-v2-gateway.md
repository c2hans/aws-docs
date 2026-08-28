---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/classic-streams-v2-gateway.html
---

# Classic streams, V2 gateways for AWS IoT SiteWise Edge
<a name="classic-streams-v2-gateway"></a>

Understand the features and limitations of Classic streams, V2 gateways for AWS IoT SiteWise Edge.

The Classic streams, V2 gateway maintains traditional functionality familiar from earlier AWS IoT SiteWise deployments before the introduction of MQTT-enabled, V3 gateways. These SiteWise Edge gateways are considered Classic streams, V2 gateways. They maintain backward compatibility and are functional with the data processing pack. While the Classic streams, V2 gateway offers reliable performance for existing setups, it has limitations compared to newer gateway options. Specifically, this gateway type is not fully compatible with the advanced features available in the MQTT-enabled, V3 gateway destination. To use the MQTT messaging protocol, you can create a new MQTT-enabled, V3 gateway. For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md).

**Topics**
+ [Use packs to collect and process data in SiteWise Edge](data-packs.md)
+ [Configure the AWS IoT SiteWise publisher component](configure-publisher-component.md)
+ [Destinations and AWS IoT Greengrass stream manager](destinations-gg-stream-manager.md)
+ [Configure edge capabilities on AWS IoT SiteWise Edge](edge-data-collection-and-processing.md)
+ [Configure edge data processing for AWS IoT SiteWise models and assets](edge-processing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
