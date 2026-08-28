---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_RegisterAppInstanceUserEndpoint.html
---

# RegisterAppInstanceUserEndpoint
<a name="API_RegisterAppInstanceUserEndpoint"></a>

Registers an endpoint under an Amazon Chime `AppInstanceUser`. The endpoint receives messages for a user. For push notifications, the endpoint is a mobile device used to receive mobile push notifications for a user.

## Request Syntax
<a name="API_RegisterAppInstanceUserEndpoint_RequestSyntax"></a>

```
POST /app-instance-users/{{appInstanceUserArn}}/endpoints HTTP/1.1
Content-type: application/json

{
   "AllowMessages": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "EndpointAttributes": {
      "DeviceToken": "{{string}}",
      "VoipDeviceToken": "{{string}}"
   },
   "Name": "{{string}}",
   "ResourceArn": "{{string}}",
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterAppInstanceUserEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceUserArn](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-uri-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_RegisterAppInstanceUserEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowMessages](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-AllowMessages"></a>
Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. `ALL` indicates the endpoint receives all messages. `NONE` indicates the endpoint receives no messages.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** [ClientRequestToken](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-ClientRequestToken"></a>
The unique ID assigned to the request. Use different tokens to register other endpoints.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [EndpointAttributes](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-EndpointAttributes"></a>
The attributes of an `Endpoint`.
Type: [EndpointAttributes](API_EndpointAttributes.md) object
Required: Yes

 ** [Name](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-Name"></a>
The name of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*`
Required: No

 ** [ResourceArn](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-ResourceArn"></a>
The ARN of the resource to which the endpoint belongs.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [Type](#API_RegisterAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-request-Type"></a>
The type of the `AppInstanceUserEndpoint`. Supported types:
+  `APNS`: The mobile notification service for an Apple device.
+  `APNS_SANDBOX`: The sandbox environment of the mobile notification service for an Apple device.
+  `GCM`: The mobile notification service for an Android device.
Populate the `ResourceArn` value of each type as `PinpointAppArn`.
Type: String
Valid Values: `APNS | APNS_SANDBOX | GCM`
Required: Yes

## Response Syntax
<a name="API_RegisterAppInstanceUserEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AppInstanceUserArn": "string",
   "EndpointId": "string"
}
```

## Response Elements
<a name="API_RegisterAppInstanceUserEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceUserArn](#API_RegisterAppInstanceUserEndpoint_ResponseSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-response-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [EndpointId](#API_RegisterAppInstanceUserEndpoint_ResponseSyntax) **   <a name="chimesdk-RegisterAppInstanceUserEndpoint-response-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`

## Errors
<a name="API_RegisterAppInstanceUserEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_RegisterAppInstanceUserEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/RegisterAppInstanceUserEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
