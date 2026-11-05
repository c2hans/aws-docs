---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-intent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger Intent
<a name="aws-properties-customerprofiles-eventtrigger-intent"></a>

<a name="aws-properties-customerprofiles-eventtrigger-intent-description"></a>The `Intent` property type specifies Property description not available. for an [AWS::CustomerProfiles::EventTrigger](aws-resource-customerprofiles-eventtrigger.md).

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-intent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-intent-syntax.json"></a>

```
{
  "[IntentDomain](#cfn-customerprofiles-eventtrigger-intent-intentdomain)" : {{String}},
  "[Type](#cfn-customerprofiles-eventtrigger-intent-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-intent-syntax.yaml"></a>

```
  [IntentDomain](#cfn-customerprofiles-eventtrigger-intent-intentdomain): {{String}}
  [Type](#cfn-customerprofiles-eventtrigger-intent-type): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-intent-properties"></a>

`IntentDomain`  <a name="cfn-customerprofiles-eventtrigger-intent-intentdomain"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `DEFAULT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-customerprofiles-eventtrigger-intent-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PRICE_SENSITIVITY | UPGRADE_UPSELL_PROPENSITY | LAST_SEARCH_INTENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
