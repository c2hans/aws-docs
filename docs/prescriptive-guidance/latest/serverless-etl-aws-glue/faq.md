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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
