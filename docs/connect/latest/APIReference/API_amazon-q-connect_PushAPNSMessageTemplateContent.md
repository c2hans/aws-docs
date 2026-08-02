---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_PushAPNSMessageTemplateContent.html
---

# PushAPNSMessageTemplateContent
<a name="API_amazon-q-connect_PushAPNSMessageTemplateContent"></a>

The content of the push message template that applies to APNS (Apple Push Notification service) notification service.

## Contents
<a name="API_amazon-q-connect_PushAPNSMessageTemplateContent_Contents"></a>

 ** action **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-action"></a>
The action to occur if a recipient taps a push notification that is based on the message template. Valid values are:
+  `OPEN_APP` - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
+  `DEEP_LINK` - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the iOS platform.
+  `URL` - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.
Type: String
Valid Values: `OPEN_APP | DEEP_LINK | URL`
Required: No

 ** body **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-body"></a>
The message body to use in a push notification that is based on the message template.
Type: [MessageTemplateBodyContentProvider](API_amazon-q-connect_MessageTemplateBodyContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** mediaUrl **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-mediaUrl"></a>
The URL of an image or video to display in push notifications that are based on the message template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** rawContent **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-rawContent"></a>
The raw, JSON-formatted string to use as the payload for a push notification that's based on the message template. If specified, this value overrides all other content for the message template.
Type: [MessageTemplateBodyContentProvider](API_amazon-q-connect_MessageTemplateBodyContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sound **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-sound"></a>
The key for the sound to play when the recipient receives a push notification that's based on the message template. The value for this key is the name of a sound file in your app's main bundle or the `Library/Sounds` folder in your app's data container. If the sound file can't be found or you specify `default` for the value, the system plays the default alert sound.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** title **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-title"></a>
The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** url **   <a name="connect-Type-amazon-q-connect_PushAPNSMessageTemplateContent-url"></a>
The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the `action` property is `URL`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_amazon-q-connect_PushAPNSMessageTemplateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/PushAPNSMessageTemplateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/PushAPNSMessageTemplateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/PushAPNSMessageTemplateContent)
