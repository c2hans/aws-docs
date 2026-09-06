---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Events
<a name="apps-application-id-events"></a>

In Amazon Pinpoint, you can create *events* to record and track how users interact with your app. For example, you can log interactions such as account creations, sign-in attempts, and purchases as events.

You can use the Events resource to record events for endpoints. This includes creating events and creating or updating data for endpoints that are associated with events.

## URI
<a name="apps-application-id-events-url"></a>

`/v1/apps/{{application-id}}/events`

## HTTP methods
<a name="apps-application-id-events-http-methods"></a>

### POST
<a name="apps-application-id-eventspost"></a>

**Operation ID:** `PutEvents`

Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.

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
| 202 | EventsResponse | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-eventsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Events resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-events-schemas"></a>

### Request bodies
<a name="apps-application-id-events-request-examples"></a>

#### POST schema
<a name="apps-application-id-events-request-body-post-example"></a>

```
{
  "BatchItem": {
  }
}
```

### Response bodies
<a name="apps-application-id-events-response-examples"></a>

#### EventsResponse schema
<a name="apps-application-id-events-response-body-eventsresponse-example"></a>

```
{
  "Results": {
  }
}
```

#### MessageBody schema
<a name="apps-application-id-events-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-events-properties"></a>

### EndpointDemographic
<a name="apps-application-id-events-model-endpointdemographic"></a>

Specifies demographic information about an endpoint, such as the applicable time zone and platform.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AppVersion | string | False | The version of the app that's associated with the endpoint. Can contain a maximum of 50 characters. |
| Locale | string | False | An identifier that represents the endpoint's language, in IETF BCP 47 format. This identifier typically consists of an ISO 639-1 alpha-2 code, followed by an underscore (\_), followed by an ISO 3166-1 alpha-2 value. For example, the locale code for United States English is `en_US`.<br />In some cases, an ISO 3166-1 numeric-3 value is used instead of an ISO 3166-1 alpha-2 value. For example, the locale code for Latin American Spanish is `es_419`.<br />In other cases, the ISO 639-1 alpha-2 is replaced with a three-letter code. For example, the locale code for Hawaiian is `haw_US`. |
| Make | string | False | The manufacturer of the endpoint device, such as `Apple` or `Samsung`. Can contain a maximum of 50 characters. |
| Model | string | False | The model name or number of the endpoint device, such as `iPhone` or `SM-G900F`. Can contain a maximum of 100 characters. |
| ModelVersion | string | False | The model version of the endpoint device. Can contain a maximum of 50 characters. |
| Platform | string | False | The platform of the endpoint device, such as `iOS`. Can contain a maximum of 50 characters. |
| PlatformVersion | string | False | The version of the platform for the endpoint device. Can contain a maximum of 50 characters. |
| Timezone | string | False | The time zone of the endpoint, specified as a tz database name value, such as `America/Los_Angeles`. |

### EndpointItemResponse
<a name="apps-application-id-events-model-endpointitemresponse"></a>

Provides the status code and message that result from processing data for an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The custom message that's returned in the response as a result of processing the endpoint data. |
| StatusCode | integer | False | The status code that's returned in the response as a result of processing the endpoint data. |

### EndpointLocation
<a name="apps-application-id-events-model-endpointlocation"></a>

Specifies geographic information about an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| City | string | False | The name of the city where the endpoint is located. Can contain a maximum of 75 characters. |
| Country | string | False | A code that represents the country or region where the endpoint is located. Must be in ISO 3166-1 Alpha-2 or Alpha-3 format. For example, for the United States, you can use `US` or `USA`. |
| Latitude | number | False | The latitude coordinate of the endpoint location, rounded to one decimal place. Must be between -90 and 90. If you specify a latitude, you must also specify a longitude. |
| Longitude | number | False | The longitude coordinate of the endpoint location, rounded to one decimal place. Must be between -180 and 180. If you specify a longitude, you must also specify a latitude. |
| PostalCode | string | False | The postal or ZIP code for the area where the endpoint is located. |
| Region | string | False | The name of the region where the endpoint is located. This value is typically a first-level subdivision a country, such as a state, province, prefecture, administrative region, district, or department. Can contain a maximum of 75 characters. |

### EndpointUser
<a name="apps-application-id-events-model-endpointuser"></a>

Specifies data for one or more attributes that describe the user who's associated with an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| UserAttributes | object | False | One or more custom attributes that describe the user by associating a name with an array of values. For example, the value of an attribute named `Interests` might be: `["Science", "Music", "Travel"]`. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.<br />An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (\#), colon (:), question mark (?), backslash (\\), and slash (/). The Amazon Pinpoint console can't display attribute names that contain these characters. This restriction doesn't apply to attribute values. |
| UserId | string | False | The unique identifier for the user. The identifier can't contain `$`, `{` or `}`. |

### Event
<a name="apps-application-id-events-model-event"></a>

Specifies information about an event that reports data to Amazon Pinpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| AppPackageName | string | False | The package name of the app that's recording the event. |
| AppTitle | string | False | The title of the app that's recording the event. |
| AppVersionCode | string | False | The version number of the app that's recording the event. |
| Attributes | object | False | One or more custom attributes that are associated with the event. |
| ClientSdkVersion | string | False | The version of the SDK that's running on the client device. |
| EventType | string | True | The name of the event. Avoid using the following characters: \# : ? \\ /. The Amazon Pinpoint console doesn't correctly display event names that contain these characters.  |
| Metrics | object | False | One or more custom metrics that are associated with the event. |
| SdkName | string | False | The name of the SDK that's being used to record the event. |
| Session | [Session](#apps-application-id-events-model-session) | False | Information about the session in which the event occurred. |
| Timestamp | string | True | The date and time, in ISO 8601 format, when the event occurred. |

### EventItemResponse
<a name="apps-application-id-events-model-eventitemresponse"></a>

Provides the status code and message that result from processing an event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A custom message that's returned in the response as a result of processing the event. |
| StatusCode | integer | False | The status code that's returned in the response as a result of processing the event. Possible values are: `202`, for events that were accepted; and, `400`, for events that weren't valid. |

### EventsBatch
<a name="apps-application-id-events-model-eventsbatch"></a>

Specifies a batch of endpoints and events to process.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Endpoint | [PublicEndpoint](#apps-application-id-events-model-publicendpoint) | True | A set of properties and attributes that are associated with the endpoint. |
| Events | object | True | A set of properties that are associated with the event. |

### EventsRequest
<a name="apps-application-id-events-model-eventsrequest"></a>

Specifies a batch of events to process.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BatchItem | object | True | The batch of events to process. For each item in a batch, the endpoint ID acts as a key that has an `EventsBatch` object as its value. The identifier can't contain `$`, `{` or `}`. |

### EventsResponse
<a name="apps-application-id-events-model-eventsresponse"></a>

Provides information about endpoints and the events that they're associated with.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Results | object | False | A map that contains a multipart response for each endpoint. For each item in this object, the endpoint ID is the key and the item response is the value. If no item response exists, the value can also be one of the following: `202`, the request was processed successfully; or `400`, the payload wasn't valid or required fields were missing. |

### ItemResponse
<a name="apps-application-id-events-model-itemresponse"></a>

Provides information about the results of a request to create or update an endpoint that's associated with an event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EndpointItemResponse | [EndpointItemResponse](#apps-application-id-events-model-endpointitemresponse) | False | The response that was received after the endpoint data was accepted. |
| EventsItemResponse | object | False | A multipart response object that contains a key and a value for each event in the request. In each object, the event ID is the key and an `EventItemResponse` object is the value. |

### MessageBody
<a name="apps-application-id-events-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### PublicEndpoint
<a name="apps-application-id-events-model-publicendpoint"></a>

Specifies the properties and attributes of an endpoint that's associated with an event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Address | string | False | The unique identifier for the recipient, such as a device token, email address, or mobile phone number. |
| Attributes | object | False | One or more custom attributes that describe the endpoint by associating a name with an array of values. You can use these attributes as filter criteria when you create segments. |
| ChannelType | string<br />Values: `PUSH \| GCM \| APNS \| APNS_SANDBOX \| APNS_VOIP \| APNS_VOIP_SANDBOX \| ADM \| SMS \| VOICE \| EMAIL \| BAIDU \| CUSTOM \| IN_APP` | False | The channel that's used when sending messages or push notifications to the endpoint. |
| Demographic | [EndpointDemographic](#apps-application-id-events-model-endpointdemographic) | False | The demographic information for the endpoint, such as the time zone and platform. |
| EffectiveDate | string | False | The date and time, in ISO 8601 format, when the endpoint was last updated. |
| EndpointStatus | string | False | Specifies whether to send messages or push notifications to the endpoint. Valid values are: `ACTIVE`, messages are sent to the endpoint; and, `INACTIVE`, messages aren’t sent to the endpoint.<br />Amazon Pinpoint automatically sets this value to `ACTIVE` when you create an endpoint or update an existing endpoint. Amazon Pinpoint automatically sets this value to `INACTIVE` if you update another endpoint that has the same address specified by the `Address` property. |
| Location | [EndpointLocation](#apps-application-id-events-model-endpointlocation) | False | The geographic information for the endpoint. |
| Metrics | object | False | One or more custom metrics that your app reports to Amazon Pinpoint for the endpoint. |
| OptOut | string | False | Specifies whether the user who's associated with the endpoint has opted out of receiving messages and push notifications from you. Possible values are: `ALL`, the user has opted out and doesn't want to receive any messages or push notifications; and, `NONE`, the user hasn't opted out and wants to receive all messages and push notifications. |
| RequestId | string | False | A unique identifier that's generated each time the endpoint is updated. |
| User | [EndpointUser](#apps-application-id-events-model-endpointuser) | False | One or more custom user attributes that your app reports to Amazon Pinpoint for the user who's associated with the endpoint. |

### Session
<a name="apps-application-id-events-model-session"></a>

Provides information about a session.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Duration | integer | False | The duration of the session, in milliseconds. Duration is required if a value is provided for the StopTimestamp. |
| Id | string | True | The unique identifier for the session. |
| StartTimestamp | string | True | The date and time when the session began. |
| StopTimestamp | string | False | The date and time when the session ended. |

## See also
<a name="apps-application-id-events-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### PutEvents
<a name="PutEvents-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/PutEvents)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/PutEvents)
