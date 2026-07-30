---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-eventdatastore-contextkeyselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::EventDataStore ContextKeySelector
<a name="aws-properties-cloudtrail-eventdatastore-contextkeyselector"></a>

An object that contains information types to be included in CloudTrail enriched events.

## Syntax
<a name="aws-properties-cloudtrail-eventdatastore-contextkeyselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-eventdatastore-contextkeyselector-syntax.json"></a>

```
{
  "[Equals](#cfn-cloudtrail-eventdatastore-contextkeyselector-equals)" : {{[ String, ... ]}},
  "[Type](#cfn-cloudtrail-eventdatastore-contextkeyselector-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-eventdatastore-contextkeyselector-syntax.yaml"></a>

```
  [Equals](#cfn-cloudtrail-eventdatastore-contextkeyselector-equals): {{
    - String}}
  [Type](#cfn-cloudtrail-eventdatastore-contextkeyselector-type): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-eventdatastore-contextkeyselector-properties"></a>

`Equals`  <a name="cfn-cloudtrail-eventdatastore-contextkeyselector-equals"></a>
A list of keys defined by Type to be included in CloudTrail enriched events.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudtrail-eventdatastore-contextkeyselector-type"></a>
Specifies the type of the event record field in ContextKeySelector. Valid values include RequestContext, TagContext.
*Required*: Yes
*Type*: String
*Allowed values*: `RequestContext | TagContext`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
