---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime EfsAccessPointConfiguration
<a name="aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration"></a>

Configuration for an Amazon EFS access point filesystem mounted into the AgentCore Runtime. EFS access points provide shared file storage accessible from your AgentCore Runtime sessions.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-accesspointarn)" : {{String}},
  "[MountPath](#cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-accesspointarn): {{String}}
  [MountPath](#cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-mountpath): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-efsaccesspointconfiguration-properties"></a>

`AccessPointArn`  <a name="cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-accesspointarn"></a>
The ARN of the EFS access point to mount into the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-bedrockagentcore-runtime-efsaccesspointconfiguration-mountpath"></a>
The mount path for the EFS access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9._-]+/?$`
*Minimum*: `6`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
