---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateMultipartReadSetUpload.html
---

# CreateMultipartReadSetUpload
<a name="API_CreateMultipartReadSetUpload"></a>

Initiates a multipart read set upload for uploading partitioned source files into a sequence store. You can directly import source files from an EC2 instance and other local compute, or from an S3 bucket. To separate these source files into parts, use the `split` operation. Each part cannot be larger than 100 MB. If the operation is successful, it provides an `uploadId` which is required by the `UploadReadSetPart` API operation to upload parts into a sequence store.

To continue uploading a multipart read set into your sequence store, you must use the `UploadReadSetPart` API operation to upload each part individually following the steps below:
+ Specify the `uploadId` obtained from the previous call to `CreateMultipartReadSetUpload`.
+ Upload parts for that `uploadId`.

When you have finished uploading parts, use the `CompleteMultipartReadSetUpload` API to complete the multipart read set upload and to retrieve the final read set IDs in the response.

To learn more about creating parts and the `split` operation, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateMultipartReadSetUpload_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/upload HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "generatedFrom": "{{string}}",
   "name": "{{string}}",
   "referenceArn": "{{string}}",
   "sampleId": "{{string}}",
   "sourceFileType": "{{string}}",
   "subjectId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMultipartReadSetUpload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-uri-sequenceStoreId"></a>
The sequence store ID for the store that is the destination of the multipart uploads.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_CreateMultipartReadSetUpload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-clientToken"></a>
An idempotency token that can be used to avoid triggering multiple multipart uploads.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [description](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-description"></a>
The description of the read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [generatedFrom](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-generatedFrom"></a>
Where the source originated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-name"></a>
The name of the read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [referenceArn](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-referenceArn"></a>
The ARN of the reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: No

 ** [sampleId](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-sampleId"></a>
The source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [sourceFileType](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-sourceFileType"></a>
The type of file being uploaded.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`
Required: Yes

 ** [subjectId](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-subjectId"></a>
The source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [tags](#API_CreateMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CreateMultipartReadSetUpload-request-tags"></a>
Any tags to add to the read set.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateMultipartReadSetUpload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "generatedFrom": "string",
   "name": "string",
   "referenceArn": "string",
   "sampleId": "string",
   "sequenceStoreId": "string",
   "sourceFileType": "string",
   "subjectId": "string",
   "tags": {
      "string" : "string"
   },
   "uploadId": "string"
}
```

## Response Elements
<a name="API_CreateMultipartReadSetUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-creationTime"></a>
The creation time of the multipart upload.
Type: Timestamp

 ** [description](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-description"></a>
The description of the read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [generatedFrom](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-generatedFrom"></a>
The source of the read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [name](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-name"></a>
The name of the read set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [referenceArn](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-referenceArn"></a>
The read set source's reference ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [sampleId](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-sampleId"></a>
The source's sample ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStoreId](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-sequenceStoreId"></a>
The sequence store ID for the store that the read set will be created in.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sourceFileType](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-sourceFileType"></a>
The file type of the read set source.
Type: String
Valid Values: `FASTQ | BAM | CRAM | UBAM`

 ** [subjectId](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-subjectId"></a>
The source's subject ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [tags](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-tags"></a>
The tags to add to the read set.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uploadId](#API_CreateMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CreateMultipartReadSetUpload-response-uploadId"></a>
The ID for the initiated multipart upload.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

## Errors
<a name="API_CreateMultipartReadSetUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** NotSupportedOperationException **
 The operation is not supported by Amazon Omics, or the API does not exist.
HTTP Status Code: 405

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

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
<a name="API_CreateMultipartReadSetUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateMultipartReadSetUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateMultipartReadSetUpload)
