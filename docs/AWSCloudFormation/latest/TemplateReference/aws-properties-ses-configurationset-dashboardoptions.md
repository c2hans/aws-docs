---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-dashboardoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet DashboardOptions
<a name="aws-properties-ses-configurationset-dashboardoptions"></a>

An object containing additional settings for your VDM configuration as applicable to the Dashboard.

## Syntax
<a name="aws-properties-ses-configurationset-dashboardoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-dashboardoptions-syntax.json"></a>

```
{
  "[EngagementMetrics](#cfn-ses-configurationset-dashboardoptions-engagementmetrics)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-dashboardoptions-syntax.yaml"></a>

```
  [EngagementMetrics](#cfn-ses-configurationset-dashboardoptions-engagementmetrics): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationset-dashboardoptions-properties"></a>

`EngagementMetrics`  <a name="cfn-ses-configurationset-dashboardoptions-engagementmetrics"></a>
Specifies the status of your VDM engagement metrics collection. Can be one of the following:
+ `ENABLED` – Amazon SES enables engagement metrics for the configuration set.
+ `DISABLED` – Amazon SES disables engagement metrics for the configuration set.
*Required*: Yes
*Type*: String
*Pattern*: `ENABLED|DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
