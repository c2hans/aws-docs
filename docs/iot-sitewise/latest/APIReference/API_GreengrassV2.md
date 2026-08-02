---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GreengrassV2.html
---

# GreengrassV2
<a name="API_GreengrassV2"></a>

Contains details for a gateway that runs on AWS IoT Greengrass V2. To create a gateway that runs on AWS IoT Greengrass V2, you must deploy the IoT SiteWise Edge component to your gateway device. Your [Greengrass device role](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html) must use the `AWSIoTSiteWiseEdgeAccess` policy. For more information, see [Using AWS IoT SiteWise at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sw-gateways.html) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_GreengrassV2_Contents"></a>

 ** coreDeviceThingName **   <a name="iotsitewise-Type-GreengrassV2-coreDeviceThingName"></a>
The name of the AWS IoT thing for your AWS IoT Greengrass V2 core device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9:_-]+$`
Required: Yes

 ** coreDeviceOperatingSystem **   <a name="iotsitewise-Type-GreengrassV2-coreDeviceOperatingSystem"></a>
The operating system of the core device in AWS IoT Greengrass V2. Specifying the operating system is required for MQTT-enabled, V3 gateways (`gatewayVersion` `3`) and not applicable for Classic stream, V2 gateways (`gatewayVersion` `2`).
Type: String
Valid Values: `LINUX_AARCH64 | LINUX_AMD64 | WINDOWS_AMD64`
Required: No

## See Also
<a name="API_GreengrassV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GreengrassV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GreengrassV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GreengrassV2)
