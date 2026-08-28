---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdatePhoneNumberRequestItem.html
---

# UpdatePhoneNumberRequestItem
<a name="API_voice-chime_UpdatePhoneNumberRequestItem"></a>

The phone number ID, product type, or calling name fields to update, used with the [BatchUpdatePhoneNumber](API_voice-chime_BatchUpdatePhoneNumber.md) and [UpdatePhoneNumber](API_voice-chime_UpdatePhoneNumber.md) actions.

## Contents
<a name="API_voice-chime_UpdatePhoneNumberRequestItem_Contents"></a>

 ** PhoneNumberId **   <a name="chimesdk-Type-voice-chime_UpdatePhoneNumberRequestItem-PhoneNumberId"></a>
The phone number ID to update.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** CallingName **   <a name="chimesdk-Type-voice-chime_UpdatePhoneNumberRequestItem-CallingName"></a>
The outbound calling name to update.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_UpdatePhoneNumberRequestItem-Name"></a>
The name of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^$|^[a-zA-Z0-9\,\.\_\-]+(\s+[a-zA-Z0-9\,\.\_\-]+)*$`
Required: No

 ** ProductType **   <a name="chimesdk-Type-voice-chime_UpdatePhoneNumberRequestItem-ProductType"></a>
The product type to update.
Type: String
Valid Values: `VoiceConnector | SipMediaApplicationDialIn`
Required: No

## See Also
<a name="API_voice-chime_UpdatePhoneNumberRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdatePhoneNumberRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdatePhoneNumberRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdatePhoneNumberRequestItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
