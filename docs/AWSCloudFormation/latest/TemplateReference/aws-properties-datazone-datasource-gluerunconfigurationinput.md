---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-gluerunconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource GlueRunConfigurationInput
<a name="aws-properties-datazone-datasource-gluerunconfigurationinput"></a>

The configuration details of the AWS Glue data source.

## Syntax
<a name="aws-properties-datazone-datasource-gluerunconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-gluerunconfigurationinput-syntax.json"></a>

```
{
  "[AutoImportDataQualityResult](#cfn-datazone-datasource-gluerunconfigurationinput-autoimportdataqualityresult)" : {{Boolean}},
  "[CatalogName](#cfn-datazone-datasource-gluerunconfigurationinput-catalogname)" : {{String}},
  "[DataAccessRole](#cfn-datazone-datasource-gluerunconfigurationinput-dataaccessrole)" : {{String}},
  "[RelationalFilterConfigurations](#cfn-datazone-datasource-gluerunconfigurationinput-relationalfilterconfigurations)" : {{[ RelationalFilterConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-gluerunconfigurationinput-syntax.yaml"></a>

```
  [AutoImportDataQualityResult](#cfn-datazone-datasource-gluerunconfigurationinput-autoimportdataqualityresult): {{Boolean}}
  [CatalogName](#cfn-datazone-datasource-gluerunconfigurationinput-catalogname): {{String}}
  [DataAccessRole](#cfn-datazone-datasource-gluerunconfigurationinput-dataaccessrole): {{String}}
  [RelationalFilterConfigurations](#cfn-datazone-datasource-gluerunconfigurationinput-relationalfilterconfigurations): {{
    - RelationalFilterConfiguration}}
```

## Properties
<a name="aws-properties-datazone-datasource-gluerunconfigurationinput-properties"></a>

`AutoImportDataQualityResult`  <a name="cfn-datazone-datasource-gluerunconfigurationinput-autoimportdataqualityresult"></a>
Specifies whether to automatically import data quality metrics as part of the data source run.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CatalogName`  <a name="cfn-datazone-datasource-gluerunconfigurationinput-catalogname"></a>
The catalog name in the AWS Glue run configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataAccessRole`  <a name="cfn-datazone-datasource-gluerunconfigurationinput-dataaccessrole"></a>
The data access role included in the configuration details of the AWS Glue data source.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelationalFilterConfigurations`  <a name="cfn-datazone-datasource-gluerunconfigurationinput-relationalfilterconfigurations"></a>
The relational filter configurations included in the configuration details of the AWS Glue data source.
*Required*: Yes
*Type*: Array of [RelationalFilterConfiguration](aws-properties-datazone-datasource-relationalfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
