---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_PresentationObject.html
---

# PresentationObject
<a name="API_PresentationObject"></a>

 An object that defines how custom line item charges are presented in the bill, containing specifications for service presentation.

## Contents
<a name="API_PresentationObject_Contents"></a>

 ** Service **   <a name="billingconductor-Type-PresentationObject-Service"></a>
 The service under which the custom line item charges will be presented. Must be a string between 1 and 128 characters matching the pattern "`^[a-zA-Z0-9]+$`".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

## See Also
<a name="API_PresentationObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/PresentationObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/PresentationObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/PresentationObject)
