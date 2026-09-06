---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsShowLocationAction.html
---

# RcsShowLocationAction
<a name="API_RcsShowLocationAction"></a>

A suggested action that shows a location on a map when tapped by the recipient.

## Contents
<a name="API_RcsShowLocationAction_Contents"></a>

 ** Latitude **   <a name="pinpoint-Type-RcsShowLocationAction-Latitude"></a>
The latitude of the location. Valid values are -90 to 90.
Type: Double
Valid Range: Minimum value of -90. Maximum value of 90.
Required: Yes

 ** Longitude **   <a name="pinpoint-Type-RcsShowLocationAction-Longitude"></a>
The longitude of the location. Valid values are -180 to 180.
Type: Double
Valid Range: Minimum value of -180. Maximum value of 180.
Required: Yes

 ** PostbackData **   <a name="pinpoint-Type-RcsShowLocationAction-PostbackData"></a>
The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Text **   <a name="pinpoint-Type-RcsShowLocationAction-Text"></a>
The display text of the action. Maximum 25 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: Yes

 ** Label **   <a name="pinpoint-Type-RcsShowLocationAction-Label"></a>
An optional label for the location pin. Maximum 100 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_RcsShowLocationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsShowLocationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsShowLocationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsShowLocationAction)
