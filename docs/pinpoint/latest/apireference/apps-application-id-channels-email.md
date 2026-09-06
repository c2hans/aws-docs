---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-channels-email.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Email Channel
<a name="apps-application-id-channels-email"></a>

A *channel* is a type of platform that you can deliver messages to. You can use the email channel to send email to users. Before you can use Amazon Pinpoint to send email, you must enable the email channel for an Amazon Pinpoint application.

The Email Channel resource represents the status, identity, and other settings of the email channel for a specific application. You can use this resource to enable, retrieve information about, update, or disable (delete) the email channel for an application.

## URI
<a name="apps-application-id-channels-email-url"></a>

`/v1/apps/{{application-id}}/channels/email`

## HTTP methods
<a name="apps-application-id-channels-email-http-methods"></a>

### GET
<a name="apps-application-id-channels-emailget"></a>

**Operation ID:** `GetEmailChannel`

Retrieves information about the status and settings of the email channel for an application.

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
| 200 | EmailChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-channels-emailput"></a>

**Operation ID:** `UpdateEmailChannel`

Enables the email channel for an application or updates the status and settings of the email channel for an application.

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
| 200 | EmailChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-channels-emaildelete"></a>

**Operation ID:** `DeleteEmailChannel`

Disables the email channel for an application and deletes any existing settings for the channel.

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
| 200 | EmailChannelResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-channels-emailoptions"></a>

Retrieves information about the communication requirements and options that are available for the Email Channel resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-channels-email-schemas"></a>

### Request bodies
<a name="apps-application-id-channels-email-request-examples"></a>

#### PUT schema
<a name="apps-application-id-channels-email-request-body-put-example"></a>

```
{
  "Enabled": boolean,
  "Identity": "string",
  "FromAddress": "string",
  "RoleArn": "string",
  "OrchestrationSendingRoleArn": "string",
  "ConfigurationSet": "string"
}
```

### Response bodies
<a name="apps-application-id-channels-email-response-examples"></a>

#### EmailChannelResponse schema
<a name="apps-application-id-channels-email-response-body-emailchannelresponse-example"></a>

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
  "Identity": "string",
  "FromAddress": "string",
  "RoleArn": "string",
  "OrchestrationSendingRoleArn": "string",
  "ConfigurationSet": "string",
  "Platform": "string",
  "MessagesPerSecond": integer,
  "HasCredential": boolean
}
```

#### MessageBody schema
<a name="apps-application-id-channels-email-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-channels-email-properties"></a>

### EmailChannelRequest
<a name="apps-application-id-channels-email-model-emailchannelrequest"></a>

Specifies the status and settings of the email channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ConfigurationSet | string | False | The [Amazon SES configuration set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html) that you want to apply to messages that you send through the channel. |
| Enabled | boolean | False | Specifies whether to enable the email channel for the application. |
| FromAddress | string | True | The verified email address that you want to send email from when you send email through the channel. |
| Identity | string | True | The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel. |
| OrchestrationSendingRoleArn | string | False | The ARN of an IAM role for Amazon Pinpoint to use to send email from your campaigns or journeys through Amazon SES. |
| RoleArn | string | False | (Depricated) The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel. |

### EmailChannelResponse
<a name="apps-application-id-channels-email-model-emailchannelresponse"></a>

Provides information about the status and settings of the email channel for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | False | The unique identifier for the application that the email channel applies to. |
| ConfigurationSet | string | False | The [Amazon SES configuration set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html) that's applied to messages that are sent through the channel. |
| CreationDate | string | False | The date and time, in ISO 8601 format, when the email channel was enabled. |
| Enabled | boolean | False | Specifies whether the email channel is enabled for the application. |
| FromAddress | string | False | The verified email address that email is sent from when you send email through the channel. |
| HasCredential | boolean | False | (Not used) This property is retained only for backward compatibility. |
| Id | string | False | (Deprecated) An identifier for the email channel. This property is retained only for backward compatibility. |
| Identity | string | False | The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that's used when you send email through the channel. |
| IsArchived | boolean | False | Specifies whether the email channel is archived. |
| LastModifiedBy | string | False | The user who last modified the email channel. |
| LastModifiedDate | string | False | The date and time, in ISO 8601 format, when the email channel was last modified. |
| MessagesPerSecond | integer | False | The maximum number of emails that can be sent through the channel each second. |
| OrchestrationSendingRoleArn | string | False | The ARN of an IAM role for Amazon Pinpoint to use to send email from your campaigns or journeys through Amazon SES. |
| Platform | string | True | The type of messaging or notification platform for the channel. For the email channel, this value is `EMAIL`. |
| RoleArn | string | False | The ARN of the AWS Identity and Access Management (IAM) role that Amazon Pinpoint uses to submit email-related event data for the channel. |
| Version | integer | False | The current version of the email channel. |

### MessageBody
<a name="apps-application-id-channels-email-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-channels-email-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetEmailChannel
<a name="GetEmailChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetEmailChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetEmailChannel)

### UpdateEmailChannel
<a name="UpdateEmailChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateEmailChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateEmailChannel)

### DeleteEmailChannel
<a name="DeleteEmailChannel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteEmailChannel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteEmailChannel)
