---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_WebAppConfiguration.html
---

# WebAppConfiguration
<a name="API_WebAppConfiguration"></a>

Configuration for the Domain web application, including Identity Center settings. If provided, all fields are required.

## Contents
<a name="API_WebAppConfiguration_Contents"></a>

 ** ehrRole **   <a name="connecthealth-Type-WebAppConfiguration-ehrRole"></a>
ARN of the IAM role used for EHR operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/.+`
Required: Yes

 ** idcApplicationId **   <a name="connecthealth-Type-WebAppConfiguration-idcApplicationId"></a>
The Identity Center application ID associated with this Domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** idcRegion **   <a name="connecthealth-Type-WebAppConfiguration-idcRegion"></a>
The AWS region where Identity Center is configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_WebAppConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/WebAppConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/WebAppConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/WebAppConfiguration)
