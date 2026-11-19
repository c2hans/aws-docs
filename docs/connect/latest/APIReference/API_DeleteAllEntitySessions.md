---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteAllEntitySessions.html
---

# DeleteAllEntitySessions

Deletes all active sessions for the specified entity in the specified Connect Customer instance. The operation supports only the `USER` entity type, so you can use it to sign out all of a user's active sessions. Use it when you need to end a user's access right away, for example when they leave your organization or you suspect that their credentials are compromised.

## Request Syntax
<a name="API_DeleteAllEntitySessions_RequestSyntax"></a>

```
POST /auth/sessions/delete-all-entity-sessions HTTP/1.1
Content-type: application/json

{
   "EntityId": "{{string}}",
   "EntityType": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteAllEntitySessions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAllEntitySessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EntityId](#API_DeleteAllEntitySessions_RequestSyntax) **   <a name="connect-DeleteAllEntitySessions-request-EntityId"></a>
The identifier of the entity whose sessions you want to delete. For `USER`, use the user ID or the user ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** [EntityType](#API_DeleteAllEntitySessions_RequestSyntax) **   <a name="connect-DeleteAllEntitySessions-request-EntityType"></a>
The type of entity whose sessions you want to delete.
The only valid value is `USER`, which signs out a user in your Connect Customer instance.
Type: String
Valid Values: `USER`
Required: Yes

 ** [InstanceId](#API_DeleteAllEntitySessions_RequestSyntax) **   <a name="connect-DeleteAllEntitySessions-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_DeleteAllEntitySessions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAllEntitySessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAllEntitySessions_Errors"></a>

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
<a name="API_DeleteAllEntitySessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteAllEntitySessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteAllEntitySessions)
