---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-datarepositoryassociation-autoexportpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::DataRepositoryAssociation AutoExportPolicy
<a name="aws-properties-fsx-datarepositoryassociation-autoexportpolicy"></a>

Describes a data repository association's automatic export policy. The `AutoExportPolicy` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.

The `AutoExportPolicy` is only supported on Amazon FSx for Lustre file systems with a data repository association.

## Syntax
<a name="aws-properties-fsx-datarepositoryassociation-autoexportpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-datarepositoryassociation-autoexportpolicy-syntax.json"></a>

```
{
  "[Events](#cfn-fsx-datarepositoryassociation-autoexportpolicy-events)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-fsx-datarepositoryassociation-autoexportpolicy-syntax.yaml"></a>

```
  [Events](#cfn-fsx-datarepositoryassociation-autoexportpolicy-events): {{
    - String}}
```

## Properties
<a name="aws-properties-fsx-datarepositoryassociation-autoexportpolicy-properties"></a>

`Events`  <a name="cfn-fsx-datarepositoryassociation-autoexportpolicy-events"></a>
The `AutoExportPolicy` can have the following event values:
+ `NEW` - New files and directories are automatically exported to the data repository as they are added to the file system.
+ `CHANGED` - Changes to files and directories on the file system are automatically exported to the data repository.
+ `DELETED` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.
You can define any combination of event types for your `AutoExportPolicy`.
*Required*: Yes
*Type*: Array of String
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
