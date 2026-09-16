---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_StartJob.html
---

# StartJob
<a name="API_geojobs_StartJob"></a>

 `StartJob` starts a new asynchronous bulk processing job. You specify the input data location in Amazon S3, the action to perform, and the output location where results are written. Currently, the Jobs APIs support bulk address validation.

For more information, see [Job concepts](https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geojobs_StartJob_RequestSyntax"></a>

```
POST /metadata/v0/jobs HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "ActionOptions": {
      "ValidateAddress": {
         "AdditionalFeatures": [ "{{string}}" ]
      }
   },
   "ClientToken": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "InputOptions": {
      "Format": "{{string}}",
      "Location": "{{string}}"
   },
   "Name": "{{string}}",
   "OutputOptions": {
      "Format": "{{string}}",
      "Location": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_geojobs_StartJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geojobs_StartJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-Action"></a>
The action to perform on the input data.
Type: String
Valid Values: `ValidateAddress`
Required: Yes

 ** [ActionOptions](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-ActionOptions"></a>
Additional parameters that can be requested for each result.
Type: [JobActionOptions](API_geojobs_JobActionOptions.md) object
Required: No

 ** [ClientToken](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-ClientToken"></a>
A unique identifier for this request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [ExecutionRoleArn](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.
The IAM role must be created in the same AWS account where you plan to run your job.
For more information about configuring IAM roles for Amazon Location jobs, see [Configure IAM permissions](https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html) in the *Amazon Location Service Developer Guide*.
Type: String
Required: Yes

 ** [InputOptions](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-InputOptions"></a>
Configuration for input data location and format.
Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.
Type: [JobInputOptions](API_geojobs_JobInputOptions.md) object
Required: Yes

 ** [Name](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-Name"></a>
An optional name for the job resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: No

 ** [OutputOptions](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-OutputOptions"></a>
Configuration for output data location and format.
Type: [JobOutputOptions](API_geojobs_JobOutputOptions.md) object
Required: Yes

 ** [Tags](#API_geojobs_StartJob_RequestSyntax) **   <a name="location-geojobs_StartJob-request-Tags"></a>
Tags and corresponding values to be associated with the job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_geojobs_StartJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": "string",
   "JobArn": "string",
   "JobId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_geojobs_StartJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_geojobs_StartJob_ResponseSyntax) **   <a name="location-geojobs_StartJob-response-CreatedAt"></a>
Job creation time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [JobArn](#API_geojobs_StartJob_ResponseSyntax) **   <a name="location-geojobs_StartJob-response-JobArn"></a>
The Amazon Resource Name (ARN) for the job resource. Used when you need to specify a resource across all AWS.
Format example: `arn:aws:geo:region:account-id:job/ExampleJob`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [JobId](#API_geojobs_StartJob_ResponseSyntax) **   <a name="location-geojobs_StartJob-response-JobId"></a>
Unique job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`

 ** [Status](#API_geojobs_StartJob_ResponseSyntax) **   <a name="location-geojobs_StartJob-response-Status"></a>
Initial job status (always "Pending" for new jobs).
Type: String
Valid Values: `Pending | Running | Completed | Failed | Cancelling | Cancelled`

## Errors
<a name="API_geojobs_StartJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.
HTTP Status Code: 400

## See Also
<a name="API_geojobs_StartJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geojobs-2020-11-19/StartJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geojobs-2020-11-19/StartJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/StartJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geojobs-2020-11-19/StartJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/StartJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geojobs-2020-11-19/StartJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geojobs-2020-11-19/StartJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geojobs-2020-11-19/StartJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geojobs-2020-11-19/StartJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/StartJob)
