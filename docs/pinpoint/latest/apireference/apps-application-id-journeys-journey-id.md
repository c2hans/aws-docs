---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Journey
<a name="apps-application-id-journeys-journey-id"></a>

A *journey* is an automated workflow that performs a series of messaging activities for an Amazon Pinpoint application. Each activity is a customizable component that specifies what causes the activity to occur, when the activity occurs, what the activity does, and which users the activity applies to. The paths and relationships between activities vary based on conditions and criteria that you define, such as specific user attributes and events.

The Journey resource represents an individual journey that's associated with an Amazon Pinpoint application. The information represented by this resource includes settings for the activities that comprise a journey, settings for the segments that define which users participate in journey activities, the messages that a journey sends, and the schedule that defines when a journey runs.

You can use this resource to retrieve information about, update, or delete a journey. To create a journey, use the [Journeys](apps-application-id-journeys.md) resource.

## URI
<a name="apps-application-id-journeys-journey-id-url"></a>

`/v1/apps/{{application-id}}/journeys/{{journey-id}}`

## HTTP methods
<a name="apps-application-id-journeys-journey-id-http-methods"></a>

### GET
<a name="apps-application-id-journeys-journey-idget"></a>

**Operation ID:** `GetJourney`

Retrieves information about the status, configuration, and other settings for a journey.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | JourneyResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="apps-application-id-journeys-journey-idput"></a>

**Operation ID:** `UpdateJourney`

Updates the configuration and other settings for a journey.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | JourneyResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 409 | MessageBody | The request failed due to a conflict with the current state of the specified resource (ConflictException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-journeys-journey-iddelete"></a>

**Operation ID:** `DeleteJourney`

Deletes a journey from an application.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | JourneyResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-journeys-journey-idoptions"></a>

Retrieves information about the communication requirements and options that are available for the Journey resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-journeys-journey-id-schemas"></a>

### Request bodies
<a name="apps-application-id-journeys-journey-id-request-examples"></a>

#### PUT schema
<a name="apps-application-id-journeys-journey-id-request-body-put-example"></a>

```
{
  "Name": "string",
  "Schedule": {
    "StartTime": "string",
    "EndTime": "string",
    "Timezone": "string"
  },
  "StartCondition": {
    "Description": "string",
    "EventStartCondition": {
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
      "SegmentId": "string"
    },
    "SegmentStartCondition": {
      "SegmentId": "string"
    }
  },
  "Limits": {
    "DailyCap": integer,
    "TotalCap": integer,
    "TimeframeCap": {
      "Days": integer,
      "Cap": integer
    },
    "MessagesPerSecond": integer,
    "EndpointReentryCap": integer,
    "EndpointReentryInterval": "string"
  },
  "StartActivity": "string",
  "Activities": {
  },
  "RefreshFrequency": "string",
  "QuietTime": {
    "Start": "string",
    "End": "string"
  },
  "WaitForQuietTime": boolean,
  "SendingSchedule": boolean,
  "OpenHours": {
    "EMAIL": {
    },
    "SMS": {
    },
    "PUSH": {
    },
    "VOICE": {
    },
    "CUSTOM": {
    }
  },
  "ClosedDays": {
    "EMAIL": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "SMS": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "PUSH": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "VOICE": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "CUSTOM": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ]
  },
  "RefreshOnSegmentUpdate": boolean,
  "LocalTime": boolean,
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "State": enum,
  "TimezoneEstimationMethods": [
    enum
  ]
}
```

### Response bodies
<a name="apps-application-id-journeys-journey-id-response-examples"></a>

#### JourneyResponse schema
<a name="apps-application-id-journeys-journey-id-response-body-journeyresponse-example"></a>

```
{
  "Name": "string",
  "Schedule": {
    "StartTime": "string",
    "EndTime": "string",
    "Timezone": "string"
  },
  "StartCondition": {
    "Description": "string",
    "EventStartCondition": {
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
      "SegmentId": "string"
    },
    "SegmentStartCondition": {
      "SegmentId": "string"
    }
  },
  "Limits": {
    "DailyCap": integer,
    "TotalCap": integer,
    "TimeframeCap": {
      "Days": integer,
      "Cap": integer
    },
    "MessagesPerSecond": integer,
    "EndpointReentryCap": integer,
    "EndpointReentryInterval": "string"
  },
  "StartActivity": "string",
  "Activities": {
  },
  "RefreshFrequency": "string",
  "QuietTime": {
    "Start": "string",
    "End": "string"
  },
  "WaitForQuietTime": boolean,
  "SendingSchedule": boolean,
  "OpenHours": {
    "EMAIL": {
    },
    "SMS": {
    },
    "PUSH": {
    },
    "VOICE": {
    },
    "CUSTOM": {
    }
  },
  "ClosedDays": {
    "EMAIL": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "SMS": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "PUSH": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "VOICE": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ],
    "CUSTOM": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
    ]
  },
  "RefreshOnSegmentUpdate": boolean,
  "LocalTime": boolean,
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "State": enum,
  "tags": {
  },
  "TimezoneEstimationMethods": [
    enum
  ],
  "Id": "string",
  "ApplicationId": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-journeys-journey-id-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-journeys-journey-id-properties"></a>

### Activity
<a name="apps-application-id-journeys-journey-id-model-activity"></a>

Specifies the configuration and other settings for an activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ConditionalSplit | [ConditionalSplitActivity](#apps-application-id-journeys-journey-id-model-conditionalsplitactivity) | False | The settings for a yes/no split activity. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify. |
| CUSTOM | [CustomMessageActivity](#apps-application-id-journeys-journey-id-model-custommessageactivity) | False | The settings for a custom message activity. This type of activity calls an AWS Lambda function or web hook that sends messages to participants. |
| Description | string | False | The custom description of the activity. |
| EMAIL | [EmailMessageActivity](#apps-application-id-journeys-journey-id-model-emailmessageactivity) | False | The settings for an email activity. This type of activity sends an email message to participants. |
| Holdout | [HoldoutActivity](#apps-application-id-journeys-journey-id-model-holdoutactivity) | False | The settings for a holdout activity. This type of activity stops a journey for a specified percentage of participants. |
| MultiCondition | [MultiConditionalSplitActivity](#apps-application-id-journeys-journey-id-model-multiconditionalsplitactivity) | False | The settings for a multivariate split activity. This type of activity sends participants down one of as many as five paths (including a default *Else* path) in a journey, based on conditions that you specify. |
| PUSH | [PushMessageActivity](#apps-application-id-journeys-journey-id-model-pushmessageactivity) | False | The settings for a push notification activity. This type of activity sends a push notification to participants. |
| RandomSplit | [RandomSplitActivity](#apps-application-id-journeys-journey-id-model-randomsplitactivity) | False | The settings for a random split activity. This type of activity randomly sends specified percentages of participants down one of as many as five paths in a journey, based on conditions that you specify. |
| SMS | [SMSMessageActivity](#apps-application-id-journeys-journey-id-model-smsmessageactivity) | False | The settings for an SMS activity. This type of activity sends a text message to participants. |
| Wait | [WaitActivity](#apps-application-id-journeys-journey-id-model-waitactivity) | False | The settings for a wait activity. This type of activity waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey. |

### AttributeDimension
<a name="apps-application-id-journeys-journey-id-model-attributedimension"></a>

Specifies attribute-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AttributeType | string<br />Values: `INCLUSIVE \| EXCLUSIVE \| CONTAINS \| BEFORE \| AFTER \| BETWEEN \| NOT_BETWEEN \| ON` | False | The type of segment dimension to use. Valid values are:+   `INCLUSIVE` – endpoints that have attributes matching the values are included in the segment. <br />+   `EXCLUSIVE` – endpoints that have attributes matching the values are excluded from the segment. <br />+   `CONTAINS` – endpoints that have attributes' substrings match the values are included in the segment. <br />+   `BEFORE` – endpoints with attributes read as ISO\_INSTANT datetimes before the value are included in the segment. <br />+   `AFTER` – endpoints with attributes read as ISO\_INSTANT datetimes after the value are included in the segment. <br />+   `BETWEEN` – endpoints with attributes read as ISO\_INSTANT datetimes between the values are included in the segment. <br />+   `ON` – endpoints with attributes read as ISO\_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.  |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `AttributeType` property, endpoints are included or excluded from the segment if their attribute values match the criteria values. |

### ClosedDays
<a name="apps-application-id-journeys-journey-id-model-closeddays"></a>

The time when a journey will not send messages. QuietTime should be configured first and SendingSchedule should be set to true.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CUSTOM | Array of type [ClosedDaysRule](#apps-application-id-journeys-journey-id-model-closeddaysrule) | False | Rules for the Custom channel. |
| EMAIL | Array of type [ClosedDaysRule](#apps-application-id-journeys-journey-id-model-closeddaysrule) | False | Rules for the Email channel. |
| PUSH | Array of type [ClosedDaysRule](#apps-application-id-journeys-journey-id-model-closeddaysrule) | False | Rules for the Push channel. |
| SMS | Array of type [ClosedDaysRule](#apps-application-id-journeys-journey-id-model-closeddaysrule) | False | Rules for the SMS channel. |
| VOICE | Array of type [ClosedDaysRule](#apps-application-id-journeys-journey-id-model-closeddaysrule) | False | Rules for the Voice channel. |

### ClosedDaysRule
<a name="apps-application-id-journeys-journey-id-model-closeddaysrule"></a>

Specifies the rule settings for when messages can't be sent.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndDateTime | string | True | EndDateTime ISO 8601 format |
| Name | string | True | The name of the closed rule. |
| StartDateTime | string | True | StartDateTime ISO 8601 format |

### Condition
<a name="apps-application-id-journeys-journey-id-model-condition"></a>

Specifies the conditions to evaluate for an activity in a journey, and how to evaluate those conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Conditions | Array of type [SimpleCondition](#apps-application-id-journeys-journey-id-model-simplecondition) | False | The conditions to evaluate for the activity. |
| Operator | string<br />Values: `ALL \| ANY` | False | Specifies how to handle multiple conditions for the activity. For example, if you specify two conditions for an activity, whether both or only one of the conditions must be met for the activity to be performed. |

### ConditionalSplitActivity
<a name="apps-application-id-journeys-journey-id-model-conditionalsplitactivity"></a>

Specifies the settings for a yes/no split activity in a journey. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify.

**Note**
To create yes/no split activities that send participants down different paths based on push notification events (such as Open or Received events), your mobile app has to specify the User ID and Endpoint ID values. For more information, see [Integrating Amazon Pinpoint with your application](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate.html) in the *Amazon Pinpoint Developer Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Condition | [Condition](#apps-application-id-journeys-journey-id-model-condition) | False | The conditions that define the paths for the activity, and the relationship between the conditions. |
| EvaluationWaitTime | [WaitTime](#apps-application-id-journeys-journey-id-model-waittime) | False | The amount of time to wait before determining whether the conditions are met, or the date and time when Amazon Pinpoint determines whether the conditions are met. |
| FalseActivity | string | False | The unique identifier for the activity to perform if the conditions aren't met. |
| TrueActivity | string | False | The unique identifier for the activity to perform if the conditions are met. |

### CustomMessageActivity
<a name="apps-application-id-journeys-journey-id-model-custommessageactivity"></a>

The settings for a custom message activity. This type of activity calls an AWS Lambda function or web hook that sends messages to participants.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryUri | string | False | The destination to send the campaign or treatment to. This value can be one of the following:+  The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment. <br />+  The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.  |
| EndpointTypes | Array of type string<br />Values: `PUSH \| GCM \| APNS \| APNS_SANDBOX \| APNS_VOIP \| APNS_VOIP_SANDBOX \| ADM \| SMS \| VOICE \| EMAIL \| BAIDU \| CUSTOM \| IN_APP` | False | The types of endpoints to send the custom message to. Each valid value maps to a type of channel that you can associate with an endpoint by using the `ChannelType` property of an endpoint. |
| MessageConfig | [JourneyCustomMessage](#apps-application-id-journeys-journey-id-model-journeycustommessage) | False | Specifies the message data included in a custom channel message that's sent to participants in a journey. |
| NextActivity | string | False | The unique identifier for the next activity to perform, after Amazon Pinpoint calls the AWS Lambda function or web hook. |
| TemplateName | string | False | The name of the custom message template to use for the message. If specified, this value must match the name of an existing message template.  |
| TemplateVersion | string | False | The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### EmailMessageActivity
<a name="apps-application-id-journeys-journey-id-model-emailmessageactivity"></a>

Specifies the settings for an email activity in a journey. This type of activity sends an email message to participants.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MessageConfig | [JourneyEmailMessage](#apps-application-id-journeys-journey-id-model-journeyemailmessage) | False | Specifies the sender address for an email message that's sent to participants in the journey. |
| NextActivity | string | False | The unique identifier for the next activity to perform, after the message is sent. |
| TemplateName | string | False | The name of the email message template to use for the message. If specified, this value must match the name of an existing message template.  |
| TemplateVersion | string | False | The unique identifier for the version of the email template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### EventCondition
<a name="apps-application-id-journeys-journey-id-model-eventcondition"></a>

Specifies the conditions to evaluate for an event that applies to an activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Dimensions | [EventDimensions](#apps-application-id-journeys-journey-id-model-eventdimensions) | False | The dimensions for the event filter to use for the activity. |
| MessageActivity | string | False | The message identifier (`message_id`) for the message to use when determining whether message events meet the condition. |

### EventDimensions
<a name="apps-application-id-journeys-journey-id-model-eventdimensions"></a>

Specifies the dimensions for an event filter that determines when a campaign is sent or a journey activity is performed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter. |
| EventType | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as `_email.delivered` or `_custom.delivered`. For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see [Streaming Amazon Pinpoint Events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) in the *Amazon Pinpoint Developer Guide*. |
| Metrics | object | False | One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter. |

### EventFilter
<a name="apps-application-id-journeys-journey-id-model-eventfilter"></a>

Specifies the settings for an event that causes a campaign to be sent or a journey activity to be performed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Dimensions | [EventDimensions](#apps-application-id-journeys-journey-id-model-eventdimensions) | True | The dimensions for the event filter to use for the campaign or the journey activity. |
| FilterType | string<br />Values: `SYSTEM \| ENDPOINT \| USER` | True | The type of event that causes the campaign to be sent or the journey activity to be performed. Valid values are: `SYSTEM`, sends the campaign or performs the activity when a system event occurs; and, `ENDPOINT`, sends the campaign or performs the activity when an endpoint event ([Events resource](apps-application-id-events.md)) occurs. |

### EventStartCondition
<a name="apps-application-id-journeys-journey-id-model-eventstartcondition"></a>

Specifies the settings for an event that causes a journey activity to start.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EventFilter | [EventFilter](#apps-application-id-journeys-journey-id-model-eventfilter) | False | The EventFilter for defined for scheduling Event based Journey |
| SegmentId | string | False | Accept only Endpoints events from this specific dynamic segmentId |

### GPSCoordinates
<a name="apps-application-id-journeys-journey-id-model-gpscoordinates"></a>

Specifies the GPS coordinates of a location.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Latitude | number | True | The latitude coordinate of the location. |
| Longitude | number | True | The longitude coordinate of the location. |

### GPSPointDimension
<a name="apps-application-id-journeys-journey-id-model-gpspointdimension"></a>

Specifies GPS-based criteria for including or excluding endpoints from a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Coordinates | [GPSCoordinates](#apps-application-id-journeys-journey-id-model-gpscoordinates) | True | The GPS coordinates to measure distance from. |
| RangeInKilometers | number | False | The range, in kilometers, from the GPS coordinates. |

### HoldoutActivity
<a name="apps-application-id-journeys-journey-id-model-holdoutactivity"></a>

Specifies the settings for a holdout activity in a journey. This type of activity stops a journey for a specified percentage of participants.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| NextActivity | string | False | The unique identifier for the next activity to perform, after performing the holdout activity. |
| Percentage | integer | True | The percentage of participants who shouldn't continue the journey.<br />To determine which participants are held out, Amazon Pinpoint applies a probability-based algorithm to the percentage that you specify. Therefore, the actual percentage of participants who are held out may not be equal to the percentage that you specify. |

### JourneyCustomMessage
<a name="apps-application-id-journeys-journey-id-model-journeycustommessage"></a>

Specifies the message content for a custom channel message that's sent to participants in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Data | string | False | The message content that's passed to an AWS Lambda function or to a web hook. |

### JourneyEmailMessage
<a name="apps-application-id-journeys-journey-id-model-journeyemailmessage"></a>

Specifies the "From" address for an email message that's sent to participants in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| FromAddress | string | False | The verified email address to send the email message from. The default address is the `FromAddress` specified for the email channel for the application. |

### JourneyLimits
<a name="apps-application-id-journeys-journey-id-model-journeylimits"></a>

Specifies limits on the messages that a journey can send and the number of times participants can enter a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DailyCap | integer | False | The maximum number of messages that the journey can send to a single participant during a 24-hour period. The maximum value is 100. |
| EndpointReentryCap | integer | False | The maximum number of times that a participant can enter the journey. The maximum value is 100. To allow participants to enter the journey an unlimited number of times, set this value to `0`. |
| EndpointReentryInterval | string | False | Minimum time that must pass before an endpoint can re-enter a given journey. |
| MessagesPerSecond | integer | False | The maximum number of messages that the journey can send each second. |
| TimeframeCap | [JourneyTimeframeCap](#apps-application-id-journeys-journey-id-model-journeytimeframecap) | False | The number of messages that an endpoint can receive during the specified timeframe. |
| TotalCap | integer | False | The maximum number of messages a journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply. |

### JourneyPushMessage
<a name="apps-application-id-journeys-journey-id-model-journeypushmessage"></a>

Specifies the message configuration for a push notification that's sent to participants in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| TimeToLive | string | False | The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when it's sent to a push notification service. If this value is `0`, the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.<br />This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service. |

### JourneyResponse
<a name="apps-application-id-journeys-journey-id-model-journeyresponse"></a>

Provides information about the status, configuration, and other settings for a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Activities | object | False | A map that contains a set of `Activity` objects, one object for each activity in the journey. For each `Activity` object, the key is the unique identifier (string) for an activity and the value is the settings for the activity. |
| ApplicationId | string | True | The unique identifier for the application that the journey applies to. |
| ClosedDays | [ClosedDays](#apps-application-id-journeys-journey-id-model-closeddays) | False | The time when a journey will not send messages. QuietTime should be configured first and SendingSchedule should be set to true. |
| CreationDate | string | False | The date, in ISO 8601 format, when the journey was created. |
| Id | string | True | The unique identifier for the journey. |
| LastModifiedDate | string | False | The date, in ISO 8601 format, when the journey was last modified. |
| Limits | [JourneyLimits](#apps-application-id-journeys-journey-id-model-journeylimits) | False | The messaging and entry limits for the journey. |
| LocalTime | boolean | False | Specifies whether the journey's scheduled start and end times use each participant's local time. If this value is `true`, the schedule uses each participant's local time. |
| Name | string | False | The name of the journey. |
| OpenHours | [OpenHours](#apps-application-id-journeys-journey-id-model-openhours) | False | The time when a journey can send messages. QuietTime should be configured first and SendingSchedule should be set to true. |
| QuietTime | [QuietTime](#apps-application-id-journeys-journey-id-model-quiettime) | False | The quiet time settings for the journey. Quiet time is a specific time range when a journey doesn't send messages to participants, if all the following conditions are met:+  The `EndpointDemographic.Timezone` property of the endpoint for the participant is set to a valid value. <br />+  The current time in the participant's time zone is later than or equal to the time specified by the `QuietTime.Start` property for the journey. <br />+  The current time in the participant's time zone is earlier than or equal to the time specified by the `QuietTime.End` property for the journey. <br />If any of the preceding conditions isn't met, the participant will receive messages from the journey, even if quiet time is enabled. |
| RefreshFrequency | string | False | The frequency with which Amazon Pinpoint evaluates segment and event data for the journey, as a duration in ISO 8601 format. |
| RefreshOnSegmentUpdate | boolean | False | Indicates whether the journey participants should be refreshed when a segment is updated. |
| Schedule | [JourneySchedule](#apps-application-id-journeys-journey-id-model-journeyschedule) | False | The schedule settings for the journey. |
| SendingSchedule | boolean | False | Indicates if journey has Advance Quiet Time enabled. This flag should be set to true in order to allow using OpenHours and ClosedDays. |
| StartActivity | string | False | The unique identifier for the first activity in the journey. |
| StartCondition | [StartCondition](#apps-application-id-journeys-journey-id-model-startcondition) | False | The segment that defines which users are participants in the journey. |
| State | string<br />Values: `DRAFT \| ACTIVE \| PAUSED \| COMPLETED \| CANCELLED \| CLOSED \| PENDING_APPROVAL` | False | The current status of the journey. Possible values are:+   `DRAFT` – The journey is being developed and hasn't been published yet. <br />+   `ACTIVE` – The journey has been developed and published. Depending on the journey's schedule, the journey may currently be running or scheduled to start running at a later time. If a journey's status is `ACTIVE`, you can't add, change, or remove activities from it. <br />+   `COMPLETED` – The journey has been published and has finished running. All participants have entered the journey and no participants are waiting to complete the journey or any activities in the journey. <br />+   `CANCELLED` – The journey has been stopped. If a journey's status is `CANCELLED`, you can't add, change, or remove activities or segment settings from the journey. <br />+   `CLOSED` – The journey has been published and has started running. It may have also passed its scheduled end time, or passed its scheduled start time and a refresh frequency hasn't been specified for it. If a journey's status is `CLOSED`, you can't add participants to it, and no existing participants can enter the journey for the first time. However, any existing participants who are currently waiting to start an activity may continue the journey.  A journey in the `CLOSED` state is still counted against the **Maximum number of active journeys** quota. For more information see [Journey quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html#quotas-journeys).   |
| tags | object | False | This object is not used or supported. |
| TimezoneEstimationMethods | Array of type string<br />Values: `PHONE_NUMBER \| POSTAL_CODE` | False | An array of time zone estimation methods, if any, to use for determining an [Endpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html) time zone if the Endpoint does not have a value for the `Demographic.Timezone` attribute. +  `PHONE_NUMBER` - A time zone is estimated based on the `Endpoint.Location.Country` and `Endpoint.Address`. <br />+  `POSTAL_CODE` - A time zone is estimated based on the `Endpoint.Location.Country` and `Endpoint.Location.PostalCode`.  `POSTAL_CODE` estimation is only supported in the United States, United Kingdom, Australia, New Zealand, Canada, France, Italy, Spain, Germany and in regions where Amazon Pinpoint is available.  <br />+  Both - A time zone is estimated based on the `Endpoint.Location.Country`, `Endpoint.Address` and `Endpoint.Location.PostalCode`.  |
| WaitForQuietTime | boolean | False | Indicates whether endpoints in quiet hours should enter a wait activity until quiet hours have elapsed. |

### JourneySMSMessage
<a name="apps-application-id-journeys-journey-id-model-journeysmsmessage"></a>

Specifies the sender ID and message type for an SMS message that's sent to participants in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EntityId | string | False | A registered Entity ID (currently only used when sending messages to recipients in India). |
| MessageType | string<br />Values: `TRANSACTIONAL \| PROMOTIONAL` | False | The SMS message type. Valid values are `TRANSACTIONAL` (for messages that are critical or time-sensitive, such as a one-time passwords) and `PROMOTIONAL` (for messsages that aren't critical or time-sensitive, such as marketing messages). |
| OriginationNumber | string | False | The number to send the SMS message from. The phone number that you specify must exist in your Amazon Pinpoint account—you can't pass an arbitrary phone number. If you want to use a sender ID to send your message, omit this parameter and use `SenderId` instead. |
| SenderId | string | False | The sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country. For more information, see [Supported Countries and Regions](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html) in the Amazon Pinpoint User Guide. |
| TemplateId | string | False | A registered Template ID (currently only used when sending messages to recipients in India). |

### JourneySchedule
<a name="apps-application-id-journeys-journey-id-model-journeyschedule"></a>

Specifies the schedule settings for a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndTime | string | False | The scheduled time, in ISO 8601 format, when the journey ended or will end. |
| StartTime | string | False | The scheduled time, in ISO 8601 format, when the journey began or will begin. |
| Timezone | string | False | The starting UTC offset for the journey schedule, if the value of the journey's `LocalTime` property is `true`. Valid values are: `UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+08:45, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+12:45, UTC+13, UTC+13:45, UTC-02, UTC-02:30, UTC-03, UTC-03:30, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-09:30, UTC-10, and UTC-11`. |

### JourneyTimeframeCap
<a name="apps-application-id-journeys-journey-id-model-journeytimeframecap"></a>

The number of messages that can be sent to an endpoint during the specified timeframe for all journeys.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Cap | integer | False | The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply. |
| Days | integer | False | The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply. |

### MessageBody
<a name="apps-application-id-journeys-journey-id-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MetricDimension
<a name="apps-application-id-journeys-journey-id-model-metricdimension"></a>

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ComparisonOperator | string | True | The operator to use when comparing metric values. Valid values are: `GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL`, `LESS_THAN_OR_EQUAL`, and `EQUAL`. |
| Value | number | True | The value to compare. |

### MultiConditionalBranch
<a name="apps-application-id-journeys-journey-id-model-multiconditionalbranch"></a>

Specifies a condition to evaluate for an activity path in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Condition | [SimpleCondition](#apps-application-id-journeys-journey-id-model-simplecondition) | False | The condition to evaluate for the activity path. |
| NextActivity | string | False | The unique identifier for the next activity to perform, after completing the activity for the path. |

### MultiConditionalSplitActivity
<a name="apps-application-id-journeys-journey-id-model-multiconditionalsplitactivity"></a>

Specifies the settings for a multivariate split activity in a journey. This type of activity sends participants down one of as many as five paths (including a default *Else* path) in a journey, based on conditions that you specify.

**Note**
To create multivariate split activities that send participants down different paths based on push notification events (such as Open or Received events), your mobile app has to specify the User ID and Endpoint ID values. For more information, see [Integrating Amazon Pinpoint with your application](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate.html) in the *Amazon Pinpoint Developer Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Branches | Array of type [MultiConditionalBranch](#apps-application-id-journeys-journey-id-model-multiconditionalbranch) | False | The paths for the activity, including the conditions for entering each path and the activity to perform for each path. |
| DefaultActivity | string | False | The unique identifier for the activity to perform for participants who don't meet any of the conditions specified for other paths in the activity. |
| EvaluationWaitTime | [WaitTime](#apps-application-id-journeys-journey-id-model-waittime) | False | The amount of time to wait or the date and time when Amazon Pinpoint determines whether the conditions are met. |

### OpenHours
<a name="apps-application-id-journeys-journey-id-model-openhours"></a>

Specifies the times when message are allowed to be sent to endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CUSTOM | object | False | Specifies the schedule settings for the custom channel. |
| EMAIL | object | False | Specifies the schedule settings for the email channel. |
| PUSH | object | False | Specifies the schedule settings for the push channel. |
| SMS | object | False | Specifies the schedule settings for the SMS channel. |
| VOICE | object | False | Specifies the schedule settings for the voice channel. |

### OpenHoursRule
<a name="apps-application-id-journeys-journey-id-model-openhoursrule"></a>

Specifies the start and end time for OpenHours.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndTime | string | True | The end of the scheduled time, in ISO 8601 format, when the channel can't send messages. |
| StartTime | string | True | The start of the scheduled time, in ISO 8601 format, when the channel can send messages. |

### PushMessageActivity
<a name="apps-application-id-journeys-journey-id-model-pushmessageactivity"></a>

Specifies the settings for a push notification activity in a journey. This type of activity sends a push notification to participants.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MessageConfig | [JourneyPushMessage](#apps-application-id-journeys-journey-id-model-journeypushmessage) | False | Specifies the time to live (TTL) value for push notifications that are sent to participants in a journey.  |
| NextActivity | string | False | The unique identifier for the next activity to perform, after the message is sent. |
| TemplateName | string | False | The name of the push notification template to use for the message. If specified, this value must match the name of an existing message template.  |
| TemplateVersion | string | False | The unique identifier for the version of the push notification template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### QuietTime
<a name="apps-application-id-journeys-journey-id-model-quiettime"></a>

Specifies the start and end times that define a time range when messages aren't sent to endpoints.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| End | string | False | The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |
| Start | string | False | The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM. |

### RandomSplitActivity
<a name="apps-application-id-journeys-journey-id-model-randomsplitactivity"></a>

Specifies the settings for a random split activity in a journey. This type of activity randomly sends specified percentages of participants down one of as many as five paths in a journey, based on conditions that you specify.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Branches | Array of type [RandomSplitEntry](#apps-application-id-journeys-journey-id-model-randomsplitentry) | False | The paths for the activity, including the percentage of participants to enter each path and the activity to perform for each path. |

### RandomSplitEntry
<a name="apps-application-id-journeys-journey-id-model-randomsplitentry"></a>

Specifies the settings for a path in a random split activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| NextActivity | string | False | The unique identifier for the next activity to perform, after completing the activity for the path. |
| Percentage | integer | False | The percentage of participants to send down the activity path.<br />To determine which participants are sent down each path, Amazon Pinpoint applies a probability-based algorithm to the percentages that you specify for the paths. Therefore, the actual percentage of participants who are sent down a path may not be equal to the percentage that you specify. |

### RecencyDimension
<a name="apps-application-id-journeys-journey-id-model-recencydimension"></a>

Specifies criteria for including or excluding endpoints from a segment based on how recently an endpoint was active.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Duration | string<br />Values: `HR_24 \| DAY_7 \| DAY_14 \| DAY_30` | True | The duration to use when determining whether an endpoint is active or inactive. |
| RecencyType | string<br />Values: `ACTIVE \| INACTIVE` | True | The type of recency dimension to use for the segment. Valid values are: `ACTIVE`, endpoints that were active within the specified duration are included in the segment; and, `INACTIVE`, endpoints that weren't active within the specified duration are included in the segment. |

### SMSMessageActivity
<a name="apps-application-id-journeys-journey-id-model-smsmessageactivity"></a>

Specifies the settings for an SMS activity in a journey. This type of activity sends a text message to participants.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MessageConfig | [JourneySMSMessage](#apps-application-id-journeys-journey-id-model-journeysmsmessage) | False | Specifies the sender ID and message type for an SMS message that's sent to participants in a journey.  |
| NextActivity | string | False | The unique identifier for the next activity to perform, after the message is sent. |
| TemplateName | string | False | The name of the SMS message template to use for the message. If specified, this value must match the name of an existing message template.  |
| TemplateVersion | string | False | The unique identifier for the version of the SMS template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### SegmentBehaviors
<a name="apps-application-id-journeys-journey-id-model-segmentbehaviors"></a>

Specifies dimension settings for including or excluding endpoints from a segment based on how recently an endpoint was active.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Recency | [RecencyDimension](#apps-application-id-journeys-journey-id-model-recencydimension) | False | The dimension settings that are based on how recently an endpoint was active. |

### SegmentCondition
<a name="apps-application-id-journeys-journey-id-model-segmentcondition"></a>

Specifies a segment to associate with an activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| SegmentId | string | True | The unique identifier for the segment to associate with the activity. |

### SegmentDemographics
<a name="apps-application-id-journeys-journey-id-model-segmentdemographics"></a>

Specifies demographic-based dimension settings for including or excluding endpoints from a segment. These settings derive from characteristics of endpoint devices, such as platform, make, and model.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AppVersion | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The app version criteria for the segment. |
| Channel | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The channel criteria for the segment. |
| DeviceType | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The device type criteria for the segment. |
| Make | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The device make criteria for the segment. |
| Model | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The device model criteria for the segment. |
| Platform | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The device platform criteria for the segment. |

### SegmentDimensions
<a name="apps-application-id-journeys-journey-id-model-segmentdimensions"></a>

Specifies the dimension settings for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | One or more custom attributes to use as criteria for the segment. For more information see [AttributeDimension](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#apps-application-id-segments-model-attributedimension) |
| Behavior | [SegmentBehaviors](#apps-application-id-journeys-journey-id-model-segmentbehaviors) | False | The behavior-based criteria, such as how recently users have used your app, for the segment. |
| Demographic | [SegmentDemographics](#apps-application-id-journeys-journey-id-model-segmentdemographics) | False | The demographic-based criteria, such as device platform, for the segment. |
| Location | [SegmentLocation](#apps-application-id-journeys-journey-id-model-segmentlocation) | False | The location-based criteria, such as region or GPS coordinates, for the segment. |
| Metrics | object | False | One or more custom metrics to use as criteria for the segment. |
| UserAttributes | object | False | One or more custom user attributes to use as criteria for the segment. |

### SegmentLocation
<a name="apps-application-id-journeys-journey-id-model-segmentlocation"></a>

Specifies geographical dimension settings for a segment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Country | [SetDimension](#apps-application-id-journeys-journey-id-model-setdimension) | False | The country or region code, in ISO 3166-1 alpha-2 format, for the segment. |
| GPSPoint | [GPSPointDimension](#apps-application-id-journeys-journey-id-model-gpspointdimension) | False | The GPS location and range for the segment. |

### SetDimension
<a name="apps-application-id-journeys-journey-id-model-setdimension"></a>

Specifies the dimension type and values for a segment dimension.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DimensionType | string<br />Values: `INCLUSIVE \| EXCLUSIVE` | False | The type of segment dimension to use. Valid values are: `INCLUSIVE`, endpoints that match the criteria are included in the segment; and, `EXCLUSIVE`, endpoints that match the criteria are excluded from the segment. |
| Values | Array of type string | True | The criteria values to use for the segment dimension. Depending on the value of the `DimensionType` property, endpoints are included or excluded from the segment if their values match the criteria values. |

### SimpleCondition
<a name="apps-application-id-journeys-journey-id-model-simplecondition"></a>

Specifies a condition to evaluate for an activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EventCondition | [EventCondition](#apps-application-id-journeys-journey-id-model-eventcondition) | False | The dimension settings for the event that's associated with the activity. |
| SegmentCondition | [SegmentCondition](#apps-application-id-journeys-journey-id-model-segmentcondition) | False | The segment that's associated with the activity. |
| segmentDimensions | [SegmentDimensions](#apps-application-id-journeys-journey-id-model-segmentdimensions) | False | The dimension settings for the segment that's associated with the activity. |

### StartCondition
<a name="apps-application-id-journeys-journey-id-model-startcondition"></a>

Specifies the conditions for the first activity in a journey. This activity and its conditions determine which users are participants in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Description | string | False | The custom description of the condition. |
| EventStartCondition | [EventStartCondition](#apps-application-id-journeys-journey-id-model-eventstartcondition) | False | The event start condition that can trigger a journey. |
| SegmentStartCondition | [SegmentCondition](#apps-application-id-journeys-journey-id-model-segmentcondition) | False | The segment that's associated with the first activity in the journey. This segment determines which users are participants in the journey. |

### WaitActivity
<a name="apps-application-id-journeys-journey-id-model-waitactivity"></a>

Specifies the settings for a wait activity in a journey. This type of activity waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| NextActivity | string | False | The unique identifier for the next activity to perform, after performing the wait activity. |
| WaitTime | [WaitTime](#apps-application-id-journeys-journey-id-model-waittime) | False | The amount of time to wait or the date and time when the activity moves participants to the next activity in the journey. |

### WaitTime
<a name="apps-application-id-journeys-journey-id-model-waittime"></a>

Specifies a duration or a date and time that indicates when Amazon Pinpoint determines whether an activity's conditions have been met or an activity moves participants to the next activity in a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| WaitFor | string | False | The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activity's conditions have been met or moving participants to the next activity in the journey. |
| WaitUntil | string | False | The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activity's conditions have been met or the activity moves participants to the next activity in the journey. |

### WriteJourneyRequest
<a name="apps-application-id-journeys-journey-id-model-writejourneyrequest"></a>

Specifies the configuration and other settings for a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Activities | object | False | A map that contains a set of `Activity` objects, one object for each activity in the journey. For each `Activity` object, the key is the unique identifier (string) for an activity and the value is the settings for the activity. An activity identifier can contain a maximum of 100 characters. The characters must be alphanumeric characters. |
| ClosedDays | [ClosedDays](#apps-application-id-journeys-journey-id-model-closeddays) | False | The time when journey will stop sending messages. QuietTime should be configured first and SendingSchedule should be set to true. |
| CreationDate | string | False | The date, in ISO 8601 format, when the journey was created. |
| LastModifiedDate | string | False | The date, in ISO 8601 format, when the journey was last modified. |
| Limits | [JourneyLimits](#apps-application-id-journeys-journey-id-model-journeylimits) | False | The messaging and entry limits for the journey. |
| LocalTime | boolean | False | Specifies whether the journey's scheduled start and end times use each participant's local time. To base the schedule on each participant's local time, set this value to `true`. |
| Name | string | False | The name of the journey. A journey name can contain a maximum of 150 characters. The characters can be alphanumeric characters or symbols, such as underscores (\_) or hyphens (-). A journey name can't contain any spaces. |
| OpenHours | [OpenHours](#apps-application-id-journeys-journey-id-model-openhours) | False | The time when journey allow to send messages. QuietTime should be configured first and SendingSchedule should be set to true. |
| QuietTime | [QuietTime](#apps-application-id-journeys-journey-id-model-quiettime) | False | The quiet time settings for the journey. Quiet time is a specific time range when a journey doesn't send messages to participants, if all the following conditions are met:+  The `EndpointDemographic.Timezone` property of the endpoint for the participant is set to a valid value. <br />+  The current time in the participant's time zone is later than or equal to the time specified by the `QuietTime.Start` property for the journey. <br />+  The current time in the participant's time zone is earlier than or equal to the time specified by the `QuietTime.End` property for the journey. <br />If any of the preceding conditions isn't met, the participant will receive messages from the journey, even if quiet time is enabled. |
| RefreshFrequency | string | False | The frequency with which Amazon Pinpoint evaluates segment and event data for the journey, as a duration in ISO 8601 format. |
| RefreshOnSegmentUpdate | boolean | False | Indicates whether the journey participants should be refreshed when a segment is updated. |
| Schedule | [JourneySchedule](#apps-application-id-journeys-journey-id-model-journeyschedule) | False | The schedule settings for the journey. |
| SendingSchedule | boolean | False | Indicates if journey has Advance Quiet Time enabled. This flag should be set to true in order to allow using OpenHours and ClosedDays. |
| StartActivity | string | False | The unique identifier for the first activity in the journey. The identifier for this activity can contain a maximum of 128 characters. The characters must be alphanumeric characters. |
| StartCondition | [StartCondition](#apps-application-id-journeys-journey-id-model-startcondition) | False | The segment that defines which users are participants in the journey. |
| State | string<br />Values: `DRAFT \| ACTIVE \| PAUSED \| COMPLETED \| CANCELLED \| CLOSED \| PENDING_APPROVAL` | False | The status of the journey. Valid values are:+   `DRAFT` – Saves the journey and doesn't publish it. <br />+   `ACTIVE` – Saves and publishes the journey. Depending on the journey's schedule, the journey starts running immediately or at the scheduled start time. If a journey's status is `ACTIVE`, you can't add, change, or remove activities from it. <br />The `CANCELLED`, `COMPLETED`, and `CLOSED` values are not supported in requests to create or update a journey. To cancel a journey, use the [Journey State](apps-application-id-journeys-journey-id-state.md) resource. |
| TimezoneEstimationMethods | Array of type string<br />Values: `PHONE_NUMBER \| POSTAL_CODE` | False | An array of time zone estimation methods, if any, to use for determining an [Endpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html) time zone if the Endpoint does not have a value for the `Demographic.Timezone` attribute. +  `PHONE_NUMBER` - A time zone is estimated based on the `Endpoint.Location.Country` and `Endpoint.Address`. <br />+  `POSTAL_CODE` - A time zone is estimated based on the `Endpoint.Location.Country` and `Endpoint.Location.PostalCode`.  `POSTAL_CODE` estimation is only supported in the United States, United Kingdom, Australia, New Zealand, Canada, France, Italy, Spain, Germany and in regions where Amazon Pinpoint is available.  <br />+  Both - A time zone is estimated based on the `Endpoint.Location.Country`, `Endpoint.Address` and `Endpoint.Location.PostalCode`.  |
| WaitForQuietTime | boolean | False | Indicates whether endpoints in quiet hours should enter a wait activity until quiet hours have elapsed. |

## See also
<a name="apps-application-id-journeys-journey-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetJourney
<a name="GetJourney-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/GetJourney)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetJourney)

### UpdateJourney
<a name="UpdateJourney-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/UpdateJourney)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateJourney)

### DeleteJourney
<a name="DeleteJourney-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/DeleteJourney)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteJourney)
