---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CancelIngestionJob.html
---

# CancelIngestionJob
<a name="API_CancelIngestionJob"></a>

Cancels an in-progress ingestion job. Documents that were already indexed before the cancellation remain in the index.

## Request Syntax
<a name="API_CancelIngestionJob_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "collectionId": "{{string}}",
   "ingestionJobId": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelIngestionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CancelIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CancelIngestionJob-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [collectionId](#API_CancelIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CancelIngestionJob-request-collectionId"></a>
The unique identifier of the collection that the ingestion job belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [ingestionJobId](#API_CancelIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CancelIngestionJob-request-ingestionJobId"></a>
The unique identifier of the ingestion job to cancel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CancelIngestionJob_ResponseSyntax"></a>

```
{
   "collectionId": "string",
   "ingestionJobId": "string",
   "ingestionJobName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CancelIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionId](#API_CancelIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-CancelIngestionJob-response-collectionId"></a>
The unique identifier of the collection that the ingestion job belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`

 ** [ingestionJobId](#API_CancelIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-CancelIngestionJob-response-ingestionJobId"></a>
The unique identifier of the cancelled ingestion job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [ingestionJobName](#API_CancelIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-CancelIngestionJob-response-ingestionJobName"></a>
The name of the cancelled ingestion job.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`

 ** [status](#API_CancelIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-CancelIngestionJob-response-status"></a>
The current status of the ingestion job.
Type: String
Valid Values: `CREATING | ACTIVE | COMPLETED | CANCELLING | CANCELLED | FAILED | CREATE_FAILED | CANCEL_FAILED`

## Errors
<a name="API_CancelIngestionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_CancelIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CancelIngestionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CancelIngestionJob)
