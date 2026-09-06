---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserPhoneConfig.html
---

# UpdateUserPhoneConfig
<a name="API_UpdateUserPhoneConfig"></a>

Updates the phone configuration settings for the specified user.

**Note**
We recommend using the [UpdateUserConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserConfig.html) API, which supports additional functionality that is not available in the UpdateUserPhoneConfig API, such as voice enhancement settings and per-channel configuration for auto-accept and After Contact Work (ACW) timeouts. In comparison, the UpdateUserPhoneConfig API will always set the same ACW timeouts to all channels the user handles.

## Request Syntax
<a name="API_UpdateUserPhoneConfig_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/phone-config HTTP/1.1
Content-type: application/json

{
   "PhoneConfig": {
      "AfterContactWorkTimeLimit": {{number}},
      "AutoAccept": {{boolean}},
      "DeskPhoneNumber": "{{string}}",
      "PersistentConnection": {{boolean}},
      "PhoneType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateUserPhoneConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateUserPhoneConfig_RequestSyntax) **   <a name="connect-UpdateUserPhoneConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_UpdateUserPhoneConfig_RequestSyntax) **   <a name="connect-UpdateUserPhoneConfig-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_UpdateUserPhoneConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PhoneConfig](#API_UpdateUserPhoneConfig_RequestSyntax) **   <a name="connect-UpdateUserPhoneConfig-request-PhoneConfig"></a>
Information about phone configuration settings for the user.
Type: [UserPhoneConfig](API_UserPhoneConfig.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateUserPhoneConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateUserPhoneConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserPhoneConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateUserPhoneConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateUserPhoneConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateUserPhoneConfig)
