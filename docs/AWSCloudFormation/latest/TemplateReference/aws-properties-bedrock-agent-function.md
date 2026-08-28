---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-function.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent Function
<a name="aws-properties-bedrock-agent-function"></a>

Defines parameters that the agent needs to invoke from the user to complete the function. Corresponds to an action in an action group.

This data type is used in the following API operations:
+  [CreateAgentActionGroup request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentActionGroup.html#API_agent_CreateAgentActionGroup_RequestSyntax)
+  [CreateAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentActionGroup.html#API_agent_CreateAgentActionGroup_ResponseSyntax)
+  [UpdateAgentActionGroup request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentActionGroup.html#API_agent_UpdateAgentActionGroup_RequestSyntax)
+  [UpdateAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentActionGroup.html#API_agent_UpdateAgentActionGroup_ResponseSyntax)
+  [GetAgentActionGroup response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html#API_agent_GetAgentActionGroup_ResponseSyntax)

## Syntax
<a name="aws-properties-bedrock-agent-function-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-function-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-agent-function-description)" : {{String}},
  "[Name](#cfn-bedrock-agent-function-name)" : {{String}},
  "[Parameters](#cfn-bedrock-agent-function-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RequireConfirmation](#cfn-bedrock-agent-function-requireconfirmation)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-function-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-agent-function-description): {{String}}
  [Name](#cfn-bedrock-agent-function-name): {{String}}
  [Parameters](#cfn-bedrock-agent-function-parameters): {{
    {{Key}}: {{Value}}}}
  [RequireConfirmation](#cfn-bedrock-agent-function-requireconfirmation): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-function-properties"></a>

`Description`  <a name="cfn-bedrock-agent-function-description"></a>
A description of the function and its purpose.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-agent-function-name"></a>
A name for the function.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-bedrock-agent-function-parameters"></a>
The parameters that the agent elicits from the user to fulfill the function.
*Required*: No
*Type*: Object of [ParameterDetail](aws-properties-bedrock-agent-parameterdetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireConfirmation`  <a name="cfn-bedrock-agent-function-requireconfirmation"></a>
Contains information if user confirmation is required to invoke the function.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
