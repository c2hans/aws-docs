---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringConfiguration.html
---

# IntelligentTieringConfiguration
<a name="API_IntelligentTieringConfiguration"></a>

Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.

For information about the S3 Intelligent-Tiering storage class, see [Storage class for automatically optimizing frequently and infrequently accessed objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html#sc-dynamic-data-access).

## Contents
<a name="API_IntelligentTieringConfiguration_Contents"></a>

 ** Id **   <a name="AmazonS3-Type-IntelligentTieringConfiguration-Id"></a>
The ID used to identify the S3 Intelligent-Tiering configuration.
Type: String
Required: Yes

 ** Status **   <a name="AmazonS3-Type-IntelligentTieringConfiguration-Status"></a>
Specifies the status of the configuration.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** Tierings **   <a name="AmazonS3-Type-IntelligentTieringConfiguration-Tierings"></a>
Specifies the S3 Intelligent-Tiering storage class tier of the configuration.
Type: Array of [Tiering](API_Tiering.md) data types
Required: Yes

 ** Filter **   <a name="AmazonS3-Type-IntelligentTieringConfiguration-Filter"></a>
Specifies a bucket filter. The configuration only includes objects that meet the filter's criteria.
Type: [IntelligentTieringFilter](API_IntelligentTieringFilter.md) data type
Required: No

## See Also
<a name="API_IntelligentTieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
