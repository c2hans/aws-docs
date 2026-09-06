---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-eventdatastore-insightselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::EventDataStore InsightSelector
<a name="aws-properties-cloudtrail-eventdatastore-insightselector"></a>

A JSON string that contains a list of Insights types that are logged on an event data store.

## Syntax
<a name="aws-properties-cloudtrail-eventdatastore-insightselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-eventdatastore-insightselector-syntax.json"></a>

```
{
  "[InsightType](#cfn-cloudtrail-eventdatastore-insightselector-insighttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-eventdatastore-insightselector-syntax.yaml"></a>

```
  [InsightType](#cfn-cloudtrail-eventdatastore-insightselector-insighttype): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-eventdatastore-insightselector-properties"></a>

`InsightType`  <a name="cfn-cloudtrail-eventdatastore-insightselector-insighttype"></a>
The type of Insights events to log on an event data store. `ApiCallRateInsight` and `ApiErrorRateInsight` are valid Insight types.
The `ApiCallRateInsight` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.
The `ApiErrorRateInsight` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
*Required*: No
*Type*: String
*Allowed values*: `ApiCallRateInsight | ApiErrorRateInsight`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
