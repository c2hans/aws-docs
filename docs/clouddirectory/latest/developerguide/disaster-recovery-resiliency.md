---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/disaster-recovery-resiliency.html
---

Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Resilience in Amazon Cloud Directory
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. Cloud Directory was built on those principles and is available in multiple AWS Regions, which are physically isolated from each other. Within each Region, the service is further supported through at least three Availability Zones, minimizing service downtime due to nonavailability of any single Availability Zone.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).
