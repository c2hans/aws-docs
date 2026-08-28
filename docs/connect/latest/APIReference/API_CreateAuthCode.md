---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateAuthCode.html
---

# CreateAuthCode
<a name="API_CreateAuthCode"></a>

Creates an authorization code for the specified Connect Customer instance. The authorization code can be used to establish a session with scoped permissions defined by the specified scope parameters.

## Request Syntax
<a name="API_CreateAuthCode_RequestSyntax"></a>

```
POST /auth/code/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "MaxSessionDurationMinutes": {{number}},
   "Scope": {
      "DomainName": "{{string}}",
      "EntityId": "{{string}}",
      "EntityType": "{{string}}",
      "SecurityProfileIds": [ "{{string}}" ]
   },
   "SessionInactivityDurationMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateAuthCode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateAuthCode_RequestSyntax) **   <a name="connect-CreateAuthCode-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateAuthCode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxSessionDurationMinutes](#API_CreateAuthCode_RequestSyntax) **   <a name="connect-CreateAuthCode-request-MaxSessionDurationMinutes"></a>
The maximum duration of the session, in minutes. Minimum value of 1440 (24 hours). Maximum value of 43200 (30 days). If no value is provided, the session will expire after 400 days.
Type: Integer
Valid Range: Minimum value of 1440. Maximum value of 43200.
Required: No

 ** [Scope](#API_CreateAuthCode_RequestSyntax) **   <a name="connect-CreateAuthCode-request-Scope"></a>
The scope for the authorization code. Defines the permissions and access boundaries for the session.
Type: [AuthScope](API_AuthScope.md) object
Required: Yes

 ** [SessionInactivityDurationMinutes](#API_CreateAuthCode_RequestSyntax) **   <a name="connect-CreateAuthCode-request-SessionInactivityDurationMinutes"></a>
The duration of inactivity, in minutes, after which the session expires. Minimum value of 1440 (24 hours). Maximum value of 20160 (14 days).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20160.
Required: Yes

## Response Syntax
<a name="API_CreateAuthCode_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthCode": "string",
   "EntityId": "string",
   "EntityType": "string",
   "SessionId": "string"
}
```

## Response Elements
<a name="API_CreateAuthCode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthCode](#API_CreateAuthCode_ResponseSyntax) **   <a name="connect-CreateAuthCode-response-AuthCode"></a>
The authorization code to use for establishing a session.
Type: String

 ** [EntityId](#API_CreateAuthCode_ResponseSyntax) **   <a name="connect-CreateAuthCode-response-EntityId"></a>
The identifier of the entity associated with the authorization code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`

 ** [EntityType](#API_CreateAuthCode_ResponseSyntax) **   <a name="connect-CreateAuthCode-response-EntityType"></a>
The type of entity associated with the authorization code.
Type: String
Valid Values: `CUSTOMER_PROFILE`

 ** [SessionId](#API_CreateAuthCode_ResponseSyntax) **   <a name="connect-CreateAuthCode-response-SessionId"></a>
The identifier of the session created with the authorization code.
Type: String
Length Constraints: Maximum length of 36.

## Errors
<a name="API_CreateAuthCode_Errors"></a>

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
<a name="API_CreateAuthCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateAuthCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateAuthCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
