---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-crawlerlimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase CrawlerLimits
<a name="aws-properties-wisdom-knowledgebase-crawlerlimits"></a>

The limits of the crawler.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-crawlerlimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-crawlerlimits-syntax.json"></a>

```
{
  "[RateLimit](#cfn-wisdom-knowledgebase-crawlerlimits-ratelimit)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-crawlerlimits-syntax.yaml"></a>

```
  [RateLimit](#cfn-wisdom-knowledgebase-crawlerlimits-ratelimit): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-crawlerlimits-properties"></a>

`RateLimit`  <a name="cfn-wisdom-knowledgebase-crawlerlimits-ratelimit"></a>
The limit rate at which the crawler is configured.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `3000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
