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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
