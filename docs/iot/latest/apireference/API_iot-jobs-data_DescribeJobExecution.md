---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_DescribeJobExecution.html
---

# DescribeJobExecution
<a name="API_iot-jobs-data_DescribeJobExecution"></a>

Gets details of a job execution.

Requires permission to access the [DescribeJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-jobs-data_DescribeJobExecution_RequestSyntax"></a>

```
GET /things/{{thingName}}/jobs/{{jobId}}?executionNumber={{executionNumber}}&includeJobDocument={{includeJobDocument}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iot-jobs-data_DescribeJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionNumber](#API_iot-jobs-data_DescribeJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_DescribeJobExecution-request-uri-executionNumber"></a>
Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.

 ** [includeJobDocument](#API_iot-jobs-data_DescribeJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_DescribeJobExecution-request-uri-includeJobDocument"></a>
Optional. Unless set to false, the response contains the job document. The default is true.

 ** [jobId](#API_iot-jobs-data_DescribeJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_DescribeJobExecution-request-uri-jobId"></a>
The unique identifier assigned to this job when it was created.
Pattern: `[a-zA-Z0-9_-]+|^\$next`
Required: Yes

 ** [thingName](#API_iot-jobs-data_DescribeJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_DescribeJobExecution-request-uri-thingName"></a>
The thing name associated with the device the job execution is running on.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iot-jobs-data_DescribeJobExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iot-jobs-data_DescribeJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "execution": {
      "approximateSecondsBeforeTimedOut": number,
      "executionNumber": number,
      "jobDocument": "string",
      "jobId": "string",
      "lastUpdatedAt": number,
      "queuedAt": number,
      "startedAt": number,
      "status": "string",
      "statusDetails": {
         "string" : "string"
      },
      "thingName": "string",
      "versionNumber": number
   }
}
```

## Response Elements
<a name="API_iot-jobs-data_DescribeJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [execution](#API_iot-jobs-data_DescribeJobExecution_ResponseSyntax) **   <a name="iot-iot-jobs-data_DescribeJobExecution-response-execution"></a>
Contains data about a job execution.
Type: [JobExecution](API_iot-jobs-data_JobExecution.md) object

## Errors
<a name="API_iot-jobs-data_DescribeJobExecution_Errors"></a>

 ** CertificateValidationException **
The certificate is invalid.
 ** message **
Additional information about the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The contents of the request were invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** TerminalStateException **
The job is in a terminal state.
HTTP Status Code: 410

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message associated with the exception.
 ** payload **
The payload associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_iot-jobs-data_DescribeJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-jobs-data-2017-09-29/DescribeJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/DescribeJobExecution)
