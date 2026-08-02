---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceAttributes.html
---

# CustomLogSourceAttributes
<a name="API_CustomLogSourceAttributes"></a>

The attributes of a third-party custom source.

## Contents
<a name="API_CustomLogSourceAttributes_Contents"></a>

 ** crawlerArn **   <a name="securitylake-Type-CustomLogSourceAttributes-crawlerArn"></a>
The ARN of the AWS Glue crawler.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`
Required: No

 ** databaseArn **   <a name="securitylake-Type-CustomLogSourceAttributes-databaseArn"></a>
The ARN of the AWS Glue database where results are written, such as: `arn:aws:daylight:us-east-1::database/sometable/*`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`
Required: No

 ** tableArn **   <a name="securitylake-Type-CustomLogSourceAttributes-tableArn"></a>
The ARN of the AWS Glue table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`
Required: No

## See Also
<a name="API_CustomLogSourceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CustomLogSourceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CustomLogSourceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CustomLogSourceAttributes)
