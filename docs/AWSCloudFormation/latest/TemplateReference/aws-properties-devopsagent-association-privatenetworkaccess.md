---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-privatenetworkaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association PrivateNetworkAccess
<a name="aws-properties-devopsagent-association-privatenetworkaccess"></a>

Private network access to your application inside a VPC, through a private connection.

## Syntax
<a name="aws-properties-devopsagent-association-privatenetworkaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-privatenetworkaccess-syntax.json"></a>

```
{
  "[PrivateConnectionName](#cfn-devopsagent-association-privatenetworkaccess-privateconnectionname)" : {{String}},
  "[RuntimeRoleArn](#cfn-devopsagent-association-privatenetworkaccess-runtimerolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-privatenetworkaccess-syntax.yaml"></a>

```
  [PrivateConnectionName](#cfn-devopsagent-association-privatenetworkaccess-privateconnectionname): {{String}}
  [RuntimeRoleArn](#cfn-devopsagent-association-privatenetworkaccess-runtimerolearn): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-privatenetworkaccess-properties"></a>

`PrivateConnectionName`  <a name="cfn-devopsagent-association-privatenetworkaccess-privateconnectionname"></a>
The name of the private connection that supplies the VPC configuration for this release management environment. You create the private connection with the `AWS::DevOpsAgent::PrivateConnection` resource.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeRoleArn`  <a name="cfn-devopsagent-association-privatenetworkaccess-runtimerolearn"></a>
The ARN of the IAM role that AWS DevOps Agent assumes at runtime to connect to your VPC.
In the trust policy of the role, allow the `aidevops.amazonaws.com` service principal to call `sts:AssumeRole`, `sts:SetSourceIdentity`, and `sts:TagSession`.
Add the `aws:SourceAccount` and `aws:SourceArn` condition keys to the trust policy, so that only your account and your Agent Spaces can use the role.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
