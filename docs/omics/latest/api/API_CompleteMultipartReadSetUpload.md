---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CompleteMultipartReadSetUpload.html
---

# CompleteMultipartReadSetUpload
<a name="API_CompleteMultipartReadSetUpload"></a>

Completes a multipart read set upload into a sequence store after you have initiated the upload process with `CreateMultipartReadSetUpload` and uploaded all read set parts using `UploadReadSetPart`. You must specify the parts you uploaded using the parts parameter. If the operation is successful, it returns the read set ID(s) of the uploaded read set(s).

For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CompleteMultipartReadSetUpload_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/upload/{{uploadId}}/complete HTTP/1.1
Content-type: application/json

{
   "parts": [
      {
         "checksum": "{{string}}",
         "partNumber": {{number}},
         "partSource": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CompleteMultipartReadSetUpload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_CompleteMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CompleteMultipartReadSetUpload-request-uri-sequenceStoreId"></a>
The sequence store ID for the store involved in the multipart upload.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [uploadId](#API_CompleteMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CompleteMultipartReadSetUpload-request-uri-uploadId"></a>
The ID for the multipart upload.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_CompleteMultipartReadSetUpload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [parts](#API_CompleteMultipartReadSetUpload_RequestSyntax) **   <a name="omics-CompleteMultipartReadSetUpload-request-parts"></a>
The individual uploads or parts of a multipart upload.
Type: Array of [CompleteReadSetUploadPartListItem](API_CompleteReadSetUploadPartListItem.md) objects
Required: Yes

## Response Syntax
<a name="API_CompleteMultipartReadSetUpload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "readSetId": "string"
}
```

## Response Elements
<a name="API_CompleteMultipartReadSetUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [readSetId](#API_CompleteMultipartReadSetUpload_ResponseSyntax) **   <a name="omics-CompleteMultipartReadSetUpload-response-readSetId"></a>
The read set ID created for an uploaded read set.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

## Errors
<a name="API_CompleteMultipartReadSetUpload_Errors"></a>

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
<a name="API_CompleteMultipartReadSetUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CompleteMultipartReadSetUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CompleteMultipartReadSetUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
