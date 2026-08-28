---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflowRuns.html
---

# ListWorkflowRuns
<a name="API_ListWorkflowRuns"></a>

Lists all runs for a specified workflow, with optional pagination and filtering support.

## Request Syntax
<a name="API_ListWorkflowRuns_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "WorkflowArn": "{{string}}",
   "WorkflowVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWorkflowRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListWorkflowRuns_RequestSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-request-MaxResults"></a>
The maximum number of workflow runs to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListWorkflowRuns_RequestSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-request-NextToken"></a>
The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to `ListWorkflowRuns`.
Type: String
Required: No

 ** [WorkflowArn](#API_ListWorkflowRuns_RequestSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-request-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

 ** [WorkflowVersion](#API_ListWorkflowRuns_RequestSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-request-WorkflowVersion"></a>
Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_ListWorkflowRuns_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WorkflowRuns": [
      {
         "RunDetailSummary": {
            "CreatedOn": "string",
            "EndedAt": "string",
            "StartedAt": "string",
            "Status": "string"
         },
         "RunId": "string",
         "RunType": "string",
         "WorkflowArn": "string",
         "WorkflowVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkflowRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWorkflowRuns_ResponseSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-response-NextToken"></a>
The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.
Type: String

 ** [WorkflowRuns](#API_ListWorkflowRuns_ResponseSyntax) **   <a name="mwaaserverless-ListWorkflowRuns-response-WorkflowRuns"></a>
A list of workflow run summaries for the specified workflow.
Type: Array of [WorkflowRunSummary](API_WorkflowRunSummary.md) objects

## Errors
<a name="API_ListWorkflowRuns_Errors"></a>

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
<a name="API_ListWorkflowRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/ListWorkflowRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/ListWorkflowRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
