---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_MetaFlowWhatsAppBusinessAccountInfo.html
---

# MetaFlowWhatsAppBusinessAccountInfo
<a name="API_MetaFlowWhatsAppBusinessAccountInfo"></a>

Contains WhatsApp Business Account metadata associated with a Flow, as returned by Meta.

## Contents
<a name="API_MetaFlowWhatsAppBusinessAccountInfo_Contents"></a>

 ** id **   <a name="Social-Type-MetaFlowWhatsAppBusinessAccountInfo-id"></a>
The WhatsApp Business Account ID from Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** name **   <a name="Social-Type-MetaFlowWhatsAppBusinessAccountInfo-name"></a>
The name of the WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** currency **   <a name="Social-Type-MetaFlowWhatsAppBusinessAccountInfo-currency"></a>
The currency code for the WhatsApp Business Account (for example, USD).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** messageTemplateNamespace **   <a name="Social-Type-MetaFlowWhatsAppBusinessAccountInfo-messageTemplateNamespace"></a>
The message template namespace for the WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** timezoneId **   <a name="Social-Type-MetaFlowWhatsAppBusinessAccountInfo-timezoneId"></a>
The timezone ID for the WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

## See Also
<a name="API_MetaFlowWhatsAppBusinessAccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/MetaFlowWhatsAppBusinessAccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/MetaFlowWhatsAppBusinessAccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/MetaFlowWhatsAppBusinessAccountInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
