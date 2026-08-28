---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-urlconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource UrlConfiguration
<a name="aws-properties-bedrock-datasource-urlconfiguration"></a>

The configuration of web URLs that you want to crawl. You should be authorized to crawl the URLs.

## Syntax
<a name="aws-properties-bedrock-datasource-urlconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-urlconfiguration-syntax.json"></a>

```
{
  "[SeedUrls](#cfn-bedrock-datasource-urlconfiguration-seedurls)" : {{[ SeedUrl, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-urlconfiguration-syntax.yaml"></a>

```
  [SeedUrls](#cfn-bedrock-datasource-urlconfiguration-seedurls): {{
    - SeedUrl}}
```

## Properties
<a name="aws-properties-bedrock-datasource-urlconfiguration-properties"></a>

`SeedUrls`  <a name="cfn-bedrock-datasource-urlconfiguration-seedurls"></a>
One or more seed or starting point URLs.
*Required*: Yes
*Type*: Array of [SeedUrl](aws-properties-bedrock-datasource-seedurl.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
