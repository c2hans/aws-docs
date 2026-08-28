---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-agentspace-operatorapp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::AgentSpace OperatorApp
<a name="aws-properties-devopsagent-agentspace-operatorapp"></a>

Configuration for the DevOps Agent web app.

## Syntax
<a name="aws-properties-devopsagent-agentspace-operatorapp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-agentspace-operatorapp-syntax.json"></a>

```
{
  "[Iam](#cfn-devopsagent-agentspace-operatorapp-iam)" : {{IamAuthConfiguration}},
  "[Idc](#cfn-devopsagent-agentspace-operatorapp-idc)" : {{IdcAuthConfiguration}}
}
```

### YAML
<a name="aws-properties-devopsagent-agentspace-operatorapp-syntax.yaml"></a>

```
  [Iam](#cfn-devopsagent-agentspace-operatorapp-iam): {{
    IamAuthConfiguration}}
  [Idc](#cfn-devopsagent-agentspace-operatorapp-idc): {{
    IdcAuthConfiguration}}
```

## Properties
<a name="aws-properties-devopsagent-agentspace-operatorapp-properties"></a>

`Iam`  <a name="cfn-devopsagent-agentspace-operatorapp-iam"></a>
IAM-based authentication configuration for the DevOps Agent web app.
*Required*: No
*Type*: [IamAuthConfiguration](aws-properties-devopsagent-agentspace-iamauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Idc`  <a name="cfn-devopsagent-agentspace-operatorapp-idc"></a>
IAM Identity Center authentication configuration for the DevOps Agent web app.
*Required*: No
*Type*: [IdcAuthConfiguration](aws-properties-devopsagent-agentspace-idcauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
