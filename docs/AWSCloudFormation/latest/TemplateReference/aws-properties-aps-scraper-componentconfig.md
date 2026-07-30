---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-componentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper ComponentConfig
<a name="aws-properties-aps-scraper-componentconfig"></a>

Configuration settings for a scraper component.

## Syntax
<a name="aws-properties-aps-scraper-componentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-componentconfig-syntax.json"></a>

```
{
  "[Options](#cfn-aps-scraper-componentconfig-options)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-aps-scraper-componentconfig-syntax.yaml"></a>

```
  [Options](#cfn-aps-scraper-componentconfig-options): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-aps-scraper-componentconfig-properties"></a>

`Options`  <a name="cfn-aps-scraper-componentconfig-options"></a>
Configuration options for the scraper component.
*Required*: No
*Type*: Object of String
*Pattern*: `^[A-Za-z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
