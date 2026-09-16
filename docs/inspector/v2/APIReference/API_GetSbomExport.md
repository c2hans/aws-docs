---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetSbomExport.html
---

# GetSbomExport
<a name="API_GetSbomExport"></a>

Gets details of a software bill of materials (SBOM) report.

## Request Syntax
<a name="API_GetSbomExport_RequestSyntax"></a>

```
POST /sbomexport/get HTTP/1.1
Content-type: application/json

{
   "reportId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetSbomExport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSbomExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [reportId](#API_GetSbomExport_RequestSyntax) **   <a name="inspector2-GetSbomExport-request-reportId"></a>
The report ID of the SBOM export to get details for.
Type: String
Pattern: `.*\b[a-f0-9]{8}\b-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-\b[a-f0-9]{12}\b.*`
Required: Yes

## Response Syntax
<a name="API_GetSbomExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorCode": "string",
   "errorMessage": "string",
   "filterCriteria": {
      "accountId": [
         {
            "comparison": "string",
            "value": "string"
         }
      ],
      "ec2InstanceTags": [
         {
            "comparison": "string",
            "key": "string",
            "value": "string"
         }
      ],
      "ecrImageTags": [
         {
            "comparison": "string",
            "value": "string"
         }
      ],
      "ecrRepositoryName": [
         {
            "comparison": "string",
            "value": "string"
         }
      ],
      "lambdaFunctionName": [
         {
            "comparison": "string",
            "value": "string"
         }
      ],
      "lambdaFunctionTags": [
         {
            "comparison": "string",
            "key": "string",
            "value": "string"
         }
      ],
      "resourceId": [
         {
            "comparison": "string",
            "value": "string"
         }
      ],
      "resourceType": [
         {
            "comparison": "string",
            "value": "string"
         }
      ]
   },
   "format": "string",
   "reportId": "string",
   "s3Destination": {
      "bucketName": "string",
      "keyPrefix": "string",
      "kmsKeyArn": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_GetSbomExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorCode](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-errorCode"></a>
An error code.
Type: String
Valid Values: `INTERNAL_ERROR | INVALID_PERMISSIONS | NO_FINDINGS_FOUND | BUCKET_NOT_FOUND | INCOMPATIBLE_BUCKET_REGION | MALFORMED_KMS_KEY`

 ** [errorMessage](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-errorMessage"></a>
An error message.
Type: String
Length Constraints: Minimum length of 1.

 ** [filterCriteria](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-filterCriteria"></a>
Contains details about the resource filter criteria used for the software bill of materials (SBOM) report.
Type: [ResourceFilterCriteria](API_ResourceFilterCriteria.md) object

 ** [format](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-format"></a>
The format of the software bill of materials (SBOM) report.
Type: String
Valid Values: `CYCLONEDX_1_4 | SPDX_2_3`

 ** [reportId](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-reportId"></a>
The report ID of the software bill of materials (SBOM) report.
Type: String
Pattern: `.*\b[a-f0-9]{8}\b-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-\b[a-f0-9]{12}\b.*`

 ** [s3Destination](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-s3Destination"></a>
Contains details of the Amazon S3 bucket and AWS KMS key used to export findings
Type: [Destination](API_Destination.md) object

 ** [status](#API_GetSbomExport_ResponseSyntax) **   <a name="inspector2-GetSbomExport-response-status"></a>
The status of the software bill of materials (SBOM) report.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | CANCELLED | FAILED`

## Errors
<a name="API_GetSbomExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetSbomExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetSbomExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetSbomExport)
