---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elementalinference-feed-getoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Feed GetOutput
<a name="aws-properties-elementalinference-feed-getoutput"></a>

Contains configuration information about one output in a feed.

## Syntax
<a name="aws-properties-elementalinference-feed-getoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elementalinference-feed-getoutput-syntax.json"></a>

```
{
  "[Description](#cfn-elementalinference-feed-getoutput-description)" : {{String}},
  "[Name](#cfn-elementalinference-feed-getoutput-name)" : {{String}},
  "[OutputConfig](#cfn-elementalinference-feed-getoutput-outputconfig)" : {{OutputConfig}},
  "[Status](#cfn-elementalinference-feed-getoutput-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-elementalinference-feed-getoutput-syntax.yaml"></a>

```
  [Description](#cfn-elementalinference-feed-getoutput-description): {{String}}
  [Name](#cfn-elementalinference-feed-getoutput-name): {{String}}
  [OutputConfig](#cfn-elementalinference-feed-getoutput-outputconfig): {{
    OutputConfig}}
  [Status](#cfn-elementalinference-feed-getoutput-status): {{String}}
```

## Properties
<a name="aws-properties-elementalinference-feed-getoutput-properties"></a>

`Description`  <a name="cfn-elementalinference-feed-getoutput-description"></a>
The description that you assign to this output.
*Required*: No
*Type*: String
*Pattern*: `^[\w \-\.',@:;]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-elementalinference-feed-getoutput-name"></a>
The user-friendly name that you assign to this output.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputConfig`  <a name="cfn-elementalinference-feed-getoutput-outputconfig"></a>
Contains one typed output. Including a specific typed output enables the corresponding Elemental Inference in the feed.
*Required*: Yes
*Type*: [OutputConfig](aws-properties-elementalinference-feed-outputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-elementalinference-feed-getoutput-status"></a>
The status that you assign to this output.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
