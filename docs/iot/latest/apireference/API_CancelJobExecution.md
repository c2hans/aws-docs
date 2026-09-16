---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJobExecution.html
---

# CancelJobExecution
<a name="API_CancelJobExecution"></a>

Cancels the execution of a job for a given thing.

Requires permission to access the [CancelJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CancelJobExecution_RequestSyntax"></a>

```
PUT /things/{{thingName}}/jobs/{{jobId}}/cancel?force={{force}} HTTP/1.1
Content-type: application/json

{
   "expectedVersion": {{number}},
   "statusDetails": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CancelJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [force](#API_CancelJobExecution_RequestSyntax) **   <a name="iot-CancelJobExecution-request-uri-force"></a>
(Optional) If `true` the job execution will be canceled if it has status IN\_PROGRESS or QUEUED, otherwise the job execution will be canceled only if it has status QUEUED. If you attempt to cancel a job execution that is IN\_PROGRESS, and you do not set `force` to `true`, then an `InvalidStateTransitionException` will be thrown. The default is `false`.
Canceling a job execution which is "IN\_PROGRESS", will cause the device to be unable to update the job execution status. Use caution and ensure that the device is able to recover to a valid state.

 ** [jobId](#API_CancelJobExecution_RequestSyntax) **   <a name="iot-CancelJobExecution-request-uri-jobId"></a>
The ID of the job to be canceled.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [thingName](#API_CancelJobExecution_RequestSyntax) **   <a name="iot-CancelJobExecution-request-uri-thingName"></a>
The name of the thing whose execution of the job will be canceled.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CancelJobExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedVersion](#API_CancelJobExecution_RequestSyntax) **   <a name="iot-CancelJobExecution-request-expectedVersion"></a>
(Optional) The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)
Type: Long
Required: No

 ** [statusDetails](#API_CancelJobExecution_RequestSyntax) **   <a name="iot-CancelJobExecution-request-statusDetails"></a>
A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. You can specify at most 10 name/value pairs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

## Response Syntax
<a name="API_CancelJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelJobExecution_Errors"></a>

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidStateTransitionException **
An attempt was made to change to an invalid state, for example by deleting a job or a job execution which is "IN\_PROGRESS" without setting the `force` parameter.
 ** message **
The message for the exception.
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
The message for the exception.
HTTP Status Code: 400

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_CancelJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CancelJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CancelJobExecution)
