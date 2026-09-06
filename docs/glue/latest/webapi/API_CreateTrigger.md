---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateTrigger.html
---

# CreateTrigger
<a name="API_CreateTrigger"></a>

Creates a new trigger.

Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

## Request Syntax
<a name="API_CreateTrigger_RequestSyntax"></a>

```
{
   "Actions": [
      {
         "Arguments": {
            "{{string}}" : "{{string}}"
         },
         "CrawlerName": "{{string}}",
         "JobName": "{{string}}",
         "NotificationProperty": {
            "NotifyDelayAfter": {{number}}
         },
         "SecurityConfiguration": "{{string}}",
         "Timeout": {{number}}
      }
   ],
   "Description": "{{string}}",
   "EventBatchingCondition": {
      "BatchSize": {{number}},
      "BatchWindow": {{number}}
   },
   "Name": "{{string}}",
   "Predicate": {
      "Conditions": [
         {
            "CrawlerName": "{{string}}",
            "CrawlState": "{{string}}",
            "JobName": "{{string}}",
            "LogicalOperator": "{{string}}",
            "State": "{{string}}"
         }
      ],
      "Logical": "{{string}}"
   },
   "Schedule": "{{string}}",
   "StartOnCreation": {{boolean}},
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Type": "{{string}}",
   "WorkflowName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrigger_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Actions"></a>
The actions initiated by this trigger when it fires.
Type: Array of [Action](API_Action.md) objects
Required: Yes

 ** [Description](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Description"></a>
A description of the new trigger.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [EventBatchingCondition](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-EventBatchingCondition"></a>
Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.
Type: [EventBatchingCondition](API_EventBatchingCondition.md) object
Required: No

 ** [Name](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Name"></a>
The name of the trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Predicate](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Predicate"></a>
A predicate to specify when the new trigger should fire.
This field is required when the trigger type is `CONDITIONAL`.
Type: [Predicate](API_Predicate.md) object
Required: No

 ** [Schedule](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Schedule"></a>
A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
This field is required when the trigger type is SCHEDULED.
Type: String
Required: No

 ** [StartOnCreation](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-StartOnCreation"></a>
Set to `true` to start `SCHEDULED` and `CONDITIONAL` triggers when created. True is not supported for `ON_DEMAND` triggers.
Type: Boolean
Required: No

 ** [Tags](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Tags"></a>
The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Type](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-Type"></a>
The type of the new trigger.
Type: String
Valid Values: `SCHEDULED | CONDITIONAL | ON_DEMAND | EVENT`
Required: Yes

 ** [WorkflowName](#API_CreateTrigger_RequestSyntax) **   <a name="Glue-CreateTrigger-request-WorkflowName"></a>
The name of the workflow associated with the trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_CreateTrigger_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateTrigger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateTrigger_ResponseSyntax) **   <a name="Glue-CreateTrigger-response-Name"></a>
The name of the trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateTrigger_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateTrigger)
