---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-nfsexports.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume NfsExports
<a name="aws-properties-fsx-volume-nfsexports"></a>

The configuration object for mounting a Network File System (NFS) file system.

## Syntax
<a name="aws-properties-fsx-volume-nfsexports-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-nfsexports-syntax.json"></a>

```
{
  "[ClientConfigurations](#cfn-fsx-volume-nfsexports-clientconfigurations)" : {{[ ClientConfigurations, ... ]}}
}
```

### YAML
<a name="aws-properties-fsx-volume-nfsexports-syntax.yaml"></a>

```
  [ClientConfigurations](#cfn-fsx-volume-nfsexports-clientconfigurations): {{
    - ClientConfigurations}}
```

## Properties
<a name="aws-properties-fsx-volume-nfsexports-properties"></a>

`ClientConfigurations`  <a name="cfn-fsx-volume-nfsexports-clientconfigurations"></a>
A list of configuration objects that contain the client and options for mounting the OpenZFS file system.
*Required*: Yes
*Type*: [Array](aws-properties-fsx-volume-clientconfigurations.md) of [ClientConfigurations](aws-properties-fsx-volume-clientconfigurations.md)
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
