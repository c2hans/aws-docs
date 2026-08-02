---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-customlaunchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup CustomLaunchTemplate
<a name="aws-properties-pcs-computenodegroup-customlaunchtemplate"></a>

An Amazon EC2 launch template AWS PCS uses to launch compute nodes.

## Syntax
<a name="aws-properties-pcs-computenodegroup-customlaunchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-customlaunchtemplate-syntax.json"></a>

```
{
  "[TemplateId](#cfn-pcs-computenodegroup-customlaunchtemplate-templateid)" : {{String}},
  "[Version](#cfn-pcs-computenodegroup-customlaunchtemplate-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-customlaunchtemplate-syntax.yaml"></a>

```
  [TemplateId](#cfn-pcs-computenodegroup-customlaunchtemplate-templateid): {{String}}
  [Version](#cfn-pcs-computenodegroup-customlaunchtemplate-version): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-customlaunchtemplate-properties"></a>

`TemplateId`  <a name="cfn-pcs-computenodegroup-customlaunchtemplate-templateid"></a>
The ID of the EC2 launch template to use to provision instances.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-pcs-computenodegroup-customlaunchtemplate-version"></a>
The version of the EC2 launch template to use to provision instances.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
