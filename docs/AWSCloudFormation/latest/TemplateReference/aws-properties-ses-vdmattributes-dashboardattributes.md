---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-vdmattributes-dashboardattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::VdmAttributes DashboardAttributes
<a name="aws-properties-ses-vdmattributes-dashboardattributes"></a>

An object containing additional settings for your VDM configuration as applicable to the Dashboard.

## Syntax
<a name="aws-properties-ses-vdmattributes-dashboardattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-vdmattributes-dashboardattributes-syntax.json"></a>

```
{
  "[EngagementMetrics](#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-vdmattributes-dashboardattributes-syntax.yaml"></a>

```
  [EngagementMetrics](#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics): {{String}}
```

## Properties
<a name="aws-properties-ses-vdmattributes-dashboardattributes-properties"></a>

`EngagementMetrics`  <a name="cfn-ses-vdmattributes-dashboardattributes-engagementmetrics"></a>
Specifies the status of your VDM engagement metrics collection. Can be one of the following:
+ `ENABLED` – Amazon SES enables engagement metrics for your account.
+ `DISABLED` – Amazon SES disables engagement metrics for your account.
*Required*: No
*Type*: String
*Pattern*: `ENABLED|DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
