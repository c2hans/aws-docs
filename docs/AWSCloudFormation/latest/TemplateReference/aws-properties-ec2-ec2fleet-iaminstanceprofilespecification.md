---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-iaminstanceprofilespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet IamInstanceProfileSpecification
<a name="aws-properties-ec2-ec2fleet-iaminstanceprofilespecification"></a>

Describes an IAM instance profile.

## Syntax
<a name="aws-properties-ec2-ec2fleet-iaminstanceprofilespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-iaminstanceprofilespecification-syntax.json"></a>

```
{
  "[Arn](#cfn-ec2-ec2fleet-iaminstanceprofilespecification-arn)" : {{String}},
  "[Name](#cfn-ec2-ec2fleet-iaminstanceprofilespecification-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-iaminstanceprofilespecification-syntax.yaml"></a>

```
  [Arn](#cfn-ec2-ec2fleet-iaminstanceprofilespecification-arn): {{String}}
  [Name](#cfn-ec2-ec2fleet-iaminstanceprofilespecification-name): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-iaminstanceprofilespecification-properties"></a>

`Arn`  <a name="cfn-ec2-ec2fleet-iaminstanceprofilespecification-arn"></a>
The Amazon Resource Name (ARN) of the instance profile.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ec2-ec2fleet-iaminstanceprofilespecification-name"></a>
The name of the instance profile.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
