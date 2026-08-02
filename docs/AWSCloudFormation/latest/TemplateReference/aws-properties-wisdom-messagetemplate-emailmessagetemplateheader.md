---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate EmailMessageTemplateHeader
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplateheader"></a>

The email headers to include in email messages.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplateheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplateheader-syntax.json"></a>

```
{
  "[Name](#cfn-wisdom-messagetemplate-emailmessagetemplateheader-name)" : {{String}},
  "[Value](#cfn-wisdom-messagetemplate-emailmessagetemplateheader-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplateheader-syntax.yaml"></a>

```
  [Name](#cfn-wisdom-messagetemplate-emailmessagetemplateheader-name): {{String}}
  [Value](#cfn-wisdom-messagetemplate-emailmessagetemplateheader-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplateheader-properties"></a>

`Name`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplateheader-name"></a>
The name of the email header.
*Required*: No
*Type*: String
*Pattern*: `^[!-9;-@A-~]+$`
*Minimum*: `1`
*Maximum*: `126`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplateheader-value"></a>
The value of the email header.
*Required*: No
*Type*: String
*Pattern*: `[ -~]*`
*Minimum*: `1`
*Maximum*: `870`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
