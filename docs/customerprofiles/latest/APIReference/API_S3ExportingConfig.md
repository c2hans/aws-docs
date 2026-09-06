---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_S3ExportingConfig.html
---

# S3ExportingConfig
<a name="API_connect-customer-profiles_S3ExportingConfig"></a>

Configuration information about the S3 bucket where Identity Resolution Jobs write result files.

## Contents
<a name="API_connect-customer-profiles_S3ExportingConfig_Contents"></a>

 ** S3BucketName **   <a name="connect-Type-connect-customer-profiles_S3ExportingConfig-S3BucketName"></a>
The name of the S3 bucket where Identity Resolution Jobs write result files.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9.-]+$`
Required: Yes

 ** S3KeyName **   <a name="connect-Type-connect-customer-profiles_S3ExportingConfig-S3KeyName"></a>
The S3 key name of the location where Identity Resolution Jobs write result files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Pattern: `.*`
Required: No

## See Also
<a name="API_connect-customer-profiles_S3ExportingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/S3ExportingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/S3ExportingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/S3ExportingConfig)
