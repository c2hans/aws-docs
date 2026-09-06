---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PropertyNotification.html
---

# PropertyNotification
<a name="API_PropertyNotification"></a>

Contains asset property value notification information. When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see [Interacting with other services](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_PropertyNotification_Contents"></a>

 ** state **   <a name="iotsitewise-Type-PropertyNotification-state"></a>
The current notification state.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** topic **   <a name="iotsitewise-Type-PropertyNotification-topic"></a>
The MQTT topic to which AWS IoT SiteWise publishes property value update notifications.
Type: String
Required: Yes

## See Also
<a name="API_PropertyNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PropertyNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PropertyNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PropertyNotification)
