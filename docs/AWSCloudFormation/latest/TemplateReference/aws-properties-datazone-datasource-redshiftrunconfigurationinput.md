---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftRunConfigurationInput
<a name="aws-properties-datazone-datasource-redshiftrunconfigurationinput"></a>

The relational filter configurations included in the configuration details of the Amazon Redshift data source.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftrunconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftrunconfigurationinput-syntax.json"></a>

```
{
  "[DataAccessRole](#cfn-datazone-datasource-redshiftrunconfigurationinput-dataaccessrole)" : {{String}},
  "[RedshiftCredentialConfiguration](#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftcredentialconfiguration)" : {{RedshiftCredentialConfiguration}},
  "[RedshiftStorage](#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftstorage)" : {{RedshiftStorage}},
  "[RelationalFilterConfigurations](#cfn-datazone-datasource-redshiftrunconfigurationinput-relationalfilterconfigurations)" : {{[ RelationalFilterConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftrunconfigurationinput-syntax.yaml"></a>

```
  [DataAccessRole](#cfn-datazone-datasource-redshiftrunconfigurationinput-dataaccessrole): {{String}}
  [RedshiftCredentialConfiguration](#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftcredentialconfiguration): {{
    RedshiftCredentialConfiguration}}
  [RedshiftStorage](#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftstorage): {{
    RedshiftStorage}}
  [RelationalFilterConfigurations](#cfn-datazone-datasource-redshiftrunconfigurationinput-relationalfilterconfigurations): {{
    - RelationalFilterConfiguration}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftrunconfigurationinput-properties"></a>

`DataAccessRole`  <a name="cfn-datazone-datasource-redshiftrunconfigurationinput-dataaccessrole"></a>
The data access role included in the configuration details of the Amazon Redshift data source.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftCredentialConfiguration`  <a name="cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftcredentialconfiguration"></a>
The details of the credentials required to access an Amazon Redshift cluster.
*Required*: No
*Type*: [RedshiftCredentialConfiguration](aws-properties-datazone-datasource-redshiftcredentialconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftStorage`  <a name="cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftstorage"></a>
The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.
*Required*: No
*Type*: [RedshiftStorage](aws-properties-datazone-datasource-redshiftstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelationalFilterConfigurations`  <a name="cfn-datazone-datasource-redshiftrunconfigurationinput-relationalfilterconfigurations"></a>
The relational filter configurations included in the configuration details of the AWS Glue data source.
*Required*: Yes
*Type*: Array of [RelationalFilterConfiguration](aws-properties-datazone-datasource-relationalfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
