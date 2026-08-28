---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-prefetchschedule-recurringconsumption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PrefetchSchedule RecurringConsumption
<a name="aws-properties-mediatailor-prefetchschedule-recurringconsumption"></a>

The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.

## Syntax
<a name="aws-properties-mediatailor-prefetchschedule-recurringconsumption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-prefetchschedule-recurringconsumption-syntax.json"></a>

```
{
  "[AvailMatchingCriteria](#cfn-mediatailor-prefetchschedule-recurringconsumption-availmatchingcriteria)" : {{[ AvailMatchingCriteria, ... ]}},
  "[RetrievedAdExpirationSeconds](#cfn-mediatailor-prefetchschedule-recurringconsumption-retrievedadexpirationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-prefetchschedule-recurringconsumption-syntax.yaml"></a>

```
  [AvailMatchingCriteria](#cfn-mediatailor-prefetchschedule-recurringconsumption-availmatchingcriteria): {{
    - AvailMatchingCriteria}}
  [RetrievedAdExpirationSeconds](#cfn-mediatailor-prefetchschedule-recurringconsumption-retrievedadexpirationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-prefetchschedule-recurringconsumption-properties"></a>

`AvailMatchingCriteria`  <a name="cfn-mediatailor-prefetchschedule-recurringconsumption-availmatchingcriteria"></a>
The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.
*Required*: No
*Type*: [Array](aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.md) of [AvailMatchingCriteria](aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetrievedAdExpirationSeconds`  <a name="cfn-mediatailor-prefetchschedule-recurringconsumption-retrievedadexpirationseconds"></a>
The number of seconds that an ad is available for insertion after it was prefetched.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
