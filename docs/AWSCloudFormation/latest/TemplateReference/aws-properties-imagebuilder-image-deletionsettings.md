---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-deletionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image DeletionSettings
<a name="aws-properties-imagebuilder-image-deletionsettings"></a>

Contains deletion settings of underlying resources of an image when it is replaced or deleted, including its Amazon Machine Images (AMIs), snapshots, or containers.

**Note**
If you specify the `Retain` option in the [DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html) or [UpdateReplacePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatereplacepolicy.html), Image Builder does not delete the underlying resources.

## Syntax
<a name="aws-properties-imagebuilder-image-deletionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-deletionsettings-syntax.json"></a>

```
{
  "[ExecutionRole](#cfn-imagebuilder-image-deletionsettings-executionrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-deletionsettings-syntax.yaml"></a>

```
  [ExecutionRole](#cfn-imagebuilder-image-deletionsettings-executionrole): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-deletionsettings-properties"></a>

`ExecutionRole`  <a name="cfn-imagebuilder-image-deletionsettings-executionrole"></a>
The name or Amazon Resource Name (ARN) of the IAM role that grants Image Builder permission to delete the image and its underlying resources. This property is required when you specify `DeletionSettings`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
