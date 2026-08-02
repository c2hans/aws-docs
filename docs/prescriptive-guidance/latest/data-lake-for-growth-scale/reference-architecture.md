---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/reference-architecture.html
---

# Reference architecture
<a name="reference-architecture"></a>

The following diagram shows this guide's reference architecture for growing and scaling a data lake on the AWS Cloud.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/76ed6d32-cb10-48fb-b937-80c2da72967b.png)

The diagram shows the following components:

1. A data producer layer in different AWS accounts.

1. A data consumer layer in different AWS accounts.

1. A centralized catalog in an AWS account.

1. Although each line of business only has one data producer and one data consumer, the guide's reference architecture supports multiple data producers and data consumers for each line of business. It's typical to onboard one data producer with one or multiple data consumers that include both data-serving and application types. For more information about this, see the [Reference architecture components ](reference-architecture-components.md)section of this guide.

1. The centralized catalog is the interface used by data producers and data consumers to share and consume data.

The reference architecture's approach makes it possible to standardize data sharing and consumption, and independently scale data producers and data consumers without growing your management overhead. The reference architecture also enables data production and distribution across different data producers. Any data producer can be part of the data lake, share their data, and contribute to the overall value provided by the data lake.

This approach enables your organization to harvest data value throughout your lines of business and external data owners, without causing a bottleneck by constraining data collection and processing in a single pipeline.
