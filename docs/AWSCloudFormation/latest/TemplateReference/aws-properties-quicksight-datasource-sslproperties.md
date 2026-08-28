---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-sslproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource SslProperties
<a name="aws-properties-quicksight-datasource-sslproperties"></a>

Secure Socket Layer (SSL) properties that apply when Quick Sight connects to your underlying data source.

## Syntax
<a name="aws-properties-quicksight-datasource-sslproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-sslproperties-syntax.json"></a>

```
{
  "[DisableSsl](#cfn-quicksight-datasource-sslproperties-disablessl)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-sslproperties-syntax.yaml"></a>

```
  [DisableSsl](#cfn-quicksight-datasource-sslproperties-disablessl): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-datasource-sslproperties-properties"></a>

`DisableSsl`  <a name="cfn-quicksight-datasource-sslproperties-disablessl"></a>
A Boolean option to control whether SSL should be disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
