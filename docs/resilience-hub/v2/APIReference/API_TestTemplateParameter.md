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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
