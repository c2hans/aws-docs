---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccountSummary.html
---

# LinkedWhatsAppBusinessAccountSummary
<a name="API_LinkedWhatsAppBusinessAccountSummary"></a>

The details of a linked WhatsApp Business Account.

## Contents
<a name="API_LinkedWhatsAppBusinessAccountSummary_Contents"></a>

 ** arn **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-arn"></a>
The ARN of the linked WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*:waba/[0-9a-zA-Z]+`
Required: Yes

 ** eventDestinations **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-eventDestinations"></a>
The event destinations for the linked WhatsApp Business Account.
Type: Array of [WhatsAppBusinessAccountEventDestination](API_WhatsAppBusinessAccountEventDestination.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** id **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-id"></a>
The ID of the linked WhatsApp Business Account, formatted as `waba-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

 ** linkDate **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-linkDate"></a>
The date the WhatsApp Business Account was linked.
Type: Timestamp
Required: Yes

 ** registrationStatus **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-registrationStatus"></a>
The registration status of the linked WhatsApp Business Account.
Type: String
Valid Values: `COMPLETE | INCOMPLETE`
Required: Yes

 ** wabaId **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-wabaId"></a>
The WhatsApp Business Account ID provided by Meta.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** wabaName **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-wabaName"></a>
The name of the linked WhatsApp Business Account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** datasetId **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-datasetId"></a>
The Meta Conversions API dataset ID associated with this WhatsApp Business Account. This value is a numeric string of 10 to 20 digits. This field is not present when no dataset has been created for this account.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `[0-9]+`
Required: No

 ** marketingMessagesOnboardingStatus **   <a name="Social-Type-LinkedWhatsAppBusinessAccountSummary-marketingMessagesOnboardingStatus"></a>
The onboarding status for the Marketing Messages API. This value is fetched from Meta and indicates whether the WhatsApp Business Account is onboarded for Meta's Marketing Messages API.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_LinkedWhatsAppBusinessAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/LinkedWhatsAppBusinessAccountSummary)
