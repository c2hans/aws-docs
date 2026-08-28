---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tutorials-dbt.html
---

# Using dbt-core with EMR Serverless
<a name="tutorials-dbt"></a>

With Amazon EMR release `emr-7.13.0` and later, you can use dbt-core with [Spark Connect enabled interactive sessions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/spark-connect.html) to run transformations on EMR Serverless.

**To use dbt-core with EMR Serverless**

1. Install the dbt-spark adapter with session support.

   ```
   pip install dbt-spark[session]
   ```

1. In your dbt profile (`profiles.yml`), set the `host` config as `NA`. This field is required but ignored when `SPARK_REMOTE` is set.

   ```
   emrs_spark_sample:
     target: dev
     outputs:
       dev:
         type: spark
         method: session
         schema: sample_schema
         host: NA
   ```

1. Start an interactive session and set `SPARK_REMOTE` to the session endpoint URL before running dbt. For more information about how to get the session endpoint URL, see [Run interactive sessions with Amazon EMR Serverless through Spark Connect](spark-connect.md).

   ```
   import os
   os.environ['SPARK_REMOTE'] = {{spark_remote_url}}
   ```

1. Run dbt commands against the interactive session on the EMR Serverless application.

   ```
   dbt run --select {{my_dbt_model}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
