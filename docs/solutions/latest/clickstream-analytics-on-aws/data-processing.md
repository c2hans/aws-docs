---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-processing.html
---

# Data processing
<a name="data-processing"></a>

 Clickstream Analytics on AWS provides an inbuilt data schema to parse and model the raw event data sent from your web and mobile apps, which makes it easy for you to analyze the data in analytics engines (such as RedShift and Athena).

 Data Processing module includes two functionalities:
+  **Transformation**: Extract the data from files sank by ingestion module, then parse each event data and transform them to guidance data model.
+  **Enrichment**: Add additional dimensions/fields to event data.

 This chapter includes:
+  [Data schema](data-schema.md)
+  [Configure execution parameters](execution-parameters.md)
+  [Configure custom plugins](processing-plugin.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
