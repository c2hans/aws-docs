---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/latest-version.html
---

# Use the latest AWS Glue version
<a name="latest-version"></a>

We recommend using the latest AWS Glue version. There are several optimizations and upgrades built into each version that might automatically improve job performance. For example, AWS Glue 4.0 provides following new features:
+ **New optimized Apache Spark 3.3.0 runtime** – AWS Glue 4.0 builds upon the Apache Spark 3.3.0 runtime, bringing comparable performance improvements to open source Spark. The Spark 3.3.0 runtime builds upon many of the innovations from Spark 2.x.
+ **Enhanced Amazon Redshift connector** – AWS Glue 4.0 and later versions provide Amazon Redshift integration for Apache Spark. The integration builds on an existing open source connector and enhances it for performance and security. The integration helps applications perform up to 10 times faster. For more information, see the blog post about [Amazon Redshift integration with Apache Spark](https://aws.amazon.com/blogs/aws/new-amazon-redshift-integration-with-apache-spark/).
+ **SIMD-based execution for vectorized reads with CSV and JSON data** – AWS Glue version 3.0 and later versions add optimized readers that can significantly speed up overall job performance compared with row-based readers. For more information about CSV data, see [Optimize read performance with vectorized SIMD CSV reader](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-csv-home.html#aws-glue-programming-etl-format-simd-csv-reader). For more information about JSON data, see [Using vectorized SIMD JSON reader with Apache Arrow columnar format](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-json-home.html#aws-glue-programming-etl-format-simd-json-reader).

Each AWS Glue version will include upgrades of this sort, among many, including connectors, driver and library updates. For more information, see [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) and [Migrating AWS Glue jobs to AWS Glue version 4.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-40.html).
