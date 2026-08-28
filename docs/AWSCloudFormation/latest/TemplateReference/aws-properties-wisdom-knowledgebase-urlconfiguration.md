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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
