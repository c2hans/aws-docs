---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_TemplateSummary.html
---

# TemplateSummary
<a name="API_connect-cases_TemplateSummary"></a>

Template summary information.

## Contents
<a name="API_connect-cases_TemplateSummary_Contents"></a>

 ** name **   <a name="connect-Type-connect-cases_TemplateSummary-name"></a>
The template name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** status **   <a name="connect-Type-connect-cases_TemplateSummary-status"></a>
The status of the template.
Type: String
Valid Values: `Active | Inactive`
Required: Yes

 ** templateArn **   <a name="connect-Type-connect-cases_TemplateSummary-templateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** templateId **   <a name="connect-Type-connect-cases_TemplateSummary-templateId"></a>
The unique identifier for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** tagPropagationConfigurations **   <a name="connect-Type-connect-cases_TemplateSummary-tagPropagationConfigurations"></a>
Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.
Type: Array of [TagPropagationConfiguration](API_connect-cases_TagPropagationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_connect-cases_TemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/TemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/TemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/TemplateSummary)
