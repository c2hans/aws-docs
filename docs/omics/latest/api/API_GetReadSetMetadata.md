---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetMetadata.html
---

# GetReadSetMetadata
<a name="API_GetReadSetMetadata"></a>

Retrieves the metadata for a read set from a sequence store in JSON format. This operation does not return tags. To retrieve the list of tags for a read set, use the `ListTagsForResource` API operation.

## Request Syntax
<a name="API_GetReadSetMetadata_RequestSyntax"></a>

```
GET /sequencestore/{{sequenceStoreId}}/readset/{{id}}/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReadSetMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReadSetMetadata_RequestSyntax) **   <a name="omics-GetReadSetMetadata-request-uri-id"></a>
The read set's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [sequenceStoreId](#API_GetReadSetMetadata_RequestSyntax) **   <a name="omics-GetReadSetMetadata-request-uri-sequenceStoreId"></a>
The read set's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReadSetMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReadSetMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationJobId": "string",
   "creationTime": "string",
   "creationType": "string",
   "description": "string",
   "etag": {
      "algorithm": "string",
      "source1": "string",
      "source2": "string"
   },
   "files": {
      "index": {
         "contentLength": number,
         "partSize": number,
         "s3Access": {
            "s3Uri": "string"
         },
         "totalParts": number
      },
      "source1": {
         "contentLength": number,
         "partSize": number,
         "s3Access": {
            "s3Uri": "string"
         },
         "totalParts": number
      },
      "source2": {
         "contentLength": number,
         "partSize": number,
         "s3Access": {
            "s3Uri": "string"
         },
         "totalParts": number
      }
   },
   "fileType": "string",
   "id": "string",
   "name": "string",
   "referenceArn": "string",
   "sampleId": "string",
   "sequenceInformation": {
      "alignment": "string",
      "generatedFrom": "string",
      "totalBaseCount": number,
      "totalReadCount": number
   },
   "sequenceStoreId": "string",
   "status": "string",
   "statusMessage": "string",
   "subjectId": "string"
}
```

## Response Elements
<a name="API_GetReadSetMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-arn"></a>
The read set's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationJobId](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-creationJobId"></a>
The read set's creation job ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-zA-Z0-9]+`

 ** [creationTime](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-creationTime"></a>
When the read set was created.
Type: Timestamp

 ** [creationType](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-creationType"></a>
 The creation type of the read set.
Type: String
Valid Values: `IMPORT | UPLOAD`

 ** [description](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-description"></a>
The read set's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [etag](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-etag"></a>
The entity tag (ETag) is a hash of the object meant to represent its semantic content.
Type: [ETag](API_ETag.md) object

 ** [files](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-files"></a>
The read set's files.
Type: [ReadSetFiles](API_ReadSetFiles.md) object

 ** [fileType](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-fileType"></a>
The read set's file type.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`

 ** [id](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-id"></a>
The read set's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-name"></a>
The read set's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [referenceArn](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-referenceArn"></a>
The read set's genome reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [sampleId](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-sampleId"></a>
The read set's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceInformation](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-sequenceInformation"></a>
The read set's sequence information.
Type: [SequenceInformation](API_SequenceInformation.md) object

 ** [sequenceStoreId](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-sequenceStoreId"></a>
The read set's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [status](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-status"></a>
The read set's status.
Type: String
Valid Values: `ARCHIVED | ACTIVATING | ACTIVE | DELETING | DELETED | PROCESSING_UPLOAD | UPLOAD_FAILED`

 ** [statusMessage](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-statusMessage"></a>
The status message for a read set. It provides more detail as to why the read set has a status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [subjectId](#API_GetReadSetMetadata_ResponseSyntax) **   <a name="omics-GetReadSetMetadata-response-subjectId"></a>
The read set's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetReadSetMetadata_Errors"></a>

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
<a name="API_GetReadSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReadSetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReadSetMetadata)
