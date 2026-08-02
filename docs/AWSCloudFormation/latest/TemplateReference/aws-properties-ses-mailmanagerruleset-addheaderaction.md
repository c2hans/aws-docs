---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-addheaderaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet AddHeaderAction
<a name="aws-properties-ses-mailmanagerruleset-addheaderaction"></a>

The action to add a header to a message. When executed, this action will add the given header to the message.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-addheaderaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-addheaderaction-syntax.json"></a>

```
{
  "[HeaderName](#cfn-ses-mailmanagerruleset-addheaderaction-headername)" : {{String}},
  "[HeaderValue](#cfn-ses-mailmanagerruleset-addheaderaction-headervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-addheaderaction-syntax.yaml"></a>

```
  [HeaderName](#cfn-ses-mailmanagerruleset-addheaderaction-headername): {{String}}
  [HeaderValue](#cfn-ses-mailmanagerruleset-addheaderaction-headervalue): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-addheaderaction-properties"></a>

`HeaderName`  <a name="cfn-ses-mailmanagerruleset-addheaderaction-headername"></a>
The name of the header to add to an email. The header must be prefixed with "X-". Headers are added regardless of whether the header name pre-existed in the email.
*Required*: Yes
*Type*: String
*Pattern*: `^[xX]\-[a-zA-Z0-9\-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderValue`  <a name="cfn-ses-mailmanagerruleset-addheaderaction-headervalue"></a>
The value of the header to add to the email.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
