---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/lake-house-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Lake house architecture
<a name="lake-house-architecture"></a>

 Game developers often use data warehouse alongside a data lake. Data warehouse can provide lower latency and better performance of SQL queries working with local data. That’s why one of the common use-cases for the data warehouse in games analytics is building daily aggregations to be consumed from business intelligence (BI) solutions. Games can generate a lot of data, even logging activity down to the key stroke. This can result in having to process terabytes of data every day, and the data may reside in, or need to be loaded into, different data stores. These data stores can be a cache such as [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/), a relational database such as [Amazon Aurora](https://aws.amazon.com/rds/aurora/), a NoSQL database such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and log data potentially being stored in Amazon S3. The challenge then becomes having to manage that data, and finding ways to get meaningful insights throughout your repositories.

 For example, DynamoDB performs well for specific use cases such as reading and writing data with single digit millisecond latency. But it should not be used as a source for your analytical queries, as there is no one tool that is perfect for every job. Having a lake house architecture allows customers to easily move data to and from their data stores in a fast and secure manner. This also allows customers to connect their data lake to their databases and data warehouses using the [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html), which is integrated with many AWS services.

 Instead of building a siloed data warehouse, you can use technologies to integrate data lake with it. For example, use [Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) to query data directly from the S3 data lake, or the [Amazon Redshift](https://aws.amazon.com/redshift/) [COPY](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source-s3.html) command to load data from S3 directly into Amazon Redshift in a parallelized way. Many customers don’t want to have to load ten or 20 years’ worth of data into their data warehouse when they rarely need to query it. Extending your data warehouse to a data lake is a great option in this case, as you can keep your historical (cold) data in your data lake to help save on cost, and use your data warehouse to query your data lake when necessary.

 Refer to [Derive Insights from AWS Modern Data](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.html) for more details, and the [Build a Lake House Architecture on AWS](https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/) blog entry for a deep dive.

![A diagram depicting AWS lake house architecture.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/lake-house-architecture.png)
