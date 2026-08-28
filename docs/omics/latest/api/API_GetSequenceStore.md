---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetSequenceStore.html
---

# GetSequenceStore
<a name="API_GetSequenceStore"></a>

Retrieves metadata for a sequence store using its ID and returns it in JSON format.

## Request Syntax
<a name="API_GetSequenceStore_RequestSyntax"></a>

```
GET /sequencestore/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSequenceStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetSequenceStore_RequestSyntax) **   <a name="omics-GetSequenceStore-request-uri-id"></a>
The store's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetSequenceStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSequenceStore_ResponseSyntax"></a>

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
   "statusMessage": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetSequenceStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationTime](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [eTagAlgorithmFamily](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-eTagAlgorithmFamily"></a>
The algorithm family of the ETag.
Type: String
Valid Values: `MD5up | SHA256up | SHA512up`

 ** [fallbackLocation](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-fallbackLocation"></a>
An S3 location that is used to store files that have failed a direct upload.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`

 ** [id](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [propagatedSetLevelTags](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-propagatedSetLevelTags"></a>
The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [s3Access](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-s3Access"></a>
The S3 metadata of a sequence store, including the ARN and S3 URI of the S3 bucket.
Type: [SequenceStoreS3Access](API_SequenceStoreS3Access.md) object

 ** [sseConfig](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object

 ** [status](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-status"></a>
The status of the sequence store.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`

 ** [statusMessage](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-statusMessage"></a>
The status message of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [updateTime](#API_GetSequenceStore_ResponseSyntax) **   <a name="omics-GetSequenceStore-response-updateTime"></a>
The last-updated time of the sequence store.
Type: Timestamp

## Errors
<a name="API_GetSequenceStore_Errors"></a>

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
<a name="API_GetSequenceStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetSequenceStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetSequenceStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
