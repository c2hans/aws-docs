---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_TemplateSummary.html
---

# TemplateSummary
<a name="API_TemplateSummary"></a>

Provides a summary of a WhatsApp message template's key attributes.

## Contents
<a name="API_TemplateSummary_Contents"></a>

 ** metaTemplateId **   <a name="Social-Type-TemplateSummary-metaTemplateId"></a>
The numeric ID assigned to the template by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: No

 ** templateCategory **   <a name="Social-Type-TemplateSummary-templateCategory"></a>
The category of the template (for example, UTILITY or MARKETING).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** templateLanguage **   <a name="Social-Type-TemplateSummary-templateLanguage"></a>
The language code of the template (for example, en\_US).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Required: No

 ** templateName **   <a name="Social-Type-TemplateSummary-templateName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** templateQualityScore **   <a name="Social-Type-TemplateSummary-templateQualityScore"></a>
The quality score assigned to the template by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** templateStatus **   <a name="Social-Type-TemplateSummary-templateStatus"></a>
The current status of the template (for example, APPROVED, PENDING, or REJECTED).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

## See Also
<a name="API_TemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/TemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/TemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/TemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
