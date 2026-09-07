---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/what-is-a-modern-data-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# What is a Modern Data architecture?
<a name="what-is-a-modern-data-architecture"></a>

 Many organizations are moving their data from various silos into a data lake, where they have a single place to apply machine learning and analytics. The vast majority of data lakes are built on [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3). At the same time, customers are leveraging purpose-built analytics stores that are optimized for specific use cases. Customers want the freedom to move data between their centralized data lakes and the surrounding purpose-built analytics stores in a seamless, secure, and compliant way, to get insights with speed and agility. We call this modern approach to analytics Modern Data architecture.

![Diagram showing Modern Data architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/modern-data-architecture.png)

 Modern Data architecture is an evolution from data warehouse and data lake-based solutions. The following table lists this evolution from data and performance characteristics.

* Table 1: Evolution of data and analytics architectures to Modern Data *

|   |  Data warehouse  |  Data lake  |  Modern Data  |
| --- | --- | --- | --- |
|  Data  |  Relational data from transactional systems, operational databases, and line of business applications  |  All data, including structured, semi-structured, and unstructured  |  Modern Data is the next step of the evolution that enables querying data across data warehouse, data lake, and databases  |
|  Performance  |  Fastest query results using local storage  |  Query results getting faster using low-cost storage and decoupling of compute and storage  |  Faster and deeper insights without moving data  |
