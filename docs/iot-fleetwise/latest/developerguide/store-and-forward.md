---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/store-and-forward.html
---

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Store and forward campaign data
<a name="store-and-forward"></a>

**Important**
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

Use data partitions within campaigns to temporarily store signal data on the Edge for vehicles and fleets. By configuring upload and storage options for data partitions, you can optimize your ideal conditions for data forwarding to your designated data destinations (like an Amazon S3 bucket). For example, you can configure the data partition to store data on a vehicle until it connects to Wi-Fi. Then, once the vehicle connects, the campaign triggers the data in that particular partition to be sent to the cloud. Alternatively, you can collect data using AWS IoT Jobs.

**Topics**
+ [Create data partitions](create-campaign-data-partitions.md)
+ [Upload campaign data](update-campaign-cli-data-partitions.md)
+ [Upload data using AWS IoT Jobs](update-campaign-cli-data-partitions-jobs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
