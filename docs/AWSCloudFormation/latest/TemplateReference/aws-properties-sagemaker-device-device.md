---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-device-device.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Device Device
<a name="aws-properties-sagemaker-device-device"></a>

Information of a particular device.

## Syntax
<a name="aws-properties-sagemaker-device-device-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-device-device-syntax.json"></a>

```
{
  "[Description](#cfn-sagemaker-device-device-description)" : {{String}},
  "[DeviceName](#cfn-sagemaker-device-device-devicename)" : {{String}},
  "[IotThingName](#cfn-sagemaker-device-device-iotthingname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-device-device-syntax.yaml"></a>

```
  [Description](#cfn-sagemaker-device-device-description): {{String}}
  [DeviceName](#cfn-sagemaker-device-device-devicename): {{String}}
  [IotThingName](#cfn-sagemaker-device-device-iotthingname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-device-device-properties"></a>

`Description`  <a name="cfn-sagemaker-device-device-description"></a>
Description of the device.
*Required*: No
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceName`  <a name="cfn-sagemaker-device-device-devicename"></a>
The name of the device.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IotThingName`  <a name="cfn-sagemaker-device-device-iotthingname"></a>
AWS Internet of Things (IoT) object name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
