---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-trail-insightselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Trail InsightSelector
<a name="aws-properties-cloudtrail-trail-insightselector"></a>

A JSON string that contains a list of Insights types that are logged on a trail.

## Syntax
<a name="aws-properties-cloudtrail-trail-insightselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-trail-insightselector-syntax.json"></a>

```
{
  "[EventCategories](#cfn-cloudtrail-trail-insightselector-eventcategories)" : {{[ String, ... ]}},
  "[InsightType](#cfn-cloudtrail-trail-insightselector-insighttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-trail-insightselector-syntax.yaml"></a>

```
  [EventCategories](#cfn-cloudtrail-trail-insightselector-eventcategories): {{
    - String}}
  [InsightType](#cfn-cloudtrail-trail-insightselector-insighttype): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-trail-insightselector-properties"></a>

`EventCategories`  <a name="cfn-cloudtrail-trail-insightselector-eventcategories"></a>
Select the event category on which Insights should be enabled.
+ If EventCategories is not provided, the specified Insights types are enabled on management API calls by default.
+ If EventCategories is provided, the given event categories will overwrite the existing ones. For example, if a trail already has Insights enabled on management events, and then a PutInsightSelectors request is made with only data events specified in EventCategories, Insights on management events will be disabled.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsightType`  <a name="cfn-cloudtrail-trail-insightselector-insighttype"></a>
The type of Insights events to log on a trail. `ApiCallRateInsight` and `ApiErrorRateInsight` are valid Insight types.
The `ApiCallRateInsight` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.
The `ApiErrorRateInsight` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
*Required*: No
*Type*: String
*Allowed values*: `ApiCallRateInsight | ApiErrorRateInsight`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
