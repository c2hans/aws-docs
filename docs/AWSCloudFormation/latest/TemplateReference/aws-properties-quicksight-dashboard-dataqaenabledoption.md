---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dataqaenabledoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DataQAEnabledOption
<a name="aws-properties-quicksight-dashboard-dataqaenabledoption"></a>

Adds Q&A capabilities to a dashboard. If no topic is linked, Dashboard Q&A uses the data values that are rendered on the dashboard. End users can use Dashboard Q&A to ask for different slices of the data that they see on the dashboard. If a topic is linked, Topic Q&A is enabled.

## Syntax
<a name="aws-properties-quicksight-dashboard-dataqaenabledoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dataqaenabledoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-dashboard-dataqaenabledoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dataqaenabledoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-dashboard-dataqaenabledoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dataqaenabledoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-dashboard-dataqaenabledoption-availabilitystatus"></a>
The status of the Data Q&A option on the dashboard.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
