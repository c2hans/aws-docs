---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-websourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource WebSourceConfiguration
<a name="aws-properties-bedrock-datasource-websourceconfiguration"></a>

The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.

## Syntax
<a name="aws-properties-bedrock-datasource-websourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-websourceconfiguration-syntax.json"></a>

```
{
  "[UrlConfiguration](#cfn-bedrock-datasource-websourceconfiguration-urlconfiguration)" : {{UrlConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-websourceconfiguration-syntax.yaml"></a>

```
  [UrlConfiguration](#cfn-bedrock-datasource-websourceconfiguration-urlconfiguration): {{
    UrlConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-websourceconfiguration-properties"></a>

`UrlConfiguration`  <a name="cfn-bedrock-datasource-websourceconfiguration-urlconfiguration"></a>
The configuration of the URL/URLs.
*Required*: Yes
*Type*: [UrlConfiguration](aws-properties-bedrock-datasource-urlconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
