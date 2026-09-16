---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-baidu.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Baidu Channel
<a name="apps-application-id-channels-baidu"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the Baidu channel to send push notification messages to the Baidu Cloud Push service, which is a Chinese cloud service. Before you can use Amazon Pinpoint to send notification messages to the Baidu Cloud Push service, you must enable the Baidu channel for an Amazon Pinpoint application.

The Baidu Channel resource represents the status and authentication settings of the Baidu channel for a specific application. You can use this resource to enable, retrieve information about, update, or disable (delete) the Baidu channel for an application.

## URI
<a name="apps-application-id-channels-baidu-url"></a>

`/v1/apps/{{application-id}}/channels/baidu`

## HTTP methods
<a name="apps-application-id-channels-baidu-http-methods"></a>

### GET
<a name="apps-application-id-channels-baiduget"></a>

**Operation ID:** `GetBaiduChannel`

Retrieves information about the status and settings of the Baidu channel for an application.

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
| 200 | BaiduChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-channels-baiduput"></a>

**Operation ID:** `UpdateBaiduChannel`

Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.

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
| 200 | BaiduChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-channels-baidudelete"></a>

**Operation ID:** `DeleteBaiduChannel`

Disables the Baidu channel for an application and deletes any existing settings for the channel.

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
| 200 | BaiduChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channels-baiduoptions"></a>

Retrieves information about the communication requirements and options that are available for the Baidu Channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-baidu-schemas"></a>

### Request bodies
<a name="apps-application-id-channels-baidu-request-examples"></a>

#### PUT schema
<a name="apps-application-id-channels-baidu-request-body-put-example"></a>

```
{
  "ApiKey": "string",
  "SecretKey": "string",
  "Enabled": boolean
}
```

### Response bodies
<a name="apps-application-id-channels-baidu-response-examples"></a>

#### BaiduChannelResponse schema
<a name="apps-application-id-channels-baidu-response-body-baiduchannelresponse-example"></a>

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
  "Credential": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-channels-baidu-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-baidu-properties"></a>

### BaiduChannelRequest
<a name="apps-application-id-channels-baidu-model-baiduchannelrequest"></a>

Specifies the status and settings of the Baidu (Baidu Cloud Push) channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApiKey | string | True | The API key that you received from the Baidu Cloud Push service to communicate with the service. |
| Enabled | boolean | False | Specifies whether to enable the Baidu channel for the application. |
| SecretKey | string | True | The secret key that you received from the Baidu Cloud Push service to communicate with the service. |

### BaiduChannelResponse
<a name="apps-application-id-channels-baidu-model-baiduchannelresponse"></a>

Provides information about the status and settings of the Baidu (Baidu Cloud Push) channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application that the Baidu channel applies to. |
| CreationDate | string | False | The date and time when the Baidu channel was enabled. |
| Credential | string | True | The API key that you received from the Baidu Cloud Push service to communicate with the service. |
| Enabled | boolean | False | Specifies whether the Baidu channel is enabled for the application. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| Id | string | False | (Deprecated) An identifier for the Baidu channel. This property is retained only for backward compatibility. |
| IsArchived | boolean | False | Specifies whether the Baidu channel is archived. |
| LastModifiedBy | string | False | The user who last modified the Baidu channel. |
| LastModifiedDate | string | False | The date and time when the Baidu channel was last modified. |
| Platform | string | True | The type of messaging or notification platform for the channel. For the Baidu channel, this value is `BAIDU`. |
| Version | integer | False | The current version of the Baidu channel. |

### MessageBody
<a name="apps-application-id-channels-baidu-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-channels-baidu-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBaiduChannel
<a name="GetBaiduChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/GetBaiduChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetBaiduChannel)

### UpdateBaiduChannel
<a name="UpdateBaiduChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/UpdateBaiduChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateBaiduChannel)

### DeleteBaiduChannel
<a name="DeleteBaiduChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/DeleteBaiduChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteBaiduChannel)
