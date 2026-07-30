---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-framework-controlscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::Framework ControlScope
<a name="aws-properties-backup-framework-controlscope"></a>

A framework consists of one or more controls. Each control has its own control scope. The control scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. If no scope is specified, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

**Note**
To set a control scope that includes all of a particular resource, leave the `ControlScope` empty or do not pass it when calling `CreateFramework`.

## Syntax
<a name="aws-properties-backup-framework-controlscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-framework-controlscope-syntax.json"></a>

```
{
  "[ComplianceResourceIds](#cfn-backup-framework-controlscope-complianceresourceids)" : {{[ String, ... ]}},
  "[ComplianceResourceTypes](#cfn-backup-framework-controlscope-complianceresourcetypes)" : {{[ String, ... ]}},
  "[Tags](#cfn-backup-framework-controlscope-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-backup-framework-controlscope-syntax.yaml"></a>

```
  [ComplianceResourceIds](#cfn-backup-framework-controlscope-complianceresourceids): {{
    - String}}
  [ComplianceResourceTypes](#cfn-backup-framework-controlscope-complianceresourcetypes): {{
    - String}}
  [Tags](#cfn-backup-framework-controlscope-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-backup-framework-controlscope-properties"></a>

`ComplianceResourceIds`  <a name="cfn-backup-framework-controlscope-complianceresourceids"></a>
The ID of the only AWS resource that you want your control scope to contain.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComplianceResourceTypes`  <a name="cfn-backup-framework-controlscope-complianceresourcetypes"></a>
Describes whether the control scope includes one or more types of resources, such as `EFS` or `RDS`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-backup-framework-controlscope-tags"></a>
The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).
The structure to assign a tag is: `[{"Key":"string","Value":"string"}]`.
*Required*: No
*Type*: Array of [Tag](aws-properties-backup-framework-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
