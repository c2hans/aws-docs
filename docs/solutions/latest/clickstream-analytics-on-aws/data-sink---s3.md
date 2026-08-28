---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-sink---s3.html
---

# Data sink - S3
<a name="data-sink---s3"></a>

 In this option, clickstream data is buffered in the memory of ingestion Server, then sink into a S3 bucket. This option provides the best cost-performance in case real-time data consumption is not required.

**Note**
Unlike Kafka and KDS data sink, this option buffers data in the ingestion server and responses 200 code to SDK client before sink into S3, so there is chance data could be lost while ingestion server fails and auto-scaled machine is in the process of creation. But it is worth to note that this probability is very low because of the High-availability design of the guidance.
+  **Buffer size**: Specify the data size to buffer before sending to Amazon S3. The higher buffer size may be lower in cost with higher latency, while the lower buffer size will be faster in delivery with higher cost. Min: 1 MiB, Max: 50 MiB
+  **Buffer interval**: Specify the maximum interval (in seconds) for saving buffer to S3. The higher interval allows more time to collect data and the size of data may be bigger. The lower interval sends the data more frequently and may be more advantageous when looking at shorter cycles of data activity. Min: 60 Seconds, Max: 3600 Seconds

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
