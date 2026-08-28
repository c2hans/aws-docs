---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable PopulationAnalysisConfiguration
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration"></a>

Contains the configuration that defines the analysis used to populate an intermediate table.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration-syntax.json"></a>

```
{
  "[SqlParameters](#cfn-cleanrooms-intermediatetable-populationanalysisconfiguration-sqlparameters)" : {{PopulationAnalysisSqlParameters}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration-syntax.yaml"></a>

```
  [SqlParameters](#cfn-cleanrooms-intermediatetable-populationanalysisconfiguration-sqlparameters): {{
    PopulationAnalysisSqlParameters}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-populationanalysisconfiguration-properties"></a>

`SqlParameters`  <a name="cfn-cleanrooms-intermediatetable-populationanalysisconfiguration-sqlparameters"></a>
The SQL parameters for the population analysis, including the query string or analysis template ARN.
*Required*: No
*Type*: [PopulationAnalysisSqlParameters](aws-properties-cleanrooms-intermediatetable-populationanalysissqlparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
