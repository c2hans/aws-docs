---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactMediaProcessing.html
---

# StopContactMediaProcessing
<a name="API_StopContactMediaProcessing"></a>

 Stops in-flight message processing for an ongoing chat session.

## Request Syntax
<a name="API_StopContactMediaProcessing_RequestSyntax"></a>

```
POST /contact/stop-contact-media-processing HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopContactMediaProcessing_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopContactMediaProcessing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_StopContactMediaProcessing_RequestSyntax) **   <a name="connect-StopContactMediaProcessing-request-ContactId"></a>
 The identifier of the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [InstanceId](#API_StopContactMediaProcessing_RequestSyntax) **   <a name="connect-StopContactMediaProcessing-request-InstanceId"></a>
 The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_StopContactMediaProcessing_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopContactMediaProcessing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopContactMediaProcessing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StopContactMediaProcessing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StopContactMediaProcessing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StopContactMediaProcessing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
