---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/next-steps.html
---

# Next steps
<a name="next-steps"></a>

## Understanding AWS Glue transformations
<a name="transformations"></a>

For more efficient data processing, AWS Glue includes built-in [transformation functions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-transforms.html). The functions pass from transform to transform in a data structure called a DynamicFrame, which is an extension to an [Apache Spark](https://spark.apache.org/) SQL DataFrame. A DynamicFrame is similar to a DataFrame, except that each record is self-describing, so no schema is required initially.

To get acquainted with several AWS Glue PySpark built-in functions, see the blog post [Building an AWS Glue ETL pipeline locally without an AWS account](https://aws.amazon.com/blogs/big-data/building-an-aws-glue-etl-pipeline-locally-without-an-aws-account/).

## Authoring your first ETL job
<a name="authoring"></a>

If you haven't written an ETL job before, you can get started by using the [Three AWS Glue ETL job types for converting data to Apache Parquet](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet.html) pattern.

If you have experience writing ETL jobs, you can use the [AWS Glue GitHub examples](https://github.com/aws-samples/aws-glue-samples/tree/master/examples) to explore more deeply.

## Pricing
<a name="pricing"></a>

For pricing information, see [AWS Glue pricing](https://aws.amazon.com/glue/pricing/). You can also use the [AWS Pricing Calculator](https://calculator.aws/#/createCalculator) to estimate your monthly cost for using different AWS Glue components.
