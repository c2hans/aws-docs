---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-seedurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SeedUrl
<a name="aws-properties-bedrock-datasource-seedurl"></a>

The seed or starting point URL. You should be authorized to crawl the URL.

## Syntax
<a name="aws-properties-bedrock-datasource-seedurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-seedurl-syntax.json"></a>

```
{
  "[Url](#cfn-bedrock-datasource-seedurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-seedurl-syntax.yaml"></a>

```
  [Url](#cfn-bedrock-datasource-seedurl-url): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-seedurl-properties"></a>

`Url`  <a name="cfn-bedrock-datasource-seedurl-url"></a>
A seed or starting point URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https?://[A-Za-z0-9][^\s]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
