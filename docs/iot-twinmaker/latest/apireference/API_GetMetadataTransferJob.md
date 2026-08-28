---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetMetadataTransferJob.html
---

# GetMetadataTransferJob
<a name="API_GetMetadataTransferJob"></a>

Retrieves information about a metadata transfer job.

## Request Syntax
<a name="API_GetMetadataTransferJob_RequestSyntax"></a>

```
GET /metadata-transfer-jobs/{{metadataTransferJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMetadataTransferJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metadataTransferJobId](#API_GetMetadataTransferJob_RequestSyntax) **   <a name="tm-GetMetadataTransferJob-request-uri-metadataTransferJobId"></a>
The metadata transfer job Id.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetMetadataTransferJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMetadataTransferJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": number,
   "description": "string",
   "destination": {
      "iotTwinMakerConfiguration": {
         "workspace": "string"
      },
      "s3Configuration": {
         "location": "string"
      },
      "type": "string"
   },
   "metadataTransferJobId": "string",
   "metadataTransferJobRole": "string",
   "progress": {
      "failedCount": number,
      "skippedCount": number,
      "succeededCount": number,
      "totalCount": number
   },
   "reportUrl": "string",
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
            "workspace": "string"
         },
         "s3Configuration": {
            "location": "string"
         },
         "type": "string"
      }
   ],
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
<a name="API_GetMetadataTransferJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-arn"></a>
The metadata transfer job ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-creationDateTime"></a>
The metadata transfer job's creation DateTime property.
Type: Timestamp

 ** [description](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-description"></a>
The metadata transfer job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [destination](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-destination"></a>
The metadata transfer job's destination.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object

 ** [metadataTransferJobId](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-metadataTransferJobId"></a>
The metadata transfer job Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

 ** [metadataTransferJobRole](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-metadataTransferJobRole"></a>
The metadata transfer job's role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`

 ** [progress](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-progress"></a>
The metadata transfer job's progress.
Type: [MetadataTransferJobProgress](API_MetadataTransferJobProgress.md) object

 ** [reportUrl](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-reportUrl"></a>
The metadata transfer job's report URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`

 ** [sources](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-sources"></a>
The metadata transfer job's sources.
Type: Array of [SourceConfiguration](API_SourceConfiguration.md) objects
Array Members: Fixed number of 1 item.

 ** [status](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-status"></a>
The metadata transfer job's status.
Type: [MetadataTransferJobStatus](API_MetadataTransferJobStatus.md) object

 ** [updateDateTime](#API_GetMetadataTransferJob_ResponseSyntax) **   <a name="tm-GetMetadataTransferJob-response-updateDateTime"></a>
The metadata transfer job's update DateTime property.
Type: Timestamp

## Errors
<a name="API_GetMetadataTransferJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

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
<a name="API_GetMetadataTransferJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetMetadataTransferJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetMetadataTransferJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
