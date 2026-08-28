---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockRetention.html
---

# ObjectLockRetention
<a name="API_ObjectLockRetention"></a>

A Retention configuration for an object.

## Contents
<a name="API_ObjectLockRetention_Contents"></a>

 ** Mode **   <a name="AmazonS3-Type-ObjectLockRetention-Mode"></a>
Indicates the Retention mode for the specified object.
Type: String
Valid Values: `GOVERNANCE | COMPLIANCE`
Required: No

 ** RetainUntilDate **   <a name="AmazonS3-Type-ObjectLockRetention-RetainUntilDate"></a>
The date on which this Object Lock Retention will expire.
Type: Timestamp
Required: No

## See Also
<a name="API_ObjectLockRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectLockRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectLockRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectLockRetention)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
