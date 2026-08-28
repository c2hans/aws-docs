---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-clientconfigurations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume ClientConfigurations
<a name="aws-properties-fsx-volume-clientconfigurations"></a>

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

## Syntax
<a name="aws-properties-fsx-volume-clientconfigurations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-clientconfigurations-syntax.json"></a>

```
{
  "[Clients](#cfn-fsx-volume-clientconfigurations-clients)" : {{String}},
  "[Options](#cfn-fsx-volume-clientconfigurations-options)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-fsx-volume-clientconfigurations-syntax.yaml"></a>

```
  [Clients](#cfn-fsx-volume-clientconfigurations-clients): {{String}}
  [Options](#cfn-fsx-volume-clientconfigurations-options): {{
    - String}}
```

## Properties
<a name="aws-properties-fsx-volume-clientconfigurations-properties"></a>

`Clients`  <a name="cfn-fsx-volume-clientconfigurations-clients"></a>
A value that specifies who can mount the file system. You can provide a wildcard character (`*`), an IP address (`0.0.0.0`), or a CIDR address (`192.0.2.0/24`). By default, Amazon FSx uses the wildcard character when specifying the client.
*Required*: Yes
*Type*: String
*Pattern*: `^[ -~]{1,128}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-fsx-volume-clientconfigurations-options"></a>
The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports). When choosing your options, consider the following:
+ `crossmnt` is used by default. If you don't specify `crossmnt` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory.
+ `sync` is used by default. If you instead specify `async`, the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
