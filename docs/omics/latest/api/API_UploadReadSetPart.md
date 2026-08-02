---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UploadReadSetPart.html
---

# UploadReadSetPart
<a name="API_UploadReadSetPart"></a>

Uploads a specific part of a read set into a sequence store. When you a upload a read set part with a part number that already exists, the new part replaces the existing one. This operation returns a JSON formatted response containing a string identifier that is used to confirm that parts are being added to the intended upload.

For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_UploadReadSetPart_RequestSyntax"></a>

```
PUT /sequencestore/{{sequenceStoreId}}/upload/{{uploadId}}/part?partNumber={{partNumber}}&partSource={{partSource}} HTTP/1.1

{{payload}}
```

## URI Request Parameters
<a name="API_UploadReadSetPart_RequestParameters"></a>

The request uses the following URI parameters.

 ** [partNumber](#API_UploadReadSetPart_RequestSyntax) **   <a name="omics-UploadReadSetPart-request-uri-partNumber"></a>
The number of the part being uploaded.
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** [partSource](#API_UploadReadSetPart_RequestSyntax) **   <a name="omics-UploadReadSetPart-request-uri-partSource"></a>
The source file for an upload part.
Valid Values: `SOURCE1 | SOURCE2`
Required: Yes

 ** [sequenceStoreId](#API_UploadReadSetPart_RequestSyntax) **   <a name="omics-UploadReadSetPart-request-uri-sequenceStoreId"></a>
The Sequence Store ID used for the multipart upload.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [uploadId](#API_UploadReadSetPart_RequestSyntax) **   <a name="omics-UploadReadSetPart-request-uri-uploadId"></a>
The ID for the initiated multipart upload.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_UploadReadSetPart_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_UploadReadSetPart_RequestSyntax) **   <a name="omics-UploadReadSetPart-request-payload"></a>
The read set data to upload for a part.
Required: Yes

## Response Syntax
<a name="API_UploadReadSetPart_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "checksum": "string"
}
```

## Response Elements
<a name="API_UploadReadSetPart_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checksum](#API_UploadReadSetPart_ResponseSyntax) **   <a name="omics-UploadReadSetPart-response-checksum"></a>
An identifier used to confirm that parts are being added to the intended upload.
Type: String

## Errors
<a name="API_UploadReadSetPart_Errors"></a>

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
<a name="API_UploadReadSetPart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UploadReadSetPart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UploadReadSetPart)
