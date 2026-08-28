---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/approaches.html
---

# Modernization approaches
<a name="approaches"></a>

When it comes to historian modernization, you can take any of the following approaches:
+ [Migrate existing OT system applications to an on-premises containerized platform](#migrate-containerized-platform)
+ [Adopt an existing cloud-based solution](#existing-cloud-solution)
+ [Create a custom cloud-based solution](#custom-solution)

## Migrate existing OT system applications to an on-premises containerized platform
<a name="migrate-containerized-platform"></a>

This approach involves the transfer of data and applications from the existing system to a modern platform that provides increased performance and scalability.

![A containerized platform deployed across multiple factories.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/images/guide-img/600bf5f6-76d8-4aa3-9ff9-c13baa9d233a/images/de0b5448-138c-461e-a528-d83c1b82e617.png)

## Adopt an existing cloud-based solution
<a name="existing-cloud-solution"></a>

This approach involves using available cloud-based products, such as those available in the [AWS Marketplace](https://aws.amazon.com/marketplace), to store and manage data. The cloud provides increased scalability and can improve data security. Additionally, you can also use cloud-based solutions to automate and streamline the manufacturing process.

![On-premises historians forwarding data to a modern application in the cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/images/guide-img/600bf5f6-76d8-4aa3-9ff9-c13baa9d233a/images/ee1dd272-df33-49f0-93d5-c113ea6d7611.png)

## Create a custom cloud-based solution
<a name="custom-solution"></a>

When you build a custom solution, you can forward data from on-premises historians to a modernized, enterprise historian in the cloud. Alternatively, you can eliminate on-premises historians, collect and process data in an edge network, and then store and process data in the cloud. The architecture of a custom solution depends on the unique use cases of your organization. For a sample custom solution, see [Delivering Industrial DataOps on Industrial Data Fabric](https://docs.aws.amazon.com/architecture-diagrams/latest/delivering-dataops-on-industrial-data-fabric/delivering-dataops-on-industrial-data-fabric.html#diagram1). If you'd like support developing a custom solution, contact [AWS Professional Services](https://pages.awscloud.com/AWS-Professional-Services.html).

A modern, cloud-native historian approach focuses on number of activities, including:
+ Standardize views of processes and machine models.
+ Integrate enterprise cloud-based historians with data stores for advanced analytics.
+ Perform advanced AI/ML analyses of cold data to provide preventive maintenance, anomaly detection, and predictive quality insights.
+ Use a cloud-native, centralized data store as an enterprise historian, and use fully managed AWS services, such as [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) and [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html).
+ Configure multi-tier, cloud-optimized services to store time-series data. For hot data, you can use AWS IoT SiteWise or Timestream. For cold data, you can use [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ Enhance product quality with real-time analytics services that process data at the edge, such as AWS IoT SiteWise.

For more information about the benefits of using AWS services to modernize historians in the cloud, see [Using AWS to modernize historians](using-aws.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
