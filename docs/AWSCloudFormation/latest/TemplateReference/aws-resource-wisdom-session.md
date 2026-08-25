---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-session.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Session
<a name="aws-resource-wisdom-session"></a>

Creates a session. A session is a contextual container used for generating recommendations. Connect Customer creates a new Amazon Q in Connect session for each contact on which Amazon Q in Connect is enabled.

## Syntax
<a name="aws-resource-wisdom-session-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-session-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::Session",
  "Properties" : {
      "[AssistantId](#cfn-wisdom-session-assistantid)" : {{String}},
      "[Description](#cfn-wisdom-session-description)" : {{String}},
      "[Name](#cfn-wisdom-session-name)" : {{String}},
      "[Tags](#cfn-wisdom-session-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-session-syntax.yaml"></a>

```
Type: AWS::Wisdom::Session
Properties:
  [AssistantId](#cfn-wisdom-session-assistantid): {{String}}
  [Description](#cfn-wisdom-session-description): {{String}}
  [Name](#cfn-wisdom-session-name): {{String}}
  [Tags](#cfn-wisdom-session-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-wisdom-session-properties"></a>

`AssistantId`  <a name="cfn-wisdom-session-assistantid"></a>
The identifier of the Amazon Q in Connect assistant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-wisdom-session-description"></a>
The description of the session.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-wisdom-session-name"></a>
The name of the session.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-session-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-wisdom-session-tagsitems.md)
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-wisdom-session-return-values"></a>

### Ref
<a name="aws-resource-wisdom-session-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-session-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-session-return-values-fn--getatt-fn--getatt"></a>

`SessionArn`  <a name="SessionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the session.

`SessionId`  <a name="SessionId-fn::getatt"></a>
The identifier of the session.
