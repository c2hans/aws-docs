---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJobExecution.html
---

# DeleteJobExecution
<a name="API_DeleteJobExecution"></a>

Deletes a job execution.

Requires permission to access the [DeleteJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteJobExecution_RequestSyntax"></a>

```
DELETE /things/{{thingName}}/jobs/{{jobId}}/executionNumber/{{executionNumber}}?force={{force}}&namespaceId={{namespaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteJobExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionNumber](#API_DeleteJobExecution_RequestSyntax) **   <a name="iot-DeleteJobExecution-request-uri-executionNumber"></a>
The ID of the job execution to be deleted. The `executionNumber` refers to the execution of a particular job on a particular device.
Note that once a job execution is deleted, the `executionNumber` may be reused by IoT, so be sure you get and use the correct value here.
Required: Yes

 ** [force](#API_DeleteJobExecution_RequestSyntax) **   <a name="iot-DeleteJobExecution-request-uri-force"></a>
(Optional) When true, you can delete a job execution which is "IN\_PROGRESS". Otherwise, you can only delete a job execution which is in a terminal state ("SUCCEEDED", "FAILED", "REJECTED", "REMOVED" or "CANCELED") or an exception will occur. The default is false.
Deleting a job execution which is "IN\_PROGRESS", will cause the device to be unable to access job information or update the job execution status. Use caution and ensure that the device is able to recover to a valid state.

 ** [jobId](#API_DeleteJobExecution_RequestSyntax) **   <a name="iot-DeleteJobExecution-request-uri-jobId"></a>
The ID of the job whose execution on a particular device will be deleted.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [namespaceId](#API_DeleteJobExecution_RequestSyntax) **   <a name="iot-DeleteJobExecution-request-uri-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Pattern: `[a-zA-Z0-9_-]+`

 ** [thingName](#API_DeleteJobExecution_RequestSyntax) **   <a name="iot-DeleteJobExecution-request-uri-thingName"></a>
The name of the thing whose job execution will be deleted.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DeleteJobExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteJobExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteJobExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteJobExecution_Errors"></a>

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

## See Also
<a name="API_DeleteJobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteJobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteJobExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
