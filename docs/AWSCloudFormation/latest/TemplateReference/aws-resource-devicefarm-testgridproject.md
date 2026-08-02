---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devicefarm-testgridproject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DeviceFarm::TestGridProject
<a name="aws-resource-devicefarm-testgridproject"></a>

A Selenium testing project. Projects are used to collect and collate sessions.

## Syntax
<a name="aws-resource-devicefarm-testgridproject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devicefarm-testgridproject-syntax.json"></a>

```
{
  "Type" : "AWS::DeviceFarm::TestGridProject",
  "Properties" : {
      "[Description](#cfn-devicefarm-testgridproject-description)" : {{String}},
      "[Name](#cfn-devicefarm-testgridproject-name)" : {{String}},
      "[Tags](#cfn-devicefarm-testgridproject-tags)" : {{[ Tag, ... ]}},
      "[VpcConfig](#cfn-devicefarm-testgridproject-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-devicefarm-testgridproject-syntax.yaml"></a>

```
Type: AWS::DeviceFarm::TestGridProject
Properties:
  [Description](#cfn-devicefarm-testgridproject-description): {{String}}
  [Name](#cfn-devicefarm-testgridproject-name): {{String}}
  [Tags](#cfn-devicefarm-testgridproject-tags): {{
    - Tag}}
  [VpcConfig](#cfn-devicefarm-testgridproject-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-devicefarm-testgridproject-properties"></a>

`Description`  <a name="cfn-devicefarm-testgridproject-description"></a>
A human-readable description for the project.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-devicefarm-testgridproject-name"></a>
A human-readable name for the project.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-devicefarm-testgridproject-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *AWS CloudFormation guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-devicefarm-testgridproject-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-devicefarm-testgridproject-vpcconfig"></a>
The VPC security groups and subnets that are attached to a project.
*Required*: No
*Type*: [VpcConfig](aws-properties-devicefarm-testgridproject-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devicefarm-testgridproject-return-values"></a>

### Ref
<a name="aws-resource-devicefarm-testgridproject-return-values-ref"></a>

Not supported for this resource.

### Fn::GetAtt
<a name="aws-resource-devicefarm-testgridproject-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devicefarm-testgridproject-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `TestGrid` project. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide*.
