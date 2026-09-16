---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetTriggers.html
---

# GetTriggers
<a name="API_GetTriggers"></a>

Gets all the triggers associated with a job.

## Request Syntax
<a name="API_GetTriggers_RequestSyntax"></a>

```
{
   "DependentJobName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTriggers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DependentJobName](#API_GetTriggers_RequestSyntax) **   <a name="Glue-GetTriggers-request-DependentJobName"></a>
The name of the job to retrieve triggers for. The trigger that can start this job is returned, and if there is no such trigger, all triggers are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_GetTriggers_RequestSyntax) **   <a name="Glue-GetTriggers-request-MaxResults"></a>
The maximum size of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_GetTriggers_RequestSyntax) **   <a name="Glue-GetTriggers-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetTriggers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Triggers": [
      {
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
   ]
}
```

## Response Elements
<a name="API_GetTriggers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetTriggers_ResponseSyntax) **   <a name="Glue-GetTriggers-response-NextToken"></a>
A continuation token, if not all the requested triggers have yet been returned.
Type: String

 ** [Triggers](#API_GetTriggers_ResponseSyntax) **   <a name="Glue-GetTriggers-response-Triggers"></a>
A list of triggers for the specified job.
Type: Array of [Trigger](API_Trigger.md) objects

## Errors
<a name="API_GetTriggers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetTriggers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetTriggers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetTriggers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetTriggers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetTriggers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetTriggers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetTriggers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetTriggers)
