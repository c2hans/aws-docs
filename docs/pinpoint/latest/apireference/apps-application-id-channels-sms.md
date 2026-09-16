---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-sms.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# SMS Channel
<a name="apps-application-id-channels-sms"></a>

A *channel* is a type of platform that you can deliver messages to. To send an SMS text message, you send the message through the SMS channel. Before you can use Amazon Pinpoint to send text messages, you must enable the SMS channel for an Amazon Pinpoint application.

The SMS Channel resource represents the status, sender ID, and other settings of the SMS channel for a specific application. You can use this resource to enable, retrieve information about, update, or disable (delete) the SMS channel for an application.

## URI
<a name="apps-application-id-channels-sms-url"></a>

`/v1/apps/{{application-id}}/channels/sms`

## HTTP methods
<a name="apps-application-id-channels-sms-http-methods"></a>

### GET
<a name="apps-application-id-channels-smsget"></a>

**Operation ID:** `GetSmsChannel`

Retrieves information about the status and settings of the SMS channel for an application.

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
| 200 | SMSChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-channels-smsput"></a>

**Operation ID:** `UpdateSmsChannel`

Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.

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
| 200 | SMSChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-channels-smsdelete"></a>

**Operation ID:** `DeleteSmsChannel`

Disables the SMS channel for an application and deletes any existing settings for the channel.

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
| 200 | SMSChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channels-smsoptions"></a>

Retrieves information about the communication requirements and options that are available for the SMS Channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-sms-schemas"></a>

### Request bodies
<a name="apps-application-id-channels-sms-request-examples"></a>

#### PUT schema
<a name="apps-application-id-channels-sms-request-body-put-example"></a>

```
{
  "Enabled": boolean,
  "ShortCode": "string",
  "SenderId": "string"
}
```

### Response bodies
<a name="apps-application-id-channels-sms-response-examples"></a>

#### SMSChannelResponse schema
<a name="apps-application-id-channels-sms-response-body-smschannelresponse-example"></a>

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
  "ShortCode": "string",
  "SenderId": "string",
  "Platform": "string",
  "PromotionalMessagesPerSecond": integer,
  "TransactionalMessagesPerSecond": integer,
  "HasCredential": boolean
}
```

#### MessageBody schema
<a name="apps-application-id-channels-sms-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-sms-properties"></a>

### MessageBody
<a name="apps-application-id-channels-sms-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### SMSChannelRequest
<a name="apps-application-id-channels-sms-model-smschannelrequest"></a>

Specifies the status and settings of the SMS channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Enabled | boolean | False | Specifies whether to enable the SMS channel for the application. |
| SenderId | string | False | The alphabetic Sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country or region. To specify a phone number as the sender, omit this parameter and use `OriginationNumber` instead. For more information about support for Sender ID by country, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html). |
| ShortCode | string | False | The registered short code that you want to use when you send messages through the SMS channel. |

### SMSChannelResponse
<a name="apps-application-id-channels-sms-model-smschannelresponse"></a>

Provides information about the status and settings of the SMS channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application that the SMS channel applies to. |
| CreationDate | string | False | The date and time, in ISO 8601 format, when the SMS channel was enabled. |
| Enabled | boolean | False | Specifies whether the SMS channel is enabled for the application. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| Id | string | False | (Deprecated) An identifier for the SMS channel. This property is retained only for backward compatibility. |
| IsArchived | boolean | False | Specifies whether the SMS channel is archived. |
| LastModifiedBy | string | False | The user who last modified the SMS channel. |
| LastModifiedDate | string | False | The date and time, in ISO 8601 format, when the SMS channel was last modified. |
| Platform | string | True | The type of messaging or notification platform for the channel. For the SMS channel, this value is `SMS`. |
| PromotionalMessagesPerSecond | integer | False | The maximum number of promotional messages that you can send through the SMS channel each second. |
| SenderId | string | False | The SMS Sender ID that was used to send the message. |
| ShortCode | string | False | The registered short code to use when you send messages through the SMS channel. |
| TransactionalMessagesPerSecond | integer | False | The maximum number of transactional messages that you can send through the SMS channel each second. |
| Version | integer | False | The current version of the SMS channel. |

## See also
<a name="apps-application-id-channels-sms-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSmsChannel
<a name="GetSmsChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/GetSmsChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetSmsChannel)

### UpdateSmsChannel
<a name="UpdateSmsChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/UpdateSmsChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateSmsChannel)

### DeleteSmsChannel
<a name="DeleteSmsChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/DeleteSmsChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteSmsChannel)
