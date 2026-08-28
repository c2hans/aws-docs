---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-mariadbparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource MariaDbParameters
<a name="aws-properties-quicksight-datasource-mariadbparameters"></a>

The parameters for MariaDB.

## Syntax
<a name="aws-properties-quicksight-datasource-mariadbparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-mariadbparameters-syntax.json"></a>

```
{
  "[Database](#cfn-quicksight-datasource-mariadbparameters-database)" : {{String}},
  "[Host](#cfn-quicksight-datasource-mariadbparameters-host)" : {{String}},
  "[Port](#cfn-quicksight-datasource-mariadbparameters-port)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-mariadbparameters-syntax.yaml"></a>

```
  [Database](#cfn-quicksight-datasource-mariadbparameters-database): {{String}}
  [Host](#cfn-quicksight-datasource-mariadbparameters-host): {{String}}
  [Port](#cfn-quicksight-datasource-mariadbparameters-port): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-datasource-mariadbparameters-properties"></a>

`Database`  <a name="cfn-quicksight-datasource-mariadbparameters-database"></a>
Database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-mariadbparameters-host"></a>
Host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-mariadbparameters-port"></a>
Port.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
