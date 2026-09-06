---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html
---

# ExportVectorEnrichmentJob
<a name="API_geospatial_ExportVectorEnrichmentJob"></a>

Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.

## Request Syntax
<a name="API_geospatial_ExportVectorEnrichmentJob_RequestSyntax"></a>

```
POST /export-vector-enrichment-jobs HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "ClientToken": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "OutputConfig": {
      "S3Data": {
         "KmsKeyId": "{{string}}",
         "S3Uri": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_geospatial_ExportVectorEnrichmentJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geospatial_ExportVectorEnrichmentJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_geospatial_ExportVectorEnrichmentJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-request-Arn"></a>
The Amazon Resource Name (ARN) of the Vector Enrichment job.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:vector-enrichment-job/[a-z0-9]{12,}`
Required: Yes

 ** [ClientToken](#API_geospatial_ExportVectorEnrichmentJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Required: No

 ** [ExecutionRoleArn](#API_geospatial_ExportVectorEnrichmentJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** [OutputConfig](#API_geospatial_ExportVectorEnrichmentJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-request-OutputConfig"></a>
Output location information for exporting Vector Enrichment Job results.
Type: [ExportVectorEnrichmentJobOutputConfig](API_geospatial_ExportVectorEnrichmentJobOutputConfig.md) object
Required: Yes

## Response Syntax
<a name="API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "ExecutionRoleArn": "string",
   "ExportStatus": "string",
   "OutputConfig": {
      "S3Data": {
         "KmsKeyId": "string",
         "S3Uri": "string"
      }
   }
}
```

## Response Elements
<a name="API_geospatial_ExportVectorEnrichmentJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the Vector Enrichment job being exported.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:vector-enrichment-job/[a-z0-9]{12,}`

 ** [CreationTime](#API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [ExecutionRoleArn](#API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permission to upload to the location in OutputConfig.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`

 ** [ExportStatus](#API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-response-ExportStatus"></a>
The status of the results the Vector Enrichment job being exported.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [OutputConfig](#API_geospatial_ExportVectorEnrichmentJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportVectorEnrichmentJob-response-OutputConfig"></a>
Output location information for exporting Vector Enrichment Job results.
Type: [ExportVectorEnrichmentJobOutputConfig](API_geospatial_ExportVectorEnrichmentJobOutputConfig.md) object

## Errors
<a name="API_geospatial_ExportVectorEnrichmentJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** ResourceId **
Identifier of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
 ** ResourceId **

HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
 ** ResourceId **
Identifier of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** ResourceId **
Identifier of the resource affected.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** ResourceId **

HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** ResourceId **

HTTP Status Code: 400

## See Also
<a name="API_geospatial_ExportVectorEnrichmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ExportVectorEnrichmentJob)
