---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetTriggers.html
---

# BatchGetTriggers
<a name="API_BatchGetTriggers"></a>

Returns a list of resource metadata for a given list of trigger names. After calling the `ListTriggers` operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.

## Request Syntax
<a name="API_BatchGetTriggers_RequestSyntax"></a>

```
{
   "TriggerNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetTriggers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TriggerNames](#API_BatchGetTriggers_RequestSyntax) **   <a name="Glue-BatchGetTriggers-request-TriggerNames"></a>
A list of trigger names, which may be the names returned from the `ListTriggers` operation.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetTriggers_ResponseSyntax"></a>

```
{
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
   ],
   "TriggersNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetTriggers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Triggers](#API_BatchGetTriggers_ResponseSyntax) **   <a name="Glue-BatchGetTriggers-response-Triggers"></a>
A list of trigger definitions.
Type: Array of [Trigger](API_Trigger.md) objects

 ** [TriggersNotFound](#API_BatchGetTriggers_ResponseSyntax) **   <a name="Glue-BatchGetTriggers-response-TriggersNotFound"></a>
A list of names of triggers not found.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetTriggers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchGetTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetTriggers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
