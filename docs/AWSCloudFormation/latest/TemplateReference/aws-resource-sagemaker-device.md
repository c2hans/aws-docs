---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-device.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Device
<a name="aws-resource-sagemaker-device"></a>

The `AWS::SageMaker::Device` resource is an Amazon SageMaker resource type that allows you to register your Devices against an existing SageMaker Edge Manager DeviceFleet. Each device must be listed individually in the CFN specification.

## Syntax
<a name="aws-resource-sagemaker-device-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-device-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Device",
  "Properties" : {
      "[Device](#cfn-sagemaker-device-device)" : {{Device}},
      "[DeviceFleetName](#cfn-sagemaker-device-devicefleetname)" : {{String}},
      "[Tags](#cfn-sagemaker-device-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-device-syntax.yaml"></a>

```
Type: AWS::SageMaker::Device
Properties:
  [Device](#cfn-sagemaker-device-device): {{
    Device}}
  [DeviceFleetName](#cfn-sagemaker-device-devicefleetname): {{String}}
  [Tags](#cfn-sagemaker-device-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-device-properties"></a>

`Device`  <a name="cfn-sagemaker-device-device"></a>
Edge device you want to create.
*Required*: No
*Type*: [Device](aws-properties-sagemaker-device-device.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceFleetName`  <a name="cfn-sagemaker-device-devicefleetname"></a>
The name of the fleet the device belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-device-tags"></a>
An array of key-value pairs that contain metadata to help you categorize and organize your devices. Each tag consists of a key and a value, both of which you define.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-device-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-device-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-device-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DeviceFleetName.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
