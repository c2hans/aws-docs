---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html
---

# Partitions
<a name="partitions"></a>

 AWS groups Regions into [partitions](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). Every Region is in exactly one partition, and each partition has one or more Regions. Partitions have independent instances of AWS Identity and Access Management (IAM) and provide a hard boundary between Regions in different partitions. AWS commercial Regions are in the `aws` partition, Regions in [China](https://www.amazonaws.cn/en/about-aws/china/) are in the `aws-cn` partition, [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) Regions are in the `aws-us-gov` partition, and the [AWS European Sovereign Cloud](https://aws.amazon.com/compliance/europe-digital-sovereignty/) is the `aws-eusc` partition. Some AWS services are designed to provide cross-Region functionality, such as [Amazon Simple Storage Service (Amazon S3) Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario) or [AWS Transit Gateway Inter-Region peering](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html). These types of capabilities are only supported between Regions in the same partition. You can’t use IAM credentials from one partition to interact with resources in a different partition.
