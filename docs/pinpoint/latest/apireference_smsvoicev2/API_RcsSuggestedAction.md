---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsSuggestedAction.html
---

# RcsSuggestedAction
<a name="API_RcsSuggestedAction"></a>

A suggested action displayed to the RCS message recipient. Can be a reply, open URL, dial phone, show location, request location, or create calendar event.

## Contents
<a name="API_RcsSuggestedAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CreateCalendarEvent **   <a name="pinpoint-Type-RcsSuggestedAction-CreateCalendarEvent"></a>
A suggested action that creates a calendar event on the user's device.
Type: [RcsCreateCalendarEventAction](API_RcsCreateCalendarEventAction.md) object
Required: No

 ** DialPhone **   <a name="pinpoint-Type-RcsSuggestedAction-DialPhone"></a>
A suggested action that initiates a phone call to the specified number.
Type: [RcsDialPhoneAction](API_RcsDialPhoneAction.md) object
Required: No

 ** OpenUrl **   <a name="pinpoint-Type-RcsSuggestedAction-OpenUrl"></a>
A suggested action that opens a URL in the user's browser or a webview.
Type: [RcsOpenUrlAction](API_RcsOpenUrlAction.md) object
Required: No

 ** Reply **   <a name="pinpoint-Type-RcsSuggestedAction-Reply"></a>
A suggested reply that sends predefined text and postback data when tapped.
Type: [RcsReplyAction](API_RcsReplyAction.md) object
Required: No

 ** RequestLocation **   <a name="pinpoint-Type-RcsSuggestedAction-RequestLocation"></a>
A suggested action that requests the user's current location.
Type: [RcsRequestLocationAction](API_RcsRequestLocationAction.md) object
Required: No

 ** ShowLocation **   <a name="pinpoint-Type-RcsSuggestedAction-ShowLocation"></a>
A suggested action that shows a location on a map.
Type: [RcsShowLocationAction](API_RcsShowLocationAction.md) object
Required: No

## See Also
<a name="API_RcsSuggestedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsSuggestedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsSuggestedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsSuggestedAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
