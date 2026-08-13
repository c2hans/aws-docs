---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-agent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent
<a name="aws-resource-bedrock-agent"></a>

Specifies an agent as a resource in a top-level template. Minimally, you must specify the following properties:
+ AgentName – Specify a name for the agent.
+ AgentResourceRoleArn – Specify the Amazon Resource Name (ARN) of the service role with permissions to invoke API operations on the agent. For more information, see [Create a service role for Agents for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-permissions.html).
+ FoundationModel – Specify the model ID of a foundation model to use when invoking the agent. For more information, see [Supported regions and models for Agents for Amazon Bedrock](https://docs.aws.amazon.com//bedrock/latest/userguide/agents-supported.html).

For more information about using agents in Amazon Bedrock, see [Agents for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrock-agent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-agent-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Agent",
  "Properties" : {
      "[ActionGroups](#cfn-bedrock-agent-actiongroups)" : {{[ AgentActionGroup, ... ]}},
      "[AgentCollaboration](#cfn-bedrock-agent-agentcollaboration)" : {{String}},
      "[AgentCollaborators](#cfn-bedrock-agent-agentcollaborators)" : {{[ AgentCollaborator, ... ]}},
      "[AgentName](#cfn-bedrock-agent-agentname)" : {{String}},
      "[AgentResourceRoleArn](#cfn-bedrock-agent-agentresourcerolearn)" : {{String}},
      "[AutoPrepare](#cfn-bedrock-agent-autoprepare)" : {{Boolean}},
      "[CustomerEncryptionKeyArn](#cfn-bedrock-agent-customerencryptionkeyarn)" : {{String}},
      "[CustomOrchestration](#cfn-bedrock-agent-customorchestration)" : {{CustomOrchestration}},
      "[Description](#cfn-bedrock-agent-description)" : {{String}},
      "[FoundationModel](#cfn-bedrock-agent-foundationmodel)" : {{String}},
      "[GuardrailConfiguration](#cfn-bedrock-agent-guardrailconfiguration)" : {{GuardrailConfiguration}},
      "[IdleSessionTTLInSeconds](#cfn-bedrock-agent-idlesessionttlinseconds)" : {{Number}},
      "[Instruction](#cfn-bedrock-agent-instruction)" : {{String}},
      "[KnowledgeBases](#cfn-bedrock-agent-knowledgebases)" : {{[ AgentKnowledgeBase, ... ]}},
      "[MemoryConfiguration](#cfn-bedrock-agent-memoryconfiguration)" : {{MemoryConfiguration}},
      "[OrchestrationType](#cfn-bedrock-agent-orchestrationtype)" : {{String}},
      "[PromptOverrideConfiguration](#cfn-bedrock-agent-promptoverrideconfiguration)" : {{PromptOverrideConfiguration}},
      "[SkipResourceInUseCheckOnDelete](#cfn-bedrock-agent-skipresourceinusecheckondelete)" : {{Boolean}},
      "[Tags](#cfn-bedrock-agent-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TestAliasTags](#cfn-bedrock-agent-testaliastags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-agent-syntax.yaml"></a>

```
Type: AWS::Bedrock::Agent
Properties:
  [ActionGroups](#cfn-bedrock-agent-actiongroups): {{
    - AgentActionGroup}}
  [AgentCollaboration](#cfn-bedrock-agent-agentcollaboration): {{String}}
  [AgentCollaborators](#cfn-bedrock-agent-agentcollaborators): {{
    - AgentCollaborator}}
  [AgentName](#cfn-bedrock-agent-agentname): {{String}}
  [AgentResourceRoleArn](#cfn-bedrock-agent-agentresourcerolearn): {{String}}
  [AutoPrepare](#cfn-bedrock-agent-autoprepare): {{Boolean}}
  [CustomerEncryptionKeyArn](#cfn-bedrock-agent-customerencryptionkeyarn): {{String}}
  [CustomOrchestration](#cfn-bedrock-agent-customorchestration): {{
    CustomOrchestration}}
  [Description](#cfn-bedrock-agent-description): {{String}}
  [FoundationModel](#cfn-bedrock-agent-foundationmodel): {{String}}
  [GuardrailConfiguration](#cfn-bedrock-agent-guardrailconfiguration): {{
    GuardrailConfiguration}}
  [IdleSessionTTLInSeconds](#cfn-bedrock-agent-idlesessionttlinseconds): {{Number}}
  [Instruction](#cfn-bedrock-agent-instruction): {{String}}
  [KnowledgeBases](#cfn-bedrock-agent-knowledgebases): {{
    - AgentKnowledgeBase}}
  [MemoryConfiguration](#cfn-bedrock-agent-memoryconfiguration): {{
    MemoryConfiguration}}
  [OrchestrationType](#cfn-bedrock-agent-orchestrationtype): {{String}}
  [PromptOverrideConfiguration](#cfn-bedrock-agent-promptoverrideconfiguration): {{
    PromptOverrideConfiguration}}
  [SkipResourceInUseCheckOnDelete](#cfn-bedrock-agent-skipresourceinusecheckondelete): {{Boolean}}
  [Tags](#cfn-bedrock-agent-tags): {{
    {{Key}}: {{Value}}}}
  [TestAliasTags](#cfn-bedrock-agent-testaliastags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-agent-properties"></a>

`ActionGroups`  <a name="cfn-bedrock-agent-actiongroups"></a>
The action groups that belong to an agent.
*Required*: No
*Type*: Array of [AgentActionGroup](aws-properties-bedrock-agent-agentactiongroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentCollaboration`  <a name="cfn-bedrock-agent-agentcollaboration"></a>
The agent's collaboration settings.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | SUPERVISOR | SUPERVISOR_ROUTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentCollaborators`  <a name="cfn-bedrock-agent-agentcollaborators"></a>
Property description not available.
*Required*: No
*Type*: Array of [AgentCollaborator](aws-properties-bedrock-agent-agentcollaborator.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentName`  <a name="cfn-bedrock-agent-agentname"></a>
The name of the agent.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentResourceRoleArn`  <a name="cfn-bedrock-agent-agentresourcerolearn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoPrepare`  <a name="cfn-bedrock-agent-autoprepare"></a>
Specifies whether to automatically update the `DRAFT` version of the agent after making changes to the agent. The `DRAFT` version can be continually iterated upon during internal development. By default, this value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerEncryptionKeyArn`  <a name="cfn-bedrock-agent-customerencryptionkeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that encrypts the agent.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomOrchestration`  <a name="cfn-bedrock-agent-customorchestration"></a>
 Contains custom orchestration configurations for the agent.
*Required*: No
*Type*: [CustomOrchestration](aws-properties-bedrock-agent-customorchestration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-agent-description"></a>
The description of the agent.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FoundationModel`  <a name="cfn-bedrock-agent-foundationmodel"></a>
The foundation model used for orchestration by the agent.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardrailConfiguration`  <a name="cfn-bedrock-agent-guardrailconfiguration"></a>
Details about the guardrail associated with the agent.
*Required*: No
*Type*: [GuardrailConfiguration](aws-properties-bedrock-agent-guardrailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleSessionTTLInSeconds`  <a name="cfn-bedrock-agent-idlesessionttlinseconds"></a>
The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.
*Required*: No
*Type*: Number
*Minimum*: `60`
*Maximum*: `5400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-bedrock-agent-instruction"></a>
Instructions that tell the agent what it should do and how it should interact with users.
*Required*: No
*Type*: String
*Minimum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBases`  <a name="cfn-bedrock-agent-knowledgebases"></a>
The knowledge bases associated with the agent.
*Required*: No
*Type*: Array of [AgentKnowledgeBase](aws-properties-bedrock-agent-agentknowledgebase.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryConfiguration`  <a name="cfn-bedrock-agent-memoryconfiguration"></a>
Contains memory configuration for the agent.
*Required*: No
*Type*: [MemoryConfiguration](aws-properties-bedrock-agent-memoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrchestrationType`  <a name="cfn-bedrock-agent-orchestrationtype"></a>
 Specifies the orchestration strategy for the agent.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | CUSTOM_ORCHESTRATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptOverrideConfiguration`  <a name="cfn-bedrock-agent-promptoverrideconfiguration"></a>
Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).
*Required*: No
*Type*: [PromptOverrideConfiguration](aws-properties-bedrock-agent-promptoverrideconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkipResourceInUseCheckOnDelete`  <a name="cfn-bedrock-agent-skipresourceinusecheckondelete"></a>
Specifies whether to delete the resource even if it's in use. By default, this value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-agent-tags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestAliasTags`  <a name="cfn-bedrock-agent-testaliastags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-agent-return-values"></a>

### Ref
<a name="aws-resource-bedrock-agent-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent base ID.

For example, `{ "Ref": "myAgent" }` could return the value `"AGENT12345"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-agent-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-agent-return-values-fn--getatt-fn--getatt"></a>

`AgentArn`  <a name="AgentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the agent.

`AgentId`  <a name="AgentId-fn::getatt"></a>
The unique identifier of the agent.

`AgentStatus`  <a name="AgentStatus-fn::getatt"></a>
The status of the agent and whether it is ready for use. The following statuses are possible:
+ CREATING – The agent is being created.
+ PREPARING – The agent is being prepared.
+ PREPARED – The agent is prepared and ready to be invoked.
+ NOT\_PREPARED – The agent has been created but not yet prepared.
+ FAILED – The agent API operation failed.
+ UPDATING – The agent is being updated.
+ DELETING – The agent is being deleted.

`AgentVersion`  <a name="AgentVersion-fn::getatt"></a>
The version of the agent.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the agent was created.

`FailureReasons`  <a name="FailureReasons-fn::getatt"></a>
Contains reasons that the agent-related API that you invoked failed.

`PreparedAt`  <a name="PreparedAt-fn::getatt"></a>
The time at which the agent was last prepared.

`RecommendedActions`  <a name="RecommendedActions-fn::getatt"></a>
Contains recommended actions to take for the agent-related API that you invoked to succeed.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the agent was last updated.

## Examples
<a name="aws-resource-bedrock-agent--examples"></a>

### Create an agent
<a name="aws-resource-bedrock-agent--examples--Create_an_agent"></a>

The following example creates an agent that orchestrates on the Anthropic Claude v2 foundation model to help customers with IT problems. It contains one action group and one knowledge base.

#### YAML
<a name="aws-resource-bedrock-agent--examples--Create_an_agent--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: "CFN stack for creating an agent"
Resources:
   ExampleAgentResource:
      Type: AWS::Bedrock::Agent
      Properties:
        AgentName: "Example Agent"
        AgentResourceRoleArn: "arn:aws:iam::123456789012:role/AmazonBedrockExecutionRoleForAgents_user"
        FoundationModel: "anthropic.claude-v2"
        Instruction: "You are an IT agent who solves customer's problems"
        Description: "Description is here"
        IdleSessionTTLInSeconds: 900
        CustomerEncryptionKeyArn: "arn:aws:kms:us-west-2:123456789012:key/1234abcd-ab12-34cd-56ef-abcdefg123456"
        ActionGroups:
          - ActionGroupName: "IT Action"
            Description: "Testing latest IT Management action"
            ActionGroupExecutor:
              Lambda: "arn:aws:lambda:us-west-2:123456789012:function:ItAgentLambda"
            ApiSchema:
              S3:
                S3BucketName: "apischema-s3"
                S3ObjectKey: "ApiSchema.json"
        KnowledgeBases:
          - KnowledgeBaseId: "1234567890"
            Description: "IT Knowledge Base"
            KnowledgeBaseState: ENABLED
```

#### JSON
<a name="aws-resource-bedrock-agent--examples--Create_an_agent--json"></a>

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "CFN stack for creating an agent",
   "Resources": {
      "ExampleAgentResource": {
         "Type": "AWS::Bedrock::Agent",
         "Properties": {
            "AgentName": "Example Agent",
            "AgentResourceRoleArn": "arn:aws:iam::123456789012:role/AmazonBedrockExecutionRoleForAgents_user",
            "FoundationModel": "anthropic.claude-v2",
            "Instruction": "You are an IT agent who solves customer's problems",
            "Description": "Description is here",
            "IdleSessionTTLInSeconds": 900,
            "CustomerEncryptionKeyArn": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-ab12-34cd-56ef-abcdefg123456",
            "ActionGroups": [
               {
                  "ActionGroupName": "IT Action",
                  "Description": "Testing latest IT Management action",
                  "ActionGroupExecutor": {
                     "Lambda": "arn:aws:lambda:us-west-2:123456789012:function:ItAgentLambda"
                  },
                  "ApiSchema": {
                     "S3": {
                        "S3BucketName": "apischema-s3",
                        "S3ObjectKey": "ApiSchema.json"
                     }
                  }
               }
            ],
            "KnowledgeBases": [
               {
                  "KnowledgeBaseId": "1234567890",
                  "Description": "IT Knowledge Base",
                  "KnowledgeBaseState": "ENABLED"
               }
            ]
         }
      }
   }
}
```
