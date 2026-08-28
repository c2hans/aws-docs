---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-filesystemconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime FilesystemConfiguration
<a name="aws-properties-bedrockagentcore-runtime-filesystemconfiguration"></a>

Configuration for a filesystem that can be mounted into the AgentCore Runtime.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-filesystemconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-filesystemconfiguration-syntax.json"></a>

```
{
  "[CapacityProviderVolume](#cfn-bedrockagentcore-runtime-filesystemconfiguration-capacityprovidervolume)" : {{CapacityProviderVolumeConfiguration}},
  "[EfsAccessPoint](#cfn-bedrockagentcore-runtime-filesystemconfiguration-efsaccesspoint)" : {{EfsAccessPointConfiguration}},
  "[S3FilesAccessPoint](#cfn-bedrockagentcore-runtime-filesystemconfiguration-s3filesaccesspoint)" : {{S3FilesAccessPointConfiguration}},
  "[SessionStorage](#cfn-bedrockagentcore-runtime-filesystemconfiguration-sessionstorage)" : {{SessionStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-filesystemconfiguration-syntax.yaml"></a>

```
  [CapacityProviderVolume](#cfn-bedrockagentcore-runtime-filesystemconfiguration-capacityprovidervolume): {{
    CapacityProviderVolumeConfiguration}}
  [EfsAccessPoint](#cfn-bedrockagentcore-runtime-filesystemconfiguration-efsaccesspoint): {{
    EfsAccessPointConfiguration}}
  [S3FilesAccessPoint](#cfn-bedrockagentcore-runtime-filesystemconfiguration-s3filesaccesspoint): {{
    S3FilesAccessPointConfiguration}}
  [SessionStorage](#cfn-bedrockagentcore-runtime-filesystemconfiguration-sessionstorage): {{
    SessionStorageConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-filesystemconfiguration-properties"></a>

`CapacityProviderVolume`  <a name="cfn-bedrockagentcore-runtime-filesystemconfiguration-capacityprovidervolume"></a>
Property description not available.
*Required*: No
*Type*: [CapacityProviderVolumeConfiguration](aws-properties-bedrockagentcore-runtime-capacityprovidervolumeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EfsAccessPoint`  <a name="cfn-bedrockagentcore-runtime-filesystemconfiguration-efsaccesspoint"></a>
Configuration for an Amazon EFS access point to mount into the AgentCore Runtime.
*Required*: No
*Type*: [EfsAccessPointConfiguration](aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FilesAccessPoint`  <a name="cfn-bedrockagentcore-runtime-filesystemconfiguration-s3filesaccesspoint"></a>
Configuration for an Amazon S3 Files access point to mount into the AgentCore Runtime.
*Required*: No
*Type*: [S3FilesAccessPointConfiguration](aws-properties-bedrockagentcore-runtime-s3filesaccesspointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionStorage`  <a name="cfn-bedrockagentcore-runtime-filesystemconfiguration-sessionstorage"></a>
Configuration for session storage. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.
*Required*: No
*Type*: [SessionStorageConfiguration](aws-properties-bedrockagentcore-runtime-sessionstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
