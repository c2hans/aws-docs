---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_InboundAdditionalRecipients.html
---

# InboundAdditionalRecipients
<a name="API_InboundAdditionalRecipients"></a>

Information about the additional TO and CC recipients of an inbound email contact.

**Note**
You can include up to 50 email addresses in total, distributed across [DestinationEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html#API_StartEmailContact_RequestBody), `ToAddresses`, and `CcAddresses`. This total must include one required `DestinationEmailAddress`. You can then specify up to 49 addresses allocated across `ToAddresses` and `CcAddresses` as needed.

## Contents
<a name="API_InboundAdditionalRecipients_Contents"></a>

 ** CcAddresses **   <a name="connect-Type-InboundAdditionalRecipients-CcAddresses"></a>
The **additional** recipients information present in cc list. You must have 1 required recipient (`DestinationEmailAddress`). You can then specify up to 49 additional recipients (across `ToAddresses` and `CcAddresses`), for a total of 50 recipients.
Type: Array of [EmailAddressInfo](API_EmailAddressInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ToAddresses **   <a name="connect-Type-InboundAdditionalRecipients-ToAddresses"></a>
The **additional** recipients information present in to list. You must have 1 required recipient (`DestinationEmailAddress`). You can then specify up to 49 additional recipients (across `ToAddresses` and `CcAddresses`), for a total of 50 recipients.
Type: Array of [EmailAddressInfo](API_EmailAddressInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_InboundAdditionalRecipients_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/InboundAdditionalRecipients)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/InboundAdditionalRecipients)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/InboundAdditionalRecipients)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
