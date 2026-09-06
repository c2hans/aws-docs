---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TriggerUpdate.html
---

# TriggerUpdate
<a name="API_TriggerUpdate"></a>

A structure used to provide information used to update a trigger. This object updates the previous trigger definition by overwriting it completely.

## Contents
<a name="API_TriggerUpdate_Contents"></a>

 ** Actions **   <a name="Glue-Type-TriggerUpdate-Actions"></a>
The actions initiated by this trigger.
Type: Array of [Action](API_Action.md) objects
Required: No

 ** Description **   <a name="Glue-Type-TriggerUpdate-Description"></a>
A description of this trigger.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EventBatchingCondition **   <a name="Glue-Type-TriggerUpdate-EventBatchingCondition"></a>
Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.
Type: [EventBatchingCondition](API_EventBatchingCondition.md) object
Required: No

 ** Name **   <a name="Glue-Type-TriggerUpdate-Name"></a>
Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Predicate **   <a name="Glue-Type-TriggerUpdate-Predicate"></a>
The predicate of this trigger, which defines when it will fire.
Type: [Predicate](API_Predicate.md) object
Required: No

 ** Schedule **   <a name="Glue-Type-TriggerUpdate-Schedule"></a>
A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
Type: String
Required: No

## See Also
<a name="API_TriggerUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TriggerUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TriggerUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TriggerUpdate)
