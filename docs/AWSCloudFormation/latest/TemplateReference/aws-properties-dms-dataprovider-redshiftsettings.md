---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-redshiftsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider RedshiftSettings
<a name="aws-properties-dms-dataprovider-redshiftsettings"></a>

Provides information that defines an Amazon Redshift endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-redshiftsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-redshiftsettings-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-dms-dataprovider-redshiftsettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-redshiftsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-redshiftsettings-servername)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-redshiftsettings-syntax.yaml"></a>

```
  [DatabaseName](#cfn-dms-dataprovider-redshiftsettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-redshiftsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-redshiftsettings-servername): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-redshiftsettings-properties"></a>

`DatabaseName`  <a name="cfn-dms-dataprovider-redshiftsettings-databasename"></a>
The name of the Amazon Redshift data warehouse (service) that you are working with.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-redshiftsettings-port"></a>
The port number for Amazon Redshift. The default value is 5439.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-redshiftsettings-servername"></a>
The name of the Amazon Redshift cluster you are using.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
