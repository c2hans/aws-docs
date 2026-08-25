---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule TrafficShapingTpsConfiguration
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration"></a>

The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-syntax.json"></a>

```
{
  "[PeakConcurrentUsers](#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peakconcurrentusers)" : {{Integer}},
  "[PeakTps](#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peaktps)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-syntax.yaml"></a>

```
  [PeakConcurrentUsers](#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peakconcurrentusers): {{Integer}}
  [PeakTps](#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peaktps): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-properties"></a>

`PeakConcurrentUsers`  <a name="cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peakconcurrentusers"></a>
The expected peak number of concurrent viewers for your content. MediaTailor uses this value along with peak TPS to determine how to distribute prefetch requests across the available capacity without exceeding your ADS limits.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeakTps`  <a name="cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peaktps"></a>
The maximum number of transactions per second (TPS) that your ad decision server (ADS) can handle. MediaTailor uses this value along with concurrent users and headroom multiplier to calculate optimal traffic distribution and prevent ADS overload.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
