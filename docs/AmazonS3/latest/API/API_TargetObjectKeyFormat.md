---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_TargetObjectKeyFormat.html
---

# TargetObjectKeyFormat
<a name="API_TargetObjectKeyFormat"></a>

Amazon S3 key format for log objects. Only one format, PartitionedPrefix or SimplePrefix, is allowed.

## Contents
<a name="API_TargetObjectKeyFormat_Contents"></a>

 ** PartitionedPrefix **   <a name="AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix"></a>
Partitioned S3 key for log objects.
Type: [PartitionedPrefix](API_PartitionedPrefix.md) data type
Required: No

 ** SimplePrefix **   <a name="AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix"></a>
To use the simple format for S3 keys for log objects. To specify SimplePrefix format, set SimplePrefix to {}.
Type: [SimplePrefix](API_SimplePrefix.md) data type
Required: No

## See Also
<a name="API_TargetObjectKeyFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/TargetObjectKeyFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/TargetObjectKeyFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/TargetObjectKeyFormat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
