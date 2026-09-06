---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetEarthObservationJob.html
---

# GetEarthObservationJob
<a name="API_geospatial_GetEarthObservationJob"></a>

Get the details for a previously initiated Earth Observation job.

## Request Syntax
<a name="API_geospatial_GetEarthObservationJob_RequestSyntax"></a>

```
GET /earth-observation-jobs/{{Arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geospatial_GetEarthObservationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_geospatial_GetEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the Earth Observation job.
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`
Required: Yes

## Request Body
<a name="API_geospatial_GetEarthObservationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geospatial_GetEarthObservationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "DurationInSeconds": number,
   "ErrorDetails": {
      "Message": "string",
      "Type": "string"
   },
   "ExecutionRoleArn": "string",
   "ExportErrorDetails": {
      "ExportResults": {
         "Message": "string",
         "Type": "string"
      },
      "ExportSourceImages": {
         "Message": "string",
         "Type": "string"
      }
   },
   "ExportStatus": "string",
   "InputConfig": {
      "PreviousEarthObservationJobArn": "string",
      "RasterDataCollectionQuery": {
         "AreaOfInterest": { ... },
         "PropertyFilters": {
            "LogicalOperator": "string",
            "Properties": [
               {
                  "Property": { ... }
               }
            ]
         },
         "RasterDataCollectionArn": "string",
         "RasterDataCollectionName": "string",
         "TimeRangeFilter": {
            "EndTime": "string",
            "StartTime": "string"
         }
      }
   },
   "JobConfig": { ... },
   "KmsKeyId": "string",
   "Name": "string",
   "OutputBands": [
      {
         "BandName": "string",
         "OutputDataType": "string"
      }
   ],
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_geospatial_GetEarthObservationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the Earth Observation job.
Type: String

 ** [CreationTime](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-CreationTime"></a>
The creation time of the initiated Earth Observation job.
Type: Timestamp

 ** [DurationInSeconds](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-DurationInSeconds"></a>
The duration of Earth Observation job, in seconds.
Type: Integer

 ** [ErrorDetails](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-ErrorDetails"></a>
Details about the errors generated during the Earth Observation job.
Type: [EarthObservationJobErrorDetails](API_geospatial_EarthObservationJobErrorDetails.md) object

 ** [ExecutionRoleArn](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`

 ** [ExportErrorDetails](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-ExportErrorDetails"></a>
Details about the errors generated during ExportEarthObservationJob.
Type: [ExportErrorDetails](API_geospatial_ExportErrorDetails.md) object

 ** [ExportStatus](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-ExportStatus"></a>
The status of the Earth Observation job.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [InputConfig](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-InputConfig"></a>
Input data for the Earth Observation job.
Type: [InputConfigOutput](API_geospatial_InputConfigOutput.md) object

 ** [JobConfig](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-JobConfig"></a>
An object containing information about the job configuration.
Type: [JobConfigInput](API_geospatial_JobConfigInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [KmsKeyId](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-KmsKeyId"></a>
The Key Management Service key ID for server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [Name](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-Name"></a>
The name of the Earth Observation job.
Type: String

 ** [OutputBands](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-OutputBands"></a>
Bands available in the output of an operation.
Type: Array of [OutputBand](API_geospatial_OutputBand.md) objects

 ** [Status](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-Status"></a>
The status of a previously initiated Earth Observation job.
Type: String
Valid Values: `INITIALIZING | IN_PROGRESS | STOPPING | COMPLETED | STOPPED | FAILED | DELETING | DELETED`

 ** [Tags](#API_geospatial_GetEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_GetEarthObservationJob-response-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map

## Errors
<a name="API_geospatial_GetEarthObservationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
 ** ResourceId **

HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
 ** ResourceId **
Identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** ResourceId **

HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** ResourceId **

HTTP Status Code: 400

## See Also
<a name="API_geospatial_GetEarthObservationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/GetEarthObservationJob)
