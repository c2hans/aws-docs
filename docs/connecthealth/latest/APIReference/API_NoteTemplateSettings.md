---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_NoteTemplateSettings.html
---

# NoteTemplateSettings
<a name="API_NoteTemplateSettings"></a>

Settings for the note template to use for clinical note generation

## Contents
<a name="API_NoteTemplateSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customTemplate **   <a name="connecthealth-Type-NoteTemplateSettings-customTemplate"></a>

Type: [CustomTemplate](API_CustomTemplate.md) object
Required: No

 ** managedTemplate **   <a name="connecthealth-Type-NoteTemplateSettings-managedTemplate"></a>

Type: [ManagedTemplate](API_ManagedTemplate.md) object
Required: No

## See Also
<a name="API_NoteTemplateSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/NoteTemplateSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/NoteTemplateSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/NoteTemplateSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
