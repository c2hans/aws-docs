---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsCreateCalendarEventAction.html
---

# RcsCreateCalendarEventAction
<a name="API_RcsCreateCalendarEventAction"></a>

A suggested action that creates a calendar event on the recipient's device.

## Contents
<a name="API_RcsCreateCalendarEventAction_Contents"></a>

 ** EndTime **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-EndTime"></a>
The end time of the calendar event in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** PostbackData **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-PostbackData"></a>
The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** StartTime **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-StartTime"></a>
The start time of the calendar event in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** Text **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-Text"></a>
The display text of the action. Maximum 25 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: Yes

 ** Title **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-Title"></a>
The title of the calendar event. Maximum 100 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **   <a name="pinpoint-Type-RcsCreateCalendarEventAction-Description"></a>
An optional description for the calendar event. Maximum 500 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_RcsCreateCalendarEventAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsCreateCalendarEventAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsCreateCalendarEventAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsCreateCalendarEventAction)
