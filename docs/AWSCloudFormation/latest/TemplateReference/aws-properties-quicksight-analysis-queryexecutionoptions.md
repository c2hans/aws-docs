---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-queryexecutionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis QueryExecutionOptions
<a name="aws-properties-quicksight-analysis-queryexecutionoptions"></a>

A structure that describes the query execution options.

## Syntax
<a name="aws-properties-quicksight-analysis-queryexecutionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-queryexecutionoptions-syntax.json"></a>

```
{
  "[QueryExecutionMode](#cfn-quicksight-analysis-queryexecutionoptions-queryexecutionmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-queryexecutionoptions-syntax.yaml"></a>

```
  [QueryExecutionMode](#cfn-quicksight-analysis-queryexecutionoptions-queryexecutionmode): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-queryexecutionoptions-properties"></a>

`QueryExecutionMode`  <a name="cfn-quicksight-analysis-queryexecutionoptions-queryexecutionmode"></a>
A structure that describes the query execution mode.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
