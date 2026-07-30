---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness S3FilesAccessPointConfiguration
<a name="aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration"></a>

Configuration for an Amazon S3 Files access point filesystem mounted into the AgentCore Runtime. S3 Files access points provide shared file storage accessible from your AgentCore Runtime sessions.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-accesspointarn)" : {{String}},
  "[MountPath](#cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-accesspointarn): {{String}}
  [MountPath](#cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-mountpath): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-s3filesaccesspointconfiguration-properties"></a>

`AccessPointArn`  <a name="cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-accesspointarn"></a>
The ARN of the S3 Files access point to mount into the AgentCore Runtime.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-bedrockagentcore-harness-s3filesaccesspointconfiguration-mountpath"></a>
The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9._-]+/?$`
*Minimum*: `6`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
