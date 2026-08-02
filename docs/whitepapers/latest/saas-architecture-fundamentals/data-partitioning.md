---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/data-partitioning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data partitioning
<a name="data-partitioning"></a>

 *Data partitioning* is used to describe different strategies used to represent data in a multi-tenant environment. This term is used broadly to cover a range of different approaches and models that can be used to associate different data constructs with individual tenants.

 Note that there is often a temptation to view data partitioning and tenant isolation as interchangeable. These two concepts are not meant to be equivalent. When we talk about *data partitioning*, we are talking about how tenant data is stored for individual tenants. Partitioning data does not ensure that the data is isolated. Isolation must still be applied separately to ensure that one tenant can’t access the resources of another tenant.

 Each AWS storage technology brings its own set of considerations to the data partitioning strategy. For example, isolating data in Amazon DynamoDB will look very different than isolating data with [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS).

 Generally, when you think about data partitioning, you start by thinking about whether the data will be siloed or pooled. In a siloed model, you have a distinct storage construct for each tenant with no co-mingled data. For pooled partitioning, the data is co-mingled and partitioned based on a tenant identifier that determines which data is associated with each tenant.

 As an example, with Amazon DynamoDB, a siloed model uses a separate table for each tenant. Pooling data in Amazon DynamoDB is achieved by storing the tenant identifier in the partition key of each Amazon DynamoDB table that manages data for all tenants.

 You can imagine how this might vary across the range of AWS services, with each one introducing its own constructs that may require a different approach to realizing silo and pooled storage models with each service.

 While data partitioning and tenant isolation are separate topics, the data partitioning strategies you choose are likely to be influenced by the isolation model of your data. For example, you might silo some storage because that approach best aligns with the requirements of your domain or customers. Or, you might choose silo because the pool model may not allow you to enforce isolation with the level of granularity that your solution requires.

 Noisy neighbor can also impact your approach to isolation. Some workloads or use cases in your application may need to be kept separate to limit impacts from other tenants or to meet service level agreements (SLAs).
