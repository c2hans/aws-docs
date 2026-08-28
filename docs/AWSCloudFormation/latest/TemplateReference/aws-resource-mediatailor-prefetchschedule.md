---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-prefetchschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule
<a name="aws-resource-mediatailor-prefetchschedule"></a>

A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-resource-mediatailor-prefetchschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-prefetchschedule-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::PrefetchSchedule",
  "Properties" : {
      "[Consumption](#cfn-mediatailor-prefetchschedule-consumption)" : {{PrefetchConsumption}},
      "[Name](#cfn-mediatailor-prefetchschedule-name)" : {{String}},
      "[PlaybackConfigurationName](#cfn-mediatailor-prefetchschedule-playbackconfigurationname)" : {{String}},
      "[RecurringPrefetchConfiguration](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration)" : {{RecurringPrefetchConfiguration}},
      "[Retrieval](#cfn-mediatailor-prefetchschedule-retrieval)" : {{PrefetchRetrieval}},
      "[ScheduleType](#cfn-mediatailor-prefetchschedule-scheduletype)" : {{String}},
      "[StreamId](#cfn-mediatailor-prefetchschedule-streamid)" : {{String}},
      "[Tags](#cfn-mediatailor-prefetchschedule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-prefetchschedule-syntax.yaml"></a>

```
Type: AWS::MediaTailor::PrefetchSchedule
Properties:
  [Consumption](#cfn-mediatailor-prefetchschedule-consumption): {{
    PrefetchConsumption}}
  [Name](#cfn-mediatailor-prefetchschedule-name): {{String}}
  [PlaybackConfigurationName](#cfn-mediatailor-prefetchschedule-playbackconfigurationname): {{String}}
  [RecurringPrefetchConfiguration](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration): {{
    RecurringPrefetchConfiguration}}
  [Retrieval](#cfn-mediatailor-prefetchschedule-retrieval): {{
    PrefetchRetrieval}}
  [ScheduleType](#cfn-mediatailor-prefetchschedule-scheduletype): {{String}}
  [StreamId](#cfn-mediatailor-prefetchschedule-streamid): {{String}}
  [Tags](#cfn-mediatailor-prefetchschedule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediatailor-prefetchschedule-properties"></a>

`Consumption`  <a name="cfn-mediatailor-prefetchschedule-consumption"></a>
Consumption settings determine how, and when, MediaTailor places the prefetched ads into ad breaks for single prefetch schedules. Ad consumption occurs within a span of time that you define, called a *consumption window*. You can designate which ad breaks that MediaTailor fills with prefetch ads by setting avail matching criteria.
*Required*: No
*Type*: [PrefetchConsumption](aws-properties-mediatailor-prefetchschedule-prefetchconsumption.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-mediatailor-prefetchschedule-name"></a>
The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlaybackConfigurationName`  <a name="cfn-mediatailor-prefetchschedule-playbackconfigurationname"></a>
The name of the playback configuration to create the prefetch schedule for.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecurringPrefetchConfiguration`  <a name="cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration"></a>
The settings that determine how and when MediaTailor prefetches ads and inserts them into ad breaks.
*Required*: No
*Type*: [RecurringPrefetchConfiguration](aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Retrieval`  <a name="cfn-mediatailor-prefetchschedule-retrieval"></a>
A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).
*Required*: No
*Type*: [PrefetchRetrieval](aws-properties-mediatailor-prefetchschedule-prefetchretrieval.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScheduleType`  <a name="cfn-mediatailor-prefetchschedule-scheduletype"></a>
The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.
For more information about the prefetch types and when you might use each, see [Prefetching ads in AWS Elemental MediaTailor.](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html)
*Required*: No
*Type*: String
*Allowed values*: `SINGLE | RECURRING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamId`  <a name="cfn-mediatailor-prefetchschedule-streamid"></a>
An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediatailor-prefetchschedule-tags"></a>
The tags assigned to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediatailor-prefetchschedule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediatailor-prefetchschedule-return-values"></a>

### Ref
<a name="aws-resource-mediatailor-prefetchschedule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediatailor-prefetchschedule-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediatailor-prefetchschedule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the prefetch schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
