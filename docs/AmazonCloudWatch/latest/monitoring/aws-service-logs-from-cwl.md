---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-service-logs-from-cwl.html
---

# AWS service logs from CloudWatch Logs
<a name="aws-service-logs-from-cwl"></a>

Intercepts log events from CloudWatch Logs that match the log event metadata configuration.

**Important**
Pipelines with processors mutate the log events in the original CloudWatch log group they are intercepted from for logs from AWS services. To preserve unmodified copies of your log data, enable the `include_original` option in the `cloudwatch_logs` sink configuration, or use the **Keep original log** toggle in the console. For more information, see [Sinks](pipeline-sinks.md).

**Configuration**
Configure the CloudWatch Logs source with the following parameters:

```
source:
  cloudwatch_logs:
    aws:
      sts_role_arn: "arn:aws:iam::123456789012:role/MyCloudWatchLogsRole"
    log_event_metadata:
      data_source_name: "<data_source_name>"
      data_source_type: "<data_source_type>"
```Parameters

`aws.sts_role_arn` (required)
The ARN of the IAM role to assume for CloudWatch Logs interception.

`log_event_metadata.data_source_name` (required)
Identifies the specific AWS service that generated the log events or a custom log source name. For custom logs, this can be any string up to 15 characters when `data_source_type` is "default".

`log_event_metadata.data_source_type` (required)
Specifies the category or type of logs within the AWS service, or "default" for custom logs. Set to "default" to enable custom log source names.

For more information on data source name and type, see the [CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-source-discovery-management.html#how-to-get-started-data-sources).

**Restrictions**
The following restrictions apply to CloudWatch Logs sources:
+ No two pipelines can use the `cloudwatch_logs` source with identical `data_source_name` and `data_source_type` metadata criteria.
+ When `data_source_name` is `aws_cloudtrail`, only empty processors (`[]`) or the `ocsf` processor are allowed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
