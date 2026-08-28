---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-fsrmconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem FsrmConfiguration
<a name="aws-properties-fsx-filesystem-fsrmconfiguration"></a>

<a name="aws-properties-fsx-filesystem-fsrmconfiguration-description"></a>The `FsrmConfiguration` property type specifies Property description not available. for an [AWS::FSx::FileSystem](aws-resource-fsx-filesystem.md).

## Syntax
<a name="aws-properties-fsx-filesystem-fsrmconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-fsrmconfiguration-syntax.json"></a>

```
{
  "[EventLogDestination](#cfn-fsx-filesystem-fsrmconfiguration-eventlogdestination)" : {{String}},
  "[FsrmServiceEnabled](#cfn-fsx-filesystem-fsrmconfiguration-fsrmserviceenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-fsrmconfiguration-syntax.yaml"></a>

```
  [EventLogDestination](#cfn-fsx-filesystem-fsrmconfiguration-eventlogdestination): {{String}}
  [FsrmServiceEnabled](#cfn-fsx-filesystem-fsrmconfiguration-fsrmserviceenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-fsx-filesystem-fsrmconfiguration-properties"></a>

`EventLogDestination`  <a name="cfn-fsx-filesystem-fsrmconfiguration-eventlogdestination"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FsrmServiceEnabled`  <a name="cfn-fsx-filesystem-fsrmconfiguration-fsrmserviceenabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
