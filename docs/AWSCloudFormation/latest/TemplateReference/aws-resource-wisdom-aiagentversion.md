---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-aiagentversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgentVersion
<a name="aws-resource-wisdom-aiagentversion"></a>

Creates and Amazon Q in Connect AI Agent version.

## Syntax
<a name="aws-resource-wisdom-aiagentversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-aiagentversion-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AIAgentVersion",
  "Properties" : {
      "[AIAgentId](#cfn-wisdom-aiagentversion-aiagentid)" : {{String}},
      "[AssistantId](#cfn-wisdom-aiagentversion-assistantid)" : {{String}},
      "[ModifiedTimeSeconds](#cfn-wisdom-aiagentversion-modifiedtimeseconds)" : {{Number}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-aiagentversion-syntax.yaml"></a>

```
Type: AWS::Wisdom::AIAgentVersion
Properties:
  [AIAgentId](#cfn-wisdom-aiagentversion-aiagentid): {{String}}
  [AssistantId](#cfn-wisdom-aiagentversion-assistantid): {{String}}
  [ModifiedTimeSeconds](#cfn-wisdom-aiagentversion-modifiedtimeseconds): {{Number}}
```

## Properties
<a name="aws-resource-wisdom-aiagentversion-properties"></a>

`AIAgentId`  <a name="cfn-wisdom-aiagentversion-aiagentid"></a>
The identifier of the AI Agent.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssistantId`  <a name="cfn-wisdom-aiagentversion-assistantid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModifiedTimeSeconds`  <a name="cfn-wisdom-aiagentversion-modifiedtimeseconds"></a>
The time the AI Agent version was last modified in seconds.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-aiagentversion-return-values"></a>

### Ref
<a name="aws-resource-wisdom-aiagentversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-aiagentversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-aiagentversion-return-values-fn--getatt-fn--getatt"></a>

`AIAgentArn`  <a name="AIAgentArn-fn::getatt"></a>
Property description not available.

`AIAgentVersionId`  <a name="AIAgentVersionId-fn::getatt"></a>
Property description not available.

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
Property description not available.

`VersionNumber`  <a name="VersionNumber-fn::getatt"></a>
The version number for this AI Agent version.
