---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobParameters.html
---

# ProtectedJobParameters
<a name="API_ProtectedJobParameters"></a>

The parameters for the protected job.

## Contents
<a name="API_ProtectedJobParameters_Contents"></a>

 ** analysisTemplateArn **   <a name="API-Type-ProtectedJobParameters-analysisTemplateArn"></a>
 The ARN of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** parameters **   <a name="API-Type-ProtectedJobParameters-parameters"></a>
Runtime configuration values passed to the PySpark analysis script. Parameter names and types must match those defined in the analysis template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[0-9a-zA-Z_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_ProtectedJobParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobParameters)
