---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectRetentionOperation.html
---

# S3SetObjectRetentionOperation
<a name="API_control_S3SetObjectRetentionOperation"></a>

Contains the configuration parameters for the Object Lock retention action for an S3 Batch Operations job. Batch Operations passes every object to the underlying `PutObjectRetention` API operation. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide*.

**Note**
This functionality is not supported by directory buckets.

## Contents
<a name="API_control_S3SetObjectRetentionOperation_Contents"></a>

 ** Retention **   <a name="AmazonS3-Type-control_S3SetObjectRetentionOperation-Retention"></a>
Contains the Object Lock retention mode to be applied to all objects in the Batch Operations job. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide*.
Type: [S3Retention](API_control_S3Retention.md) data type
Required: Yes

 ** BypassGovernanceRetention **   <a name="AmazonS3-Type-control_S3SetObjectRetentionOperation-BypassGovernanceRetention"></a>
Indicates if the action should be applied to objects in the Batch Operations job even if they have Object Lock ` GOVERNANCE` type in place.
Type: Boolean
Required: No

## See Also
<a name="API_control_S3SetObjectRetentionOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectRetentionOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectRetentionOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectRetentionOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
