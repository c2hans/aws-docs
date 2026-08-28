---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Metrics.html
---

# Metrics
<a name="API_Metrics"></a>

 A container specifying replication metrics-related settings enabling replication metrics and events.

## Contents
<a name="API_Metrics_Contents"></a>

 ** Status **   <a name="AmazonS3-Type-Metrics-Status"></a>
 Specifies whether the replication metrics are enabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** EventThreshold **   <a name="AmazonS3-Type-Metrics-EventThreshold"></a>
 A container specifying the time threshold for emitting the `s3:Replication:OperationMissedThreshold` event.
Type: [ReplicationTimeValue](API_ReplicationTimeValue.md) data type
Required: No

## See Also
<a name="API_Metrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Metrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Metrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Metrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
