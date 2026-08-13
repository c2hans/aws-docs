---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-session.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Session
<a name="aws-resource-bedrock-session"></a>

Creates a session to temporarily store conversations for generative AI (GenAI) applications built with open-source frameworks such as LangGraph and LlamaIndex. Sessions enable you to save the state of conversations at checkpoints, with the added security and infrastructure of AWS. For more information, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

By default, Amazon Bedrock uses AWS-managed keys for session encryption, including session metadata, or you can use your own KMS key. For more information, see [Amazon Bedrock session encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html).

**Note**
 You use a session to store state and conversation history for generative AI applications built with open-source frameworks. For Amazon Bedrock Agents, the service automatically manages conversation context and associates them with the agent-specific sessionId you specify in the [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) API operation.

Related APIs:
+  [ListSessions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html)
+  [GetSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html)
+  [EndSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html)
+  [DeleteSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html)

## Syntax
<a name="aws-resource-bedrock-session-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-session-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Session",
  "Properties" : {
      "[EncryptionKeyArn](#cfn-bedrock-session-encryptionkeyarn)" : {{String}},
      "[SessionMetadata](#cfn-bedrock-session-sessionmetadata)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tags](#cfn-bedrock-session-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-session-syntax.yaml"></a>

```
Type: AWS::Bedrock::Session
Properties:
  [EncryptionKeyArn](#cfn-bedrock-session-encryptionkeyarn): {{String}}
  [SessionMetadata](#cfn-bedrock-session-sessionmetadata): {{
    {{Key}}: {{Value}}}}
  [Tags](#cfn-bedrock-session-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-session-properties"></a>

`EncryptionKeyArn`  <a name="cfn-bedrock-session-encryptionkeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SessionMetadata`  <a name="cfn-bedrock-session-sessionmetadata"></a>
Provides information about the execution process for different types of invocations, such as model invocation, knowledge base invocation, agent collaborator invocation, guardrail invocation, and code interpreter Invocation.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]{1,100}$`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-session-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-session-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-session-return-values"></a>

### Ref
<a name="aws-resource-bedrock-session-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-session-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-session-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp for when the session was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp for when the session was last modified.

`SessionArn`  <a name="SessionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the session.

`SessionId`  <a name="SessionId-fn::getatt"></a>
The unique identifier for the session.

`SessionStatus`  <a name="SessionStatus-fn::getatt"></a>
The current status of the session.
