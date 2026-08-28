---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-devicedefinition-device.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::DeviceDefinition Device
<a name="aws-properties-greengrass-devicedefinition-device"></a>

<a name="aws-properties-greengrass-devicedefinition-device-description"></a> A device is an AWS IoT device (thing) that's added to a Greengrass group. Greengrass devices can communicate with the Greengrass core in the same group. For more information, see [What Is AWS IoT Greengrass?](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-devicedefinition-device-inheritance"></a> In an CloudFormation template, the `Devices` property of the [`DeviceDefinitionVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html) property type contains a list of `Device` property types.

## Syntax
<a name="aws-properties-greengrass-devicedefinition-device-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-devicedefinition-device-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-greengrass-devicedefinition-device-certificatearn)" : {{String}},
  "[Id](#cfn-greengrass-devicedefinition-device-id)" : {{String}},
  "[SyncShadow](#cfn-greengrass-devicedefinition-device-syncshadow)" : {{Boolean}},
  "[ThingArn](#cfn-greengrass-devicedefinition-device-thingarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-devicedefinition-device-syntax.yaml"></a>

```
  [CertificateArn](#cfn-greengrass-devicedefinition-device-certificatearn): {{String}}
  [Id](#cfn-greengrass-devicedefinition-device-id): {{String}}
  [SyncShadow](#cfn-greengrass-devicedefinition-device-syncshadow): {{Boolean}}
  [ThingArn](#cfn-greengrass-devicedefinition-device-thingarn): {{String}}
```

## Properties
<a name="aws-properties-greengrass-devicedefinition-device-properties"></a>

`CertificateArn`  <a name="cfn-greengrass-devicedefinition-device-certificatearn"></a>
The Amazon Resource Name (ARN) of the device certificate for the device. This X.509 certificate is used to authenticate the device with AWS IoT and AWS IoT Greengrass services.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Id`  <a name="cfn-greengrass-devicedefinition-device-id"></a>
A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Maximum length is 128 characters with pattern `[a-zA-Z0-9:_-]+`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SyncShadow`  <a name="cfn-greengrass-devicedefinition-device-syncshadow"></a>
Indicates whether the device's local shadow is synced with the cloud automatically.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThingArn`  <a name="cfn-greengrass-devicedefinition-device-thingarn"></a>
The ARN of the device, which is an AWS IoT device (thing).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-devicedefinition-device--seealso"></a>
+ [Device](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-device.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
