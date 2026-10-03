---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateNotifyParameters.html
---

# UpdateNotifyParameters
<a name="API_UpdateNotifyParameters"></a>

The updated delivery parameters for the preapproved notify-template route. Absent members preserve the current value, and the empty sentinel on a member clears it.

## Contents
<a name="API_UpdateNotifyParameters_Contents"></a>

 ** notifyTemplateId **   <a name="endusermessaging-Type-UpdateNotifyParameters-notifyTemplateId"></a>
The updated identifier of a preapproved notify template for the SMS or voice channels. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** voiceId **   <a name="endusermessaging-Type-UpdateNotifyParameters-voiceId"></a>
The updated Amazon Polly voice ID. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[A-Za-z0-9]*`
Required: No

## See Also
<a name="API_UpdateNotifyParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateNotifyParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateNotifyParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateNotifyParameters)
