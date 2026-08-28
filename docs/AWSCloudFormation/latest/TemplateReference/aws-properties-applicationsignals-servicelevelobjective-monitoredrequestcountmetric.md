---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective MonitoredRequestCountMetric
<a name="aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric"></a>

This structure defines the metric that is used as the "good request" or "bad request" value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` is divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-syntax.json"></a>

```
{
  "[BadCountMetric](#cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-badcountmetric)" : {{[ MetricDataQuery, ... ]}},
  "[GoodCountMetric](#cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-goodcountmetric)" : {{[ MetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-syntax.yaml"></a>

```
  [BadCountMetric](#cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-badcountmetric): {{
    - MetricDataQuery}}
  [GoodCountMetric](#cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-goodcountmetric): {{
    - MetricDataQuery}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-properties"></a>

`BadCountMetric`  <a name="cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-badcountmetric"></a>
If you want to count "bad requests" to determine the percentage of successful requests for this request-based SLO, specify the metric to use as "bad requests" in this structure.
*Required*: No
*Type*: Array of [MetricDataQuery](aws-properties-applicationsignals-servicelevelobjective-metricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoodCountMetric`  <a name="cfn-applicationsignals-servicelevelobjective-monitoredrequestcountmetric-goodcountmetric"></a>
If you want to count "good requests" to determine the percentage of successful requests for this request-based SLO, specify the metric to use as "good requests" in this structure.
*Required*: No
*Type*: Array of [MetricDataQuery](aws-properties-applicationsignals-servicelevelobjective-metricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
