---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Channels
<a name="apps-application-id-channels"></a>

A *channel* is a type of platform that you can deliver messages to. For example, use the email channel to send email to newsletter subscribers, use the SMS channel to send SMS text messages to your customers, or use a push notification channel to send push notifications to users of your iOS or Android app.

You can use the Channels resource to retrieve information about the history and status of each channel for a specific application. To retrieve more detailed information about a specific type of channel or to perform other channel-specific operations, use the resource for that type of channel.

## URI
<a name="apps-application-id-channels-url"></a>

`/v1/apps/{{application-id}}/channels`

## HTTP methods
<a name="apps-application-id-channels-http-methods"></a>

### GET
<a name="apps-application-id-channelsget"></a>

**Operation ID:** `GetChannels`

Retrieves information about the history and status of each channel for an application.

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
| 200 | ChannelsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channelsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Channels resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-schemas"></a>

### Response bodies
<a name="apps-application-id-channels-response-examples"></a>

#### ChannelsResponse schema
<a name="apps-application-id-channels-response-body-channelsresponse-example"></a>

```
{
  "Channels": {
  }
}
```

#### MessageBody schema
<a name="apps-application-id-channels-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-properties"></a>

### ChannelResponse
<a name="apps-application-id-channels-model-channelresponse"></a>

Provides information about the general settings and status of a channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application. |
| CreationDate | string | False | The date and time, in ISO 8601 format, when the channel was enabled. |
| Enabled | boolean | False | Specifies whether the channel is enabled for the application. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| Id | string | False | (Deprecated) An identifier for the channel. This property is retained only for backward compatibility. |
| IsArchived | boolean | False | Specifies whether the channel is archived. |
| LastModifiedBy | string | False | The user who last modified the channel. |
| LastModifiedDate | string | False | The date and time, in ISO 8601 format, when the channel was last modified. |
| Version | integer | False | The current version of the channel. |

### ChannelsResponse
<a name="apps-application-id-channels-model-channelsresponse"></a>

Provides information about the general settings and status of all channels for an application, including channels that aren't enabled for the application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Channels | object | True | A map that contains a multipart response for each channel. For each item in this object, the `ChannelType` is the key and the `Channel` is the value. |

### MessageBody
<a name="apps-application-id-channels-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-channels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetChannels
<a name="GetChannels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetChannels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetChannels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
