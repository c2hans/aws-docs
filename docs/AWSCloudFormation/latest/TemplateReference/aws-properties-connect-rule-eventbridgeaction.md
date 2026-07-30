---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-eventbridgeaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule EventBridgeAction
<a name="aws-properties-connect-rule-eventbridgeaction"></a>

The EventBridge action definition.

## Syntax
<a name="aws-properties-connect-rule-eventbridgeaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-eventbridgeaction-syntax.json"></a>

```
{
  "[Name](#cfn-connect-rule-eventbridgeaction-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-eventbridgeaction-syntax.yaml"></a>

```
  [Name](#cfn-connect-rule-eventbridgeaction-name): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-eventbridgeaction-properties"></a>

`Name`  <a name="cfn-connect-rule-eventbridgeaction-name"></a>
The name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
