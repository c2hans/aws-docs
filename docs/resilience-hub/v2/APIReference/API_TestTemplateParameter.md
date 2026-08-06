---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestTemplateParameter.html
---

# TestTemplateParameter
<a name="API_TestTemplateParameter"></a>

Describes a parameter accepted by a test template.

## Contents
<a name="API_TestTemplateParameter_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-TestTemplateParameter-name"></a>
The name of the parameter.
Type: String
Required: Yes

 ** required **   <a name="ngresiliencehub-Type-TestTemplateParameter-required"></a>
Indicates whether the parameter is required.
Type: Boolean
Required: Yes

 ** type **   <a name="ngresiliencehub-Type-TestTemplateParameter-type"></a>
The data type of the parameter.
Type: String
Valid Values: `STRING | STRING_LIST | INTEGER`
Required: Yes

 ** defaultValue **   <a name="ngresiliencehub-Type-TestTemplateParameter-defaultValue"></a>
The default value of the parameter.
Type: String
Required: No

 ** description **   <a name="ngresiliencehub-Type-TestTemplateParameter-description"></a>
A description of the parameter.
Type: String
Required: No

 ** maxValues **   <a name="ngresiliencehub-Type-TestTemplateParameter-maxValues"></a>
The maximum number of values the parameter accepts.
Type: Integer
Required: No

## See Also
<a name="API_TestTemplateParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestTemplateParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestTemplateParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestTemplateParameter)
