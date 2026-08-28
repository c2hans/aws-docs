---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ProfileTemplate.html
---

# ProfileTemplate
<a name="API_ProfileTemplate"></a>

The profile template.

## Contents
<a name="API_ProfileTemplate_Contents"></a>

 ** CreatedAt **   <a name="wellarchitected-Type-ProfileTemplate-CreatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** TemplateName **   <a name="wellarchitected-Type-ProfileTemplate-TemplateName"></a>
The name of the profile template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** TemplateQuestions **   <a name="wellarchitected-Type-ProfileTemplate-TemplateQuestions"></a>
Profile template questions.
Type: Array of [ProfileTemplateQuestion](API_ProfileTemplateQuestion.md) objects
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-ProfileTemplate-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_ProfileTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ProfileTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ProfileTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ProfileTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
