---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/common-scaling-challenges.html
---

# Common scaling challenges
<a name="common-scaling-challenges"></a>

A data lake goes through several stages when its data grows after the initial deployment. If you didn't use scalable architecture to design your data lake, your organization might encounter challenges and can be disadvantaged by the data lake's growth.

The following sections explain how a typical data lake's growth can cause scaling challenges.

## Initial data lake deployment
<a name="initial-deployment"></a>

The following diagram shows a data lake's architecture after its initial deployment by Line of business A.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/2ede26a7-96c8-48b5-8a76-0e460dc1d9b8.png)

The diagram shows the following components:
+ The data producer account collects and processes data, stores the processed data, and prepares it for consumption.
+ Data in the data producer account is stored in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) buckets, which can have multiple data layers.
+ You can use AWS services for data processing (for example, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)).
+ The data producer not only produces and stores data in the data lake but then also needs to decide what data to share with a data consumer and how to share it. AWS Lake Formation manages the data lake in the data producer account, in addition to managing cross-account data sharing from the data producer to the data consumer.
+ The data consumer account consumes shared data from the data producer account for specific business use cases.

## Data consumers increase
<a name="data-consumers-increase"></a>

The following diagram shows that more data is brought into the data lake when Line of business A's data grows. The data lake then attracts more data consumers to leverage and gain value from the data.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/ec8a9b4e-e527-451b-a2d9-04934444dc62.png)

The diagram shows how an organization generates nearly continuous value from an existing data asset and that this attracts more data consumers. However, when data consumers increase, the data producer only has the following two options to accommodate this growth:
+ Manually manage data sharing and access by individual data consumers, which is not a scalable approach.
+ Develop an automated or semi-automated process for data sharing and managing data access. Although this could be a scalable option, it requires significant time and effort to design and build because internal and external data consumers have different security control requirements. In the future, additional time and effort would also be required for any solution improvements.

## Data producers increase
<a name="data-producers-increase"></a>

The following diagram shows the data lake architecture when multiple lines of business join as data producers.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/c286682d-9cb3-4ddb-aafd-aba8763ff956.png)

The data lake's architecture becomes increasingly complicated, even with only three data producers and three data consumers.

Each data producer needs to handle data sharing and data access management for multiple data consumers. It is unrealistic to expect all data producers to develop an automated or semi-automated process for data sharing and data access management. Some data producers might choose to not share their data and therefore avoid unaffordable management overhead. Similarly, each data consumer needs to interact with multiple data producers to understand their different data consumption processes. This means that individual data consumers face increasing management overhead for handling different data-sharing patterns.

In many organizations, this data lake causes bottlenecks and cannot grow or scale. This might mean that your organization must redesign and rebuild its data lake to remove the bottleneck, which can cost significant time, resources, and money.
