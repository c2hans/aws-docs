---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StopNotebookRun.html
---

# StopNotebookRun
<a name="API_StopNotebookRun"></a>

Stops a running [notebook run](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_StopNotebookRun_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/notebook-runs/{{identifier}}/stop HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopNotebookRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_StopNotebookRun_RequestSyntax) **   <a name="datazone-StopNotebookRun-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_StopNotebookRun_RequestSyntax) **   <a name="datazone-StopNotebookRun-request-uri-identifier"></a>
The identifier of the notebook run to stop.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StopNotebookRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopNotebookRun_RequestSyntax) **   <a name="datazone-StopNotebookRun-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

## Response Syntax
<a name="API_StopNotebookRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainId": "string",
   "id": "string",
   "owningProjectId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StopNotebookRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_StopNotebookRun_ResponseSyntax) **   <a name="datazone-StopNotebookRun-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_StopNotebookRun_ResponseSyntax) **   <a name="datazone-StopNotebookRun-response-id"></a>
The identifier of the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_StopNotebookRun_ResponseSyntax) **   <a name="datazone-StopNotebookRun-response-owningProjectId"></a>
The identifier of the project that owns the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_StopNotebookRun_ResponseSyntax) **   <a name="datazone-StopNotebookRun-response-status"></a>
The status of the notebook run.
Type: String
Valid Values: `QUEUED | STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED`

## Errors
<a name="API_StopNotebookRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopNotebookRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StopNotebookRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StopNotebookRun)
