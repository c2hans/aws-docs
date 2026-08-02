---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartDataTransformationJob.html
---

# StartDataTransformationJob
<a name="API_StartDataTransformationJob"></a>

Starts an asynchronous data transformation job that converts source files from Amazon Simple Storage Service (Amazon S3) and writes the output to Amazon S3 or AWS HealthLake.

## Request Syntax
<a name="API_StartDataTransformationJob_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DriftDetectionEnabled": {{boolean}},
   "InputDataConfig": {
      "S3Uri": "{{string}}",
      "SourceFormat": "{{string}}"
   },
   "JobName": "{{string}}",
   "OutputDataConfig": {
      "S3Configuration": {
         "KmsKeyId": "{{string}}",
         "S3Uri": "{{string}}"
      }
   },
   "ProfileId": "{{string}}",
   "ProvenanceEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_StartDataTransformationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [DataAccessRoleArn](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that AWS HealthLake assumes to read from and write to the specified Amazon S3 locations.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [DriftDetectionEnabled](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-DriftDetectionEnabled"></a>
Specifies whether drift detection is enabled for this job. When enabled, AWS HealthLake writes a drift report to the output Amazon S3 location alongside the converted files.
Type: Boolean
Required: No

 ** [InputDataConfig](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-InputDataConfig"></a>
The Amazon S3 location and format of the source files to transform.
Type: [TransformationInputDataConfig](API_TransformationInputDataConfig.md) object
Required: Yes

 ** [JobName](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-JobName"></a>
A descriptive name for the data transformation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-%@]*`
Required: No

 ** [OutputDataConfig](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-OutputDataConfig"></a>
The Amazon S3 output location and AWS Key Management Service (AWS KMS) encryption configuration.
Type: [TransformationOutputDataConfig](API_TransformationOutputDataConfig.md) object
Required: Yes

 ** [ProfileId](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-ProfileId"></a>
The unique identifier of the data transformation profile to use for conversion.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [ProvenanceEnabled](#API_StartDataTransformationJob_RequestSyntax) **   <a name="HealthLake-StartDataTransformationJob-request-ProvenanceEnabled"></a>
Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation job. When provenance is enabled, the service also generates related DocumentReference and Device resources. If you don't specify a value, the default is `true`. To disable provenance output, set this parameter to `false`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StartDataTransformationJob_ResponseSyntax"></a>

```
{
   "JobId": "string",
   "JobStatus": "string"
}
```

## Response Elements
<a name="API_StartDataTransformationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartDataTransformationJob_ResponseSyntax) **   <a name="HealthLake-StartDataTransformationJob-response-JobId"></a>
The unique identifier assigned to the data transformation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [JobStatus](#API_StartDataTransformationJob_ResponseSyntax) **   <a name="HealthLake-StartDataTransformationJob-response-JobStatus"></a>
The initial status of the data transformation job.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`

## Errors
<a name="API_StartDataTransformationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_StartDataTransformationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/StartDataTransformationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/StartDataTransformationJob)
