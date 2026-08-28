---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-template-template.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Template Template
<a name="aws-properties-ses-template-template"></a>

An object that defines the email template to use for an email message, and the values to use for any message variables in that template. An *email template* is a type of message template that contains content that you want to reuse in email messages that you send. You can specifiy the email template by providing the name or ARN of an *email template* previously saved in your Amazon SES account or by providing the full template content.

## Syntax
<a name="aws-properties-ses-template-template-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-template-template-syntax.json"></a>

```
{
  "[HtmlPart](#cfn-ses-template-template-htmlpart)" : {{String}},
  "[SubjectPart](#cfn-ses-template-template-subjectpart)" : {{String}},
  "[TemplateName](#cfn-ses-template-template-templatename)" : {{String}},
  "[TextPart](#cfn-ses-template-template-textpart)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-template-template-syntax.yaml"></a>

```
  [HtmlPart](#cfn-ses-template-template-htmlpart): {{String}}
  [SubjectPart](#cfn-ses-template-template-subjectpart): {{String}}
  [TemplateName](#cfn-ses-template-template-templatename): {{String}}
  [TextPart](#cfn-ses-template-template-textpart): {{String}}
```

## Properties
<a name="aws-properties-ses-template-template-properties"></a>

`HtmlPart`  <a name="cfn-ses-template-template-htmlpart"></a>
The HTML body of the email.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubjectPart`  <a name="cfn-ses-template-template-subjectpart"></a>
The subject line of the email.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-ses-template-template-templatename"></a>
The name of the template. You will refer to this name when you send email using the `SendEmail` or `SendBulkEmail` operations.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextPart`  <a name="cfn-ses-template-template-textpart"></a>
The email body that is visible to recipients whose email clients do not display HTML content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
