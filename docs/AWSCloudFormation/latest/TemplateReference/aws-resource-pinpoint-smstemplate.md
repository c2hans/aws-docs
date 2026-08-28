---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pinpoint-smstemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::SmsTemplate
<a name="aws-resource-pinpoint-smstemplate"></a>

Creates a message template that you can use in messages that are sent through the SMS channel. A *message template* is a set of content and settings that you can define, save, and reuse in messages for any of your Amazon Pinpoint applications.

## Syntax
<a name="aws-resource-pinpoint-smstemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pinpoint-smstemplate-syntax.json"></a>

```
{
  "Type" : "AWS::Pinpoint::SmsTemplate",
  "Properties" : {
      "[Body](#cfn-pinpoint-smstemplate-body)" : {{String}},
      "[DefaultSubstitutions](#cfn-pinpoint-smstemplate-defaultsubstitutions)" : {{String}},
      "[Tags](#cfn-pinpoint-smstemplate-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}},
      "[TemplateDescription](#cfn-pinpoint-smstemplate-templatedescription)" : {{String}},
      "[TemplateName](#cfn-pinpoint-smstemplate-templatename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pinpoint-smstemplate-syntax.yaml"></a>

```
Type: AWS::Pinpoint::SmsTemplate
Properties:
  [Body](#cfn-pinpoint-smstemplate-body): {{String}}
  [DefaultSubstitutions](#cfn-pinpoint-smstemplate-defaultsubstitutions): {{String}}
  [Tags](#cfn-pinpoint-smstemplate-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
  [TemplateDescription](#cfn-pinpoint-smstemplate-templatedescription): {{String}}
  [TemplateName](#cfn-pinpoint-smstemplate-templatename): {{String}}
```

## Properties
<a name="aws-resource-pinpoint-smstemplate-properties"></a>

`Body`  <a name="cfn-pinpoint-smstemplate-body"></a>
The message body to use in text messages that are based on the message template.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSubstitutions`  <a name="cfn-pinpoint-smstemplate-defaultsubstitutions"></a>
A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-pinpoint-smstemplate-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateDescription`  <a name="cfn-pinpoint-smstemplate-templatedescription"></a>
A custom description of the message template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-pinpoint-smstemplate-templatename"></a>
The name of the message template to use for the message. If specified, this value must match the name of an existing message template.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-pinpoint-smstemplate-return-values"></a>

### Ref
<a name="aws-resource-pinpoint-smstemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the message template (`TemplateName`).

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-pinpoint-smstemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-pinpoint-smstemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the message template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
