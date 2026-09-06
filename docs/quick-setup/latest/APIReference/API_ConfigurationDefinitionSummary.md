---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ConfigurationDefinitionSummary.html
---

# ConfigurationDefinitionSummary
<a name="API_ConfigurationDefinitionSummary"></a>

A summarized definition of a Quick Setup configuration definition.

## Contents
<a name="API_ConfigurationDefinitionSummary_Contents"></a>

 ** FirstClassParameters **   <a name="quicksetup-Type-ConfigurationDefinitionSummary-FirstClassParameters"></a>
The common parameters and values for the configuration definition.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9+=@_\/\s-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: No

 ** Id **   <a name="quicksetup-Type-ConfigurationDefinitionSummary-Id"></a>
The ID of the configuration definition.
Type: String
Required: No

 ** Type **   <a name="quicksetup-Type-ConfigurationDefinitionSummary-Type"></a>
The type of the Quick Setup configuration used by the configuration definition.
Type: String
Required: No

 ** TypeVersion **   <a name="quicksetup-Type-ConfigurationDefinitionSummary-TypeVersion"></a>
The version of the Quick Setup type used by the configuration definition.
Type: String
Required: No

## See Also
<a name="API_ConfigurationDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ConfigurationDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ConfigurationDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ConfigurationDefinitionSummary)
