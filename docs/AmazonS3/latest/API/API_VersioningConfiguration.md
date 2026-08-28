---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_VersioningConfiguration.html
---

# VersioningConfiguration
<a name="API_VersioningConfiguration"></a>

Describes the versioning state of an Amazon S3 bucket. For more information, see [PUT Bucket versioning](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTVersioningStatus.html) in the *Amazon S3 API Reference*.

## Contents
<a name="API_VersioningConfiguration_Contents"></a>

 ** MFADelete **   <a name="AmazonS3-Type-VersioningConfiguration-MFADelete"></a>
Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** Status **   <a name="AmazonS3-Type-VersioningConfiguration-Status"></a>
The versioning state of the bucket.
Type: String
Valid Values: `Enabled | Suspended`
Required: No

## See Also
<a name="API_VersioningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/VersioningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/VersioningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/VersioningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
