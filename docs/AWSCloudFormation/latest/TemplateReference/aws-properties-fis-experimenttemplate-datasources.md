---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-datasources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate DataSources
<a name="aws-properties-fis-experimenttemplate-datasources"></a>

Describes the data sources for the experiment report.

## Syntax
<a name="aws-properties-fis-experimenttemplate-datasources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-datasources-syntax.json"></a>

```
{
  "[CloudWatchDashboards](#cfn-fis-experimenttemplate-datasources-cloudwatchdashboards)" : {{[ CloudWatchDashboard, ... ]}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-datasources-syntax.yaml"></a>

```
  [CloudWatchDashboards](#cfn-fis-experimenttemplate-datasources-cloudwatchdashboards): {{
    - CloudWatchDashboard}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-datasources-properties"></a>

`CloudWatchDashboards`  <a name="cfn-fis-experimenttemplate-datasources-cloudwatchdashboards"></a>
The CloudWatch dashboards to include as data sources in the experiment report.
*Required*: No
*Type*: Array of [CloudWatchDashboard](aws-properties-fis-experimenttemplate-cloudwatchdashboard.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
