---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-s3.html
---

# Amazon S3
<a name="amazon-s3"></a>

For Amazon S3, Centralized Logging with OpenSearch ingests logs in a specified Amazon S3 location continuously or performs one-time ingestion. You can also filter logs based on Amazon S3 prefix or parse logs with custom Log Config.

The following guides you to create a log pipeline that ingests logs from an Amazon S3 bucket.

## Create a log analytics pipeline (OpenSearch Engine)
<a name="create-a-log-analytics-pipeline-opensearch-engine-2"></a>

 **Prerequisites**

Make sure you have imported an Amazon OpenSearch Service domain. For more information, see [Domain operations](domain-operations.md).

 **Follow these steps:**

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Analytics Pipelines**, choose **Application Log**.

1. Choose **Create a pipeline**.

1. Choose **Amazon S3** as Log Source, choose **Amazon OpenSearch Service**, and choose **Next**.

1. Choose the Amazon S3 bucket where your logs are stored. If needed, enter **Prefix filter**, which is optional.

1. Choose **Ingestion mode** based on your need. If you want to ingest logs continuously, select **On-going**; if you only must ingest logs once, select **One-time**.

1. Specify **Compression format** if your log files are compressed, and choose **Next**.

You have created a log source for the log analytics pipeline. Now you are ready to make further configurations for the log analytics pipeline with Amazon S3 as log source.

1. Select a log config. If you do not find the desired log config from the dropdown list, choose **Create New**. Refer to [Log Config](log-config.md) for more information.

1. Choose **Next**.

1. Specify **Index name** in lowercase.

1. In the **Specify OpenSearch domain** section, select an imported domain for **Amazon OpenSearch Service domain**.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch creates the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. Choose **Next**.

1. Enable **Alarms** if needed and select an existing SNS topic. If you choose **Create a new SNS topic**, provide a name and an email address for the new SNS topic.

1. Add tags if needed.

1. Choose **Create**.

1. Wait for the application pipeline to turn to an "Active" state.

## Create a log analytics pipeline (Light Engine)
<a name="create-a-log-analytics-pipeline-light-engine-2"></a>

 **Follow these steps:**

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Analytics Pipelines**, choose **Application Log**.

1. Choose **Create a pipeline**.

1. Choose **Amazon S3** as Log Source, choose **Light Engine**, and choose **Next**.

1. Choose the Amazon S3 bucket where your logs are stored. If needed, enter **Prefix filter**, which is optional.

1. Choose **Ingestion mode** based on your need. If you want to ingest the log continuously, select **On-going**.

You have created a log source for the log analytics pipeline. Now you are ready to make further configurations for the log analytics pipeline with Amazon S3 as log source.

1. Select a log config. If you do not find the desired log config from the dropdown list, choose Create New. Refer to [Log Config](log-config.md) for more information.

1. Choose Next.

1. In the Specify Light Engine Configuration section, if you want to ingest associated templated Grafana dashboards, select Yes for the sample dashboard.

1. You can choose an existing Grafana, or if you must import a new one, you can go to Grafana for configuration.

1. Select an S3 bucket to store partitioned logs and define a name for the log table. We have provided a predefined table name, but you can modify it according to your business needs.

1. The log processing frequency is set to 5 minutes by default, with a minimum processing frequency of 1 minute.

1. In the Log Lifecycle section, enter the log merge time and log archive time. We have provided default values, but you can adjust them based on your business requirements.

1. Select Next.

1. Enable Alarms if needed and select an existing SNS topic. If you choose Create a new SNS topic, provide a name and an email address for the new SNS topic.

1. If desired, add tags.

1. Select Create.

1. Wait for the application pipeline to turn to "Active" state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
