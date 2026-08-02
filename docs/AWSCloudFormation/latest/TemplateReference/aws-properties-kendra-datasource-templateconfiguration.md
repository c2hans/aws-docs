---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-templateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource TemplateConfiguration
<a name="aws-properties-kendra-datasource-templateconfiguration"></a>

Provides a template for the configuration information to connect to your data source.

## Syntax
<a name="aws-properties-kendra-datasource-templateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-templateconfiguration-syntax.json"></a>

```
{
  "[Template](#cfn-kendra-datasource-templateconfiguration-template)" : {{Json}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-templateconfiguration-syntax.yaml"></a>

```
  [Template](#cfn-kendra-datasource-templateconfiguration-template): {{Json}}
```

## Properties
<a name="aws-properties-kendra-datasource-templateconfiguration-properties"></a>

`Template`  <a name="cfn-kendra-datasource-templateconfiguration-template"></a>
The template schema used for the data source, where templates schemas are supported.
See [Data source template schemas](https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
