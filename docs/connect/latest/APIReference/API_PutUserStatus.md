---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PutUserStatus.html
---

# PutUserStatus
<a name="API_PutUserStatus"></a>

Changes the current status of a user or agent in Connect Customer. If the agent is currently handling a contact, this sets the agent's next status.

For more information, see [Agent status](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html) and [Set your next status](https://docs.aws.amazon.com/connect/latest/adminguide/set-next-status.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_PutUserStatus_RequestSyntax"></a>

```
PUT /users/{{InstanceId}}/{{UserId}}/status HTTP/1.1
Content-type: application/json

{
   "AgentStatusId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutUserStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_PutUserStatus_RequestSyntax) **   <a name="connect-PutUserStatus-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_PutUserStatus_RequestSyntax) **   <a name="connect-PutUserStatus-request-uri-UserId"></a>
The identifier of the user.
Required: Yes

## Request Body
<a name="API_PutUserStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AgentStatusId](#API_PutUserStatus_RequestSyntax) **   <a name="connect-PutUserStatus-request-AgentStatusId"></a>
The identifier of the agent status.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutUserStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutUserStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutUserStatus_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_PutUserStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/PutUserStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PutUserStatus)
