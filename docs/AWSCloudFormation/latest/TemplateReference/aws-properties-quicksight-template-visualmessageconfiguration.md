---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visualmessageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisualMessageConfiguration
<a name="aws-properties-quicksight-template-visualmessageconfiguration"></a>

The configuration for a customizable message displayed on a visual. Supports parameter substitution in text fields.

## Syntax
<a name="aws-properties-quicksight-template-visualmessageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visualmessageconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-quicksight-template-visualmessageconfiguration-description)" : {{String}},
  "[DescriptionVisibility](#cfn-quicksight-template-visualmessageconfiguration-descriptionvisibility)" : {{String}},
  "[Enabled](#cfn-quicksight-template-visualmessageconfiguration-enabled)" : {{Boolean}},
  "[LinkText](#cfn-quicksight-template-visualmessageconfiguration-linktext)" : {{String}},
  "[LinkUrl](#cfn-quicksight-template-visualmessageconfiguration-linkurl)" : {{String}},
  "[LinkVisibility](#cfn-quicksight-template-visualmessageconfiguration-linkvisibility)" : {{String}},
  "[Title](#cfn-quicksight-template-visualmessageconfiguration-title)" : {{String}},
  "[TitleVisibility](#cfn-quicksight-template-visualmessageconfiguration-titlevisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visualmessageconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-quicksight-template-visualmessageconfiguration-description): {{String}}
  [DescriptionVisibility](#cfn-quicksight-template-visualmessageconfiguration-descriptionvisibility): {{String}}
  [Enabled](#cfn-quicksight-template-visualmessageconfiguration-enabled): {{Boolean}}
  [LinkText](#cfn-quicksight-template-visualmessageconfiguration-linktext): {{String}}
  [LinkUrl](#cfn-quicksight-template-visualmessageconfiguration-linkurl): {{String}}
  [LinkVisibility](#cfn-quicksight-template-visualmessageconfiguration-linkvisibility): {{String}}
  [Title](#cfn-quicksight-template-visualmessageconfiguration-title): {{String}}
  [TitleVisibility](#cfn-quicksight-template-visualmessageconfiguration-titlevisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-visualmessageconfiguration-properties"></a>

`Description`  <a name="cfn-quicksight-template-visualmessageconfiguration-description"></a>
The description text of the message that is displayed on the visual.
*Required*: No
*Type*: String
*Pattern*: `^[^*;=`{}~\x00-\x08\x0E-\x1F\x7F]*$`
*Minimum*: `0`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DescriptionVisibility`  <a name="cfn-quicksight-template-visualmessageconfiguration-descriptionvisibility"></a>
Specifies whether the description of the message is displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-quicksight-template-visualmessageconfiguration-enabled"></a>
Specifies whether the custom message is displayed on the visual. When set to `true`, the custom message appears in place of the default message. When set to `false` or omitted, the default message is displayed.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkText`  <a name="cfn-quicksight-template-visualmessageconfiguration-linktext"></a>
The display text of the hyperlink that is shown in the message.
*Required*: No
*Type*: String
*Pattern*: `^[^*;=`{}~\x00-\x08\x0E-\x1F\x7F]*$`
*Minimum*: `0`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkUrl`  <a name="cfn-quicksight-template-visualmessageconfiguration-linkurl"></a>
The destination URL of the hyperlink that is shown in the message. Only valid `http`, `https`, and `mailto` URLs are supported.
*Required*: No
*Type*: String
*Pattern*: `^(?:(?:[hH][tT][tT][pP][sS]?://|[mM][aA][iI][lL][tT][oO]:)\S*<<\$.+?>>\S*|[hH][tT][tT][pP][sS]?://[a-zA-Z\d.-]+\.[a-zA-Z]{2,63}(?::\d+)?(?:[/?#][^\s]*)?|[mM][aA][iI][lL][tT][oO]:[^\s@]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,63})$(?![\s\S])`
*Minimum*: `0`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkVisibility`  <a name="cfn-quicksight-template-visualmessageconfiguration-linkvisibility"></a>
Specifies whether the hyperlink in the message is displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-visualmessageconfiguration-title"></a>
The title text of the message that is displayed on the visual.
*Required*: No
*Type*: String
*Pattern*: `^[^*;=`{}~\x00-\x08\x0E-\x1F\x7F]*$`
*Minimum*: `0`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TitleVisibility`  <a name="cfn-quicksight-template-visualmessageconfiguration-titlevisibility"></a>
Specifies whether the title of the message is displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
