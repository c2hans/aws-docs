---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentactiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent AgentActionGroup
<a name="aws-properties-bedrock-agent-agentactiongroup"></a>

 Contains details of the inline agent's action group.

## Syntax
<a name="aws-properties-bedrock-agent-agentactiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-agentactiongroup-syntax.json"></a>

```
{
  "[ActionGroupExecutor](#cfn-bedrock-agent-agentactiongroup-actiongroupexecutor)" : {{ActionGroupExecutor}},
  "[ActionGroupName](#cfn-bedrock-agent-agentactiongroup-actiongroupname)" : {{String}},
  "[ActionGroupState](#cfn-bedrock-agent-agentactiongroup-actiongroupstate)" : {{String}},
  "[ApiSchema](#cfn-bedrock-agent-agentactiongroup-apischema)" : {{APISchema}},
  "[Description](#cfn-bedrock-agent-agentactiongroup-description)" : {{String}},
  "[FunctionSchema](#cfn-bedrock-agent-agentactiongroup-functionschema)" : {{FunctionSchema}},
  "[ParentActionGroupSignature](#cfn-bedrock-agent-agentactiongroup-parentactiongroupsignature)" : {{String}},
  "[SkipResourceInUseCheckOnDelete](#cfn-bedrock-agent-agentactiongroup-skipresourceinusecheckondelete)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-agentactiongroup-syntax.yaml"></a>

```
  [ActionGroupExecutor](#cfn-bedrock-agent-agentactiongroup-actiongroupexecutor): {{
    ActionGroupExecutor}}
  [ActionGroupName](#cfn-bedrock-agent-agentactiongroup-actiongroupname): {{String}}
  [ActionGroupState](#cfn-bedrock-agent-agentactiongroup-actiongroupstate): {{String}}
  [ApiSchema](#cfn-bedrock-agent-agentactiongroup-apischema): {{
    APISchema}}
  [Description](#cfn-bedrock-agent-agentactiongroup-description): {{String}}
  [FunctionSchema](#cfn-bedrock-agent-agentactiongroup-functionschema): {{
    FunctionSchema}}
  [ParentActionGroupSignature](#cfn-bedrock-agent-agentactiongroup-parentactiongroupsignature): {{String}}
  [SkipResourceInUseCheckOnDelete](#cfn-bedrock-agent-agentactiongroup-skipresourceinusecheckondelete): {{Boolean}}
```

## Properties
<a name="aws-properties-bedrock-agent-agentactiongroup-properties"></a>

`ActionGroupExecutor`  <a name="cfn-bedrock-agent-agentactiongroup-actiongroupexecutor"></a>
 The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.
*Required*: No
*Type*: [ActionGroupExecutor](aws-properties-bedrock-agent-actiongroupexecutor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionGroupName`  <a name="cfn-bedrock-agent-agentactiongroup-actiongroupname"></a>
 The name of the action group.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionGroupState`  <a name="cfn-bedrock-agent-agentactiongroup-actiongroupstate"></a>
Specifies whether the action group is available for the agent to invoke or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiSchema`  <a name="cfn-bedrock-agent-agentactiongroup-apischema"></a>
 Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html).
*Required*: No
*Type*: [APISchema](aws-properties-bedrock-agent-apischema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-agent-agentactiongroup-description"></a>
 A description of the action group.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionSchema`  <a name="cfn-bedrock-agent-agentactiongroup-functionschema"></a>
 Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.
*Required*: No
*Type*: [FunctionSchema](aws-properties-bedrock-agent-functionschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentActionGroupSignature`  <a name="cfn-bedrock-agent-agentactiongroup-parentactiongroupsignature"></a>
If this field is set as `AMAZON.UserInput`, the agent can request the user for additional information when trying to complete a task. The `description`, `apiSchema`, and `actionGroupExecutor` fields must be blank for this action group.
During orchestration, if the agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an [Observation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html) reprompting the user for more information.
*Required*: No
*Type*: String
*Allowed values*: `AMAZON.UserInput | AMAZON.CodeInterpreter`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkipResourceInUseCheckOnDelete`  <a name="cfn-bedrock-agent-agentactiongroup-skipresourceinusecheckondelete"></a>
Specifies whether to delete the resource even if it's in use. By default, this value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
