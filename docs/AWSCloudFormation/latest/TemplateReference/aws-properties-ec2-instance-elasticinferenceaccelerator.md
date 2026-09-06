---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-elasticinferenceaccelerator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance ElasticInferenceAccelerator
<a name="aws-properties-ec2-instance-elasticinferenceaccelerator"></a>

**Note**
Amazon Elastic Inference is no longer available.

Specifies the Elastic Inference Accelerator for the instance.

`ElasticInferenceAccelerator` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-elasticinferenceaccelerator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-elasticinferenceaccelerator-syntax.json"></a>

```
{
  "[Count](#cfn-ec2-instance-elasticinferenceaccelerator-count)" : {{Integer}},
  "[Type](#cfn-ec2-instance-elasticinferenceaccelerator-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-elasticinferenceaccelerator-syntax.yaml"></a>

```
  [Count](#cfn-ec2-instance-elasticinferenceaccelerator-count): {{Integer}}
  [Type](#cfn-ec2-instance-elasticinferenceaccelerator-type): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-elasticinferenceaccelerator-properties"></a>

`Count`  <a name="cfn-ec2-instance-elasticinferenceaccelerator-count"></a>
The number of elastic inference accelerators to attach to the instance.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-ec2-instance-elasticinferenceaccelerator-type"></a>
 The type of elastic inference accelerator. The possible values are `eia1.medium`, `eia1.large`, `eia1.xlarge`, `eia2.medium`, `eia2.large`, and `eia2.xlarge`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
