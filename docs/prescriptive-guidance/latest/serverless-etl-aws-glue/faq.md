---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about serverless ETL on AWS Glue.

## When should I use Python shell instead of Apache Spark for AWS Glue jobs?
<a name="q1"></a>

Use Python shell when you have basic ETL jobs or small datasets that don't require the distributed computing capabilities of Apache Spark. Use Apache Spark for more complex ETL jobs or large datasets that require the high processing power that Spark is optimized to handle.

## What is the recommended AWS Glue version for my project?
<a name="q2"></a>

We generally recommend using the latest version of AWS Glue. The [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) page lists the differences between versions, along with their compatibility with various versions of Python and Spark.
