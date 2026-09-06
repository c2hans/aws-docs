---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Trigger.html
---

# Trigger
<a name="API_Trigger"></a>

Information about a specific trigger.

## Contents
<a name="API_Trigger_Contents"></a>

 ** Actions **   <a name="Glue-Type-Trigger-Actions"></a>
The actions initiated by this trigger.
Type: Array of [Action](API_Action.md) objects
Required: No

 ** Description **   <a name="Glue-Type-Trigger-Description"></a>
A description of this trigger.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EventBatchingCondition **   <a name="Glue-Type-Trigger-EventBatchingCondition"></a>
Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.
Type: [EventBatchingCondition](API_EventBatchingCondition.md) object
Required: No

 ** Id **   <a name="Glue-Type-Trigger-Id"></a>
Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="Glue-Type-Trigger-Name"></a>
The name of the trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Predicate **   <a name="Glue-Type-Trigger-Predicate"></a>
The predicate of this trigger, which defines when it will fire.
Type: [Predicate](API_Predicate.md) object
Required: No

 ** Schedule **   <a name="Glue-Type-Trigger-Schedule"></a>
A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
Type: String
Required: No

 ** State **   <a name="Glue-Type-Trigger-State"></a>
The current state of the trigger.
Type: String
Valid Values: `CREATING | CREATED | ACTIVATING | ACTIVATED | DEACTIVATING | DEACTIVATED | DELETING | UPDATING`
Required: No

 ** Type **   <a name="Glue-Type-Trigger-Type"></a>
The type of trigger that this is.
Type: String
Valid Values: `SCHEDULED | CONDITIONAL | ON_DEMAND | EVENT`
Required: No

 ** WorkflowName **   <a name="Glue-Type-Trigger-WorkflowName"></a>
The name of the workflow associated with the trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Trigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Trigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Trigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Trigger)
