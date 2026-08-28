---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elementalinference-feed-subtitlingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Feed SubtitlingConfig
<a name="aws-properties-elementalinference-feed-subtitlingconfig"></a>

<a name="aws-properties-elementalinference-feed-subtitlingconfig-description"></a>The `SubtitlingConfig` property type specifies Property description not available. for an [AWS::ElementalInference::Feed](aws-resource-elementalinference-feed.md).

## Syntax
<a name="aws-properties-elementalinference-feed-subtitlingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elementalinference-feed-subtitlingconfig-syntax.json"></a>

```
{
  "[AspectRatio](#cfn-elementalinference-feed-subtitlingconfig-aspectratio)" : {{AspectRatio}},
  "[Dictionary](#cfn-elementalinference-feed-subtitlingconfig-dictionary)" : {{String}},
  "[Language](#cfn-elementalinference-feed-subtitlingconfig-language)" : {{String}},
  "[ProfanityFilter](#cfn-elementalinference-feed-subtitlingconfig-profanityfilter)" : {{String}}
}
```

### YAML
<a name="aws-properties-elementalinference-feed-subtitlingconfig-syntax.yaml"></a>

```
  [AspectRatio](#cfn-elementalinference-feed-subtitlingconfig-aspectratio): {{
    AspectRatio}}
  [Dictionary](#cfn-elementalinference-feed-subtitlingconfig-dictionary): {{String}}
  [Language](#cfn-elementalinference-feed-subtitlingconfig-language): {{String}}
  [ProfanityFilter](#cfn-elementalinference-feed-subtitlingconfig-profanityfilter): {{String}}
```

## Properties
<a name="aws-properties-elementalinference-feed-subtitlingconfig-properties"></a>

`AspectRatio`  <a name="cfn-elementalinference-feed-subtitlingconfig-aspectratio"></a>
Property description not available.
*Required*: No
*Type*: [AspectRatio](aws-properties-elementalinference-feed-aspectratio.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dictionary`  <a name="cfn-elementalinference-feed-subtitlingconfig-dictionary"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-elementalinference-feed-subtitlingconfig-language"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `eng | eng-au | eng-gb | eng-us | fra | ita | deu | spa | por`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfanityFilter`  <a name="cfn-elementalinference-feed-subtitlingconfig-profanityfilter"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | CENSOR | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
