---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-seedurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase SeedUrl
<a name="aws-properties-wisdom-knowledgebase-seedurl"></a>

A URL for crawling.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax.json"></a>

```
{
  "[Url](#cfn-wisdom-knowledgebase-seedurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax.yaml"></a>

```
  [Url](#cfn-wisdom-knowledgebase-seedurl-url): {{String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-seedurl-properties"></a>

`Url`  <a name="cfn-wisdom-knowledgebase-seedurl-url"></a>
URL for crawling
*Required*: No
*Type*: String
*Pattern*: `^https?://[A-Za-z0-9][^\s]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
