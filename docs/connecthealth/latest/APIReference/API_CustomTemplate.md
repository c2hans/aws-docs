---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CustomTemplate.html
---

# CustomTemplate
<a name="API_CustomTemplate"></a>

Configuration for using a custom note template with specific instructions

## Contents
<a name="API_CustomTemplate_Contents"></a>

 ** templateInstructions **   <a name="connecthealth-Type-CustomTemplate-templateInstructions"></a>
Custom instructions for each section of the template
Type: Array of [TemplateSectionInstruction](API_TemplateSectionInstruction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** templateType **   <a name="connecthealth-Type-CustomTemplate-templateType"></a>
The base template type to customize
Type: String
Valid Values: `HISTORY_AND_PHYSICAL | GIRPP | DAP | SIRP | BIRP | BEHAVIORAL_SOAP`
Required: Yes

## See Also
<a name="API_CustomTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/CustomTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/CustomTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/CustomTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
