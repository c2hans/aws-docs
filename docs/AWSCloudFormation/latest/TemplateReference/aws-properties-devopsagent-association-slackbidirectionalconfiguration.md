---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-slackbidirectionalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SlackBidirectionalConfiguration
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration"></a>

<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-description"></a>The `SlackBidirectionalConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-devopsagent-association-slackbidirectionalconfiguration-enabled)" : {{Boolean}},
  "[RoleArn](#cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-devopsagent-association-slackbidirectionalconfiguration-enabled): {{Boolean}}
  [RoleArn](#cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-properties"></a>

`Enabled`  <a name="cfn-devopsagent-association-slackbidirectionalconfiguration-enabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
