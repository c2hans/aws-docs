---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUserEndpoint.html
---

# UpdateAppInstanceUserEndpoint
<a name="API_UpdateAppInstanceUserEndpoint"></a>

Updates the details of an `AppInstanceUserEndpoint`. You can update the name and `AllowMessage` values.

## Request Syntax
<a name="API_UpdateAppInstanceUserEndpoint_RequestSyntax"></a>

```
PUT /app-instance-users/{{appInstanceUserArn}}/endpoints/{{endpointId}} HTTP/1.1
Content-type: application/json

{
   "AllowMessages": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAppInstanceUserEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceUserArn](#API_UpdateAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-request-uri-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [endpointId](#API_UpdateAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-request-uri-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`
Required: Yes

## Request Body
<a name="API_UpdateAppInstanceUserEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowMessages](#API_UpdateAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-request-AllowMessages"></a>
Boolean that controls whether the `AppInstanceUserEndpoint` is opted in to receive messages. `ALL` indicates the endpoint will receive all messages. `NONE` indicates the endpoint will receive no messages.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** [Name](#API_UpdateAppInstanceUserEndpoint_RequestSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-request-Name"></a>
The name of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateAppInstanceUserEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceUserArn": "string",
   "EndpointId": "string"
}
```

## Response Elements
<a name="API_UpdateAppInstanceUserEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceUserArn](#API_UpdateAppInstanceUserEndpoint_ResponseSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-response-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [EndpointId](#API_UpdateAppInstanceUserEndpoint_ResponseSyntax) **   <a name="chimesdk-UpdateAppInstanceUserEndpoint-response-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`

## Errors
<a name="API_UpdateAppInstanceUserEndpoint_Errors"></a>

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
<a name="API_UpdateAppInstanceUserEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/UpdateAppInstanceUserEndpoint)
