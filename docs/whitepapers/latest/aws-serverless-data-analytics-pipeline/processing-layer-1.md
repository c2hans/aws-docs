---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/processing-layer-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Processing layer
<a name="processing-layer-1"></a>

 The processing layer in our architecture is composed of two types of components:
+  Components used to create multi-step data processing pipelines.
+  Components to orchestrate data processing pipelines on schedule or in response to event triggers (such as ingestion of new data into the landing zone).

 AWS Glue and [AWS Step Functions](https://aws.amazon.com/step-functions/) provide serverless components to build, orchestrate, and run pipelines that can easily scale to process large data volumes. Multi-step workflows built using AWS Glue and Step Functions can catalog, validate, clean, transform, and enrich individual datasets and advance them from raw to cleaned and cleaned to curated zones in the storage layer.

 AWS Glue is a serverless, pay-per-use ETL service for building and running Python or Spark jobs (written in [Scala](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-scala.html) or [Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html)) without requiring you to deploy or manage clusters. [AWS Glue automatically generates the code](https://aws.amazon.com/blogs/big-data/simplify-data-pipelines-with-aws-glue-automatic-code-generation-and-workflows/) to accelerate your data transformations and loading processes. AWS Glue ETL builds on top of Apache Spark and provides commonly used out-of-the-box data source connectors, [data structures](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html), and [ETL transformations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html) to validate, clean, transform, and flatten data stored in many open-source formats such as CSV, JSON, Parquet, and Avro. AWS Glue ETL also provides capabilities to incrementally process partitioned data.

 Additionally, you can use AWS Glue to define and run [crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) that can crawl folders in the data lake, discover datasets and their partitions, infer schema, and define tables in the Lake Formation catalog. AWS Glue provides more than a dozen [built-in classifiers](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html) that can parse a variety of data structures stored in open-source formats. AWS Glue also provides [triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html) and [workflow capabilities](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) that you can use to build multi-step end- to-end data processing pipelines that include job dependencies and running parallel steps. You can schedule AWS Glue jobs and workflows or run them on demand. AWS Glue natively integrates with AWS services in storage, catalog, and [security](https://docs.aws.amazon.com/glue/latest/dg/security.html) layers.

 To make it easy to clean and normalize data, Glue also provides a visual data preparation tool called AWS Glue DataBrew which is an interactive, point-and-click visual interface without requiring to write any code.

 Step Functions is a serverless engine that you can use to build and orchestrate scheduled or event-driven data processing workflows. You use Step Functions to build complex data processing pipelines that involve orchestrating steps implemented by using multiple AWS services such as AWS Glue, [AWS Lambda](https://aws.amazon.com/lambda), [*Amazon Elastic Container Service*](https://aws.amazon.com/ecs) (Amazon ECS) containers, and more. Step Functions provides visual representations of complex workflows and their running state to make them easy to understand. It manages state, checkpoints, and restarts of the workflow for you to make sure that the steps in your data pipeline run in order and as expected. Built-in try/catch, retry, and rollback capabilities deal with errors and exceptions automatically.
