---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_CancelJob.html
---

# CancelJob
<a name="API_geojobs_CancelJob"></a>

 `CancelJob` cancels a job that is currently running or pending. If the job is already in a terminal state (`Completed`, `Failed`, or `Cancelled`), the operation returns successfully with the current status.

For more information, see [Job concepts](https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geojobs_CancelJob_RequestSyntax"></a>

```
POST /metadata/v0/jobs/cancel-job HTTP/1.1
Content-type: application/json

{
   "JobId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geojobs_CancelJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geojobs_CancelJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [JobId](#API_geojobs_CancelJob_RequestSyntax) **   <a name="location-geojobs_CancelJob-request-JobId"></a>
The unique identifier of the job to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`
Required: Yes

## Response Syntax
<a name="API_geojobs_CancelJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobArn": "string",
   "JobId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_geojobs_CancelJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobArn](#API_geojobs_CancelJob_ResponseSyntax) **   <a name="location-geojobs_CancelJob-response-JobArn"></a>
Amazon Resource Name (ARN) of the cancelled job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`

 ** [JobId](#API_geojobs_CancelJob_ResponseSyntax) **   <a name="location-geojobs_CancelJob-response-JobId"></a>
Unique job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[-._\w]+`

 ** [Status](#API_geojobs_CancelJob_ResponseSyntax) **   <a name="location-geojobs_CancelJob-response-Status"></a>
Job status after cancellation request.
Type: String
Valid Values: `Pending | Running | Completed | Failed | Cancelling | Cancelled`

## Errors
<a name="API_geojobs_CancelJob_Errors"></a>

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
<a name="API_geojobs_CancelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geojobs-2020-11-19/CancelJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/CancelJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
