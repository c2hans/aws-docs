---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-gcm.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# GCM Channel
<a name="apps-application-id-channels-gcm"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the GCM channel to send push notification messages to the Firebase Cloud Messaging (FCM) service, which replaces the Google Cloud Messaging (GCM) service. Before you can use Amazon Pinpoint to send notification messages to FCM, you must enable the GCM channel for an Amazon Pinpoint application.

The GCM Channel resource represents the status and authentication settings of the GCM channel for a specific application. You can use this resource to enable, retrieve information about, update, or disable (delete) the GCM channel for an application.

## URI
<a name="apps-application-id-channels-gcm-url"></a>

`/v1/apps/{{application-id}}/channels/gcm`

## HTTP methods
<a name="apps-application-id-channels-gcm-http-methods"></a>

### GET
<a name="apps-application-id-channels-gcmget"></a>

**Operation ID:** `GetGcmChannel`

Retrieves information about the status and settings of the GCM channel for an application.

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
| 200 | GCMChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-channels-gcmput"></a>

**Operation ID:** `UpdateGcmChannel`

Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.

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
| 200 | GCMChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-channels-gcmdelete"></a>

**Operation ID:** `DeleteGcmChannel`

Disables the GCM channel for an application and deletes any existing settings for the channel.

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
| 200 | GCMChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channels-gcmoptions"></a>

Retrieves information about the communication requirements and options that are available for the GCM Channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-gcm-schemas"></a>

### Request bodies
<a name="apps-application-id-channels-gcm-request-examples"></a>

#### PUT schema
<a name="apps-application-id-channels-gcm-request-body-put-example"></a>

```
{
  "ApiKey": "string",
  "Enabled": boolean,
  "ServiceJson": "string",
  "DefaultAuthenticationMethod": "string"
}
```

### Response bodies
<a name="apps-application-id-channels-gcm-response-examples"></a>

#### GCMChannelResponse schema
<a name="apps-application-id-channels-gcm-response-body-gcmchannelresponse-example"></a>

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
  "Credential": "string",
  "HasFcmServiceCredentials": boolean,
  "DefaultAuthenticationMethod": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-channels-gcm-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-gcm-properties"></a>

### GCMChannelRequest
<a name="apps-application-id-channels-gcm-model-gcmchannelrequest"></a>

Specifies the status and settings of the GCM channel for an application. This channel enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApiKey | string | False | The Web API Key, also referred to as an *API\_KEY* or *server key*, that you received from Google to communicate with Google services. |
| DefaultAuthenticationMethod | string | False | The default authentication method used for GCM. Values are either "TOKEN" or "KEY". Defaults to "KEY".  |
| Enabled | boolean | False | Specifies whether to enable the GCM channel for the application. |
| ServiceJson | string | False | The contents of the JSON file provided by Google during registration in order to generate an access token for authentication. For more information see [Migrate from legacy FCM APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1). |

### GCMChannelResponse
<a name="apps-application-id-channels-gcm-model-gcmchannelresponse"></a>

Provides information about the status and settings of the GCM channel for an application. The GCM channel enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application that the GCM channel applies to. |
| CreationDate | string | False | The date and time when the GCM channel was enabled. |
| Credential | string | False | The Web API Key, also referred to as an *API\_KEY* or *server key*, that you received from Google to communicate with Google services. |
| DefaultAuthenticationMethod | string | False | The default authentication method used for GCM. Values are either "TOKEN" or "KEY". Defaults to "KEY".  |
| Enabled | boolean | False | Specifies whether the GCM channel is enabled for the application. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| HasFcmServiceCredentials | boolean | False | Returns true if the JSON file provided by Google during registration process was used in the **ServiceJson** field of the request. |
| Id | string | False | (Deprecated) An identifier for the GCM channel. This property is retained only for backward compatibility. |
| IsArchived | boolean | False | Specifies whether the GCM channel is archived. |
| LastModifiedBy | string | False | The user who last modified the GCM channel. |
| LastModifiedDate | string | False | The date and time when the GCM channel was last modified. |
| Platform | string | True | The type of messaging or notification platform for the channel. For the GCM channel, this value is `GCM`. |
| Version | integer | False | The current version of the GCM channel. |

### MessageBody
<a name="apps-application-id-channels-gcm-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-channels-gcm-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetGcmChannel
<a name="GetGcmChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetGcmChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetGcmChannel)

### UpdateGcmChannel
<a name="UpdateGcmChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateGcmChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateGcmChannel)

### DeleteGcmChannel
<a name="DeleteGcmChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteGcmChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteGcmChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
