---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-managedsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ManagedSourceConfiguration
<a name="aws-properties-wisdom-knowledgebase-managedsourceconfiguration"></a>

Source configuration for managed resources.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-managedsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-managedsourceconfiguration-syntax.json"></a>

```
{
  "[WebCrawlerConfiguration](#cfn-wisdom-knowledgebase-managedsourceconfiguration-webcrawlerconfiguration)" : {{WebCrawlerConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-managedsourceconfiguration-syntax.yaml"></a>

```
  [WebCrawlerConfiguration](#cfn-wisdom-knowledgebase-managedsourceconfiguration-webcrawlerconfiguration): {{
    WebCrawlerConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-managedsourceconfiguration-properties"></a>

`WebCrawlerConfiguration`  <a name="cfn-wisdom-knowledgebase-managedsourceconfiguration-webcrawlerconfiguration"></a>
Configuration data for web crawler data source.
*Required*: Yes
*Type*: [WebCrawlerConfiguration](aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
