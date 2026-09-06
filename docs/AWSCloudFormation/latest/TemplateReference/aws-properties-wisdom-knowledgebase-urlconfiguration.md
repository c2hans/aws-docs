---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-urlconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase UrlConfiguration
<a name="aws-properties-wisdom-knowledgebase-urlconfiguration"></a>

The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-urlconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-urlconfiguration-syntax.json"></a>

```
{
  "[SeedUrls](#cfn-wisdom-knowledgebase-urlconfiguration-seedurls)" : {{[ SeedUrl, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-urlconfiguration-syntax.yaml"></a>

```
  [SeedUrls](#cfn-wisdom-knowledgebase-urlconfiguration-seedurls): {{
    - SeedUrl}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-urlconfiguration-properties"></a>

`SeedUrls`  <a name="cfn-wisdom-knowledgebase-urlconfiguration-seedurls"></a>
List of URLs for crawling.
*Required*: No
*Type*: Array of [SeedUrl](aws-properties-wisdom-knowledgebase-seedurl.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
