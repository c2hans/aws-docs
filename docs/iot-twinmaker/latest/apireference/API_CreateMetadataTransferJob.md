---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateMetadataTransferJob.html
---

# CreateMetadataTransferJob
<a name="API_CreateMetadataTransferJob"></a>

Creates a new metadata transfer job.

## Request Syntax
<a name="API_CreateMetadataTransferJob_RequestSyntax"></a>

```
POST /metadata-transfer-jobs HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "destination": {
      "iotTwinMakerConfiguration": {
         "workspace": "{{string}}"
      },
      "s3Configuration": {
         "location": "{{string}}"
      },
      "type": "{{string}}"
   },
   "metadataTransferJobId": "{{string}}",
   "sources": [
      {
         "iotSiteWiseConfiguration": {
            "filters": [
               { ... }
            ]
         },
         "iotTwinMakerConfiguration": {
            "filters": [
               { ... }
            ],
            "workspace": "{{string}}"
         },
         "s3Configuration": {
            "location": "{{string}}"
         },
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMetadataTransferJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMetadataTransferJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateMetadataTransferJob_RequestSyntax) **   <a name="tm-CreateMetadataTransferJob-request-description"></a>
The metadata transfer job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [destination](#API_CreateMetadataTransferJob_RequestSyntax) **   <a name="tm-CreateMetadataTransferJob-request-destination"></a>
The metadata transfer job destination.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: Yes

 ** [metadataTransferJobId](#API_CreateMetadataTransferJob_RequestSyntax) **   <a name="tm-CreateMetadataTransferJob-request-metadataTransferJobId"></a>
The metadata transfer job Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

 ** [sources](#API_CreateMetadataTransferJob_RequestSyntax) **   <a name="tm-CreateMetadataTransferJob-request-sources"></a>
The metadata transfer job sources.
Type: Array of [SourceConfiguration](API_SourceConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreateMetadataTransferJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": number,
   "metadataTransferJobId": "string",
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "queuedPosition": number,
      "state": "string"
   }
}
```

## Response Elements
<a name="API_CreateMetadataTransferJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateMetadataTransferJob_ResponseSyntax) **   <a name="tm-CreateMetadataTransferJob-response-arn"></a>
The metadata transfer job ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_CreateMetadataTransferJob_ResponseSyntax) **   <a name="tm-CreateMetadataTransferJob-response-creationDateTime"></a>
The The metadata transfer job creation DateTime property.
Type: Timestamp

 ** [metadataTransferJobId](#API_CreateMetadataTransferJob_ResponseSyntax) **   <a name="tm-CreateMetadataTransferJob-response-metadataTransferJobId"></a>
The metadata transfer job Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

 ** [status](#API_CreateMetadataTransferJob_ResponseSyntax) **   <a name="tm-CreateMetadataTransferJob-response-status"></a>
The metadata transfer job response status.
Type: [MetadataTransferJobStatus](API_MetadataTransferJobStatus.md) object

## Errors
<a name="API_CreateMetadataTransferJob_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_CreateMetadataTransferJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/CreateMetadataTransferJob)
