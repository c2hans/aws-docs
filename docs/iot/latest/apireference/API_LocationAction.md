---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_LocationAction.html
---

# LocationAction
<a name="API_LocationAction"></a>

The Amazon Location rule action sends device location updates from an MQTT message to an Amazon Location tracker resource.

## Contents
<a name="API_LocationAction_Contents"></a>

 ** deviceId **   <a name="iot-Type-LocationAction-deviceId"></a>
The unique ID of the device providing the location data.
Type: String
Required: Yes

 ** latitude **   <a name="iot-Type-LocationAction-latitude"></a>
A string that evaluates to a double value that represents the latitude of the device's location.
Type: String
Required: Yes

 ** longitude **   <a name="iot-Type-LocationAction-longitude"></a>
A string that evaluates to a double value that represents the longitude of the device's location.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-LocationAction-roleArn"></a>
The IAM role that grants permission to write to the Amazon Location resource.
Type: String
Required: Yes

 ** trackerName **   <a name="iot-Type-LocationAction-trackerName"></a>
The name of the tracker resource in Amazon Location in which the location is updated.
Type: String
Required: Yes

 ** timestamp **   <a name="iot-Type-LocationAction-timestamp"></a>
The time that the location data was sampled. The default value is the time the MQTT message was processed.
Type: [LocationTimestamp](API_LocationTimestamp.md) object
Required: No

## See Also
<a name="API_LocationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/LocationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/LocationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/LocationAction)
