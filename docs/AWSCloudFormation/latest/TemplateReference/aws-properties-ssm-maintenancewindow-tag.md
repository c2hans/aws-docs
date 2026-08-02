---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-maintenancewindow-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::MaintenanceWindow Tag
<a name="aws-properties-ssm-maintenancewindow-tag"></a>

Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In AWS Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

## Syntax
<a name="aws-properties-ssm-maintenancewindow-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-maintenancewindow-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ssm-maintenancewindow-tag-key)" : {{String}},
  "[Value](#cfn-ssm-maintenancewindow-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-maintenancewindow-tag-syntax.yaml"></a>

```
  [Key](#cfn-ssm-maintenancewindow-tag-key): {{String}}
  [Value](#cfn-ssm-maintenancewindow-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ssm-maintenancewindow-tag-properties"></a>

`Key`  <a name="cfn-ssm-maintenancewindow-tag-key"></a>
The name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ssm-maintenancewindow-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
