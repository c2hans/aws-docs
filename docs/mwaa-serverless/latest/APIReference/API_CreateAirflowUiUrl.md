---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateAirflowUiUrl.html
---

# CreateAirflowUiUrl
<a name="API_CreateAirflowUiUrl"></a>

Creates a launch URL that opens the Apache Airflow UI for your workflows in Amazon Managed Workflows for Apache Airflow Serverless. The UI shows the workflows in your account in the current AWS Region. To start a UI session, open the URL in a browser before it expires.

The UI runs with the permissions of the IAM identity that you use to call this operation. You see only the workflows, workflow runs, and logs that the identity can read, and you can start a workflow run only if the identity has permission to start one.

The UI session uses the caller's permissions. The session works only from the network address that opened the URL. It ends at `SessionExpiresAt` or when you sign out from the UI.

## Request Syntax
<a name="API_CreateAirflowUiUrl_RequestSyntax"></a>

```
{
   "ExpiresInSeconds": {{number}},
   "SessionDurationInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_CreateAirflowUiUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExpiresInSeconds](#API_CreateAirflowUiUrl_RequestSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-request-ExpiresInSeconds"></a>
Specifies the number of seconds that the launch URL stays valid. This value limits only the time to open the URL, not the length of the UI session. The default is 300.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** [SessionDurationInSeconds](#API_CreateAirflowUiUrl_RequestSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-request-SessionDurationInSeconds"></a>
Specifies the number of seconds that the UI session lasts, starting from when you call this operation. The default is 43200 (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 43200.
Required: No

## Response Syntax
<a name="API_CreateAirflowUiUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string",
   "SessionExpiresAt": "string",
   "SessionId": "string",
   "UrlExpiresAt": "string"
}
```

## Response Elements
<a name="API_CreateAirflowUiUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreateAirflowUiUrl_ResponseSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-response-AuthorizedUrl"></a>
The launch URL that opens the Airflow UI. Open it in a browser before `UrlExpiresAt`. The UI session uses the permissions of the identity that called this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SessionExpiresAt](#API_CreateAirflowUiUrl_ResponseSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-response-SessionExpiresAt"></a>
The UI session ends at this time. The value is in ISO 8601 date-time format. After this time, create a new URL to open the UI again.
Type: Timestamp

 ** [SessionId](#API_CreateAirflowUiUrl_ResponseSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-response-SessionId"></a>
The URL starts a UI session that has this identifier.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`

 ** [UrlExpiresAt](#API_CreateAirflowUiUrl_ResponseSyntax) **   <a name="mwaaserverless-CreateAirflowUiUrl-response-UrlExpiresAt"></a>
The launch URL stops being valid at this time. The value is in ISO 8601 date-time format.
Type: Timestamp

## Errors
<a name="API_CreateAirflowUiUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of the resource.
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
<a name="API_CreateAirflowUiUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/CreateAirflowUiUrl)
