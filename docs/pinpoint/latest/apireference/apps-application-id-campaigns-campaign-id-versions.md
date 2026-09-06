---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Campaign Versions
<a name="apps-application-id-campaigns-campaign-id-versions"></a>

A *campaign* represents a messaging initiative that engages a specific segment of users for an Amazon Pinpoint application. The Campaign Versions resource provides information about versions of a specific campaign, such as the schedule, messaging limits, and message settings for each version of the campaign.

You can use this resource to retrieve information about versions of a campaign.

## URI
<a name="apps-application-id-campaigns-campaign-id-versions-url"></a>

`/v1/apps/{{application-id}}/campaigns/{{campaign-id}}/versions`

## HTTP methods
<a name="apps-application-id-campaigns-campaign-id-versions-http-methods"></a>

### GET
<a name="apps-application-id-campaigns-campaign-id-versionsget"></a>

**Operation ID:** `GetCampaignVersions`

Retrieves information about the status, configuration, and other settings for all versions of a campaign.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{campaign-id}} | String | True | The unique identifier for the campaign. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| token | String | False | The `NextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CampaignsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-campaigns-campaign-id-versionsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Campaign Versions resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{campaign-id}} | String | True | The unique identifier for the campaign. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-campaigns-campaign-id-versions-schemas"></a>

### Response bodies
<a name="apps-application-id-campaigns-campaign-id-versions-response-examples"></a>

#### CampaignsResponse schema
<a name="apps-application-id-campaigns-campaign-id-versions-response-body-campaignsresponse-example"></a>

```
{
  "Item": [
    {
      "TreatmentName": "string",
      "TreatmentDescription": "string",
      "MessageConfiguration": {
        "DefaultMessage": {
          "Body": "string",
          "Title": "string",
          "ImageUrl": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "MediaUrl": "string",
          "Action": enum,
          "Url": "string",
          "SilentPush": boolean,
          "JsonBody": "string",
          "RawContent": "string",
          "TimeToLive": integer
        },
        "APNSMessage": {
          "Body": "string",
          "Title": "string",
          "ImageUrl": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "MediaUrl": "string",
          "Action": enum,
          "Url": "string",
          "SilentPush": boolean,
          "JsonBody": "string",
          "RawContent": "string",
          "TimeToLive": integer
        },
        "GCMMessage": {
          "Body": "string",
          "Title": "string",
          "ImageUrl": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "MediaUrl": "string",
          "Action": enum,
          "Url": "string",
          "SilentPush": boolean,
          "JsonBody": "string",
          "RawContent": "string",
          "TimeToLive": integer
        },
        "ADMMessage": {
          "Body": "string",
          "Title": "string",
          "ImageUrl": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "MediaUrl": "string",
          "Action": enum,
          "Url": "string",
          "SilentPush": boolean,
          "JsonBody": "string",
          "RawContent": "string",
          "TimeToLive": integer
        },
        "BaiduMessage": {
          "Body": "string",
          "Title": "string",
          "ImageUrl": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "MediaUrl": "string",
          "Action": enum,
          "Url": "string",
          "SilentPush": boolean,
          "JsonBody": "string",
          "RawContent": "string",
          "TimeToLive": integer
        },
        "EmailMessage": {
          "Body": "string",
          "Title": "string",
          "HtmlBody": "string",
          "FromAddress": "string",
          "Headers": [
            {
              "Name": "string",
              "Value": "string"
            }
          ]
        },
        "SMSMessage": {
          "Body": "string",
          "MessageType": enum,
          "SenderId": "string",
          "OriginationNumber": "string",
          "EntityId": "string",
          "TemplateId": "string"
        },
        "CustomMessage": {
          "Data": "string"
        },
        "InAppMessage": {
          "Body": "string",
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
      },
      "Schedule": {
        "StartTime": "string",
        "EndTime": "string",
        "Frequency": enum,
        "IsLocalTime": boolean,
        "Timezone": "string",
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
        }
      },
      "TemplateConfiguration": {
        "SMSTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "EmailTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "PushTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "VoiceTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "InAppTemplate": {
          "Name": "string",
          "Version": "string"
        }
      },
      "CustomDeliveryConfiguration": {
        "EndpointTypes": [
          enum
        ],
        "DeliveryUri": "string"
      },
      "Id": "string",
      "ApplicationId": "string",
      "CreationDate": "string",
      "LastModifiedDate": "string",
      "SegmentId": "string",
      "SegmentVersion": integer,
      "AdditionalTreatments": [
        {
          "TreatmentName": "string",
          "TreatmentDescription": "string",
          "MessageConfiguration": {
            "DefaultMessage": {
              "Body": "string",
              "Title": "string",
              "ImageUrl": "string",
              "ImageIconUrl": "string",
              "ImageSmallIconUrl": "string",
              "MediaUrl": "string",
              "Action": enum,
              "Url": "string",
              "SilentPush": boolean,
              "JsonBody": "string",
              "RawContent": "string",
              "TimeToLive": integer
            },
            "APNSMessage": {
              "Body": "string",
              "Title": "string",
              "ImageUrl": "string",
              "ImageIconUrl": "string",
              "ImageSmallIconUrl": "string",
              "MediaUrl": "string",
              "Action": enum,
              "Url": "string",
              "SilentPush": boolean,
              "JsonBody": "string",
              "RawContent": "string",
              "TimeToLive": integer
            },
            "GCMMessage": {
              "Body": "string",
              "Title": "string",
              "ImageUrl": "string",
              "ImageIconUrl": "string",
              "ImageSmallIconUrl": "string",
              "MediaUrl": "string",
              "Action": enum,
              "Url": "string",
              "SilentPush": boolean,
              "JsonBody": "string",
              "RawContent": "string",
              "TimeToLive": integer
            },
            "ADMMessage": {
              "Body": "string",
              "Title": "string",
              "ImageUrl": "string",
              "ImageIconUrl": "string",
              "ImageSmallIconUrl": "string",
              "MediaUrl": "string",
              "Action": enum,
              "Url": "string",
              "SilentPush": boolean,
              "JsonBody": "string",
              "RawContent": "string",
              "TimeToLive": integer
            },
            "BaiduMessage": {
              "Body": "string",
              "Title": "string",
              "ImageUrl": "string",
              "ImageIconUrl": "string",
              "ImageSmallIconUrl": "string",
              "MediaUrl": "string",
              "Action": enum,
              "Url": "string",
              "SilentPush": boolean,
              "JsonBody": "string",
              "RawContent": "string",
              "TimeToLive": integer
            },
            "EmailMessage": {
              "Body": "string",
              "Title": "string",
              "HtmlBody": "string",
              "FromAddress": "string",
              "Headers": [
                {
                  "Name": "string",
                  "Value": "string"
                }
              ]
            },
            "SMSMessage": {
              "Body": "string",
              "MessageType": enum,
              "SenderId": "string",
              "OriginationNumber": "string",
              "EntityId": "string",
              "TemplateId": "string"
            },
            "CustomMessage": {
              "Data": "string"
            },
            "InAppMessage": {
              "Body": "string",
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
          },
          "Schedule": {
            "StartTime": "string",
            "EndTime": "string",
            "Frequency": enum,
            "IsLocalTime": boolean,
            "Timezone": "string",
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
            }
          },
          "TemplateConfiguration": {
            "SMSTemplate": {
              "Name": "string",
              "Version": "string"
            },
            "EmailTemplate": {
              "Name": "string",
              "Version": "string"
            },
            "PushTemplate": {
              "Name": "string",
              "Version": "string"
            },
            "VoiceTemplate": {
              "Name": "string",
              "Version": "string"
            },
            "InAppTemplate": {
              "Name": "string",
              "Version": "string"
            }
          },
          "CustomDeliveryConfiguration": {
            "EndpointTypes": [
              enum
            ],
            "DeliveryUri": "string"
          },
          "SizePercent": integer,
          "Id": "string",
          "State": {
            "CampaignStatus": enum
          }
        }
      ],
      "HoldoutPercent": integer,
      "Name": "string",
      "Limits": {
        "Daily": integer,
        "Total": integer,
        "Session": integer,
        "MessagesPerSecond": integer,
        "MaximumDuration": integer
      },
      "Description": "string",
      "Hook": {
        "LambdaFunctionName": "string",
        "WebUrl": "string",
        "Mode": enum
      },
      "State": {
        "CampaignStatus": enum
      },
      "DefaultState": {
        "CampaignStatus": enum
      },
      "Version": integer,
      "IsPaused": boolean,
      "Arn": "string",
      "tags": {
      },
      "Priority": integer
    }
  ],
  "NextToken": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-campaigns-campaign-id-versions-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-campaigns-campaign-id-versions-properties"></a>

### AttributeDimension
<a name="apps-application-id-campaigns-campaign-id-versions-model-attributedimension"></a>

Specifies attribute-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AttributeType | string<br />Values: `INCLUSIVE \| EXCLUSIVE \| CONTAINS \| BEFORE \| AFTER \| BETWEEN \| NOT_BETWEEN \| ON` | False | The type of segment dimension to use. Valid values are:+   `INCLUSIVE` – endpoints that have attributes matching the values are included in the segment. <br />+   `EXCLUSIVE` – endpoints that have attributes matching the values are excluded from the segment. <br />+   `CONTAINS` – endpoints that have attributes' substrings match the values are included in the segment. <br />+   `BEFORE` – endpoints with attributes read as ISO\_INSTANT datetimes before the value are included in the segment. <br />+   `AFTER` – endpoints with attributes read as ISO\_INSTANT datetimes after the value are included in the segment. <br />+   `BETWEEN` – endpoints with attributes read as ISO\_INSTANT datetimes between the values are included in the segment. <br />+   `ON` – endpoints with attributes read as ISO\_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.  |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `AttributeType` property, endpoints are included or excluded from the segment if their attribute values match the criteria values. |

### CampaignCustomMessage
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaigncustommessage"></a>

Specifies the contents of a message that's sent through a custom channel to recipients of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Data | string | False | The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB. |

### CampaignEmailMessage
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignemailmessage"></a>

Specifies the content and "From" address for an email message that's sent to recipients of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The body of the email for recipients whose email clients don't render HTML content. |
| FromAddress | string | False | The verified email address to send the email from. The default address is the `FromAddress` specified for the email channel for the application. |
| Headers | Array of type [MessageHeader](#apps-application-id-campaigns-campaign-id-versions-model-messageheader) | False | The list of [MessageHeaders](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-emailheader) for the email. You can have up to 15 MessageHeaders for each email. |
| HtmlBody | string | False | The body of the email, in HTML format, for recipients whose email clients render HTML content. |
| Title | string | False | The subject line, or title, of the email. |

### CampaignEventFilter
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaigneventfilter"></a>

Specifies the settings for events that cause a campaign to be sent.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Dimensions | [EventDimensions](#apps-application-id-campaigns-campaign-id-versions-model-eventdimensions) | True | The dimension settings of the event filter for the campaign. |
| FilterType | string<br />Values: `SYSTEM \| ENDPOINT \| USER` | True | The type of event that causes the campaign to be sent. Valid values are: `SYSTEM`, sends the campaign when a system event occurs; and, `ENDPOINT`, sends the campaign when an endpoint event ([Events](apps-application-id-events.md) resource) occurs. |

### CampaignHook
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignhook"></a>

Specifies settings for invoking an AWS Lambda function that customizes a segment for a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| LambdaFunctionName | string | False | The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign. |
| Mode | string<br />Values: `DELIVERY \| FILTER` | False | The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:+   `FILTER` – Invoke the function to customize the segment that's used by a campaign. <br />+   `DELIVERY` – (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the `CustomDeliveryConfiguration` and `CampaignCustomMessage` objects of the campaign.  |
| WebUrl | string | False | The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS. |

### CampaignInAppMessage
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaigninappmessage"></a>

Specifies the appearance of an in-app message, including the message type, the title and body text, text and background colors, and the configurations of buttons that appear in the message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The body text of the in-app notification. |
| Content | Array of type [InAppMessageContent](#apps-application-id-campaigns-campaign-id-versions-model-inappmessagecontent) | False | An array that contains configurtion information about the in-app message for the campaign, including title and body text, text colors, background colors, image URLs, and button configurations. |
| CustomConfig | object | False | An object that contains custom data (in the form of key-value pairs) that is included in the in-app messaging payload. |
| Layout | string<br />Values: `BOTTOM_BANNER \| TOP_BANNER \| OVERLAYS \| MOBILE_FEED \| MIDDLE_BANNER \| CAROUSEL` | False | A string that describes how the in-app message will appear. You can specify one of the following:+  `BOTTOM_BANNER` – a message that appears as a banner at the bottom of the page. <br />+  `TOP_BANNER` – a message that appears as a banner at the top of the page. <br />+  `OVERLAYS` – a message that covers entire screen. <br />+  `MOBILE_FEED` – a message that appears in a window in front of the page. <br />+  `MIDDLE_BANNER` – a message that appears as a banner in the middle of the page. <br />+  `CAROUSEL` – a scrollable layout of up to five unique messages.  |

### CampaignLimits
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignlimits"></a>

For a campaign, specifies limits on the messages that the campaign can send. For an application, specifies the default limits for messages that campaigns in the application can send.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Daily | integer | False | The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100. |
| MaximumDuration | integer | False | The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds. |
| MessagesPerSecond | integer | False | The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000. |
| Session | integer | False | The maximum number of messages that the campaign can send per user session. |
| Total | integer | False | The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100. |

### CampaignResponse
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignresponse"></a>

Provides information about the status, configuration, and other settings for a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AdditionalTreatments | Array of type [TreatmentResource](#apps-application-id-campaigns-campaign-id-versions-model-treatmentresource) | False | An array of responses, one for each treatment that you defined for the campaign, in addition to the default treatment. |
| ApplicationId | string | True | The unique identifier for the application that the campaign applies to. |
| Arn | string | True | The Amazon Resource Name (ARN) of the campaign. |
| CreationDate | string | True | The date, in ISO 8601 format, when the campaign was created. |
| CustomDeliveryConfiguration | [CustomDeliveryConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-customdeliveryconfiguration) | False | The delivery configuration settings for sending the campaign through a custom channel. |
| DefaultState | [CampaignState](#apps-application-id-campaigns-campaign-id-versions-model-campaignstate) | False | The current status of the campaign's default treatment. This value exists only for campaigns that have more than one treatment. |
| Description | string | False | The custom description of the campaign. |
| HoldoutPercent | integer | False | The allocated percentage of users (segment members) who shouldn't receive messages from the campaign. |
| Hook | [CampaignHook](#apps-application-id-campaigns-campaign-id-versions-model-campaignhook) | False | The settings for the AWS Lambda function to use as a code hook for the campaign. You can use this hook to customize the segment that's used by the campaign. |
| Id | string | True | The unique identifier for the campaign. |
| IsPaused | boolean | False | Specifies whether the campaign is paused. A paused campaign doesn't run unless you resume it by changing this value to `false`. If you restart a campaign, the campaign restarts from the beginning and not at the point you paused it. |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the campaign was last modified.  |
| Limits | [CampaignLimits](#apps-application-id-campaigns-campaign-id-versions-model-campaignlimits) | False | The messaging limits for the campaign. |
| MessageConfiguration | [MessageConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-messageconfiguration) | False | The message configuration settings for the campaign. |
| Name | string | False | The name of the campaign. |
| Priority | integer | False | Defines the priority of the campaign. This value used to determine the order in which messages are displayed to the recipient if there are multiple messages scheduled to be displayed at the same time. |
| Schedule | [Schedule](#apps-application-id-campaigns-campaign-id-versions-model-schedule) | False | The schedule settings for the campaign. |
| SegmentId | string | True | The unique identifier for the segment that's associated with the campaign. |
| SegmentVersion | integer | True | The version number of the segment that's associated with the campaign. |
| State | [CampaignState](#apps-application-id-campaigns-campaign-id-versions-model-campaignstate) | False | The current status of the campaign. |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the campaign. Each tag consists of a required tag key and an associated tag value. |
| TemplateConfiguration | [TemplateConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-templateconfiguration) | False | The message template that’s used for the campaign. |
| TreatmentDescription | string | False | The custom description of the default treatment for the campaign. |
| TreatmentName | string | False | The custom name of the default treatment for the campaign, if the campaign has multiple treatments. A *treatment* is a variation of a campaign that's used for A/B testing. |
| Version | integer | False | The version number of the campaign. |

### CampaignSmsMessage
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignsmsmessage"></a>

Specifies the content and settings for an SMS message that's sent to recipients of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The body of the SMS message. |
| EntityId | string | False | A registered Entity ID (currently only used when sending messages to recipients in India). |
| MessageType | string<br />Values: `TRANSACTIONAL \| PROMOTIONAL` | False | The SMS message type. Valid values are `TRANSACTIONAL` (for messages that are critical or time-sensitive, such as a one-time passwords) and `PROMOTIONAL` (for messsages that aren't critical or time-sensitive, such as marketing messages). |
| OriginationNumber | string | False | The number to send the SMS message from. The phone number that you specify must exist in your Amazon Pinpoint account—you can't pass an arbitrary phone number. If you want to use a sender ID to send your message, omit this parameter and use `SenderId` instead. |
| SenderId | string | False | The alphabetic Sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country or region. To specify a phone number as the sender, omit this parameter and use `OriginationNumber` instead. For more information about support for Sender ID by country, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html). |
| TemplateId | string | False | A registered Template ID (currently only used when sending messages to recipients in India). |

### CampaignState
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignstate"></a>

Provides information about the status of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CampaignStatus | string<br />Values: `SCHEDULED \| EXECUTING \| PENDING_NEXT_RUN \| COMPLETED \| PAUSED \| DELETED \| INVALID \| PENDING_APPROVAL \| DRAFT` | False | The current status of the campaign, or the current status of a treatment that belongs to an A/B test campaign.<br />If a campaign uses A/B testing, the campaign has a status of `COMPLETED` only if all campaign treatments have a status of `COMPLETED`. If you delete the segment that's associated with a campaign, the campaign fails and has a status of `DELETED`. |

### CampaignsResponse
<a name="apps-application-id-campaigns-campaign-id-versions-model-campaignsresponse"></a>

Provides information about the configuration and other settings for all the campaigns that are associated with an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [CampaignResponse](#apps-application-id-campaigns-campaign-id-versions-model-campaignresponse) | True | An array of responses, one for each campaign that's associated with the application. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### CustomDeliveryConfiguration
<a name="apps-application-id-campaigns-campaign-id-versions-model-customdeliveryconfiguration"></a>

Specifies the delivery configuration settings for sending a campaign or campaign treatment through a custom channel. This object is required if you use the `CampaignCustomMessage` object to define the message to send for the campaign or campaign treatment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryUri | string | True | The destination to send the campaign or treatment to. This value can be one of the following:+  The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment. <br />+  The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.  |
| EndpointTypes | Array of type string<br />Values: `PUSH \| GCM \| APNS \| APNS_SANDBOX \| APNS_VOIP \| APNS_VOIP_SANDBOX \| ADM \| SMS \| VOICE \| EMAIL \| BAIDU \| CUSTOM \| IN_APP` | False | The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the `ChannelType` property of an endpoint. |

### DefaultButtonConfiguration
<a name="apps-application-id-campaigns-campaign-id-versions-model-defaultbuttonconfiguration"></a>

Information about the default behavior for a button that appears in an in-app message. You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color of a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BorderRadius | integer | False | The border radius of a button. |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | True | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:+  `LINK` – A link to a web destination. <br />+  `DEEP_LINK` – A link to a specific page in an application. <br />+  `CLOSE` – Dismisses the message.  |
| Link | string | False | The destination (such as a URL) for a button. |
| Text | string | True | The text that appears on a button in an in-app message. |
| TextColor | string | False | The color of the body text in a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### EventDimensions
<a name="apps-application-id-campaigns-campaign-id-versions-model-eventdimensions"></a>

Specifies the dimensions for an event filter that determines when a campaign is sent or a journey activity is performed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter. |
| EventType | [SetDimension](#apps-application-id-campaigns-campaign-id-versions-model-setdimension) | False | The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as `_email.delivered` or `_custom.delivered`. For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see [Streaming Amazon Pinpoint Events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) in the *Amazon Pinpoint Developer Guide*. |
| Metrics | object | False | One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter. |

### InAppMessageBodyConfig
<a name="apps-application-id-campaigns-campaign-id-versions-model-inappmessagebodyconfig"></a>

Configuration information related to the main body text of an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the main body text of the message. |
| Body | string | True | The main body text of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppMessageButton
<a name="apps-application-id-campaigns-campaign-id-versions-model-inappmessagebutton"></a>

Configuration information for a button that appears in an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Android | [OverrideButtonConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to Android. |
| DefaultConfig | [DefaultButtonConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-defaultbuttonconfiguration) | False | An object that defines the default behavior for a button in an in-app message. |
| IOS | [OverrideButtonConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to iOS devices. |
| Web | [OverrideButtonConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages for web applications. |

### InAppMessageContent
<a name="apps-application-id-campaigns-campaign-id-versions-model-inappmessagecontent"></a>

Configuration information related to an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color for an in-app message banner, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BodyConfig | [InAppMessageBodyConfig](#apps-application-id-campaigns-campaign-id-versions-model-inappmessagebodyconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| HeaderConfig | [InAppMessageHeaderConfig](#apps-application-id-campaigns-campaign-id-versions-model-inappmessageheaderconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| ImageUrl | string | False | The URL of the image that appears on an in-app message banner. |
| PrimaryBtn | [InAppMessageButton](#apps-application-id-campaigns-campaign-id-versions-model-inappmessagebutton) | False | An object that contains configuration information about the primary button in an in-app message. |
| SecondaryBtn | [InAppMessageButton](#apps-application-id-campaigns-campaign-id-versions-model-inappmessagebutton) | False | An object that contains configuration information about the secondary button in an in-app message. |

### InAppMessageHeaderConfig
<a name="apps-application-id-campaigns-campaign-id-versions-model-inappmessageheaderconfig"></a>

Configuration information related to the message header for an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the title of the message. |
| Header | string | True | The text that appears in the header or title of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### Message
<a name="apps-application-id-campaigns-campaign-id-versions-model-message"></a>

Specifies the content and settings for a push notification that's sent to recipients of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if a recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android. <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| Body | string | False | The body of the notification message. The maximum number of characters is 200. |
| ImageIconUrl | string | False | The URL of the image to display as the push notification icon, such as the icon for the app. |
| ImageSmallIconUrl | string | False | The URL of the image to display as the small, push notification icon, such as a small version of the icon for the app. |
| ImageUrl | string | False | The URL of an image to display in the push notification. |
| JsonBody | string | False | The JSON payload to use for a silent push notification. |
| MediaUrl | string | False | The URL of the image or video to display in the push notification. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message. |
| SilentPush | boolean | False | Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration, displaying messages in an in-app message center, or supporting phone home functionality. |
| TimeToLive | integer | False | The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when it's sent to a push notification service. If this value is `0`, the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.<br />This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service. |
| Title | string | False | The title to display above the notification message on a recipient's device. |
| Url | string | False | The URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### MessageBody
<a name="apps-application-id-campaigns-campaign-id-versions-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MessageConfiguration
<a name="apps-application-id-campaigns-campaign-id-versions-model-messageconfiguration"></a>

Specifies the message configuration settings for a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ADMMessage | [Message](#apps-application-id-campaigns-campaign-id-versions-model-message) | False | The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message. |
| APNSMessage | [Message](#apps-application-id-campaigns-campaign-id-versions-model-message) | False | The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message. |
| BaiduMessage | [Message](#apps-application-id-campaigns-campaign-id-versions-model-message) | False | The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message. |
| CustomMessage | [CampaignCustomMessage](#apps-application-id-campaigns-campaign-id-versions-model-campaigncustommessage) | False | The message that the campaign sends through a custom channel, as specified by the delivery configuration (`CustomDeliveryConfiguration`) settings for the campaign. If specified, this message overrides the default message. |
| DefaultMessage | [Message](#apps-application-id-campaigns-campaign-id-versions-model-message) | False | The default message that the campaign sends through all the channels that are configured for the campaign. |
| EmailMessage | [CampaignEmailMessage](#apps-application-id-campaigns-campaign-id-versions-model-campaignemailmessage) | False | The message that the campaign sends through the email channel. If specified, this message overrides the default message.The maximum email message size is 200 KB. You can use email templates to send larger email messages. |
| GCMMessage | [Message](#apps-application-id-campaigns-campaign-id-versions-model-message) | False | The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message. |
| InAppMessage | [CampaignInAppMessage](#apps-application-id-campaigns-campaign-id-versions-model-campaigninappmessage) | False | The default message for the in-app messaging channel. This message overrides the default message (`DefaultMessage`). |
| SMSMessage | [CampaignSmsMessage](#apps-application-id-campaigns-campaign-id-versions-model-campaignsmsmessage) | False | The message that the campaign sends through the SMS channel. If specified, this message overrides the default message. |

### MessageHeader
<a name="apps-application-id-campaigns-campaign-id-versions-model-messageheader"></a>

Contains the name and value pair of an message header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string | False | The name of the message header. The header name can contain up to 126 characters. |
| Value | string | False | The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the `{CreationDate}` attribute, it renders as `YYYY-MM-DDTHH:MM:SS.SSSZ` and is 24 characters in length. |

### MetricDimension
<a name="apps-application-id-campaigns-campaign-id-versions-model-metricdimension"></a>

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ComparisonOperator | string | True | The operator to use when comparing metric values. Valid values are: `GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN_OR_EQUAL`, and `EQUAL`. |
| Value | number | True | The value to compare. |

### OverrideButtonConfiguration
<a name="apps-application-id-campaigns-campaign-id-versions-model-overridebuttonconfiguration"></a>

Configuration information related to the configuration of a button with settings that are specific to a certain device type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | False | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:+  `LINK` – A link to a web destination. <br />+  `DEEP_LINK` – A link to a specific page in an application. <br />+  `CLOSE` – Dismisses the message.  |
| Link | string | False | The destination (such as a URL) for a button. |

### QuietTime
<a name="apps-application-id-campaigns-campaign-id-versions-model-quiettime"></a>

Specifies the start and end times that define a time range when messages aren't sent to endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| End | string | False | The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |
| Start | string | False | The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |

### Schedule
<a name="apps-application-id-campaigns-campaign-id-versions-model-schedule"></a>

Specifies the schedule settings for a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndTime | string | False | The scheduled time, in ISO 8601 format, when the campaign ended or will end. |
| EventFilter | [CampaignEventFilter](#apps-application-id-campaigns-campaign-id-versions-model-campaigneventfilter) | False | The type of event that causes the campaign to be sent, if the value of the `Frequency` property is `EVENT`. |
| Frequency | string<br />Values: `ONCE \| HOURLY \| DAILY \| WEEKLY \| MONTHLY \| EVENT \| IN_APP_EVENT` | False | Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event. |
| IsLocalTime | boolean | False | Specifies whether the start and end times for the campaign schedule use each recipient's local time. To base the schedule on each recipient's local time, set this value to `true`. |
| QuietTime | [QuietTime](#apps-application-id-campaigns-campaign-id-versions-model-quiettime) | False | The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesn't send messages to endpoints, if all the following conditions are met:+  The `EndpointDemographic.Timezone` property of the endpoint is set to a valid value. <br />+  The current time in the endpoint's time zone is later than or equal to the time specified by the `QuietTime.Start` property for the campaign. <br />+  The current time in the endpoint's time zone is earlier than or equal to the time specified by the `QuietTime.End` property for the campaign. <br />If any of the preceding conditions isn't met, the endpoint will receive messages from the campaign, even if quiet time is enabled. |
| StartTime | string | True | The scheduled time when the campaign began or will begin. Valid values are: `IMMEDIATE`, to start the campaign immediately; or, a specific time in ISO 8601 format. |
| Timezone | string | False | The starting UTC offset for the campaign schedule, if the value of the `IsLocalTime` property is `true`. Valid values are: `UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10,` and `UTC-11`. |

### SetDimension
<a name="apps-application-id-campaigns-campaign-id-versions-model-setdimension"></a>

Specifies the dimension type and values for a segment dimension.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DimensionType | string<br />Values: `INCLUSIVE \| EXCLUSIVE` | False | The type of segment dimension to use. Valid values are: `INCLUSIVE`, endpoints that match the criteria are included in the segment; and, `EXCLUSIVE`, endpoints that match the criteria are excluded from the segment. |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `DimensionType` property, endpoints are included or excluded from the segment if their values match the criteria values. |

### Template
<a name="apps-application-id-campaigns-campaign-id-versions-model-template"></a>

Specifies the name and version of the message template to use for the message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string | False | The name of the message template to use for the message. If specified, this value must match the name of an existing message template. |
| Version | string | False | The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### TemplateConfiguration
<a name="apps-application-id-campaigns-campaign-id-versions-model-templateconfiguration"></a>

Specifies the message template to use for the message, for each type of channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EmailTemplate | [Template](#apps-application-id-campaigns-campaign-id-versions-model-template) | False | The email template to use for the message. |
| InAppTemplate | [Template](#apps-application-id-campaigns-campaign-id-versions-model-template) | False | The InApp template to use for the message. The InApp template object is not supported for SendMessages. |
| PushTemplate | [Template](#apps-application-id-campaigns-campaign-id-versions-model-template) | False | The push notification template to use for the message. |
| SMSTemplate | [Template](#apps-application-id-campaigns-campaign-id-versions-model-template) | False | The SMS template to use for the message. |
| VoiceTemplate | [Template](#apps-application-id-campaigns-campaign-id-versions-model-template) | False | The voice template to use for the message. This object isn't supported for campaigns. |

### TreatmentResource
<a name="apps-application-id-campaigns-campaign-id-versions-model-treatmentresource"></a>

Specifies the settings for a campaign treatment. A *treatment* is a variation of a campaign that's used for A/B testing of a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CustomDeliveryConfiguration | [CustomDeliveryConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-customdeliveryconfiguration) | False | The delivery configuration settings for sending the treatment through a custom channel. This object is required if the `MessageConfiguration` object for the treatment specifies a `CustomMessage` object. |
| Id | string | True | The unique identifier for the treatment. |
| MessageConfiguration | [MessageConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-messageconfiguration) | False | The message configuration settings for the treatment. |
| Schedule | [Schedule](#apps-application-id-campaigns-campaign-id-versions-model-schedule) | False | The schedule settings for the treatment. |
| SizePercent | integer | True | The allocated percentage of users (segment members) that the treatment is sent to. |
| State | [CampaignState](#apps-application-id-campaigns-campaign-id-versions-model-campaignstate) | False | The current status of the treatment. |
| TemplateConfiguration | [TemplateConfiguration](#apps-application-id-campaigns-campaign-id-versions-model-templateconfiguration) | False | The message template to use for the treatment. |
| TreatmentDescription | string | False | The custom description of the treatment. |
| TreatmentName | string | False | The custom name of the treatment. |

## See also
<a name="apps-application-id-campaigns-campaign-id-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCampaignVersions
<a name="GetCampaignVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetCampaignVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetCampaignVersions)
