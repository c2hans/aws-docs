---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressIsInAddressList
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist"></a>

The address lists and the address list attribute value that is evaluated in a policy statement's conditional expression to either deny or block the incoming email.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist-syntax.json"></a>

```
{
  "[AddressLists](#cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-addresslists)" : {{[ String, ... ]}},
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist-syntax.yaml"></a>

```
  [AddressLists](#cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-addresslists): {{
    - String}}
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressisinaddresslist-properties"></a>

`AddressLists`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-addresslists"></a>
The address lists that will be used for evaluation.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressisinaddresslist-attribute"></a>
The email attribute that needs to be evaluated against the address list.
*Required*: Yes
*Type*: String
*Allowed values*: `RECIPIENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
