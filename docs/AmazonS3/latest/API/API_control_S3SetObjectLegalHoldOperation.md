---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3SetObjectLegalHoldOperation.html
---

# S3SetObjectLegalHoldOperation
<a name="API_control_S3SetObjectLegalHoldOperation"></a>

Contains the configuration for an S3 Object Lock legal hold operation that an S3 Batch Operations job passes to every object to the underlying `PutObjectLegalHold` API operation. For more information, see [Using S3 Object Lock legal hold with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html) in the *Amazon S3 User Guide*.

**Note**
This functionality is not supported by directory buckets.

## Contents
<a name="API_control_S3SetObjectLegalHoldOperation_Contents"></a>

 ** LegalHold **   <a name="AmazonS3-Type-control_S3SetObjectLegalHoldOperation-LegalHold"></a>
Contains the Object Lock legal hold status to be applied to all objects in the Batch Operations job.
Type: [S3ObjectLockLegalHold](API_control_S3ObjectLockLegalHold.md) data type
Required: Yes

## See Also
<a name="API_control_S3SetObjectLegalHoldOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectLegalHoldOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectLegalHoldOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectLegalHoldOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
