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
