---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html
---

# GetDashboardForJobRun
<a name="API_GetDashboardForJobRun"></a>

Creates and returns a URL that you can use to access the application UIs for a job run.

For jobs in a running state, the application UI is a live user interface such as the Spark or Tez web UI. For completed jobs, the application UI is a persistent application user interface such as the Spark History Server or persistent Tez UI.

**Note**
The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.

## Request Syntax
<a name="API_GetDashboardForJobRun_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/jobruns/{{jobRunId}}/dashboard?accessSystemProfileLogs={{accessSystemProfileLogs}}&attempt={{attempt}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDashboardForJobRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessSystemProfileLogs](#API_GetDashboardForJobRun_RequestSyntax) **   <a name="emrserverless-GetDashboardForJobRun-request-uri-accessSystemProfileLogs"></a>
Allows access to system profile logs for Lake Formation-enabled jobs. Default is false.

 ** [applicationId](#API_GetDashboardForJobRun_RequestSyntax) **   <a name="emrserverless-GetDashboardForJobRun-request-uri-applicationId"></a>
The ID of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [attempt](#API_GetDashboardForJobRun_RequestSyntax) **   <a name="emrserverless-GetDashboardForJobRun-request-uri-attempt"></a>
An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.
Valid Range: Minimum value of 1.

 ** [jobRunId](#API_GetDashboardForJobRun_RequestSyntax) **   <a name="emrserverless-GetDashboardForJobRun-request-uri-jobRunId"></a>
The ID of the job run.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetDashboardForJobRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDashboardForJobRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "url": "string"
}
```

## Response Elements
<a name="API_GetDashboardForJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [url](#API_GetDashboardForJobRun_ResponseSyntax) **   <a name="emrserverless-GetDashboardForJobRun-response-url"></a>
The URL to view job run's dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_GetDashboardForJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetDashboardForJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetDashboardForJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetDashboardForJobRun)
