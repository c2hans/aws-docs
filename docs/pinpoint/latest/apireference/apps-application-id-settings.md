---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-settings.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Settings
<a name="apps-application-id-settings"></a>

The Settings resource represents the default settings for an Amazon Pinpoint application. You can use this resource to retrieve information about or update the default settings for an application.

## URI
<a name="apps-application-id-settings-url"></a>

`/v1/apps/{{application-id}}/settings`

## HTTP methods
<a name="apps-application-id-settings-http-methods"></a>

### GET
<a name="apps-application-id-settingsget"></a>

**Operation ID:** `GetApplicationSettings`

Retrieves information about the settings for an application.

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
| 200 | ApplicationSettingsResource | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-settingsput"></a>

**Operation ID:** `UpdateApplicationSettings`

Updates the settings for an application.

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
| 200 | ApplicationSettingsResource | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-settingsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Settings resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-settings-schemas"></a>

### Request bodies
<a name="apps-application-id-settings-request-examples"></a>

#### PUT schema
<a name="apps-application-id-settings-request-body-put-example"></a>

```
{
  "QuietTime": {
    "Start": "string",
    "End": "string"
  },
  "Limits": {
    "Daily": integer,
    "Total": integer,
    "Session": integer,
    "MessagesPerSecond": integer,
    "MaximumDuration": integer
  },
  "CampaignHook": {
    "LambdaFunctionName": "string",
    "WebUrl": "string",
    "Mode": enum
  }
}
```

### Response bodies
<a name="apps-application-id-settings-response-examples"></a>

#### ApplicationSettingsResource schema
<a name="apps-application-id-settings-response-body-applicationsettingsresource-example"></a>

```
{
  "ApplicationId": "string",
  "LastModifiedDate": "string",
  "QuietTime": {
    "Start": "string",
    "End": "string"
  },
  "Limits": {
    "Daily": integer,
    "Total": integer,
    "Session": integer,
    "MessagesPerSecond": integer,
    "MaximumDuration": integer
  },
  "JourneyLimits": {
    "DailyCap": integer,
    "TotalCap": integer,
    "TimeframeCap": {
      "Days": integer,
      "Cap": integer
    }
  },
  "CampaignHook": {
    "LambdaFunctionName": "string",
    "WebUrl": "string",
    "Mode": enum
  }
}
```

#### MessageBody schema
<a name="apps-application-id-settings-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-settings-properties"></a>

### ApplicationSettingsJourneyLimits
<a name="apps-application-id-settings-model-applicationsettingsjourneylimits"></a>

The default sending limits for journeys in the application. To override these limits and define custom limits for a specific journey, use the Journey resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DailyCap | integer | False | The daily number of messages that an endpoint can receive from all journeys. The maximum value is 100. If set to 0, this limit will not apply. |
| TimeframeCap | [JourneyTimeframeCap](#apps-application-id-settings-model-journeytimeframecap) | False | The default maximum number of messages that can be sent to an endpoint during the specified timeframe for all journeys.  |
| TotalCap | integer | False | The default maximum number of messages that a single journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply. |

### ApplicationSettingsResource
<a name="apps-application-id-settings-model-applicationsettingsresource"></a>

Provides information about an application, including the default settings for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| CampaignHook | [CampaignHook](#apps-application-id-settings-model-campaignhook) | False | The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application. |
| JourneyLimits | [ApplicationSettingsJourneyLimits](#apps-application-id-settings-model-applicationsettingsjourneylimits) | False | The default sending limits for journeys in the application. These limits apply to each journey for the application but can be overridden, on a per journey basis, with the JourneyLimits resource. |
| LastModifiedDate | string | False | The date and time, in ISO 8601 format, when the application's settings were last modified. |
| Limits | [CampaignLimits](#apps-application-id-settings-model-campaignlimits) | False | The default sending limits for campaigns in the application. |
| QuietTime | [QuietTime](#apps-application-id-settings-model-quiettime) | False | The default quiet time for campaigns in the application. Quiet time is a specific time range when messages aren't sent to endpoints, if all the following conditions are met:  The `EndpointDemographic.Timezone` property of the endpoint is set to a valid value.   The current time in the endpoint's time zone is later than or equal to the time specified by the `QuietTime.Start` property for the application (or a campaign or journey that has custom quiet time settings).   The current time in the endpoint's time zone is earlier than or equal to the time specified by the `QuietTime.End` property for the application (or a campaign or journey that has custom quiet time settings).  <br />If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled. |

### CampaignHook
<a name="apps-application-id-settings-model-campaignhook"></a>

Specifies settings for invoking an AWS Lambda function that customizes a segment for a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| LambdaFunctionName | string | False | The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign. |
| Mode | string<br />Values: `DELIVERY \| FILTER` | False | The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:   `FILTER` – Invoke the function to customize the segment that's used by a campaign.    `DELIVERY` – (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the `CustomDeliveryConfiguration` and `CampaignCustomMessage` objects of the campaign.   |
| WebUrl | string | False | The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS. |

### CampaignLimits
<a name="apps-application-id-settings-model-campaignlimits"></a>

For a campaign, specifies limits on the messages that the campaign can send. For an application, specifies the default limits for messages that campaigns in the application can send.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Daily | integer | False | The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100. |
| MaximumDuration | integer | False | The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds. |
| MessagesPerSecond | integer | False | The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000. |
| Session | integer | False | The maximum number of messages that the campaign can send per user session. |
| Total | integer | False | The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100. |

### JourneyTimeframeCap
<a name="apps-application-id-settings-model-journeytimeframecap"></a>

The number of messages that can be sent to an endpoint during the specified timeframe for all journeys.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Cap | integer | False | The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply. |
| Days | integer | False | The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply. |

### MessageBody
<a name="apps-application-id-settings-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### QuietTime
<a name="apps-application-id-settings-model-quiettime"></a>

Specifies the start and end times that define a time range when messages aren't sent to endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| End | string | False | The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |
| Start | string | False | The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |

### WriteApplicationSettingsRequest
<a name="apps-application-id-settings-model-writeapplicationsettingsrequest"></a>

Specifies the default settings for an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CampaignHook | [CampaignHook](#apps-application-id-settings-model-campaignhook) | False | The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application.<br />To override these settings and define custom settings for a specific campaign, use the `CampaignHook` object of the [Campaign](apps-application-id-campaigns-campaign-id.md) resource. |
| Limits | [CampaignLimits](#apps-application-id-settings-model-campaignlimits) | False | The default sending limits for campaigns in the application. To override these limits and define custom limits for a specific campaign or journey, use the [Campaign](apps-application-id-campaigns-campaign-id.md) resource or the [Journey](apps-application-id-journeys-journey-id.md) resource, respectively. |
| QuietTime | [QuietTime](#apps-application-id-settings-model-quiettime) | False | The default quiet time for campaigns in the application. Quiet time is a specific time range when messages aren't sent to endpoints, if all the following conditions are met:  The `EndpointDemographic.Timezone` property of the endpoint is set to a valid value.   The current time in the endpoint's time zone is later than or equal to the time specified by the `QuietTime.Start` property for the application (or a campaign or journey that has custom quiet time settings).   The current time in the endpoint's time zone is earlier than or equal to the time specified by the `QuietTime.End` property for the application (or a campaign or journey that has custom quiet time settings).  <br />If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled.<br />To override the default quiet time settings for a specific campaign or journey, use the [Campaign](apps-application-id-campaigns-campaign-id.md) resource or the [Journey](apps-application-id-journeys-journey-id.md) resource to define a custom quiet time for the campaign or journey. |

## See also
<a name="apps-application-id-settings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApplicationSettings
<a name="GetApplicationSettings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetApplicationSettings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetApplicationSettings)

### UpdateApplicationSettings
<a name="UpdateApplicationSettings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateApplicationSettings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateApplicationSettings)
