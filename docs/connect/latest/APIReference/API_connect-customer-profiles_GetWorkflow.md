---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetWorkflow.html
---

# GetWorkflow
<a name="API_connect-customer-profiles_GetWorkflow"></a>

Get details of specified workflow.

## Request Syntax
<a name="API_connect-customer-profiles_GetWorkflow_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/workflows/{{WorkflowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [WorkflowId](#API_connect-customer-profiles_GetWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-request-uri-WorkflowId"></a>
Unique identifier for the workflow.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": {
      "AppflowIntegration": {
         "ConnectorProfileName": "string",
         "RoleArn": "string",
         "SourceConnectorType": "string"
      }
   },
   "ErrorDescription": "string",
   "LastUpdatedAt": number,
   "Metrics": {
      "AppflowIntegration": {
         "RecordsProcessed": number,
         "StepsCompleted": number,
         "TotalSteps": number
      }
   },
   "StartDate": number,
   "Status": "string",
   "WorkflowId": "string",
   "WorkflowType": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-Attributes"></a>
Attributes provided for workflow execution.
Type: [WorkflowAttributes](API_connect-customer-profiles_WorkflowAttributes.md) object

 ** [ErrorDescription](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-ErrorDescription"></a>
Workflow error messages during execution (if any).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-LastUpdatedAt"></a>
The timestamp that represents when workflow execution last updated.
Type: Timestamp

 ** [Metrics](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-Metrics"></a>
Workflow specific execution metrics.
Type: [WorkflowMetrics](API_connect-customer-profiles_WorkflowMetrics.md) object

 ** [StartDate](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-StartDate"></a>
The timestamp that represents when workflow execution started.
Type: Timestamp

 ** [Status](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-Status"></a>
Status of workflow execution.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETE | FAILED | SPLIT | RETRY | CANCELLED`

 ** [WorkflowId](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [WorkflowType](#API_connect-customer-profiles_GetWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflow-response-WorkflowType"></a>
The type of workflow. The only supported value is APPFLOW\_INTEGRATION.
Type: String
Valid Values: `APPFLOW_INTEGRATION`

## Errors
<a name="API_connect-customer-profiles_GetWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
