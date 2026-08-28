---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-nfsexports.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem NfsExports
<a name="aws-properties-fsx-filesystem-nfsexports"></a>

The configuration object for mounting a file system.

## Syntax
<a name="aws-properties-fsx-filesystem-nfsexports-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-nfsexports-syntax.json"></a>

```
{
  "[ClientConfigurations](#cfn-fsx-filesystem-nfsexports-clientconfigurations)" : {{[ ClientConfigurations, ... ]}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-nfsexports-syntax.yaml"></a>

```
  [ClientConfigurations](#cfn-fsx-filesystem-nfsexports-clientconfigurations): {{
    - ClientConfigurations}}
```

## Properties
<a name="aws-properties-fsx-filesystem-nfsexports-properties"></a>

`ClientConfigurations`  <a name="cfn-fsx-filesystem-nfsexports-clientconfigurations"></a>
A list of configuration objects that contain the client and options for mounting the OpenZFS file system.
*Required*: No
*Type*: [Array](aws-properties-fsx-filesystem-clientconfigurations.md) of [ClientConfigurations](aws-properties-fsx-filesystem-clientconfigurations.md)
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
