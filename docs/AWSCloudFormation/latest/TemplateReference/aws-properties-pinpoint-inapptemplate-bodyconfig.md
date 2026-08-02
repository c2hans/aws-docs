---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-inapptemplate-bodyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::InAppTemplate BodyConfig
<a name="aws-properties-pinpoint-inapptemplate-bodyconfig"></a>

Specifies the configuration of the main body text of the in-app message.

## Syntax
<a name="aws-properties-pinpoint-inapptemplate-bodyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-inapptemplate-bodyconfig-syntax.json"></a>

```
{
  "[Alignment](#cfn-pinpoint-inapptemplate-bodyconfig-alignment)" : {{String}},
  "[Body](#cfn-pinpoint-inapptemplate-bodyconfig-body)" : {{String}},
  "[TextColor](#cfn-pinpoint-inapptemplate-bodyconfig-textcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-inapptemplate-bodyconfig-syntax.yaml"></a>

```
  [Alignment](#cfn-pinpoint-inapptemplate-bodyconfig-alignment): {{String}}
  [Body](#cfn-pinpoint-inapptemplate-bodyconfig-body): {{String}}
  [TextColor](#cfn-pinpoint-inapptemplate-bodyconfig-textcolor): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-inapptemplate-bodyconfig-properties"></a>

`Alignment`  <a name="cfn-pinpoint-inapptemplate-bodyconfig-alignment"></a>
The text alignment of the main body text of the message. Acceptable values: `LEFT`, `CENTER`, `RIGHT`.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Body`  <a name="cfn-pinpoint-inapptemplate-bodyconfig-body"></a>
The main body text of the message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-pinpoint-inapptemplate-bodyconfig-textcolor"></a>
The color of the body text, expressed as a hex color code (such as \#000000 for black).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
