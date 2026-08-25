---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-prefetchconsumption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule PrefetchConsumption
<a name="aws-properties-mediatailor-prefetchschedule-prefetchconsumption"></a>

For single prefetch, describes how and when that MediaTailor places prefetched ads into upcoming ad breaks.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-prefetchconsumption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-prefetchconsumption-syntax.json"></a>

```
{
  "[AvailMatchingCriteria](#cfn-mediatailor-prefetchschedule-prefetchconsumption-availmatchingcriteria)" : {{[ AvailMatchingCriteria, ... ]}},
  "[EndTime](#cfn-mediatailor-prefetchschedule-prefetchconsumption-endtime)" : {{String}},
  "[StartTime](#cfn-mediatailor-prefetchschedule-prefetchconsumption-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-prefetchconsumption-syntax.yaml"></a>

```
  [AvailMatchingCriteria](#cfn-mediatailor-prefetchschedule-prefetchconsumption-availmatchingcriteria): {{
    - AvailMatchingCriteria}}
  [EndTime](#cfn-mediatailor-prefetchschedule-prefetchconsumption-endtime): {{String}}
  [StartTime](#cfn-mediatailor-prefetchschedule-prefetchconsumption-starttime): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-prefetchconsumption-properties"></a>

`AvailMatchingCriteria`  <a name="cfn-mediatailor-prefetchschedule-prefetchconsumption-availmatchingcriteria"></a>
If you only want MediaTailor to insert prefetched ads into avails (ad breaks) that match specific dynamic variables, such as `scte.event_id`, set the avail matching criteria.
*Required*: No
*Type*: [Array](aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.md) of [AvailMatchingCriteria](aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndTime`  <a name="cfn-mediatailor-prefetchschedule-prefetchconsumption-endtime"></a>
The time when MediaTailor no longer considers the prefetched ads for use in an ad break. MediaTailor automatically deletes prefetch schedules no less than seven days after the end time. If you'd like to manually delete the prefetch schedule, you can call `DeletePrefetchSchedule`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-mediatailor-prefetchschedule-prefetchconsumption-starttime"></a>
The time when prefetched ads are considered for use in an ad break. If you don't specify `StartTime`, the prefetched ads are available after MediaTailor retrieves them from the ad decision server.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
