---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateSequenceStore.html
---

# CreateSequenceStore
<a name="API_CreateSequenceStore"></a>

Creates a sequence store and returns its metadata. Sequence stores are used to store sequence data files called read sets that are saved in FASTQ, BAM, uBAM, or CRAM formats. For aligned formats (BAM and CRAM), a sequence store can only use one reference genome. For unaligned formats (FASTQ and uBAM), a reference genome is not required. You can create multiple sequence stores per region per account.

The following are optional parameters you can specify for your sequence store:
+ Use `s3AccessConfig` to configure your sequence store with S3 access logs (recommended).
+ Use `sseConfig` to define your own KMS key for encryption.
+ Use `eTagAlgorithmFamily` to define which algorithm to use for the HealthOmics eTag on objects.
+ Use `fallbackLocation` to define a backup location for storing files that have failed a direct upload.
+ Use `propagatedSetLevelTags` to configure tags that propagate to all objects in your store.

For more information, see [Creating a HealthOmics sequence store](https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateSequenceStore_RequestSyntax"></a>

```
POST /sequencestore HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "eTagAlgorithmFamily": "{{string}}",
   "fallbackLocation": "{{string}}",
   "name": "{{string}}",
   "propagatedSetLevelTags": [ "{{string}}" ],
   "s3AccessConfig": {
      "accessLogLocation": "{{string}}"
   },
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
<a name="API_CreateSequenceStore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSequenceStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-clientToken"></a>
An idempotency token used to dedupe retry requests so that duplicate runs are not created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [description](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-description"></a>
A description for the store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [eTagAlgorithmFamily](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-eTagAlgorithmFamily"></a>
The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see [ETags and data provenance](https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html) in the * AWS HealthOmics User Guide*.
Type: String
Valid Values: `MD5up | SHA256up | SHA512up`
Required: No

 ** [fallbackLocation](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-fallbackLocation"></a>
An S3 location that is used to store files that have failed a direct upload. You can add or change the `fallbackLocation` after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`
Required: No

 ** [name](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-name"></a>
A name for the store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [propagatedSetLevelTags](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-propagatedSetLevelTags"></a>
The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [s3AccessConfig](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-s3AccessConfig"></a>
S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store.
Type: [S3AccessConfig](API_S3AccessConfig.md) object
Required: No

 ** [sseConfig](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-sseConfig"></a>
Server-side encryption (SSE) settings for the store.
Type: [SseConfig](API_SseConfig.md) object
Required: No

 ** [tags](#API_CreateSequenceStore_RequestSyntax) **   <a name="omics-CreateSequenceStore-request-tags"></a>
Tags for the store. You can configure up to 50 tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSequenceStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "eTagAlgorithmFamily": "string",
   "fallbackLocation": "string",
   "id": "string",
   "name": "string",
   "propagatedSetLevelTags": [ "string" ],
   "s3Access": {
      "accessLogLocation": "string",
      "s3AccessPointArn": "string",
      "s3Uri": "string"
   },
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   },
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_CreateSequenceStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationTime](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [eTagAlgorithmFamily](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-eTagAlgorithmFamily"></a>
The algorithm family of the ETag.
Type: String
Valid Values: `MD5up | SHA256up | SHA512up`

 ** [fallbackLocation](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-fallbackLocation"></a>
An S3 location that is used to store files that have failed a direct upload.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`

 ** [id](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [propagatedSetLevelTags](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-propagatedSetLevelTags"></a>
The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [s3Access](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-s3Access"></a>
The S3 access metadata of the sequence store.
Type: [SequenceStoreS3Access](API_SequenceStoreS3Access.md) object

 ** [sseConfig](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-sseConfig"></a>
Server-side encryption (SSE) settings for the store. This contains the KMS key ARN that is used to encrypt read set objects.
Type: [SseConfig](API_SseConfig.md) object

 ** [status](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-status"></a>
The status of the sequence store.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`

 ** [statusMessage](#API_CreateSequenceStore_ResponseSyntax) **   <a name="omics-CreateSequenceStore-response-statusMessage"></a>
The status message of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_CreateSequenceStore_Errors"></a>

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
<a name="API_CreateSequenceStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateSequenceStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateSequenceStore)
