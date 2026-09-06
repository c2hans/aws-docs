---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/cost-optimization.html
---

# Cost optimization pillar
<a name="cost-optimization"></a>

The cost optimization pillar of the AWS Well-Architected Framework focuses on avoiding unnecessary costs. The following recommendations can help you meet the** **cost optimization design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Understanding spending over time and controlling fund allocation
+ Selecting resources of the right type and quantity
+ Scaling to meet business needs without overspending

## Implement cloud financial management
<a name="implement-cloud-financial-management"></a>
+ Forecast FSx for Windows File Server costs by using [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).
+ Plan and set expectations around FSx for Windows File Server costs by using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
+ Keep up to date with new service releases that can be used to optimize FSx for Windows File Server.
+ Consider combining billing for FSx for Windows File Server through a [unified tagging strategy](https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/).

## Adopt a consumption cost model
<a name="adopt-a-consumption-cost-model"></a>
+ Evaluate FSx for Windows File Server file system deployment options (Single-AZ or Multi-AZ). Choose the deployment option that meets your needs for the lowest price. For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) in the Amazon FSx documentation.
+ Evaluate FSx for Windows File Server file system storage types―solid state drive (SSD) or hard disk drive (HDD). Choose the storage type that meets your needs for the lowest price. For more information, see [Price and performance flexibility](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html#price-perf-flexibility) in the Amazon FSx documentation.

## Pay only for what you use
<a name="pay-only-for-what-you-use"></a>
+ Set the retention period for Amazon CloudWatch log groups that store FSx for Windows File Server logs. For more information, see the blog post [Reduce log-storage costs by automating retention settings in Amazon CloudWatch](https://aws.amazon.com/blogs/infrastructure-and-automation/reduce-log-storage-costs-by-automating-retention-settings-in-amazon-cloudwatch/).
+ Use the Microsoft Data Deduplication in Windows feature to identify and eliminate redundant data. For more information, see [Data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-data-dedup.html) in the Amazon FSx documentation.
+ Set user storage quotas on your file systems to limit the data storage that users can consume. For more information, see [Storage quotas](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-user-quotas.html) in the Amazon FSx documentation.
+ Set a retention period for FSx for Windows File Server file system backups and cleanup. For more information, see [Working with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html) in the Amazon FSx documentation.
