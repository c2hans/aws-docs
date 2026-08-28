---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockConfiguration.html
---

# ObjectLockConfiguration
<a name="API_ObjectLockConfiguration"></a>

The container element for Object Lock configuration parameters.

## Contents
<a name="API_ObjectLockConfiguration_Contents"></a>

 ** ObjectLockEnabled **   <a name="AmazonS3-Type-ObjectLockConfiguration-ObjectLockEnabled"></a>
Indicates whether this bucket has an Object Lock configuration enabled. Enable `ObjectLockEnabled` when you apply `ObjectLockConfiguration` to a bucket.
Type: String
Valid Values: `Enabled`
Required: No

 ** Rule **   <a name="AmazonS3-Type-ObjectLockConfiguration-Rule"></a>
Specifies the Object Lock rule for the specified object. Enable the this rule when you apply `ObjectLockConfiguration` to a bucket. Bucket settings require both a mode and a period. The period can be either `Days` or `Years` but you must select one. You cannot specify `Days` and `Years` at the same time.
Type: [ObjectLockRule](API_ObjectLockRule.md) data type
Required: No

## See Also
<a name="API_ObjectLockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectLockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectLockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectLockConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
