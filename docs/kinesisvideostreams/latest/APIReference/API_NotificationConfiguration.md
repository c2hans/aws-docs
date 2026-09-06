---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_NotificationConfiguration"></a>

Use this API to configure Amazon Simple Notification Service (Amazon SNS) notifications for when fragments become available in a stream. If this parameter is null, the configuration will be deleted from the stream.

See [Notifications in Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/notifications.html) for more information.

## Contents
<a name="API_NotificationConfiguration_Contents"></a>

 ** DestinationConfig **   <a name="KinesisVideo-Type-NotificationConfiguration-DestinationConfig"></a>
The destination information required to deliver a notification to a customer.
Type: [NotificationDestinationConfig](API_NotificationDestinationConfig.md) object
Required: Yes

 ** Status **   <a name="KinesisVideo-Type-NotificationConfiguration-Status"></a>
Indicates if a notification configuration is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/NotificationConfiguration)
