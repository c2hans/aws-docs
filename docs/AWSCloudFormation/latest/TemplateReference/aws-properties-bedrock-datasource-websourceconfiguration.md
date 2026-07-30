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
