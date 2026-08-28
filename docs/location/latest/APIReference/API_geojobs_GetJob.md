---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_GetJob.html
---

# GetJob
<a name="API_geojobs_GetJob"></a>

 `GetJob` retrieves detailed information about a specific job, including its current status, configuration, and error information if the job failed.

For more information, see [Job concepts](https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geojobs_GetJob_RequestSyntax"></a>

```
GET /metadata/v0/jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geojobs_GetJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_geojobs_GetJob_RequestSyntax) **   <a name="location-geojobs_GetJob-request-uri-JobId"></a>
The unique identifier of the job to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_geojobs_GetJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geojobs_GetJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Action": "string",
   "ActionOptions": {
      "ValidateAddress": {
         "AdditionalFeatures": [ "string" ]
      }
   },
   "CreatedAt": "string",
   "EndedAt": "string",
   "Error": {
      "Code": "string",
      "Messages": [ "string" ]
   },
   "ExecutionRoleArn": "string",
   "InputOptions": {
      "Format": "string",
      "Location": "string"
   },
   "JobArn": "string",
   "JobId": "string",
   "Name": "string",
   "OutputOptions": {
      "Format": "string",
      "Location": "string"
   },
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_geojobs_GetJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-Action"></a>
Action performed by the job.
Type: String
Valid Values: `ValidateAddress`

 ** [ActionOptions](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-ActionOptions"></a>
Additional options for configuring job action parameters.
Type: [JobActionOptions](API_geojobs_JobActionOptions.md) object

 ** [CreatedAt](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-CreatedAt"></a>
Job creation time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

 ** [EndedAt](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-EndedAt"></a>
Job completion time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`. Only returned for jobs in a terminal status: `Completed` \| `Failed` \| `Cancelled`.
Type: Timestamp

 ** [Error](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-Error"></a>
Error information if the job failed.
Type: [JobError](API_geojobs_JobError.md) object

 ** [ExecutionRoleArn](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-ExecutionRoleArn"></a>
IAM role used for permissions when running the job.
Type: String

 ** [InputOptions](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-InputOptions"></a>
Input configuration.
Type: [JobInputOptions](API_geojobs_JobInputOptions.md) object

 ** [JobArn](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-JobArn"></a>
Amazon Resource Name (ARN) of the specified job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [JobId](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-JobId"></a>
Unique job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`

 ** [Name](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-Name"></a>
Job name (if provided during creation).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`

 ** [OutputOptions](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-OutputOptions"></a>
Output configuration.
Type: [JobOutputOptions](API_geojobs_JobOutputOptions.md) object

 ** [Status](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-Status"></a>
Current job status.
Type: String
Valid Values: `Pending | Running | Completed | Failed | Cancelling | Cancelled`

 ** [Tags](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-Tags"></a>
Tags and corresponding values associated with the specified job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`

 ** [UpdatedAt](#API_geojobs_GetJob_ResponseSyntax) **   <a name="location-geojobs_GetJob-response-UpdatedAt"></a>
Last update time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp

## Errors
<a name="API_geojobs_GetJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource associated with the request could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.
HTTP Status Code: 400

## See Also
<a name="API_geojobs_GetJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geojobs-2020-11-19/GetJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geojobs-2020-11-19/GetJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/GetJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geojobs-2020-11-19/GetJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/GetJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geojobs-2020-11-19/GetJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geojobs-2020-11-19/GetJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geojobs-2020-11-19/GetJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geojobs-2020-11-19/GetJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/GetJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
