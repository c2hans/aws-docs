---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetJobRun.html
---

# GetJobRun
<a name="API_GetJobRun"></a>

Retrieves the metadata for a given job run. Job run history is accessible for 365 days for your workflow and job run.

## Request Syntax
<a name="API_GetJobRun_RequestSyntax"></a>

```
{
   "JobName": "{{string}}",
   "PredecessorsIncluded": {{boolean}},
   "RunId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetJobRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_GetJobRun_RequestSyntax) **   <a name="Glue-GetJobRun-request-JobName"></a>
Name of the job definition being run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PredecessorsIncluded](#API_GetJobRun_RequestSyntax) **   <a name="Glue-GetJobRun-request-PredecessorsIncluded"></a>
True if a list of predecessor runs should be returned.
Type: Boolean
Required: No

 ** [RunId](#API_GetJobRun_RequestSyntax) **   <a name="Glue-GetJobRun-request-RunId"></a>
The ID of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetJobRun_ResponseSyntax"></a>

```
{
   "JobRun": {
      "AllocatedCapacity": number,
      "Arguments": {
         "string" : "string"
      },
      "Attempt": number,
      "CompletedOn": number,
      "DPUSeconds": number,
      "ErrorMessage": "string",
      "ExecutionClass": "string",
      "ExecutionRoleSessionPolicy": "string",
      "ExecutionTime": number,
      "GlueVersion": "string",
      "Id": "string",
      "JobMode": "string",
      "JobName": "string",
      "JobRunQueuingEnabled": boolean,
      "JobRunState": "string",
      "LastModifiedOn": number,
      "LogGroupName": "string",
      "MaintenanceWindow": "string",
      "MaxCapacity": number,
      "NotificationProperty": {
         "NotifyDelayAfter": number
      },
      "NumberOfWorkers": number,
      "PredecessorRuns": [
         {
            "JobName": "string",
            "RunId": "string"
         }
      ],
      "PreviousRunId": "string",
      "ProfileName": "string",
      "SecurityConfiguration": "string",
      "StartedOn": number,
      "StateDetail": "string",
      "Timeout": number,
      "TriggerName": "string",
      "WorkerType": "string"
   }
}
```

## Response Elements
<a name="API_GetJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobRun](#API_GetJobRun_ResponseSyntax) **   <a name="Glue-GetJobRun-response-JobRun"></a>
The requested job-run metadata.
Type: [JobRun](API_JobRun.md) object

## Errors
<a name="API_GetJobRun_Errors"></a>

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
<a name="API_GetJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetJobRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
