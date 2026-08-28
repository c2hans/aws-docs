---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaLibraryTemplate.html
---

# MetaLibraryTemplate
<a name="API_MetaLibraryTemplate"></a>

Represents a template from Meta's library with customization options.

## Contents
<a name="API_MetaLibraryTemplate_Contents"></a>

 ** libraryTemplateName **   <a name="Social-Type-MetaLibraryTemplate-libraryTemplateName"></a>
The name of the template in Meta's library.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** templateCategory **   <a name="Social-Type-MetaLibraryTemplate-templateCategory"></a>
The category of the template (for example, UTILITY or MARKETING).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** templateLanguage **   <a name="Social-Type-MetaLibraryTemplate-templateLanguage"></a>
The language code for the template (for example, en\_US).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Required: Yes

 ** templateName **   <a name="Social-Type-MetaLibraryTemplate-templateName"></a>
The name to assign to the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** libraryTemplateBodyInputs **   <a name="Social-Type-MetaLibraryTemplate-libraryTemplateBodyInputs"></a>
Body text customizations for the template.
Type: [LibraryTemplateBodyInputs](API_LibraryTemplateBodyInputs.md) object
Required: No

 ** libraryTemplateButtonInputs **   <a name="Social-Type-MetaLibraryTemplate-libraryTemplateButtonInputs"></a>
Button customizations for the template.
Type: Array of [LibraryTemplateButtonInput](API_LibraryTemplateButtonInput.md) objects
Required: No

## See Also
<a name="API_MetaLibraryTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaLibraryTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaLibraryTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaLibraryTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
