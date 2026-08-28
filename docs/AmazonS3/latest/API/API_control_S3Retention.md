---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3Retention.html
---

# S3Retention
<a name="API_control_S3Retention"></a>

Contains the S3 Object Lock retention mode to be applied to all objects in the S3 Batch Operations job. If you don't provide `Mode` and `RetainUntilDate` data types in your operation, you will remove the retention from your objects. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_control_S3Retention_Contents"></a>

 ** Mode **   <a name="AmazonS3-Type-control_S3Retention-Mode"></a>
The Object Lock retention mode to be applied to all objects in the Batch Operations job.
Type: String
Valid Values: `COMPLIANCE | GOVERNANCE`
Required: No

 ** RetainUntilDate **   <a name="AmazonS3-Type-control_S3Retention-RetainUntilDate"></a>
The date when the applied Object Lock retention will expire on all objects set by the Batch Operations job.
Type: Timestamp
Required: No

## See Also
<a name="API_control_S3Retention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3Retention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3Retention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3Retention)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
