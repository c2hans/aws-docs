---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule PrefetchRetrieval
<a name="aws-properties-mediatailor-prefetchschedule-prefetchretrieval"></a>

A complex type that contains settings governing when MediaTailor prefetches ads, and which dynamic variables that MediaTailor includes in the request to the ad decision server.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-prefetchretrieval-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-prefetchretrieval-syntax.json"></a>

```
{
  "[DynamicVariables](#cfn-mediatailor-prefetchschedule-prefetchretrieval-dynamicvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[EndTime](#cfn-mediatailor-prefetchschedule-prefetchretrieval-endtime)" : {{String}},
  "[StartTime](#cfn-mediatailor-prefetchschedule-prefetchretrieval-starttime)" : {{String}},
  "[TrafficShapingRetrievalWindow](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingretrievalwindow)" : {{TrafficShapingRetrievalWindow}},
  "[TrafficShapingTpsConfiguration](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtpsconfiguration)" : {{TrafficShapingTpsConfiguration}},
  "[TrafficShapingType](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-prefetchretrieval-syntax.yaml"></a>

```
  [DynamicVariables](#cfn-mediatailor-prefetchschedule-prefetchretrieval-dynamicvariables): {{
    {{Key}}: {{Value}}}}
  [EndTime](#cfn-mediatailor-prefetchschedule-prefetchretrieval-endtime): {{String}}
  [StartTime](#cfn-mediatailor-prefetchschedule-prefetchretrieval-starttime): {{String}}
  [TrafficShapingRetrievalWindow](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingretrievalwindow): {{
    TrafficShapingRetrievalWindow}}
  [TrafficShapingTpsConfiguration](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtpsconfiguration): {{
    TrafficShapingTpsConfiguration}}
  [TrafficShapingType](#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtype): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-prefetchretrieval-properties"></a>

`DynamicVariables`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-dynamicvariables"></a>
The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).
You initially configure [dynamic variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) for the ADS URL when you set up your playback configuration. When you specify `DynamicVariables` for prefetch retrieval, MediaTailor includes the dynamic variables in the request to the ADS.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndTime`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-endtime"></a>
The time when prefetch retrieval ends for the ad break. Prefetching will be attempted for manifest requests that occur at or before this time.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-starttime"></a>
The time when prefetch retrievals can start for this break. Ad prefetching will be attempted for manifest requests that occur at or after this time. Defaults to the current time. If not specified, the prefetch retrieval starts as soon as possible.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingRetrievalWindow`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingretrievalwindow"></a>
The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.
*Required*: No
*Type*: [TrafficShapingRetrievalWindow](aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingTpsConfiguration`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtpsconfiguration"></a>
The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.
*Required*: No
*Type*: [TrafficShapingTpsConfiguration](aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficShapingType`  <a name="cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtype"></a>
Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.
*Required*: No
*Type*: String
*Allowed values*: `RETRIEVAL_WINDOW | TPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
