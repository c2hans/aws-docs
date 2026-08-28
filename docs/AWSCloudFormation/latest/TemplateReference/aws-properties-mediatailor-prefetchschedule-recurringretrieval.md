---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule RecurringRetrieval
<a name="aws-properties-mediatailor-prefetchschedule-recurringretrieval"></a>

With recurring prefetch, MediaTailor automatically prefetches ads for every avail that occurs during the retrieval window. The following configurations describe the MediaTailor behavior when prefetching ads for a live event.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-recurringretrieval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-recurringretrieval-syntax.json"></a>

```
{
  "[DelayAfterAvailEndSeconds](#cfn-mediatailor-prefetchschedule-recurringretrieval-delayafteravailendseconds)" : {{Integer}},
  "[DynamicVariables](#cfn-mediatailor-prefetchschedule-recurringretrieval-dynamicvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TrafficShapingRetrievalWindow](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingretrievalwindow)" : {{TrafficShapingRetrievalWindow}},
  "[TrafficShapingTpsConfiguration](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtpsconfiguration)" : {{TrafficShapingTpsConfiguration}},
  "[TrafficShapingType](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-recurringretrieval-syntax.yaml"></a>

```
  [DelayAfterAvailEndSeconds](#cfn-mediatailor-prefetchschedule-recurringretrieval-delayafteravailendseconds): {{Integer}}
  [DynamicVariables](#cfn-mediatailor-prefetchschedule-recurringretrieval-dynamicvariables): {{
    {{Key}}: {{Value}}}}
  [TrafficShapingRetrievalWindow](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingretrievalwindow): {{
    TrafficShapingRetrievalWindow}}
  [TrafficShapingTpsConfiguration](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtpsconfiguration): {{
    TrafficShapingTpsConfiguration}}
  [TrafficShapingType](#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtype): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-recurringretrieval-properties"></a>

`DelayAfterAvailEndSeconds`  <a name="cfn-mediatailor-prefetchschedule-recurringretrieval-delayafteravailendseconds"></a>
The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail. If not set, the default is 0 (no delay).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DynamicVariables`  <a name="cfn-mediatailor-prefetchschedule-recurringretrieval-dynamicvariables"></a>
The dynamic variables to use for substitution during prefetch requests to the ADS.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingRetrievalWindow`  <a name="cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingretrievalwindow"></a>
The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.
*Required*: No
*Type*: [TrafficShapingRetrievalWindow](aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingTpsConfiguration`  <a name="cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtpsconfiguration"></a>
The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.
*Required*: No
*Type*: [TrafficShapingTpsConfiguration](aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingType`  <a name="cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtype"></a>
Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.
*Required*: No
*Type*: String
*Allowed values*: `RETRIEVAL_WINDOW | TPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
