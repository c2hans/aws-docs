---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerLogDeliveryDescription.html
---

# WorkerLogDeliveryDescription
<a name="API_WorkerLogDeliveryDescription"></a>

Workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

## Contents
<a name="API_WorkerLogDeliveryDescription_Contents"></a>

 ** cloudWatchLogs **   <a name="MSKC-Type-WorkerLogDeliveryDescription-cloudWatchLogs"></a>
Details about delivering logs to Amazon CloudWatch Logs.
Type: [CloudWatchLogsLogDeliveryDescription](API_CloudWatchLogsLogDeliveryDescription.md) object
Required: No

 ** firehose **   <a name="MSKC-Type-WorkerLogDeliveryDescription-firehose"></a>
Details about delivering logs to Amazon Kinesis Data Firehose.
Type: [FirehoseLogDeliveryDescription](API_FirehoseLogDeliveryDescription.md) object
Required: No

 ** s3 **   <a name="MSKC-Type-WorkerLogDeliveryDescription-s3"></a>
Details about delivering logs to Amazon S3.
Type: [S3LogDeliveryDescription](API_S3LogDeliveryDescription.md) object
Required: No

## See Also
<a name="API_WorkerLogDeliveryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
