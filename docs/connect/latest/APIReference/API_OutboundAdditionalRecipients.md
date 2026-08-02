---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundAdditionalRecipients.html
---

# OutboundAdditionalRecipients
<a name="API_OutboundAdditionalRecipients"></a>

Information about the additional recipients of outbound email.

## Contents
<a name="API_OutboundAdditionalRecipients_Contents"></a>

 ** CcEmailAddresses **   <a name="connect-Type-OutboundAdditionalRecipients-CcEmailAddresses"></a>
Information about the **additional** CC email address recipients. Email recipients are limited to 50 total addresses: 1 required recipient in the [DestinationEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_SendOutboundEmail.html#API_SendOutboundEmail_RequestBody) field and up to 49 recipients in the 'CcEmailAddresses' field.
Type: Array of [EmailAddressInfo](API_EmailAddressInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_OutboundAdditionalRecipients_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/OutboundAdditionalRecipients)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/OutboundAdditionalRecipients)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/OutboundAdditionalRecipients)
