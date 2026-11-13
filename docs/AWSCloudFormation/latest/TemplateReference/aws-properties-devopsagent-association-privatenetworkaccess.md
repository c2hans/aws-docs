---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-privatenetworkaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association PrivateNetworkAccess
<a name="aws-properties-devopsagent-association-privatenetworkaccess"></a>

<a name="aws-properties-devopsagent-association-privatenetworkaccess-description"></a>The `PrivateNetworkAccess` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

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
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeRoleArn`  <a name="cfn-devopsagent-association-privatenetworkaccess-runtimerolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
