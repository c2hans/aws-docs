---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DestinationConfiguration.html
---

# DestinationConfiguration
<a name="API_DestinationConfiguration"></a>

The [link to action] metadata transfer job destination configuration.

## Contents
<a name="API_DestinationConfiguration_Contents"></a>

 ** type **   <a name="tm-Type-DestinationConfiguration-type"></a>
The destination type.
Type: String
Valid Values: `s3 | iotsitewise | iottwinmaker`
Required: Yes

 ** iotTwinMakerConfiguration **   <a name="tm-Type-DestinationConfiguration-iotTwinMakerConfiguration"></a>
The metadata transfer job AWS IoT TwinMaker configuration.
Type: [IotTwinMakerDestinationConfiguration](API_IotTwinMakerDestinationConfiguration.md) object
Required: No

 ** s3Configuration **   <a name="tm-Type-DestinationConfiguration-s3Configuration"></a>
The metadata transfer job S3 configuration. [need to add S3 entity]
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

## See Also
<a name="API_DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/DestinationConfiguration)
