---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CompatibleEnvironmentTemplateInput.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CompatibleEnvironmentTemplateInput
<a name="API_CompatibleEnvironmentTemplateInput"></a>

Compatible environment template data.

## Contents
<a name="API_CompatibleEnvironmentTemplateInput_Contents"></a>

 ** majorVersion **   <a name="proton-Type-CompatibleEnvironmentTemplateInput-majorVersion"></a>
The major version of the compatible environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-CompatibleEnvironmentTemplateInput-templateName"></a>
The compatible environment template name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## See Also
<a name="API_CompatibleEnvironmentTemplateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CompatibleEnvironmentTemplateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CompatibleEnvironmentTemplateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CompatibleEnvironmentTemplateInput)
