---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LocationModel.html
---

# LocationModel
<a name="API_LocationModel"></a>

Properties of a location, which can include its name, ARN (for custom locations), and ping beacon information.

## Contents
<a name="API_LocationModel_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LocationArn **   <a name="gameliftservers-Type-LocationModel-LocationArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a custom location resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:.*:location\/custom-\S+`
Required: No

 ** LocationName **   <a name="gameliftservers-Type-LocationModel-LocationName"></a>
The location's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** PingBeacon **   <a name="gameliftservers-Type-LocationModel-PingBeacon"></a>
Information about the UDP ping beacon for this location. Ping beacons are fixed endpoints that you can use to measure network latency between a player device and an Amazon GameLift Servers hosting location.
Type: [PingBeacon](API_PingBeacon.md) object
Required: No

## See Also
<a name="API_LocationModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationModel)
