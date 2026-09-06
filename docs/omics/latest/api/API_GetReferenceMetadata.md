---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceMetadata.html
---

# GetReferenceMetadata
<a name="API_GetReferenceMetadata"></a>

Retrieves metadata for a reference genome. This operation returns the number of parts, part size, and MD5 of an entire file. This operation does not return tags. To retrieve the list of tags for a read set, use the `ListTagsForResource` API operation.

## Request Syntax
<a name="API_GetReferenceMetadata_RequestSyntax"></a>

```
GET /referencestore/{{referenceStoreId}}/reference/{{id}}/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReferenceMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReferenceMetadata_RequestSyntax) **   <a name="omics-GetReferenceMetadata-request-uri-id"></a>
The reference's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [referenceStoreId](#API_GetReferenceMetadata_RequestSyntax) **   <a name="omics-GetReferenceMetadata-request-uri-referenceStoreId"></a>
The reference's reference store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReferenceMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReferenceMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationJobId": "string",
   "creationTime": "string",
   "creationType": "string",
   "description": "string",
   "files": {
      "index": {
         "contentLength": number,
         "partSize": number,
         "s3Access": {
            "s3Uri": "string"
         },
         "totalParts": number
      },
      "source": {
         "contentLength": number,
         "partSize": number,
         "s3Access": {
            "s3Uri": "string"
         },
         "totalParts": number
      }
   },
   "id": "string",
   "md5": "string",
   "name": "string",
   "referenceStoreId": "string",
   "status": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetReferenceMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-arn"></a>
The reference's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationJobId](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-creationJobId"></a>
The reference's creation job ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-zA-Z0-9]+`

 ** [creationTime](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-creationTime"></a>
When the reference was created.
Type: Timestamp

 ** [creationType](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-creationType"></a>
The reference's creation type.
Type: String
Valid Values: `IMPORT`

 ** [description](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-description"></a>
The reference's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [files](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-files"></a>
The reference's files.
Type: [ReferenceFiles](API_ReferenceFiles.md) object

 ** [id](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-id"></a>
The reference's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [md5](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-md5"></a>
The reference's MD5 checksum.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{N}]+`

 ** [name](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-name"></a>
The reference's name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [referenceStoreId](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-referenceStoreId"></a>
The reference's reference store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [status](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-status"></a>
The reference's status.
Type: String
Valid Values: `ACTIVE | DELETING | DELETED`

 ** [updateTime](#API_GetReferenceMetadata_ResponseSyntax) **   <a name="omics-GetReferenceMetadata-response-updateTime"></a>
When the reference was updated.
Type: Timestamp

## Errors
<a name="API_GetReferenceMetadata_Errors"></a>

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

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetReferenceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReferenceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReferenceMetadata)
