---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WebNotificationContent.html
---

# WebNotificationContent
<a name="API_WebNotificationContent"></a>

The content of an outbound web notification, including the notification type, the view to render, and any optional attributes used to populate the view.

## Contents
<a name="API_WebNotificationContent_Contents"></a>

 ** Type **   <a name="connect-Type-WebNotificationContent-Type"></a>
The type of web notification to send.
Type: String
Valid Values: `WIDGET_VIEW | WIDGET_ACTION`
Required: Yes

 ** Attributes **   <a name="connect-Type-WebNotificationContent-Attributes"></a>
Optional attributes used to populate the notification content, such as recommender configuration for personalized content.
Type: [ContentAttributes](API_ContentAttributes.md) object
Required: No

 ** ViewArn **   <a name="connect-Type-WebNotificationContent-ViewArn"></a>
The Amazon Resource Name (ARN) of the view to render for the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_WebNotificationContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WebNotificationContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WebNotificationContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WebNotificationContent)
