---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_TemplateSectionInstruction.html
---

# TemplateSectionInstruction
<a name="API_TemplateSectionInstruction"></a>

Instructions for generating a specific section of a clinical note

## Contents
<a name="API_TemplateSectionInstruction_Contents"></a>

 ** sectionHeader **   <a name="connecthealth-Type-TemplateSectionInstruction-sectionHeader"></a>
The header for this section of the template
Type: String
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** sectionInstruction **   <a name="connecthealth-Type-TemplateSectionInstruction-sectionInstruction"></a>
The instruction for generating this section
Type: String
Pattern: `[a-zA-Z0-9\s\*_\-#\[\]\(\)\.,:;!?'"`<>~/]+`
Required: Yes

## See Also
<a name="API_TemplateSectionInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/TemplateSectionInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/TemplateSectionInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/TemplateSectionInstruction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
