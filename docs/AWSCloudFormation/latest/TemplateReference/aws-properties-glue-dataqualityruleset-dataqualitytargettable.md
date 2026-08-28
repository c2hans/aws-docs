---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::DataQualityRuleset DataQualityTargetTable
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable"></a>

An object representing an AWS Glue table.

## Syntax
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename)" : {{String}},
  "[TableName](#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax.yaml"></a>

```
  [DatabaseName](#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename): {{String}}
  [TableName](#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename): {{String}}
```

## Properties
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-properties"></a>

`DatabaseName`  <a name="cfn-glue-dataqualityruleset-dataqualitytargettable-databasename"></a>
The name of the database where the AWS Glue table exists.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-glue-dataqualityruleset-dataqualitytargettable-tablename"></a>
The name of the AWS Glue table.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
