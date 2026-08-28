---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobExecution.html
---

# DescribeJobExecution
<a name="API_DescribeJobExecution"></a>

Describes a job execution.

Requires permission to access the [DescribeJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeJobExecution_RequestSyntax"></a>

```
GET /things/{{thingName}}/jobs/{{jobId}}?executionNumber={{executionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionNumber](#API_DescribeJobExecution_RequestSyntax) **   <a name="iot-DescribeJobExecution-request-uri-executionNumber"></a>
A string (consisting of the digits "0" through "9" which is used to specify a particular job execution on a particular device.

 ** [jobId](#API_DescribeJobExecution_RequestSyntax) **   <a name="iot-DescribeJobExecution-request-uri-jobId"></a>
The unique identifier you assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [thingName](#API_DescribeJobExecution_RequestSyntax) **   <a name="iot-DescribeJobExecution-request-uri-thingName"></a>
The name of the thing on which the job execution is running.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeJobExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "execution": {
      "approximateSecondsBeforeTimedOut": number,
      "executionNumber": number,
      "forceCanceled": boolean,
      "jobId": "string",
      "lastUpdatedAt": number,
      "queuedAt": number,
      "startedAt": number,
      "status": "string",
      "statusDetails": {
         "detailsMap": {
            "string" : "string"
         }
      },
      "thingArn": "string",
      "versionNumber": number
   }
}
```

## Response Elements
<a name="API_DescribeJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [execution](#API_DescribeJobExecution_ResponseSyntax) **   <a name="iot-DescribeJobExecution-response-execution"></a>
Information about the job execution.
Type: [JobExecution](API_JobExecution.md) object

## Errors
<a name="API_DescribeJobExecution_Errors"></a>

 ** InvalidRequestException **
The request is not valid.
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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeJobExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
