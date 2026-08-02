---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-apns_voip.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# APNs VoIP Channel
<a name="apps-application-id-channels-apns_voip"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the APNs VoIP channel to send VoIP notification messages to the Apple Push Notification service (APNs). Before you can use Amazon Pinpoint to send VoIP notification messages to APNs, you must enable the APNs VoIP channel for an Amazon Pinpoint application.

The APNs VoIP Channel resource represents the status and authentication settings of the APNs VoIP channel for a specific application. You can use this resource to enable, retrieve information about, update, or disable (delete) the APNs VoIP channel for an application.

## URI
<a name="apps-application-id-channels-apns_voip-url"></a>

`/v1/apps/{{application-id}}/channels/apns_voip`

## HTTP methods
<a name="apps-application-id-channels-apns_voip-http-methods"></a>

### GET
<a name="apps-application-id-channels-apns_voipget"></a>

**Operation ID:** `GetApnsVoipChannel`

Retrieves information about the status and settings of the APNs VoIP channel for an application.

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
| 200 | APNSVoipChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-channels-apns_voipput"></a>

**Operation ID:** `UpdateApnsVoipChannel`

Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.

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
| 200 | APNSVoipChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-channels-apns_voipdelete"></a>

**Operation ID:** `DeleteApnsVoipChannel`

Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.

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
| 200 | APNSVoipChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channels-apns_voipoptions"></a>

Retrieves information about the communication requirements and options that are available for the APNs VoIP Channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-apns_voip-schemas"></a>

### Request bodies
<a name="apps-application-id-channels-apns_voip-request-examples"></a>

#### PUT schema
<a name="apps-application-id-channels-apns_voip-request-body-put-example"></a>

```
{
  "Certificate": "string",
  "PrivateKey": "string",
  "Enabled": boolean,
  "TokenKeyId": "string",
  "TeamId": "string",
  "TokenKey": "string",
  "BundleId": "string",
  "DefaultAuthenticationMethod": "string"
}
```

### Response bodies
<a name="apps-application-id-channels-apns_voip-response-examples"></a>

#### APNSVoipChannelResponse schema
<a name="apps-application-id-channels-apns_voip-response-body-apnsvoipchannelresponse-example"></a>

```
{
  "ApplicationId": "string",
  "IsArchived": boolean,
  "Version": integer,
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "LastModifiedBy": "string",
  "Id": "string",
  "Enabled": boolean,
  "HasCredential": boolean,
  "Platform": "string",
  "HasTokenKey": boolean,
  "DefaultAuthenticationMethod": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-channels-apns_voip-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-apns_voip-properties"></a>

### APNSVoipChannelRequest
<a name="apps-application-id-channels-apns_voip-model-apnsvoipchannelrequest"></a>

Specifies the status and settings of the APNs (Apple Push Notification service) VoIP channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BundleId | string | False | The bundle identifier that's assigned to your iOS app. This identifier is used for APNs tokens. |
| Certificate | string | False | The APNs client certificate that you received from Apple, if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate. |
| DefaultAuthenticationMethod | string | False | The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs, key or certificate. |
| Enabled | boolean | False | Specifies whether to enable the APNs VoIP channel for the application. |
| PrivateKey | string | False | The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs. |
| TeamId | string | False | The identifier that's assigned to your Apple developer account team. This identifier is used for APNs tokens. |
| TokenKey | string | False | The authentication key to use for APNs tokens. |
| TokenKeyId | string | False | The key identifier that's assigned to your APNs signing key, if you want Amazon Pinpoint to communicate with APNs by using APNs tokens. |

### APNSVoipChannelResponse
<a name="apps-application-id-channels-apns_voip-model-apnsvoipchannelresponse"></a>

Provides information about the status and settings of the APNs (Apple Push Notification service) VoIP channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application that the APNs VoIP channel applies to. |
| CreationDate | string | False | The date and time when the APNs VoIP channel was enabled. |
| DefaultAuthenticationMethod | string | False | The default authentication method that Amazon Pinpoint uses to authenticate with APNs for this channel, key or certificate. |
| Enabled | boolean | False | Specifies whether the APNs VoIP channel is enabled for the application. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| HasTokenKey | boolean | False | Specifies whether the APNs VoIP channel is configured to communicate with APNs by using APNs tokens. To provide an authentication key for APNs tokens, set the `TokenKey` property of the channel. |
| Id | string | False | (Deprecated) An identifier for the APNs VoIP channel. This property is retained only for backward compatibility. |
| IsArchived | boolean | False | Specifies whether the APNs VoIP channel is archived. |
| LastModifiedBy | string | False | The user who last modified the APNs VoIP channel. |
| LastModifiedDate | string | False | The date and time when the APNs VoIP channel was last modified. |
| Platform | string | True | The type of messaging or notification platform for the channel. For the APNs VoIP channel, this value is `APNS_VOIP`. |
| Version | integer | False | The current version of the APNs VoIP channel. |

### MessageBody
<a name="apps-application-id-channels-apns_voip-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-channels-apns_voip-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApnsVoipChannel
<a name="GetApnsVoipChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetApnsVoipChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetApnsVoipChannel)

### UpdateApnsVoipChannel
<a name="UpdateApnsVoipChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateApnsVoipChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateApnsVoipChannel)

### DeleteApnsVoipChannel
<a name="DeleteApnsVoipChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteApnsVoipChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteApnsVoipChannel)
