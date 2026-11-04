---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteIngestionStream.html
---

# DeleteIngestionStream
<a name="API_DeleteIngestionStream"></a>

Deletes an ingestion stream. Documents that were already indexed by the stream remain in the index.

## Request Syntax
<a name="API_DeleteIngestionStream_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "collectionId": "{{string}}",
   "ingestionStreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteIngestionStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteIngestionStream_RequestSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [collectionId](#API_DeleteIngestionStream_RequestSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-request-collectionId"></a>
The unique identifier of the collection that the ingestion stream belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [ingestionStreamId](#API_DeleteIngestionStream_RequestSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-request-ingestionStreamId"></a>
The unique identifier of the ingestion stream to delete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DeleteIngestionStream_ResponseSyntax"></a>

```
{
   "collectionId": "string",
   "ingestionStreamId": "string",
   "ingestionStreamName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteIngestionStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionId](#API_DeleteIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-response-collectionId"></a>
The unique identifier of the collection that the ingestion stream belonged to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`

 ** [ingestionStreamId](#API_DeleteIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-response-ingestionStreamId"></a>
The unique identifier of the deleted ingestion stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [ingestionStreamName](#API_DeleteIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-response-ingestionStreamName"></a>
The name of the deleted ingestion stream.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`

 ** [status](#API_DeleteIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-DeleteIngestionStream-response-status"></a>
The current status of the ingestion stream.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_DeleteIngestionStream_Errors"></a>

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
<a name="API_DeleteIngestionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/DeleteIngestionStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteIngestionStream)
