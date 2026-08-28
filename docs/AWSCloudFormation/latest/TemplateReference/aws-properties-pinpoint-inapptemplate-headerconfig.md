---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-inapptemplate-headerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::InAppTemplate HeaderConfig
<a name="aws-properties-pinpoint-inapptemplate-headerconfig"></a>

Specifies the configuration and content of the header or title text of the in-app message.

## Syntax
<a name="aws-properties-pinpoint-inapptemplate-headerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-inapptemplate-headerconfig-syntax.json"></a>

```
{
  "[Alignment](#cfn-pinpoint-inapptemplate-headerconfig-alignment)" : {{String}},
  "[Header](#cfn-pinpoint-inapptemplate-headerconfig-header)" : {{String}},
  "[TextColor](#cfn-pinpoint-inapptemplate-headerconfig-textcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-inapptemplate-headerconfig-syntax.yaml"></a>

```
  [Alignment](#cfn-pinpoint-inapptemplate-headerconfig-alignment): {{String}}
  [Header](#cfn-pinpoint-inapptemplate-headerconfig-header): {{String}}
  [TextColor](#cfn-pinpoint-inapptemplate-headerconfig-textcolor): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-inapptemplate-headerconfig-properties"></a>

`Alignment`  <a name="cfn-pinpoint-inapptemplate-headerconfig-alignment"></a>
The text alignment of the title of the message. Acceptable values: `LEFT`, `CENTER`, `RIGHT`.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Header`  <a name="cfn-pinpoint-inapptemplate-headerconfig-header"></a>
The title text of the in-app message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-pinpoint-inapptemplate-headerconfig-textcolor"></a>
The color of the title text, expressed as a hex color code (such as \#000000 for black).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
