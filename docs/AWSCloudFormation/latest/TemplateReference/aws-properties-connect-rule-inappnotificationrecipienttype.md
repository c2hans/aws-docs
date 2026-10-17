---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-inappnotificationrecipienttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule InAppNotificationRecipientType
<a name="aws-properties-connect-rule-inappnotificationrecipienttype"></a>

<a name="aws-properties-connect-rule-inappnotificationrecipienttype-description"></a>The `InAppNotificationRecipientType` property type specifies Property description not available. for an [AWS::Connect::Rule](aws-resource-connect-rule.md).

## Syntax
<a name="aws-properties-connect-rule-inappnotificationrecipienttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-inappnotificationrecipienttype-syntax.json"></a>

```
{
  "[UserArns](#cfn-connect-rule-inappnotificationrecipienttype-userarns)" : {{[ String, ... ]}},
  "[UserTags](#cfn-connect-rule-inappnotificationrecipienttype-usertags)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-inappnotificationrecipienttype-syntax.yaml"></a>

```
  [UserArns](#cfn-connect-rule-inappnotificationrecipienttype-userarns): {{
    - String}}
  [UserTags](#cfn-connect-rule-inappnotificationrecipienttype-usertags): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-inappnotificationrecipienttype-properties"></a>

`UserArns`  <a name="cfn-connect-rule-inappnotificationrecipienttype-userarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserTags`  <a name="cfn-connect-rule-inappnotificationrecipienttype-usertags"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
