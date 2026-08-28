---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SuspendContactRecording.html
---

# SuspendContactRecording
<a name="API_SuspendContactRecording"></a>

When a contact is being recorded, this API suspends recording whatever is selected in the flow configuration: call (IVR or agent), screen, or both. If only call recording or only screen recording is enabled, then it would be suspended. For example, you might suspend the screen recording while collecting sensitive information, such as a credit card number. Then use [ResumeContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_ResumeContactRecording.html) to restart recording the screen.

The period of time that the recording is suspended is filled with silence in the final recording.

 Voice (IVR, agent) and screen recordings are supported.

## Request Syntax
<a name="API_SuspendContactRecording_RequestSyntax"></a>

```
POST /contact/suspend-recording HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "ContactRecordingType": "{{string}}",
   "InitialContactId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SuspendContactRecording_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SuspendContactRecording_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_SuspendContactRecording_RequestSyntax) **   <a name="connect-SuspendContactRecording-request-ContactId"></a>
The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ContactRecordingType](#API_SuspendContactRecording_RequestSyntax) **   <a name="connect-SuspendContactRecording-request-ContactRecordingType"></a>
The type of recording being operated on.
Type: String
Valid Values: `AGENT | IVR | SCREEN`
Required: No

 ** [InitialContactId](#API_SuspendContactRecording_RequestSyntax) **   <a name="connect-SuspendContactRecording-request-InitialContactId"></a>
The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_SuspendContactRecording_RequestSyntax) **   <a name="connect-SuspendContactRecording-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_SuspendContactRecording_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SuspendContactRecording_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SuspendContactRecording_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidActiveRegionException **
This exception occurs when an API request is made to a non-active region in an Amazon Connect instance configured with Amazon Connect Global Resiliency. For example, if the active region is US West (Oregon) and a request is made to US East (N. Virginia), the exception will be returned.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_SuspendContactRecording_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SuspendContactRecording)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SuspendContactRecording)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
