---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html
---

# ExportEarthObservationJob
<a name="API_geospatial_ExportEarthObservationJob"></a>

Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.

## Request Syntax
<a name="API_geospatial_ExportEarthObservationJob_RequestSyntax"></a>

```
POST /export-earth-observation-job HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "ClientToken": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "ExportSourceImages": {{boolean}},
   "OutputConfig": {
      "S3Data": {
         "KmsKeyId": "{{string}}",
         "S3Uri": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_geospatial_ExportEarthObservationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geospatial_ExportEarthObservationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_geospatial_ExportEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-request-Arn"></a>
The input Amazon Resource Name (ARN) of the Earth Observation job being exported.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`
Required: Yes

 ** [ClientToken](#API_geospatial_ExportEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Required: No

 ** [ExecutionRoleArn](#API_geospatial_ExportEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** [ExportSourceImages](#API_geospatial_ExportEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-request-ExportSourceImages"></a>
The source images provided to the Earth Observation job being exported.
Type: Boolean
Required: No

 ** [OutputConfig](#API_geospatial_ExportEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-request-OutputConfig"></a>
An object containing information about the output file.
Type: [OutputConfigInput](API_geospatial_OutputConfigInput.md) object
Required: Yes

## Response Syntax
<a name="API_geospatial_ExportEarthObservationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "ExecutionRoleArn": "string",
   "ExportSourceImages": boolean,
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
<a name="API_geospatial_ExportEarthObservationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-Arn"></a>
The output Amazon Resource Name (ARN) of the Earth Observation job being exported.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`

 ** [CreationTime](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [ExecutionRoleArn](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`

 ** [ExportSourceImages](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-ExportSourceImages"></a>
The source images provided to the Earth Observation job being exported.
Type: Boolean

 ** [ExportStatus](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-ExportStatus"></a>
The status of the results of the Earth Observation job being exported.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [OutputConfig](#API_geospatial_ExportEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_ExportEarthObservationJob-response-OutputConfig"></a>
An object containing information about the output file.
Type: [OutputConfigInput](API_geospatial_OutputConfigInput.md) object

## Errors
<a name="API_geospatial_ExportEarthObservationJob_Errors"></a>

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
<a name="API_geospatial_ExportEarthObservationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ExportEarthObservationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
