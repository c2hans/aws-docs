---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-eventstream.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Event Stream
<a name="apps-application-id-eventstream"></a>

The Kinesis platform offers services that you can use to load and analyze streaming data on AWS. You can configure Amazon Pinpoint to stream events to Firehose or Kinesis Data Streams. By streaming events, you enable more flexible options for analysis and storage.

You can use the Event Stream resource to create, retrieve information about, update, or delete an event stream for an application. You can configure only one event stream for each Amazon Pinpoint application. To combine data from multiple applications, configure each application to use the same stream.

## URI
<a name="apps-application-id-eventstream-url"></a>

`/v1/apps/{{application-id}}/eventstream`

## HTTP methods
<a name="apps-application-id-eventstream-http-methods"></a>

### GET
<a name="apps-application-id-eventstreamget"></a>

**Operation ID:** `GetEventStream`

Retrieves information about the event stream settings for an application.

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
| 200 | EventStream | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### POST
<a name="apps-application-id-eventstreampost"></a>

**Operation ID:** `PutEventStream`

Creates a new event stream for an application or updates the settings of an existing event stream for an application.

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
| 200 | EventStream | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="apps-application-id-eventstreamdelete"></a>

**Operation ID:** `DeleteEventStream`

Deletes the event stream for an application.

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
| 200 | EventStream | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-eventstreamoptions"></a>

Retrieves information about the communication requirements and options that are available for the Event Stream resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-eventstream-schemas"></a>

### Request bodies
<a name="apps-application-id-eventstream-request-examples"></a>

#### POST schema
<a name="apps-application-id-eventstream-request-body-post-example"></a>

```
{
  "DestinationStreamArn": "string",
  "RoleArn": "string"
}
```

### Response bodies
<a name="apps-application-id-eventstream-response-examples"></a>

#### EventStream schema
<a name="apps-application-id-eventstream-response-body-eventstream-example"></a>

```
{
  "ApplicationId": "string",
  "DestinationStreamArn": "string",
  "RoleArn": "string",
  "ExternalId": "string",
  "LastModifiedDate": "string",
  "LastUpdatedBy": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-eventstream-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-eventstream-properties"></a>

### EventStream
<a name="apps-application-id-eventstream-model-eventstream"></a>

Specifies settings for publishing event data to Amazon Kinesis Data Streams or Amazon Data Firehose delivery streams.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application to publish event data for. |
| DestinationStreamArn | string | True | The Amazon Resource Name (ARN) of the Amazon Kinesis Data Stream or Amazon Data Firehose delivery stream to publish event data to.<br />For a Kinesis Data Stream, the ARN format is: `arn:aws:kinesis:{{region}}:{{account-id}}:stream/{{stream_name}} ` <br />For a Firehose delivery stream, the ARN format is: `arn:aws:firehose:{{region}}:{{account-id}}:deliverystream/{{stream_name}} `  |
| ExternalId | string | False | (Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when publishing event data, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint. |
| LastModifiedDate | string | False | The date, in ISO 8601 format, when the event stream was last modified. |
| LastUpdatedBy | string | False | The user who last modified the event stream. |
| RoleArn | string | True | The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account. |

### MessageBody
<a name="apps-application-id-eventstream-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### WriteEventStream
<a name="apps-application-id-eventstream-model-writeeventstream"></a>

Specifies the Amazon Resource Name (ARN) of an event stream to publish events to and the AWS Identity and Access Management (IAM) role to use when publishing those events.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DestinationStreamArn | string | True | The Amazon Resource Name (ARN) of the Amazon Kinesis Data Stream or Amazon Data Firehose delivery stream that you want to publish event data to.<br />For a Kinesis Data Stream, the ARN format is: `arn:aws:kinesis:{{region}}:{{account-id}}:stream/{{stream_name}} ` <br />For a Firehose delivery stream, the ARN format is: `arn:aws:firehose:{{region}}:{{account-id}}:deliverystream/{{stream_name}} `  |
| RoleArn | string | True | The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account. |

## See also
<a name="apps-application-id-eventstream-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetEventStream
<a name="GetEventStream-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetEventStream)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetEventStream)

### PutEventStream
<a name="PutEventStream-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/PutEventStream)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/PutEventStream)

### DeleteEventStream
<a name="DeleteEventStream-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteEventStream)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteEventStream)
