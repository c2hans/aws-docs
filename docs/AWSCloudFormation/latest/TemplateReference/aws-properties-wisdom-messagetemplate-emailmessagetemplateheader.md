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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
