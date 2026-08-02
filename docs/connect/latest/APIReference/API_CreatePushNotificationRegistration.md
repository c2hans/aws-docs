---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePushNotificationRegistration.html
---

# CreatePushNotificationRegistration
<a name="API_CreatePushNotificationRegistration"></a>

Creates registration for a device token and a chat contact to receive real-time push notifications. For more information about push notifications, see [Set up push notifications in Connect Customer for mobile chat](https://docs.aws.amazon.com/connect/latest/adminguide/enable-push-notifications-for-mobile-chat.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_CreatePushNotificationRegistration_RequestSyntax"></a>

```
PUT /push-notification/{{InstanceId}}/registrations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ContactConfiguration": {
      "ContactId": "{{string}}",
      "IncludeRawMessage": {{boolean}},
      "ParticipantRole": "{{string}}"
   },
   "DeviceToken": "{{string}}",
   "DeviceType": "{{string}}",
   "PinpointAppArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePushNotificationRegistration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreatePushNotificationRegistration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactConfiguration](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-ContactConfiguration"></a>
The contact configuration for push notification registration.
Type: [ContactConfiguration](API_ContactConfiguration.md) object
Required: Yes

 ** [DeviceToken](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-DeviceToken"></a>
The push notification token issued by the Apple or Google gateways.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [DeviceType](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-DeviceType"></a>
The device type to use when sending the message.
Type: String
Valid Values: `GCM | APNS | APNS_SANDBOX`
Required: Yes

 ** [PinpointAppArn](#API_CreatePushNotificationRegistration_RequestSyntax) **   <a name="connect-CreatePushNotificationRegistration-request-PinpointAppArn"></a>
The Amazon Resource Name (ARN) of the Pinpoint application.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreatePushNotificationRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RegistrationId": "string"
}
```

## Response Elements
<a name="API_CreatePushNotificationRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegistrationId](#API_CreatePushNotificationRegistration_ResponseSyntax) **   <a name="connect-CreatePushNotificationRegistration-response-RegistrationId"></a>
The identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreatePushNotificationRegistration_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreatePushNotificationRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreatePushNotificationRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreatePushNotificationRegistration)
