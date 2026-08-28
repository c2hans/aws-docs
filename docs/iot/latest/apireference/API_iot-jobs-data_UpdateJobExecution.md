---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_UpdateJobExecution.html
---

# UpdateJobExecution
<a name="API_iot-jobs-data_UpdateJobExecution"></a>

Updates the status of a job execution.

Requires permission to access the [UpdateJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotjobsdataplane.html) action.

## Request Syntax
<a name="API_iot-jobs-data_UpdateJobExecution_RequestSyntax"></a>

```
POST /things/{{thingName}}/jobs/{{jobId}} HTTP/1.1
Content-type: application/json

{
   "executionNumber": {{number}},
   "expectedVersion": {{number}},
   "includeJobDocument": {{boolean}},
   "includeJobExecutionState": {{boolean}},
   "status": "{{string}}",
   "statusDetails": {
      "{{string}}" : "{{string}}"
   },
   "stepTimeoutInMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_iot-jobs-data_UpdateJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-uri-jobId"></a>
The unique identifier assigned to this job when it was created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [thingName](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-uri-thingName"></a>
The name of the thing associated with the device.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_iot-jobs-data_UpdateJobExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [executionNumber](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-executionNumber"></a>
Optional. A number that identifies a particular job execution on a particular device.
Type: Long
Required: No

 ** [expectedVersion](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-expectedVersion"></a>
Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)
Type: Long
Required: No

 ** [includeJobDocument](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-includeJobDocument"></a>
Optional. When set to true, the response contains the job document. The default is false.
Type: Boolean
Required: No

 ** [includeJobExecutionState](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-includeJobExecutionState"></a>
Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.
Type: Boolean
Required: No

 ** [status](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-status"></a>
The new status for the job execution (IN\_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: Yes

 ** [statusDetails](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-statusDetails"></a>
 Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
The maximum length of the value in the name/value pair is 1,024 characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** [stepTimeoutInMinutes](#API_iot-jobs-data_UpdateJobExecution_RequestSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-request-stepTimeoutInMinutes"></a>
Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling `UpdateJobExecution`, setting the status to `IN_PROGRESS`, and specifying a new timeout value in this field) the job execution status will be automatically set to `TIMED_OUT`. Note that setting or resetting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (`CreateJob` using field `timeoutConfig`).
Valid values for this parameter range from 1 to 10080 (1 minute to 7 days). A value of -1 is also valid and will cancel the current step timer (created by an earlier use of `UpdateJobExecutionRequest`).
Type: Long
Required: No

## Response Syntax
<a name="API_iot-jobs-data_UpdateJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionState": {
      "status": "string",
      "statusDetails": {
         "string" : "string"
      },
      "versionNumber": number
   },
   "jobDocument": "string"
}
```

## Response Elements
<a name="API_iot-jobs-data_UpdateJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionState](#API_iot-jobs-data_UpdateJobExecution_ResponseSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-response-executionState"></a>
A JobExecutionState object.
Type: [JobExecutionState](API_iot-jobs-data_JobExecutionState.md) object

 ** [jobDocument](#API_iot-jobs-data_UpdateJobExecution_ResponseSyntax) **   <a name="iot-iot-jobs-data_UpdateJobExecution-response-jobDocument"></a>
The contents of the Job Documents.
Type: String
Length Constraints: Maximum length of 32768.

## Errors
<a name="API_iot-jobs-data_UpdateJobExecution_Errors"></a>

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

 ** InvalidStateTransitionException **
An update attempted to change the job execution to a state that is invalid because of the job execution's current state (for example, an attempt to change a request in state SUCCESS to state IN\_PROGRESS). In this case, the body of the error message also contains the executionState field.
HTTP Status Code: 409

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
The message associated with the exception.
 ** payload **
The payload associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_iot-jobs-data_UpdateJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-jobs-data-2017-09-29/UpdateJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/UpdateJobExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
