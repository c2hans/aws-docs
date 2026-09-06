---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/syslog.html
---

# Syslog
<a name="syslog"></a>

Centralized Logging with OpenSearch collects syslog logs through UDP or TCP protocol.

The following guides you to create a log pipeline that ingests logs from a syslog endpoint.

## Create a log analytics pipeline (OpenSearch Engine)
<a name="create-a-log-analytics-pipeline-opensearch-engine-3"></a>

Prerequisites

Make sure you have imported an Amazon OpenSearch Service domain. For more information, see [Domain operations](domain-operations.md).

 **Follow these steps:**

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Analytics Pipelines**, choose **Application Log**.

1. Choose **Create a pipeline**.

1. Choose **Syslog Endpoint** as Log Source, choose **Amazon OpenSearch Service**, and choose **Next**.

1. Select **UDP** or **TCP** with custom port number. Choose **Next**.

You have created a log source for the log analytics pipeline. Now you are ready to make further configurations for the log analytics pipeline with syslog as log source.

1. Select a log config. If you do not find the desired log config from the dropdown list, choose **Create New** and follow instructions in [Log Config](log-config.md).

1. Enter a **Log Path** to specify the location of logs you want to collect.

1. Specify **Index name** in lowercase.

1. In the **Buffer** section, choose **S3** or **Kinesis Data Streams**. If you don’t want the buffer layer, choose **None**. Refer to the [Log Buffer](solution-overview.md#concepts) for more information about choosing the appropriate buffer layer.
   + Amazon S3 buffer parameters
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/syslog.html)
   + Kinesis Data Streams buffer parameters
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/syslog.html)
**Important**
You may observe duplicate logs in OpenSearch if a threshold error occurs in Kinesis Data Streams (KDS). This is because the Fluent Bit log agent uploads logs in [chunk](https://docs.fluentbit.io/manual/administration/buffering-and-storage#chunks-memory-filesystem-and-backpressure) (contains multiple records), and will retry the chunk if upload failed. Each KDS shard can support up to 1,000 records per second for writes, up to a maximum total data write rate of 1 MB per second. Estimate your log volume and choose an appropriate shard number.

1. Choose **Next**.

1. In the **Specify OpenSearch domain** section, select an imported domain for **Amazon OpenSearch Service domain**.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.
   + When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.
   + (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, enter the minimum and maximum number of OCU. For more information, see [Scaling pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Enable **Alarms** if needed and select an existing SNS topic. If you choose **Create a new SNS topic**, provide a name and an email address for the new SNS topic.

1. Add tags if needed.

1. Choose **Create**.

1. Wait for the application pipeline to turn to "Active" state.

## Create a log analytics pipeline (Light Engine)
<a name="create-a-log-analytics-pipeline-light-engine-3"></a>

 **Follow these steps:**

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the left sidebar, under **Log Analytics Pipelines**, choose **Application Log**.

1. Choose **Create a pipeline**.

1. Choose **Syslog Endpoint** as Log Source, choose **Light Engine**, and choose **Next**.

1. Select **UDP** or **TCP** with custom port number. Choose **Next**.

You have created a log source for the log analytics pipeline. Now you are ready to make further configurations for the log analytics pipeline with syslog as log source.

1. Select a log config. If you do not find the desired log config from the dropdown list, choose **Create New** and follow instructions in [Log Config](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/log-config-1.html).

1. Enter a **Log Path** to specify the location of logs you want to collect.

1. In the **Buffer** section, configure Amazon S3 buffer parameters.
   + Amazon S3 buffer parameters
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/syslog.html)

1. Choose **Next**.

1. In the **Specify Light Engine Configuration** section, if you want to ingest an associated templated Grafana dashboard, select **Yes** for the sample dashboard.

1. Choose an existing Grafana, or import a new one by making configurations in Grafana.

1. Select an Amazon S3 bucket to store partitioned logs and give a name to the log table. The solution provides a predefined table name, but you can modify it according to your needs.

1. Modify the log processing frequency if needed, which is set to **5** minutes by default with a minimum processing frequency of **1** minute.

1. In the **Log Lifecycle** section, enter the log merger time and lag archive time. The solution provides default values, which you can modify according to your needs.

1. Choose **Next**.

1. Enable **Alarms** if needed and select an exiting SNS topic. If you choose **Create a new SNS topic**, provide a name and an email address for the new SNS topic.

1. Add tags if needed.

1. Choose **Create**.

1. Wait for the application pipeline to turn to "Active" state.
