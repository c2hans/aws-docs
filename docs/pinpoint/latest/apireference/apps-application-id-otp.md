---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-otp.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# OTP Message
<a name="apps-application-id-otp"></a>

Use this resource to generate a One-Time Password (OTP) and send it to a user of your application. When the user enters the OTP code in your application, use the the [Verify OTP](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html) resource to confirm the validity of the OTP.

## URI
<a name="apps-application-id-otp-url"></a>

`/v1/apps/{{application-id}}/otp`

## HTTP methods
<a name="apps-application-id-otp-http-methods"></a>

### POST
<a name="apps-application-id-otppost"></a>

**Operation ID:** `SendOTPMessage`

Use this operation to send an OTP code to a user of your application. When you use this API, Amazon Pinpoint generates a random code and sends it to your user.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | MessageResponse | 200 response |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-otpoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-otp-schemas"></a>

### Request bodies
<a name="apps-application-id-otp-request-examples"></a>

#### POST schema
<a name="apps-application-id-otp-request-body-post-example"></a>

```
{
  "Channel": "string",
  "OriginationIdentity": "string",
  "DestinationIdentity": "string",
  "BrandName": "string",
  "Language": "string",
  "CodeLength": integer,
  "ValidityPeriod": integer,
  "ReferenceId": "string",
  "AllowedAttempts": integer,
  "EntityId": "string",
  "TemplateId": "string"
}
```

### Response bodies
<a name="apps-application-id-otp-response-examples"></a>

#### MessageResponse schema
<a name="apps-application-id-otp-response-body-messageresponse-example"></a>

```
{
  "ApplicationId": "string",
  "RequestId": "string",
  "Result": {
  },
  "EndpointResult": {
  }
}
```

#### MessageBody schema
<a name="apps-application-id-otp-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-otp-properties"></a>

### EndpointMessageResult
<a name="apps-application-id-otp-model-endpointmessageresult"></a>

Provides information about the delivery status and results of sending a message directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Address | string | False | The endpoint address that the message was delivered to. |
| DeliveryStatus | string<br />Values: `SUCCESSFUL \| THROTTLED \| TEMPORARY_FAILURE \| PERMANENT_FAILURE \| UNKNOWN_FAILURE \| OPT_OUT \| DUPLICATE` | True | The delivery status of the message. Possible values are:+   `DUPLICATE` – The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `OPT_OUT` – The SendMessages API does not honor the endpoint OPT\_OUT status.  <br />+   `PERMANENT_FAILURE` – An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again. <br />+   `SUCCESSFUL` – The message was successfully delivered to the endpoint. <br />+   `TEMPORARY_FAILURE` – A temporary error occurred. Amazon Pinpoint won't attempt to send the message again. <br />+   `THROTTLED` – Amazon Pinpoint throttled the operation to send the message to the endpoint. <br />+   `UNKNOWN_FAILURE` – An unknown error occurred.  |
| MessageId | string | False | The unique identifier for the message that was sent. |
| StatusCode | integer | True | The downstream service status code for delivering the message. |
| StatusMessage | string | False | The status message for delivering the message. |
| UpdatedToken | string | False | For push notifications that are sent through the GCM channel, specifies whether the endpoint's device registration token was updated as part of delivering the message. |

### MessageBody
<a name="apps-application-id-otp-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MessageResponse
<a name="apps-application-id-otp-model-messageresponse"></a>

Provides information about the results of a request to send a message to an endpoint address.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that was used to send the message. |
| EndpointResult | object | False | A map that contains a multipart response for each address that the message was sent to. In the map, the endpoint ID is the key and the result is the value. |
| RequestId | string | False | The identifier for the original request that the message was delivered for. |
| Result | object | False | A map that contains a multipart response for each address (email address, phone number, or push notification token) that the message was sent to. In the map, the address is the key and the result is the value. |

### MessageResult
<a name="apps-application-id-otp-model-messageresult"></a>

Provides information about the results of sending a message directly to an endpoint address.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryStatus | string<br />Values: `SUCCESSFUL \| THROTTLED \| TEMPORARY_FAILURE \| PERMANENT_FAILURE \| UNKNOWN_FAILURE \| OPT_OUT \| DUPLICATE` | True | The delivery status of the message. Possible values are:+   `DUPLICATE` – The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `OPT_OUT` – The SendMessages API does not honor the OPT\_OUT attribute when sending to endpoints and therefore will not use the OPT\_OUT message status. <br />+   `PERMANENT_FAILURE` – An error occurred when delivering the message to the endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `SUCCESSFUL` – The message was successfully delivered to the endpoint address. <br />+   `TEMPORARY_FAILURE` – A temporary error occurred. Amazon Pinpoint won't attempt to send the message again. <br />+   `THROTTLED` – Amazon Pinpoint throttled the operation to send the message to the endpoint address. <br />+   `UNKNOWN_FAILURE` – An unknown error occurred.  |
| MessageId | string | False | The unique identifier for the message that was sent. |
| StatusCode | integer | True | The downstream service status code for delivering the message. |
| StatusMessage | string | False | The status message for delivering the message. |
| UpdatedToken | string | False | For push notifications that are sent through the GCM channel, specifies whether the endpoint's device registration token was updated as part of delivering the message. |

### SendOTPMessageRequestParameters
<a name="apps-application-id-otp-model-sendotpmessagerequestparameters"></a>

Specifies the details of and parameters for the OTP that you are generating.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AllowedAttempts | integer | False | The number of times the recipient can unsuccessfully attempt to validate the OTP. If the number of attempts exceeds this value, the OTP automatically becomes invalid. The maximum number of allowed attempts is 5. The default value is 3 attempts. |
| BrandName | string | False | The name of the brand, company, or product that is associated with the OTP code. This name can contain up to 20 characters. Amazon Pinpoint automatically adds the brand name to the OTP message that it sends. |
| Channel | string | True | The communication channel that the OTP code is sent through. Currently, only SMS messages are supported, so the only acceptable value is `SMS`. |
| CodeLength | integer | False | The number of digits that will be in the OTP code that's sent to the recipient. OTP codes can contain between 5 and 8 digits, inclusive. The default value is 6 digits. |
| DestinationIdentity | string | True | The phone number, in E.164 format, that the OTP code was sent to. |
| EntityId | string | False | An Entity ID that is registered with a regulatory agency. This is currently only used when sending messages to recipients in India. If you aren't sending to recipients in India, you can omit this parameter. |
| Language | string | False | The language, in IETF BCP-47 format, to use when sending the message. Acceptable values are:+  `de-DE` – German <br />+  `en-GB` – English (UK) <br />+  `en-US` – English (US) <br />+  `es-419` – Spanish (Latin America) <br />+  `es-ES` – Spanish <br />+  `fr-CA` – French (Canada) <br />+  `fr-FR` – French <br />+  `ja-JP` – Japanese <br />+  `ko-KR` – Korean <br />+  `pt-BR` – Portuguese (Brazil) <br />+  `zh-CN` – Chinese (Simplified) <br />+  `zh-TW` – Chinese (Traditional)  |
| OriginationIdentity | string | True | The originating identity (such as a long code, short code, or sender ID) that is used to send the OTP code. If you use a long code or toll-free number to send the OTP, the phone number must be in E.164 format. |
| ReferenceId | string | True | A unique reference ID for the request. The reference ID exactly match the reference ID that you provide when you validate the OTP. The reference ID can contain between 1 and 48 characters, inclusive. For security purposes, you should use a reference ID that is unique to the application that is sending the OTP code. |
| TemplateId | string | False | A Template ID that is registered with a regulatory agency. This is currently only used when sending messages to recipients in India. If you aren't sending to recipients in India, you can omit this parameter. |
| ValidityPeriod | integer | False | The amount of time, in minutes, that the OTP code will be valid. The validity period can be between 5 and 60 minutes, inclusive. The default value is 15 minutes. |

## See also
<a name="apps-application-id-otp-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### SendOTPMessage
<a name="SendOTPMessage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/SendOTPMessage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/SendOTPMessage)
