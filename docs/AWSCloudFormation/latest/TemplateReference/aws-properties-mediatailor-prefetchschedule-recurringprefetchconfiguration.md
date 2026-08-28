---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule RecurringPrefetchConfiguration
<a name="aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration"></a>

The configuration that defines how MediaTailor performs recurring prefetch.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration-syntax.json"></a>

```
{
  "[EndTime](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-endtime)" : {{String}},
  "[RecurringConsumption](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringconsumption)" : {{RecurringConsumption}},
  "[RecurringRetrieval](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringretrieval)" : {{RecurringRetrieval}},
  "[StartTime](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration-syntax.yaml"></a>

```
  [EndTime](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-endtime): {{String}}
  [RecurringConsumption](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringconsumption): {{
    RecurringConsumption}}
  [RecurringRetrieval](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringretrieval): {{
    RecurringRetrieval}}
  [StartTime](#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-starttime): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration-properties"></a>

`EndTime`  <a name="cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-endtime"></a>
The end time for the window that MediaTailor prefetches and inserts ads in a live event.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecurringConsumption`  <a name="cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringconsumption"></a>
The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.
*Required*: Yes
*Type*: [RecurringConsumption](aws-properties-mediatailor-prefetchschedule-recurringconsumption.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecurringRetrieval`  <a name="cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringretrieval"></a>
The configuration for prefetch ad retrieval from the ADS.
*Required*: Yes
*Type*: [RecurringRetrieval](aws-properties-mediatailor-prefetchschedule-recurringretrieval.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-starttime"></a>
The start time for the window that MediaTailor prefetches and inserts ads in a live event.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
