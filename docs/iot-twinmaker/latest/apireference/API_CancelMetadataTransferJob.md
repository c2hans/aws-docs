---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CancelMetadataTransferJob.html
---

# CancelMetadataTransferJob
<a name="API_CancelMetadataTransferJob"></a>

Cancels the metadata transfer job.

## Request Syntax
<a name="API_CancelMetadataTransferJob_RequestSyntax"></a>

```
PUT /metadata-transfer-jobs/{{metadataTransferJobId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelMetadataTransferJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metadataTransferJobId](#API_CancelMetadataTransferJob_RequestSyntax) **   <a name="tm-CancelMetadataTransferJob-request-uri-metadataTransferJobId"></a>
The metadata transfer job Id.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_CancelMetadataTransferJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelMetadataTransferJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "metadataTransferJobId": "string",
   "progress": {
      "failedCount": number,
      "skippedCount": number,
      "succeededCount": number,
      "totalCount": number
   },
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "queuedPosition": number,
      "state": "string"
   },
   "updateDateTime": number
}
```

## Response Elements
<a name="API_CancelMetadataTransferJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CancelMetadataTransferJob_ResponseSyntax) **   <a name="tm-CancelMetadataTransferJob-response-arn"></a>
The metadata transfer job ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [metadataTransferJobId](#API_CancelMetadataTransferJob_ResponseSyntax) **   <a name="tm-CancelMetadataTransferJob-response-metadataTransferJobId"></a>
The metadata transfer job Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

 ** [progress](#API_CancelMetadataTransferJob_ResponseSyntax) **   <a name="tm-CancelMetadataTransferJob-response-progress"></a>
The metadata transfer job's progress.
Type: [MetadataTransferJobProgress](API_MetadataTransferJobProgress.md) object

 ** [status](#API_CancelMetadataTransferJob_ResponseSyntax) **   <a name="tm-CancelMetadataTransferJob-response-status"></a>
The metadata transfer job's status.
Type: [MetadataTransferJobStatus](API_MetadataTransferJobStatus.md) object

 ** [updateDateTime](#API_CancelMetadataTransferJob_ResponseSyntax) **   <a name="tm-CancelMetadataTransferJob-response-updateDateTime"></a>
Used to update the DateTime property.
Type: Timestamp

## Errors
<a name="API_CancelMetadataTransferJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_CancelMetadataTransferJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/CancelMetadataTransferJob)
