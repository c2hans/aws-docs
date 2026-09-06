---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-gateway-gatewayplatform.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Gateway GatewayPlatform
<a name="aws-properties-iotsitewise-gateway-gatewayplatform"></a>

The gateway's platform configuration. You can only specify one platform type in a gateway.

(Legacy only) For Greengrass V1 gateways, specify the `greengrass` parameter with a valid Greengrass group ARN.

For Greengrass V2 gateways, specify the `greengrassV2` parameter with a valid core device thing name. If creating a V3 gateway (`gatewayVersion=3`), you must also specify the `coreDeviceOperatingSystem`.

For Siemens Industrial Edge gateways, specify the `siemensIE` parameter with a valid IoT Core thing name.

## Syntax
<a name="aws-properties-iotsitewise-gateway-gatewayplatform-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-gateway-gatewayplatform-syntax.json"></a>

```
{
  "[GreengrassV2](#cfn-iotsitewise-gateway-gatewayplatform-greengrassv2)" : {{GreengrassV2}},
  "[SiemensIE](#cfn-iotsitewise-gateway-gatewayplatform-siemensie)" : {{SiemensIE}}
}
```

### YAML
<a name="aws-properties-iotsitewise-gateway-gatewayplatform-syntax.yaml"></a>

```
  [GreengrassV2](#cfn-iotsitewise-gateway-gatewayplatform-greengrassv2): {{
    GreengrassV2}}
  [SiemensIE](#cfn-iotsitewise-gateway-gatewayplatform-siemensie): {{
    SiemensIE}}
```

## Properties
<a name="aws-properties-iotsitewise-gateway-gatewayplatform-properties"></a>

`GreengrassV2`  <a name="cfn-iotsitewise-gateway-gatewayplatform-greengrassv2"></a>
A gateway that runs on AWS IoT Greengrass V2.
*Required*: No
*Type*: [GreengrassV2](aws-properties-iotsitewise-gateway-greengrassv2.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SiemensIE`  <a name="cfn-iotsitewise-gateway-gatewayplatform-siemensie"></a>
An AWS IoT SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.
*Required*: No
*Type*: [SiemensIE](aws-properties-iotsitewise-gateway-siemensie.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
