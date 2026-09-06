---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-elasticgpuspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance ElasticGpuSpecification
<a name="aws-properties-ec2-instance-elasticgpuspecification"></a>

**Note**
Amazon Elastic Graphics reached end of life on January 8, 2024.

Specifies the type of Elastic GPU. An Elastic GPU is a GPU resource that you can attach to your Amazon EC2 instance to accelerate the graphics performance of your applications.

`ElasticGpuSpecification` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-elasticgpuspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-elasticgpuspecification-syntax.json"></a>

```
{
  "[Type](#cfn-ec2-instance-elasticgpuspecification-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-elasticgpuspecification-syntax.yaml"></a>

```
  [Type](#cfn-ec2-instance-elasticgpuspecification-type): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-elasticgpuspecification-properties"></a>

`Type`  <a name="cfn-ec2-instance-elasticgpuspecification-type"></a>
The type of Elastic Graphics accelerator.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
