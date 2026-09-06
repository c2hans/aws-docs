---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-associationparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance AssociationParameter
<a name="aws-properties-ec2-instance-associationparameter"></a>

Specifies input parameter values for an SSM document in AWS Systems Manager.

`AssociationParameter` is a property of the [SsmAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociation.html) property type.

## Syntax
<a name="aws-properties-ec2-instance-associationparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-associationparameter-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-instance-associationparameter-key)" : {{String}},
  "[Value](#cfn-ec2-instance-associationparameter-value)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-instance-associationparameter-syntax.yaml"></a>

```
  [Key](#cfn-ec2-instance-associationparameter-key): {{String}}
  [Value](#cfn-ec2-instance-associationparameter-value): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-instance-associationparameter-properties"></a>

`Key`  <a name="cfn-ec2-instance-associationparameter-key"></a>
The name of an input parameter that is in the associated SSM document.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-instance-associationparameter-value"></a>
The value of an input parameter.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
