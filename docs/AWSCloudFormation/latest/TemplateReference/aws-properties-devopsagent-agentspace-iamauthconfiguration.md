---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-agentspace-iamauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::AgentSpace IamAuthConfiguration
<a name="aws-properties-devopsagent-agentspace-iamauthconfiguration"></a>

IAM-based authentication configuration for the DevOps Agent web app.

## Syntax
<a name="aws-properties-devopsagent-agentspace-iamauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-agentspace-iamauthconfiguration-syntax.json"></a>

```
{
  "[CreatedAt](#cfn-devopsagent-agentspace-iamauthconfiguration-createdat)" : {{String}},
  "[OperatorAppRoleArn](#cfn-devopsagent-agentspace-iamauthconfiguration-operatorapprolearn)" : {{String}},
  "[UpdatedAt](#cfn-devopsagent-agentspace-iamauthconfiguration-updatedat)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-agentspace-iamauthconfiguration-syntax.yaml"></a>

```
  [CreatedAt](#cfn-devopsagent-agentspace-iamauthconfiguration-createdat): {{String}}
  [OperatorAppRoleArn](#cfn-devopsagent-agentspace-iamauthconfiguration-operatorapprolearn): {{String}}
  [UpdatedAt](#cfn-devopsagent-agentspace-iamauthconfiguration-updatedat): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-agentspace-iamauthconfiguration-properties"></a>

`CreatedAt`  <a name="cfn-devopsagent-agentspace-iamauthconfiguration-createdat"></a>
The timestamp when the IAM authentication configuration was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatorAppRoleArn`  <a name="cfn-devopsagent-agentspace-iamauthconfiguration-operatorapprolearn"></a>
The ARN of the IAM role that grants access to the DevOps Agent web app.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedAt`  <a name="cfn-devopsagent-agentspace-iamauthconfiguration-updatedat"></a>
The timestamp when the IAM authentication configuration was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
