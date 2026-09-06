---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleisinaddresslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleIsInAddressList
<a name="aws-properties-ses-mailmanagerruleset-ruleisinaddresslist"></a>

The structure type for a boolean condition that provides the address lists and address list attribute to evaluate.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleisinaddresslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleisinaddresslist-syntax.json"></a>

```
{
  "[AddressLists](#cfn-ses-mailmanagerruleset-ruleisinaddresslist-addresslists)" : {{[ String, ... ]}},
  "[Attribute](#cfn-ses-mailmanagerruleset-ruleisinaddresslist-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleisinaddresslist-syntax.yaml"></a>

```
  [AddressLists](#cfn-ses-mailmanagerruleset-ruleisinaddresslist-addresslists): {{
    - String}}
  [Attribute](#cfn-ses-mailmanagerruleset-ruleisinaddresslist-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleisinaddresslist-properties"></a>

`AddressLists`  <a name="cfn-ses-mailmanagerruleset-ruleisinaddresslist-addresslists"></a>
The address lists that will be used for evaluation.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagerruleset-ruleisinaddresslist-attribute"></a>
The email attribute that needs to be evaluated against the address list.
*Required*: Yes
*Type*: String
*Allowed values*: `RECIPIENT | MAIL_FROM | SENDER | FROM | TO | CC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
