---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-gateway-greengrassv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Gateway GreengrassV2
<a name="aws-properties-iotsitewise-gateway-greengrassv2"></a>

Contains details for a gateway that runs on AWS IoT Greengrass V2. To create a gateway that runs on AWS IoT Greengrass V2, you must deploy the IoT SiteWise Edge component to your gateway device. Your [Greengrass device role](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html) must use the `AWSIoTSiteWiseEdgeAccess` policy. For more information, see [Using AWS IoT SiteWise at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sw-gateways.html) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-properties-iotsitewise-gateway-greengrassv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-gateway-greengrassv2-syntax.json"></a>

```
{
  "[CoreDeviceOperatingSystem](#cfn-iotsitewise-gateway-greengrassv2-coredeviceoperatingsystem)" : {{String}},
  "[CoreDeviceThingName](#cfn-iotsitewise-gateway-greengrassv2-coredevicethingname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-gateway-greengrassv2-syntax.yaml"></a>

```
  [CoreDeviceOperatingSystem](#cfn-iotsitewise-gateway-greengrassv2-coredeviceoperatingsystem): {{String}}
  [CoreDeviceThingName](#cfn-iotsitewise-gateway-greengrassv2-coredevicethingname): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-gateway-greengrassv2-properties"></a>

`CoreDeviceOperatingSystem`  <a name="cfn-iotsitewise-gateway-greengrassv2-coredeviceoperatingsystem"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `LINUX_AARCH64 | LINUX_AMD64 | WINDOWS_AMD64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CoreDeviceThingName`  <a name="cfn-iotsitewise-gateway-greengrassv2-coredevicethingname"></a>
The name of the AWS IoT thing for your AWS IoT Greengrass V2 core device.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
