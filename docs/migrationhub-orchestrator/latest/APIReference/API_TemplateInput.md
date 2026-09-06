---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateInput.html
---

# TemplateInput
<a name="API_TemplateInput"></a>

The input parameters of a template.

## Contents
<a name="API_TemplateInput_Contents"></a>

 ** dataType **   <a name="migrationhuborchestrator-Type-TemplateInput-dataType"></a>
The data type of the template input.
Type: String
Valid Values: `STRING | INTEGER | STRINGLIST | STRINGMAP`
Required: No

 ** inputName **   <a name="migrationhuborchestrator-Type-TemplateInput-inputName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: No

 ** required **   <a name="migrationhuborchestrator-Type-TemplateInput-required"></a>
Determine if an input is required from the template.
Type: Boolean
Required: No

## See Also
<a name="API_TemplateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/TemplateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/TemplateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/TemplateInput)
