---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable PopulationAnalysisSqlParameters
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters"></a>

Contains the SQL parameters used to populate an intermediate table.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters-syntax.json"></a>

```
{
  "[AnalysisTemplateArn](#cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-analysistemplatearn)" : {{String}},
  "[QueryString](#cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-querystring)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters-syntax.yaml"></a>

```
  [AnalysisTemplateArn](#cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-analysistemplatearn): {{String}}
  [QueryString](#cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-querystring): {{
    String}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters-properties"></a>

`AnalysisTemplateArn`  <a name="cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-analysistemplatearn"></a>
The Amazon Resource Name (ARN) of the analysis template to use for populating the intermediate table.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryString`  <a name="cfn-cleanrooms-intermediatetable-populationanalysissqlparameters-querystring"></a>
The SQL query string used to populate the intermediate table.
*Required*: No
*Type*: String
*Maximum*: `500000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
