---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-metadataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem MetadataConfiguration
<a name="aws-properties-fsx-filesystem-metadataconfiguration"></a>

The configuration that allows you to specify the performance of metadata operations for an FSx for Lustre file system.

## Syntax
<a name="aws-properties-fsx-filesystem-metadataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-metadataconfiguration-syntax.json"></a>

```
{
  "[Iops](#cfn-fsx-filesystem-metadataconfiguration-iops)" : {{Integer}},
  "[Mode](#cfn-fsx-filesystem-metadataconfiguration-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-metadataconfiguration-syntax.yaml"></a>

```
  [Iops](#cfn-fsx-filesystem-metadataconfiguration-iops): {{Integer}}
  [Mode](#cfn-fsx-filesystem-metadataconfiguration-mode): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-metadataconfiguration-properties"></a>

`Iops`  <a name="cfn-fsx-filesystem-metadataconfiguration-iops"></a>
The number of Metadata IOPS provisioned for the file system.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-fsx-filesystem-metadataconfiguration-mode"></a>
Specifies whether the file system is using the AUTOMATIC setting of metadata IOPS or if it is using a USER\_PROVISIONED value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
