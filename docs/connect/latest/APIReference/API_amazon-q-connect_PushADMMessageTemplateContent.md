---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_PushADMMessageTemplateContent.html
---

# PushADMMessageTemplateContent
<a name="API_amazon-q-connect_PushADMMessageTemplateContent"></a>

The content of the push message template that applies to ADM (Amazon Device Messaging) notification service.

## Contents
<a name="API_amazon-q-connect_PushADMMessageTemplateContent_Contents"></a>

 ** action **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-action"></a>
The action to occur if a recipient taps a push notification that is based on the message template. Valid values are:
+  `OPEN_APP` - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
+  `DEEP_LINK` - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
+  `URL` - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
Type: String
Valid Values: `OPEN_APP | DEEP_LINK | URL`
Required: No

 ** body **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-body"></a>
The message body to use in a push notification that is based on the message template.
Type: [MessageTemplateBodyContentProvider](API_amazon-q-connect_MessageTemplateBodyContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** imageIconUrl **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-imageIconUrl"></a>
The URL of the large icon image to display in the content view of a push notification that's based on the message template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** imageUrl **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-imageUrl"></a>
The URL of an image to display in a push notification that's based on the message template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** rawContent **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-rawContent"></a>
The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.
Type: [MessageTemplateBodyContentProvider](API_amazon-q-connect_MessageTemplateBodyContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** smallImageIconUrl **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-smallImageIconUrl"></a>
The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** sound **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-sound"></a>
The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** title **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-title"></a>
The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** url **   <a name="connect-Type-amazon-q-connect_PushADMMessageTemplateContent-url"></a>
The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the `action` property is `URL`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_amazon-q-connect_PushADMMessageTemplateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/PushADMMessageTemplateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/PushADMMessageTemplateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/PushADMMessageTemplateContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
