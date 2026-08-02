---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ComponentSummary.html
---

# ComponentSummary
<a name="API_ComponentSummary"></a>

The summary of the component.

## Contents
<a name="API_ComponentSummary_Contents"></a>

 ** ApplicationId **   <a name="ssmsap-Type-ComponentSummary-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** Arn **   <a name="ssmsap-Type-ComponentSummary-Arn"></a>
The Amazon Resource Name (ARN) of the component summary.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** ComponentId **   <a name="ssmsap-Type-ComponentSummary-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** ComponentType **   <a name="ssmsap-Type-ComponentSummary-ComponentType"></a>
The type of the component.
Type: String
Valid Values: `HANA | HANA_NODE | ABAP | ASCS | DIALOG | WEBDISP | WD | ERS`
Required: No

 ** Tags **   <a name="ssmsap-Type-ComponentSummary-Tags"></a>
The tags of the component.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ComponentSummary)
