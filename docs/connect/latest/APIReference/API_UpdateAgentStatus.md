---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateAgentStatus.html
---

# UpdateAgentStatus
<a name="API_UpdateAgentStatus"></a>

Updates agent status.

## Request Syntax
<a name="API_UpdateAgentStatus_RequestSyntax"></a>

```
POST /agent-status/{{InstanceId}}/{{AgentStatusId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "DisplayOrder": {{number}},
   "Name": "{{string}}",
   "ResetOrderNumber": {{boolean}},
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AgentStatusId](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-uri-AgentStatusId"></a>
The identifier of the agent status.
Required: Yes

 ** [InstanceId](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateAgentStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-Description"></a>
The description of the agent status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Required: No

 ** [DisplayOrder](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-DisplayOrder"></a>
The display order of the agent status.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Name](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-Name"></a>
The name of the agent status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** [ResetOrderNumber](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-ResetOrderNumber"></a>
A number indicating the reset order of the agent status.
Type: Boolean
Required: No

 ** [State](#API_UpdateAgentStatus_RequestSyntax) **   <a name="connect-UpdateAgentStatus-request-State"></a>
The state of the agent status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateAgentStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAgentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAgentStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAgentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateAgentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateAgentStatus)
