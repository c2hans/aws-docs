---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceCrawlerConfiguration.html
---

# CustomLogSourceCrawlerConfiguration
<a name="API_CustomLogSourceCrawlerConfiguration"></a>

The configuration used for the Glue Crawler for a third-party custom source.

## Contents
<a name="API_CustomLogSourceCrawlerConfiguration_Contents"></a>

 ** roleArn **   <a name="securitylake-Type-CustomLogSourceCrawlerConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be used by the AWS Glue crawler. The recommended IAM policies are:
+ The managed policy `AWSGlueServiceRole`
+ A custom policy granting access to your Amazon S3 Data Lake
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_CustomLogSourceCrawlerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CustomLogSourceCrawlerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CustomLogSourceCrawlerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CustomLogSourceCrawlerConfiguration)
