---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ReplicationTime.html
---

# ReplicationTime
<a name="API_control_ReplicationTime"></a>

A container that specifies S3 Replication Time Control (S3 RTC) related information, including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated.

**Note**
This is not supported by Amazon S3 on Outposts buckets.

## Contents
<a name="API_control_ReplicationTime_Contents"></a>

 ** Status **   <a name="AmazonS3-Type-control_ReplicationTime-Status"></a>
Specifies whether S3 Replication Time Control (S3 RTC) is enabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** Time **   <a name="AmazonS3-Type-control_ReplicationTime-Time"></a>
A container that specifies the time by which replication should be complete for all objects and operations on objects.
Type: [ReplicationTimeValue](API_control_ReplicationTimeValue.md) data type
Required: Yes

## See Also
<a name="API_control_ReplicationTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ReplicationTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ReplicationTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ReplicationTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
