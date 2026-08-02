---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateReferenceStore.html
---

# CreateReferenceStore
<a name="API_CreateReferenceStore"></a>

Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the `StartReferenceImportJob` API operation.

For more information, see [Creating a HealthOmics reference store](https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateReferenceStore_RequestSyntax"></a>

```
POST /referencestore HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "sseConfig": {
      "keyArn": "{{string}}",
      "type": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateReferenceStore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReferenceStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateReferenceStore_RequestSyntax) **   <a name="omics-CreateReferenceStore-request-clientToken"></a>
To ensure that requests don't run multiple times, specify a unique token for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [description](#API_CreateReferenceStore_RequestSyntax) **   <a name="omics-CreateReferenceStore-request-description"></a>
A description for the store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_CreateReferenceStore_RequestSyntax) **   <a name="omics-CreateReferenceStore-request-name"></a>
A name for the store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [sseConfig](#API_CreateReferenceStore_RequestSyntax) **   <a name="omics-CreateReferenceStore-request-sseConfig"></a>
Server-side encryption (SSE) settings for the store.
Type: [SseConfig](API_SseConfig.md) object
Required: No

 ** [tags](#API_CreateReferenceStore_RequestSyntax) **   <a name="omics-CreateReferenceStore-request-tags"></a>
Tags for the store.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateReferenceStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CreateReferenceStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationTime](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [id](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sseConfig](#API_CreateReferenceStore_ResponseSyntax) **   <a name="omics-CreateReferenceStore-response-sseConfig"></a>
The store's SSE settings.
Type: [SseConfig](API_SseConfig.md) object

## Errors
<a name="API_CreateReferenceStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateReferenceStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateReferenceStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateReferenceStore)
