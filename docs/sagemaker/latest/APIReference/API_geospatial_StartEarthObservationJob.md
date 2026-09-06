---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StartEarthObservationJob.html
---

# StartEarthObservationJob
<a name="API_geospatial_StartEarthObservationJob"></a>

Use this operation to create an Earth observation job.

## Request Syntax
<a name="API_geospatial_StartEarthObservationJob_RequestSyntax"></a>

```
POST /earth-observation-jobs HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "InputConfig": {
      "PreviousEarthObservationJobArn": "{{string}}",
      "RasterDataCollectionQuery": {
         "AreaOfInterest": { ... },
         "PropertyFilters": {
            "LogicalOperator": "{{string}}",
            "Properties": [
               {
                  "Property": { ... }
               }
            ]
         },
         "RasterDataCollectionArn": "{{string}}",
         "TimeRangeFilter": {
            "EndTime": {{number}},
            "StartTime": {{number}}
         }
      }
   },
   "JobConfig": { ... },
   "KmsKeyId": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_geospatial_StartEarthObservationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geospatial_StartEarthObservationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Required: No

 ** [ExecutionRoleArn](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** [InputConfig](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-InputConfig"></a>
Input configuration information for the Earth Observation job.
Type: [InputConfigInput](API_geospatial_InputConfigInput.md) object
Required: Yes

 ** [JobConfig](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-JobConfig"></a>
An object containing information about the job configuration.
Type: [JobConfigInput](API_geospatial_JobConfigInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [KmsKeyId](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-KmsKeyId"></a>
The Key Management Service key ID for server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [Name](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-Name"></a>
The name of the Earth Observation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** [Tags](#API_geospatial_StartEarthObservationJob_RequestSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-request-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map
Required: No

## Response Syntax
<a name="API_geospatial_StartEarthObservationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "DurationInSeconds": number,
   "ExecutionRoleArn": "string",
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
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_geospatial_StartEarthObservationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the Earth Observation job.
Type: String

 ** [CreationTime](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [DurationInSeconds](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-DurationInSeconds"></a>
The duration of the session, in seconds.
Type: Integer

 ** [ExecutionRoleArn](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that you specified for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+`

 ** [InputConfig](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-InputConfig"></a>
Input configuration information for the Earth Observation job.
Type: [InputConfigOutput](API_geospatial_InputConfigOutput.md) object

 ** [JobConfig](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-JobConfig"></a>
An object containing information about the job configuration.
Type: [JobConfigInput](API_geospatial_JobConfigInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [KmsKeyId](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-KmsKeyId"></a>
The Key Management Service key ID for server-side encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [Name](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-Name"></a>
The name of the Earth Observation job.
Type: String

 ** [Status](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-Status"></a>
The status of the Earth Observation job.
Type: String
Valid Values: `INITIALIZING | IN_PROGRESS | STOPPING | COMPLETED | STOPPED | FAILED | DELETING | DELETED`

 ** [Tags](#API_geospatial_StartEarthObservationJob_ResponseSyntax) **   <a name="sagemaker-geospatial_StartEarthObservationJob-response-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map

## Errors
<a name="API_geospatial_StartEarthObservationJob_Errors"></a>

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
<a name="API_geospatial_StartEarthObservationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)
