---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::SubscriptionTarget SubscriptionTargetForm
<a name="aws-properties-datazone-subscriptiontarget-subscriptiontargetform"></a>

The details of the subscription target configuration.

## Syntax
<a name="aws-properties-datazone-subscriptiontarget-subscriptiontargetform-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-subscriptiontarget-subscriptiontargetform-syntax.json"></a>

```
{
  "[Content](#cfn-datazone-subscriptiontarget-subscriptiontargetform-content)" : {{String}},
  "[FormName](#cfn-datazone-subscriptiontarget-subscriptiontargetform-formname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-subscriptiontarget-subscriptiontargetform-syntax.yaml"></a>

```
  [Content](#cfn-datazone-subscriptiontarget-subscriptiontargetform-content): {{String}}
  [FormName](#cfn-datazone-subscriptiontarget-subscriptiontargetform-formname): {{String}}
```

## Properties
<a name="aws-properties-datazone-subscriptiontarget-subscriptiontargetform-properties"></a>

`Content`  <a name="cfn-datazone-subscriptiontarget-subscriptiontargetform-content"></a>
The content of the subscription target configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormName`  <a name="cfn-datazone-subscriptiontarget-subscriptiontargetform-formname"></a>
The form name included in the subscription target configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
