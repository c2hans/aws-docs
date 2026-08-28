---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-sparkparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource SparkParameters
<a name="aws-properties-quicksight-datasource-sparkparameters"></a>

The parameters for Spark.

## Syntax
<a name="aws-properties-quicksight-datasource-sparkparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-sparkparameters-syntax.json"></a>

```
{
  "[Host](#cfn-quicksight-datasource-sparkparameters-host)" : {{String}},
  "[Port](#cfn-quicksight-datasource-sparkparameters-port)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-sparkparameters-syntax.yaml"></a>

```
  [Host](#cfn-quicksight-datasource-sparkparameters-host): {{String}}
  [Port](#cfn-quicksight-datasource-sparkparameters-port): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-datasource-sparkparameters-properties"></a>

`Host`  <a name="cfn-quicksight-datasource-sparkparameters-host"></a>
Host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-sparkparameters-port"></a>
Port.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
