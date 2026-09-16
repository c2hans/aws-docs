---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListTaskInstances.html
---

# ListTaskInstances
<a name="API_ListTaskInstances"></a>

Lists all task instances for a specific workflow run, with optional pagination support.

## Request Syntax
<a name="API_ListTaskInstances_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RunId": "{{string}}",
   "WorkflowArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTaskInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTaskInstances_RequestSyntax) **   <a name="mwaaserverless-ListTaskInstances-request-MaxResults"></a>
The maximum number of task instances to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTaskInstances_RequestSyntax) **   <a name="mwaaserverless-ListTaskInstances-request-NextToken"></a>
The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to `ListTaskInstances`.
Type: String
Required: No

 ** [RunId](#API_ListTaskInstances_RequestSyntax) **   <a name="mwaaserverless-ListTaskInstances-request-RunId"></a>
The unique identifier of the workflow run for which you want a list of task instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [WorkflowArn](#API_ListTaskInstances_RequestSyntax) **   <a name="mwaaserverless-ListTaskInstances-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

## Response Syntax
<a name="API_ListTaskInstances_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskInstances": [
      {
         "DurationInSeconds": number,
         "OperatorName": "string",
         "RunId": "string",
         "Status": "string",
         "TaskInstanceId": "string",
         "WorkflowArn": "string",
         "WorkflowVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTaskInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTaskInstances_ResponseSyntax) **   <a name="mwaaserverless-ListTaskInstances-response-NextToken"></a>
The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.
Type: String

 ** [TaskInstances](#API_ListTaskInstances_ResponseSyntax) **   <a name="mwaaserverless-ListTaskInstances-response-TaskInstances"></a>
A list of task instance summaries for the specified workflow run.
Type: Array of [TaskInstanceSummary](API_TaskInstanceSummary.md) objects

## Errors
<a name="API_ListTaskInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An unexpected server-side error occurred during request processing.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.
 ** QuotaCode **
The code of the quota.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the operation.
 ** ServiceCode **
The code for the service.
HTTP Status Code: 400

 ** ValidationException **
The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.
 ** FieldList **
The fields that failed validation.
 ** Reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListTaskInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/ListTaskInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/ListTaskInstances)
