---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-agentspace-idcauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::AgentSpace IdcAuthConfiguration
<a name="aws-properties-devopsagent-agentspace-idcauthconfiguration"></a>

IAM Identity Center authentication configuration for the DevOps Agent web app.

## Syntax
<a name="aws-properties-devopsagent-agentspace-idcauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-agentspace-idcauthconfiguration-syntax.json"></a>

```
{
  "[CreatedAt](#cfn-devopsagent-agentspace-idcauthconfiguration-createdat)" : {{String}},
  "[IdcApplicationArn](#cfn-devopsagent-agentspace-idcauthconfiguration-idcapplicationarn)" : {{String}},
  "[IdcInstanceArn](#cfn-devopsagent-agentspace-idcauthconfiguration-idcinstancearn)" : {{String}},
  "[OperatorAppRoleArn](#cfn-devopsagent-agentspace-idcauthconfiguration-operatorapprolearn)" : {{String}},
  "[UpdatedAt](#cfn-devopsagent-agentspace-idcauthconfiguration-updatedat)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-agentspace-idcauthconfiguration-syntax.yaml"></a>

```
  [CreatedAt](#cfn-devopsagent-agentspace-idcauthconfiguration-createdat): {{String}}
  [IdcApplicationArn](#cfn-devopsagent-agentspace-idcauthconfiguration-idcapplicationarn): {{String}}
  [IdcInstanceArn](#cfn-devopsagent-agentspace-idcauthconfiguration-idcinstancearn): {{String}}
  [OperatorAppRoleArn](#cfn-devopsagent-agentspace-idcauthconfiguration-operatorapprolearn): {{String}}
  [UpdatedAt](#cfn-devopsagent-agentspace-idcauthconfiguration-updatedat): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-agentspace-idcauthconfiguration-properties"></a>

`CreatedAt`  <a name="cfn-devopsagent-agentspace-idcauthconfiguration-createdat"></a>
The timestamp when the IAM Identity Center authentication configuration was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcApplicationArn`  <a name="cfn-devopsagent-agentspace-idcauthconfiguration-idcapplicationarn"></a>
The ARN of the IAM Identity Center application created for the DevOps Agent web app.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcInstanceArn`  <a name="cfn-devopsagent-agentspace-idcauthconfiguration-idcinstancearn"></a>
The ARN of the IAM Identity Center instance used for authentication.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatorAppRoleArn`  <a name="cfn-devopsagent-agentspace-idcauthconfiguration-operatorapprolearn"></a>
The ARN of the IAM role that grants access to the DevOps Agent web app.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedAt`  <a name="cfn-devopsagent-agentspace-idcauthconfiguration-updatedat"></a>
The timestamp when the IAM Identity Center authentication configuration was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
