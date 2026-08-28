---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-datasourceconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource DataSourceConfigurationInput
<a name="aws-properties-datazone-datasource-datasourceconfigurationinput"></a>

The configuration of the data source.

## Syntax
<a name="aws-properties-datazone-datasource-datasourceconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-datasourceconfigurationinput-syntax.json"></a>

```
{
  "[GlueRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-gluerunconfiguration)" : {{GlueRunConfigurationInput}},
  "[RedshiftRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-redshiftrunconfiguration)" : {{RedshiftRunConfigurationInput}},
  "[SageMakerRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-sagemakerrunconfiguration)" : {{SageMakerRunConfigurationInput}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-datasourceconfigurationinput-syntax.yaml"></a>

```
  [GlueRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-gluerunconfiguration): {{
    GlueRunConfigurationInput}}
  [RedshiftRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-redshiftrunconfiguration): {{
    RedshiftRunConfigurationInput}}
  [SageMakerRunConfiguration](#cfn-datazone-datasource-datasourceconfigurationinput-sagemakerrunconfiguration): {{
    SageMakerRunConfigurationInput}}
```

## Properties
<a name="aws-properties-datazone-datasource-datasourceconfigurationinput-properties"></a>

`GlueRunConfiguration`  <a name="cfn-datazone-datasource-datasourceconfigurationinput-gluerunconfiguration"></a>
The configuration of the AWS Glue data source.
*Required*: No
*Type*: [GlueRunConfigurationInput](aws-properties-datazone-datasource-gluerunconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftRunConfiguration`  <a name="cfn-datazone-datasource-datasourceconfigurationinput-redshiftrunconfiguration"></a>
The configuration of the Amazon Redshift data source.
*Required*: No
*Type*: [RedshiftRunConfigurationInput](aws-properties-datazone-datasource-redshiftrunconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SageMakerRunConfiguration`  <a name="cfn-datazone-datasource-datasourceconfigurationinput-sagemakerrunconfiguration"></a>
The Amazon SageMaker run configuration.
*Required*: No
*Type*: [SageMakerRunConfigurationInput](aws-properties-datazone-datasource-sagemakerrunconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
