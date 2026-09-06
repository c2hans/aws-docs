---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaLibraryTemplateDefinition.html
---

# MetaLibraryTemplateDefinition
<a name="API_MetaLibraryTemplateDefinition"></a>

Defines the complete structure and content of a template in Meta's library.

## Contents
<a name="API_MetaLibraryTemplateDefinition_Contents"></a>

 ** templateBody **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateBody"></a>
The body text of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** templateBodyExampleParams **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateBodyExampleParams"></a>
Example parameter values for the template body, used to demonstrate how dynamic content appears in the template.
Type: Array of strings
Required: No

 ** templateButtons **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateButtons"></a>
The buttons included in the template.
Type: Array of [LibraryTemplateButtonList](API_LibraryTemplateButtonList.md) objects
Required: No

 ** templateCategory **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateCategory"></a>
The category of the template (for example, UTILITY or MARKETING).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** templateHeader **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateHeader"></a>
The header text of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** templateId **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateId"></a>
The ID of the template in Meta's library.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: No

 ** templateIndustry **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateIndustry"></a>
The industries the template is designed for.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** templateLanguage **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateLanguage"></a>
The language code for the template (for example, en\_US).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Required: No

 ** templateName **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** templateTopic **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateTopic"></a>
The topic or subject matter of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** templateUseCase **   <a name="Social-Type-MetaLibraryTemplateDefinition-templateUseCase"></a>
The intended use case for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: No

## See Also
<a name="API_MetaLibraryTemplateDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaLibraryTemplateDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaLibraryTemplateDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaLibraryTemplateDefinition)
