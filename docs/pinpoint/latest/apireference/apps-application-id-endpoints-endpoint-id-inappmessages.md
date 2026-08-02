---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id-inappmessages.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# In-App Messages
<a name="apps-application-id-endpoints-endpoint-id-inappmessages"></a>

Use the `InAppMessages` resource to retrieve information about the in-app messages that have been sent to specific endpoints.

## URI
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-url"></a>

`/v1/apps/{{application-id}}/endpoints/{{endpoint-id}}/inappmessages`

## HTTP methods
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-http-methods"></a>

### GET
<a name="apps-application-id-endpoints-endpoint-id-inappmessagesget"></a>

**Operation ID:** `GetInAppMessages`

Retrieves information about the in-app messages that have been sent to the requested endpoint.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{endpoint-id}} | String | True | The case insensitive unique identifier for the endpoint. The identifier can't contain `$`, `{` or `}`. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | InAppMessagesResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-endpoints-endpoint-id-inappmessagesoptions"></a>

Retrieves information about the communication requirements and options that are available for the In-App Template resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{endpoint-id}} | String | True | The case insensitive unique identifier for the endpoint. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-schemas"></a>

### Response bodies
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-response-examples"></a>

#### InAppMessagesResponse schema
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-response-body-inappmessagesresponse-example"></a>

```
{
  "InAppMessageCampaigns": [
    {
      "CampaignId": "string",
      "TreatmentId": "string",
      "DailyCap": integer,
      "TotalCap": integer,
      "SessionCap": integer,
      "Priority": integer,
      "Schedule": {
        "QuietTime": {
          "Start": "string",
          "End": "string"
        },
        "EventFilter": {
          "Dimensions": {
            "EventType": {
              "DimensionType": enum,
              "Values": [
                "string"
              ]
            },
            "Attributes": {
            },
            "Metrics": {
            }
          },
          "FilterType": enum
        },
        "EndDate": "string"
      },
      "InAppMessage": {
        "Layout": enum,
        "Content": [
          {
            "HeaderConfig": {
              "Header": "string",
              "TextColor": "string",
              "Alignment": enum
            },
            "BackgroundColor": "string",
            "BodyConfig": {
              "Body": "string",
              "TextColor": "string",
              "Alignment": enum
            },
            "ImageUrl": "string",
            "PrimaryBtn": {
              "DefaultConfig": {
                "Text": "string",
                "ButtonAction": enum,
                "Link": "string",
                "TextColor": "string",
                "BackgroundColor": "string",
                "BorderRadius": integer
              },
              "Web": {
                "ButtonAction": enum,
                "Link": "string"
              },
              "IOS": {
                "ButtonAction": enum,
                "Link": "string"
              },
              "Android": {
                "ButtonAction": enum,
                "Link": "string"
              }
            },
            "SecondaryBtn": {
              "DefaultConfig": {
                "Text": "string",
                "ButtonAction": enum,
                "Link": "string",
                "TextColor": "string",
                "BackgroundColor": "string",
                "BorderRadius": integer
              },
              "Web": {
                "ButtonAction": enum,
                "Link": "string"
              },
              "IOS": {
                "ButtonAction": enum,
                "Link": "string"
              },
              "Android": {
                "ButtonAction": enum,
                "Link": "string"
              }
            }
          }
        ],
        "CustomConfig": {
        }
      }
    }
  ]
}
```

#### MessageBody schema
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-properties"></a>

### AttributeDimension
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-attributedimension"></a>

Specifies attribute-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AttributeType | string<br />Values: `INCLUSIVE \| EXCLUSIVE \| CONTAINS \| BEFORE \| AFTER \| BETWEEN \| NOT_BETWEEN \| ON` | False | The type of segment dimension to use. Valid values are:   `INCLUSIVE` – endpoints that have attributes matching the values are included in the segment.    `EXCLUSIVE` – endpoints that have attributes matching the values are excluded from the segment.    `CONTAINS` – endpoints that have attributes' substrings match the values are included in the segment.    `BEFORE` – endpoints with attributes read as ISO\_INSTANT datetimes before the value are included in the segment.    `AFTER` – endpoints with attributes read as ISO\_INSTANT datetimes after the value are included in the segment.    `BETWEEN` – endpoints with attributes read as ISO\_INSTANT datetimes between the values are included in the segment.    `ON` – endpoints with attributes read as ISO\_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.   |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `AttributeType` property, endpoints are included or excluded from the segment if their attribute values match the criteria values. |

### CampaignEventFilter
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-campaigneventfilter"></a>

Specifies the settings for events that cause a campaign to be sent.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Dimensions | [EventDimensions](#apps-application-id-endpoints-endpoint-id-inappmessages-model-eventdimensions) | True | The dimension settings of the event filter for the campaign. |
| FilterType | string<br />Values: `SYSTEM \| ENDPOINT \| USER` | True | The type of event that causes the campaign to be sent. Valid values are: `SYSTEM`, sends the campaign when a system event occurs; and, `ENDPOINT`, sends the campaign when an endpoint event ([Events](apps-application-id-events.md) resource) occurs. |

### DefaultButtonConfiguration
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-defaultbuttonconfiguration"></a>

Information about the default behavior for a button that appears in an in-app message. You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color of a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BorderRadius | integer | False | The border radius of a button. |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | True | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:  `LINK` – A link to a web destination.   `DEEP_LINK` – A link to a specific page in an application.   `CLOSE` – Dismisses the message.   |
| Link | string | False | The destination (such as a URL) for a button. |
| Text | string | True | The text that appears on a button in an in-app message. |
| TextColor | string | False | The color of the body text in a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### EventDimensions
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-eventdimensions"></a>

Specifies the dimensions for an event filter that determines when a campaign is sent or a journey activity is performed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter. |
| EventType | [SetDimension](#apps-application-id-endpoints-endpoint-id-inappmessages-model-setdimension) | False | The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as `_email.delivered` or `_custom.delivered`. For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see [Streaming Amazon Pinpoint Events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) in the *Amazon Pinpoint Developer Guide*. |
| Metrics | object | False | One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter. |

### InAppCampaignSchedule
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappcampaignschedule"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndDate | string | False | A timestamp that represents the latest time, in ISO 8601 format, that the campaign can be sent to endpoints. |
| EventFilter | [CampaignEventFilter](#apps-application-id-endpoints-endpoint-id-inappmessages-model-campaigneventfilter) | False | The type of event that causes the campaign to be sent, if the value of the `Frequency` property is `EVENT`. |
| QuietTime | [QuietTime](#apps-application-id-endpoints-endpoint-id-inappmessages-model-quiettime) | False | The start and end times that define a time range when messages aren't sent to endpoints. |

### InAppMessage
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessage"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Content | Array of type [InAppMessageContent](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagecontent) | False | Contains information about the configuration of an in-app message template. |
| CustomConfig | object | False | An object that contains custom data (in the form of key-value pairs) that is included in the in-app messaging payload. |
| Layout | string<br />Values: `BOTTOM_BANNER \| TOP_BANNER \| OVERLAYS \| MOBILE_FEED \| MIDDLE_BANNER \| CAROUSEL` | False | A string that describes how the in-app message will appear. You can specify one of the following:  `BOTTOM_BANNER` – a message that appears as a banner at the bottom of the page.   `TOP_BANNER` – a message that appears as a banner at the top of the page.   `OVERLAYS` – a message that covers entire screen.   `MOBILE_FEED` – a message that appears in a window in front of the page.   `MIDDLE_BANNER` – a message that appears as a banner in the middle of the page.   `CAROUSEL` – a scrollable layout of up to five unique messages.   |

### InAppMessageBodyConfig
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagebodyconfig"></a>

Configuration information related to the main body text of an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the main body text of the message. |
| Body | string | True | The main body text of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppMessageButton
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagebutton"></a>

Configuration information for a button that appears in an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Android | [OverrideButtonConfiguration](#apps-application-id-endpoints-endpoint-id-inappmessages-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to Android. |
| DefaultConfig | [DefaultButtonConfiguration](#apps-application-id-endpoints-endpoint-id-inappmessages-model-defaultbuttonconfiguration) | False | An object that defines the default behavior for a button in an in-app message. |
| IOS | [OverrideButtonConfiguration](#apps-application-id-endpoints-endpoint-id-inappmessages-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to iOS devices. |
| Web | [OverrideButtonConfiguration](#apps-application-id-endpoints-endpoint-id-inappmessages-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages for web applications. |

### InAppMessageCampaign
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagecampaign"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CampaignId | string | False | The unique identifier for the campaign that the in-app message applies to. |
| DailyCap | integer | False | The maximum number of times any in-app message can be shown to the user in a 24-hour period. |
| InAppMessage | [InAppMessage](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessage) | False | Specifies the settings for a message that's sent to users of an application (an in-app message). |
| Priority | integer | False | An integer between 1 and 5, inclusive, that represents the priority of the campaign, with 1 being the highest priority and 5 being the lowest. This value is used to determine the order in which messages are displayed to the recipient if there are multiple messages scheduled to be displayed at the same time. |
| Schedule | [InAppCampaignSchedule](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappcampaignschedule) | False | The schedule settings for the campaign. |
| SessionCap | integer | False | The maximum number of times an in-app message can be shown to the user during a single session in the application. |
| TotalCap | integer | False | The maximum number of times an in-app message can be shown to the user. |
| TreatmentId | string | False | The unique identifier for the campaign treatment. A treatment is a variation of a campaign that's used for A/B testing. |

### InAppMessageContent
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagecontent"></a>

Configuration information related to an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color for an in-app message banner, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BodyConfig | [InAppMessageBodyConfig](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagebodyconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| HeaderConfig | [InAppMessageHeaderConfig](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessageheaderconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| ImageUrl | string | False | The URL of the image that appears on an in-app message banner. |
| PrimaryBtn | [InAppMessageButton](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagebutton) | False | An object that contains configuration information about the primary button in an in-app message. |
| SecondaryBtn | [InAppMessageButton](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagebutton) | False | An object that contains configuration information about the secondary button in an in-app message. |

### InAppMessageHeaderConfig
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessageheaderconfig"></a>

Configuration information related to the message header for an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the title of the message. |
| Header | string | True | The text that appears in the header or title of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppMessagesResponse
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagesresponse"></a>

Object that contains information about in-app messages.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| InAppMessageCampaigns | Array of type [InAppMessageCampaign](#apps-application-id-endpoints-endpoint-id-inappmessages-model-inappmessagecampaign) | False | A list of in-app message campaigns. |

### MessageBody
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MetricDimension
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-metricdimension"></a>

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ComparisonOperator | string | True | The operator to use when comparing metric values. Valid values are: `GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN_OR_EQUAL`, and `EQUAL`. |
| Value | number | True | The value to compare. |

### OverrideButtonConfiguration
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-overridebuttonconfiguration"></a>

Configuration information related to the configuration of a button with settings that are specific to a certain device type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | False | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:  `LINK` – A link to a web destination.   `DEEP_LINK` – A link to a specific page in an application.   `CLOSE` – Dismisses the message.   |
| Link | string | False | The destination (such as a URL) for a button. |

### QuietTime
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-quiettime"></a>

Specifies the start and end times that define a time range when messages aren't sent to endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| End | string | False | The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |
| Start | string | False | The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |

### SetDimension
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-model-setdimension"></a>

Specifies the dimension type and values for a segment dimension.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DimensionType | string<br />Values: `INCLUSIVE \| EXCLUSIVE` | False | The type of segment dimension to use. Valid values are: `INCLUSIVE`, endpoints that match the criteria are included in the segment; and, `EXCLUSIVE`, endpoints that match the criteria are excluded from the segment. |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `DimensionType` property, endpoints are included or excluded from the segment if their values match the criteria values. |

## See also
<a name="apps-application-id-endpoints-endpoint-id-inappmessages-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetInAppMessages
<a name="GetInAppMessages-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetInAppMessages)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetInAppMessages)
