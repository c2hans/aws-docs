---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-rdsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource RdsParameters
<a name="aws-properties-quicksight-datasource-rdsparameters"></a>

The parameters for Amazon RDS.

## Syntax
<a name="aws-properties-quicksight-datasource-rdsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-rdsparameters-syntax.json"></a>

```
{
  "[Database](#cfn-quicksight-datasource-rdsparameters-database)" : {{String}},
  "[InstanceId](#cfn-quicksight-datasource-rdsparameters-instanceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-rdsparameters-syntax.yaml"></a>

```
  [Database](#cfn-quicksight-datasource-rdsparameters-database): {{String}}
  [InstanceId](#cfn-quicksight-datasource-rdsparameters-instanceid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-rdsparameters-properties"></a>

`Database`  <a name="cfn-quicksight-datasource-rdsparameters-database"></a>
Database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceId`  <a name="cfn-quicksight-datasource-rdsparameters-instanceid"></a>
Instance ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
