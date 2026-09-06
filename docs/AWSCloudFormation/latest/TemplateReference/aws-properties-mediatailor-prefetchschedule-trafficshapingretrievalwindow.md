---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule TrafficShapingRetrievalWindow
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow"></a>

The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow-syntax.json"></a>

```
{
  "[RetrievalWindowDurationSeconds](#cfn-mediatailor-prefetchschedule-trafficshapingretrievalwindow-retrievalwindowdurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow-syntax.yaml"></a>

```
  [RetrievalWindowDurationSeconds](#cfn-mediatailor-prefetchschedule-trafficshapingretrievalwindow-retrievalwindowdurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow-properties"></a>

`RetrievalWindowDurationSeconds`  <a name="cfn-mediatailor-prefetchschedule-trafficshapingretrievalwindow-retrievalwindowdurationseconds"></a>
The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
