---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-cloudwatchdashboard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate CloudWatchDashboard
<a name="aws-properties-fis-experimenttemplate-cloudwatchdashboard"></a>

The CloudWatch dashboards to include as data sources in the experiment report.

## Syntax
<a name="aws-properties-fis-experimenttemplate-cloudwatchdashboard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-cloudwatchdashboard-syntax.json"></a>

```
{
  "[DashboardIdentifier](#cfn-fis-experimenttemplate-cloudwatchdashboard-dashboardidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-cloudwatchdashboard-syntax.yaml"></a>

```
  [DashboardIdentifier](#cfn-fis-experimenttemplate-cloudwatchdashboard-dashboardidentifier): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-cloudwatchdashboard-properties"></a>

`DashboardIdentifier`  <a name="cfn-fis-experimenttemplate-cloudwatchdashboard-dashboardidentifier"></a>
The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
