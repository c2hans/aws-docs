---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetWorkflowSteps.html
---

# GetWorkflowSteps
<a name="API_connect-customer-profiles_GetWorkflowSteps"></a>

Get granular list of steps in workflow.

## Request Syntax
<a name="API_connect-customer-profiles_GetWorkflowSteps_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/workflows/{{WorkflowId}}/steps?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetWorkflowSteps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetWorkflowSteps_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_GetWorkflowSteps_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_GetWorkflowSteps_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [WorkflowId](#API_connect-customer-profiles_GetWorkflowSteps_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-request-uri-WorkflowId"></a>
Unique identifier for the workflow.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetWorkflowSteps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetWorkflowSteps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AppflowIntegration": {
            "BatchRecordsEndTime": "string",
            "BatchRecordsStartTime": "string",
            "CreatedAt": number,
            "ExecutionMessage": "string",
            "FlowName": "string",
            "LastUpdatedAt": number,
            "RecordsProcessed": number,
            "Status": "string"
         }
      }
   ],
   "NextToken": "string",
   "WorkflowId": "string",
   "WorkflowType": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetWorkflowSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_GetWorkflowSteps_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-response-Items"></a>
List containing workflow step details.
Type: Array of [WorkflowStepItem](API_connect-customer-profiles_WorkflowStepItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_GetWorkflowSteps_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [WorkflowId](#API_connect-customer-profiles_GetWorkflowSteps_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-response-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [WorkflowType](#API_connect-customer-profiles_GetWorkflowSteps_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetWorkflowSteps-response-WorkflowType"></a>
The type of workflow. The only supported value is APPFLOW\_INTEGRATION.
Type: String
Valid Values: `APPFLOW_INTEGRATION`

## Errors
<a name="API_connect-customer-profiles_GetWorkflowSteps_Errors"></a>

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
<a name="API_connect-customer-profiles_GetWorkflowSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetWorkflowSteps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetWorkflowSteps)
