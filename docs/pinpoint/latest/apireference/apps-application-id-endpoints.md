---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Endpoints
<a name="apps-application-id-endpoints"></a>

An *endpoint* represents a destination that you can send messages to, such as a mobile device, email address, or phone number.

You can use the Endpoints resource to create, retrieve information about, or update a batch of endpoints for a specific application. This includes updating the settings and attributes of a batch of endpoints for an application. A batch can include up to 100 endpoints. To perform these tasks for a single endpoint, use the [Endpoint](apps-application-id-endpoints-endpoint-id.md) resource.

 **Note:** Quotas apply to the number of custom attributes that you can define for endpoints. If you send a PUT request that defines additional custom attributes for a batch of endpoints and the addition of these attributes exceeds these quotas, Amazon Pinpoint returns an HTTP 400 response. For information about the quotas that apply to attributes, see [Amazon Pinpoint Quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/limits.html) in the *Amazon Pinpoint Developer Guide*. To remove custom attributes from endpoints, use the [Attributes](apps-application-id-attributes-attribute-type.md) resource.

## URI
<a name="apps-application-id-endpoints-url"></a>

`/v1/apps/{{application-id}}/endpoints`

## HTTP methods
<a name="apps-application-id-endpoints-http-methods"></a>

### PUT
<a name="apps-application-id-endpointsput"></a>

**Operation ID:** `UpdateEndpointsBatch`

Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

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
| 202 | MessageBody | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-endpointsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Endpoints resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-endpoints-schemas"></a>

### Request bodies
<a name="apps-application-id-endpoints-request-examples"></a>

#### PUT schema
<a name="apps-application-id-endpoints-request-body-put-example"></a>

```
{
  "Item": [
    {
      "ChannelType": enum,
      "Address": "string",
      "EndpointStatus": "string",
      "OptOut": "string",
      "RequestId": "string",
      "Location": {
        "Latitude": number,
        "Longitude": number,
        "PostalCode": "string",
        "City": "string",
        "Region": "string",
        "Country": "string"
      },
      "Demographic": {
        "Make": "string",
        "Model": "string",
        "ModelVersion": "string",
        "Timezone": "string",
        "Locale": "string",
        "AppVersion": "string",
        "Platform": "string",
        "PlatformVersion": "string"
      },
      "EffectiveDate": "string",
      "Attributes": {
      },
      "Metrics": {
      },
      "User": {
        "UserId": "string",
        "UserAttributes": {
        }
      },
      "Id": "string"
    }
  ]
}
```

### Response bodies
<a name="apps-application-id-endpoints-response-examples"></a>

#### MessageBody schema
<a name="apps-application-id-endpoints-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-endpoints-properties"></a>

### EndpointBatchItem
<a name="apps-application-id-endpoints-model-endpointbatchitem"></a>

Specifies an endpoint to create or update and the settings and attributes to set or change for the endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Address | string | False | The destination address for messages or push notifications that you send to the endpoint. The address varies by channel. For a push notification channel, use the token provided by the push notification service, such as an Apple Push Notification service (APNs) device token or a Firebase Cloud Messaging (FCM) registration token. For the SMS channel, use a phone number in E.164 format, such as \+12065550100. For the email channel, use an email address.<br />If the endpoint is created without an address then *OptOut* is automatically set to `ALL`. When an address is added *OptOut* has to be set to `NONE` for the endpoint to receive messages. |
| Attributes | object | False | One or more custom attributes that describe the endpoint by associating a name with an array of values. For example, the value of a custom attribute named `Interests` might be: `["Science", "Music", "Travel"]`. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.<br />An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (\#), colon (:), question mark (?), backslash (\\), and slash (/). The Amazon Pinpoint console can't display attribute names that contain these characters. This restriction doesn't apply to attribute values. |
| ChannelType | string<br />Values: `PUSH \| GCM \| APNS \| APNS_SANDBOX \| APNS_VOIP \| APNS_VOIP_SANDBOX \| ADM \| SMS \| VOICE \| EMAIL \| BAIDU \| CUSTOM \| IN_APP` | False | The channel to use when sending messages or push notifications to the endpoint. |
| Demographic | [EndpointDemographic](#apps-application-id-endpoints-model-endpointdemographic) | False | The demographic information for the endpoint, such as the time zone and platform. |
| EffectiveDate | string | False | The date and time, in ISO 8601 format, when the endpoint was created or updated. |
| EndpointStatus | string | False | Specifies whether to send messages or push notifications to the endpoint. Valid values are: `ACTIVE`, messages are sent to the endpoint; and, `INACTIVE`, messages aren’t sent to the endpoint.<br />Amazon Pinpoint automatically sets this value to `ACTIVE` when you create an endpoint or update an existing endpoint. Amazon Pinpoint automatically sets this value to `INACTIVE` if you update another endpoint that has the same address specified by the `Address` property.<br />If an endpoint is `ACTIVE`, Amazon Pinpoint will send messages through campaigns and journeys. If an `ACTIVE` endpoint enters a journey and becomes `INACTIVE` before completing the journey, Amazon Pinpoint will continue to send messages to the endpoint. If the value of `EndpointStatus` for an endpoint is `INACTIVE`, and you send a message to that endpoint through a campaign or journey, Amazon Pinpoint doesn’t attempt to send the message. If you send a message using the [SendMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#SendMessages) and [SendUserMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-users-messages.html#SendUsersMessages) API, the value of `EndpointStatus` is ignored.  |
| Id | string | False | The case insensitive unique identifier for the endpoint in the context of the batch. The identifier can't contain `$`, `{` or `}`. |
| Location | [EndpointLocation](#apps-application-id-endpoints-model-endpointlocation) | False | The geographic information for the endpoint. |
| Metrics | object | False | One or more custom metrics that your app reports to Amazon Pinpoint for the endpoint. |
| OptOut | string | False | Specifies whether the user who's associated with the endpoint has opted out of receiving messages and push notifications from you. Possible values are: `ALL`, the user has opted out and doesn't want to receive any messages or push notifications; and, `NONE`, the user hasn't opted out and wants to receive all messages and push notifications. If the value of `OptOut` for an endpoint is `ALL`, and you send a message to that endpoint through a campaign or journey, Amazon Pinpoint doesn’t attempt to send the message. If you send a message using the [SendMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#SendMessages) API, the value of `OptOut` is ignored.  |
| RequestId | string | False | The unique identifier for the request to create or update the endpoint. |
| User | [EndpointUser](#apps-application-id-endpoints-model-endpointuser) | False | One or more custom attributes that describe the user who's associated with the endpoint. |

### EndpointBatchRequest
<a name="apps-application-id-endpoints-model-endpointbatchrequest"></a>

Specifies a batch of endpoints to create or update and the settings and attributes to set or change for each endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [EndpointBatchItem](#apps-application-id-endpoints-model-endpointbatchitem) | True | An array that defines the endpoints to create or update and, for each endpoint, the property values to set or change. An array can contain a maximum of 100 items. |

### EndpointDemographic
<a name="apps-application-id-endpoints-model-endpointdemographic"></a>

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

### EndpointLocation
<a name="apps-application-id-endpoints-model-endpointlocation"></a>

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
<a name="apps-application-id-endpoints-model-endpointuser"></a>

Specifies data for one or more attributes that describe the user who's associated with an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| UserAttributes | object | False | One or more custom attributes that describe the user by associating a name with an array of values. For example, the value of an attribute named `Interests` might be: `["Science", "Music", "Travel"]`. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.<br />An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (\#), colon (:), question mark (?), backslash (\\), and slash (/). The Amazon Pinpoint console can't display attribute names that contain these characters. This restriction doesn't apply to attribute values. |
| UserId | string | False | The unique identifier for the user. The identifier can't contain `$`, `{` or `}`. |

### MessageBody
<a name="apps-application-id-endpoints-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-endpoints-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateEndpointsBatch
<a name="UpdateEndpointsBatch-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateEndpointsBatch)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateEndpointsBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
