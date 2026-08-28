---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GatewayPlatform.html
---

# GatewayPlatform
<a name="API_GatewayPlatform"></a>

The gateway's platform configuration. You can only specify one platform type in a gateway.

(Legacy only) For Greengrass V1 gateways, specify the `greengrass` parameter with a valid Greengrass group ARN.

For Greengrass V2 gateways, specify the `greengrassV2` parameter with a valid core device thing name. If creating a V3 gateway (`gatewayVersion=3`), you must also specify the `coreDeviceOperatingSystem`.

For Siemens Industrial Edge gateways, specify the `siemensIE` parameter with a valid IoT Core thing name.

## Contents
<a name="API_GatewayPlatform_Contents"></a>

 ** greengrass **   <a name="iotsitewise-Type-GatewayPlatform-greengrass"></a>
A gateway that runs on AWS IoT Greengrass.
Type: [Greengrass](API_Greengrass.md) object
Required: No

 ** greengrassV2 **   <a name="iotsitewise-Type-GatewayPlatform-greengrassV2"></a>
A gateway that runs on AWS IoT Greengrass V2.
Type: [GreengrassV2](API_GreengrassV2.md) object
Required: No

 ** siemensIE **   <a name="iotsitewise-Type-GatewayPlatform-siemensIE"></a>
A SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.
Type: [SiemensIE](API_SiemensIE.md) object
Required: No

## See Also
<a name="API_GatewayPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GatewayPlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GatewayPlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GatewayPlatform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
