---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-aipromptversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIPromptVersion
<a name="aws-resource-wisdom-aipromptversion"></a>

Creates an Amazon Q in Connect AI Prompt version.

## Syntax
<a name="aws-resource-wisdom-aipromptversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-aipromptversion-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::AIPromptVersion",
  "Properties" : {
      "[AIPromptId](#cfn-wisdom-aipromptversion-aipromptid)" : {{String}},
      "[AssistantId](#cfn-wisdom-aipromptversion-assistantid)" : {{String}},
      "[ModifiedTimeSeconds](#cfn-wisdom-aipromptversion-modifiedtimeseconds)" : {{Number}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-aipromptversion-syntax.yaml"></a>

```
Type: AWS::Wisdom::AIPromptVersion
Properties:
  [AIPromptId](#cfn-wisdom-aipromptversion-aipromptid): {{String}}
  [AssistantId](#cfn-wisdom-aipromptversion-assistantid): {{String}}
  [ModifiedTimeSeconds](#cfn-wisdom-aipromptversion-modifiedtimeseconds): {{Number}}
```

## Properties
<a name="aws-resource-wisdom-aipromptversion-properties"></a>

`AIPromptId`  <a name="cfn-wisdom-aipromptversion-aipromptid"></a>
The identifier of the Amazon Q in Connect AI prompt.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssistantId`  <a name="cfn-wisdom-aipromptversion-assistantid"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModifiedTimeSeconds`  <a name="cfn-wisdom-aipromptversion-modifiedtimeseconds"></a>
The time the AI Prompt version was last modified in seconds.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-aipromptversion-return-values"></a>

### Ref
<a name="aws-resource-wisdom-aipromptversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-aipromptversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-aipromptversion-return-values-fn--getatt-fn--getatt"></a>

`AIPromptArn`  <a name="AIPromptArn-fn::getatt"></a>
The ARN of the AI prompt.

`AIPromptVersionId`  <a name="AIPromptVersionId-fn::getatt"></a>
Property description not available.

`AssistantArn`  <a name="AssistantArn-fn::getatt"></a>
Property description not available.

`VersionNumber`  <a name="VersionNumber-fn::getatt"></a>
The version number for this AI Prompt version.
