---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateTrigger.html
---

# UpdateTrigger
<a name="API_UpdateTrigger"></a>

Updates a trigger definition.

Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

## Request Syntax
<a name="API_UpdateTrigger_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "TriggerUpdate": {
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
      "Schedule": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateTrigger_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateTrigger_RequestSyntax) **   <a name="Glue-UpdateTrigger-request-Name"></a>
The name of the trigger to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TriggerUpdate](#API_UpdateTrigger_RequestSyntax) **   <a name="Glue-UpdateTrigger-request-TriggerUpdate"></a>
The new values with which to update the trigger.
Type: [TriggerUpdate](API_TriggerUpdate.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateTrigger_ResponseSyntax"></a>

```
{
   "Trigger": {
      "Actions": [
         {
            "Arguments": {
               "string" : "string"
            },
            "CrawlerName": "string",
            "JobName": "string",
            "NotificationProperty": {
               "NotifyDelayAfter": number
            },
            "SecurityConfiguration": "string",
            "Timeout": number
         }
      ],
      "Description": "string",
      "EventBatchingCondition": {
         "BatchSize": number,
         "BatchWindow": number
      },
      "Id": "string",
      "Name": "string",
      "Predicate": {
         "Conditions": [
            {
               "CrawlerName": "string",
               "CrawlState": "string",
               "JobName": "string",
               "LogicalOperator": "string",
               "State": "string"
            }
         ],
         "Logical": "string"
      },
      "Schedule": "string",
      "State": "string",
      "Type": "string",
      "WorkflowName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateTrigger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Trigger](#API_UpdateTrigger_ResponseSyntax) **   <a name="Glue-UpdateTrigger-response-Trigger"></a>
The resulting trigger definition.
Type: [Trigger](API_Trigger.md) object

## Errors
<a name="API_UpdateTrigger_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_UpdateTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateTrigger)
