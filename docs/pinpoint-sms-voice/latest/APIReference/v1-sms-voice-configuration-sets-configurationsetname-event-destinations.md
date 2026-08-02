---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Event Destinations
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations"></a>

An *event destination* is a location where you send response information about the voice messages that you send. For example, when a voice message is delivered successfully, you can send information about that event to an Amazon CloudWatch destination.

Each configuration set can contain between 0 and 10 event destinations. Each event destination can contain a reference to one (and only one) destination, such as an Amazon CloudWatch log or Amazon Kinesis Data Firehose destination.

## URI
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-url"></a>

`/v1/sms-voice/configuration-sets/{{ConfigurationSetName}}/event-destinations`

## HTTP methods
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-http-methods"></a>

### GET
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinationsget"></a>

**Operation ID:** `GetConfigurationSetEventDestinations`

Retrieves information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ConfigurationSetName}} | String | True | The name of the configuration set that contains the event destination that you want to obtain information about. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetConfigurationSetEventDestinationsResponse | An object that contains information about an event destination. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 404 | NotFoundException | The requested resource wasn't found. |
| 429 | TooManyRequestsException | You've made too many GET requests in one second. Requests are limited to 1 per second. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### POST
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinationspost"></a>

**Operation ID:** `CreateConfigurationSetEventDestination`

Creates a new event destination in a configuration set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ConfigurationSetName}} | String | True | The name of the configuration set that you want to create the event destination in. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateConfigurationSetEventDestinationResponse | An empty object that indicates that the event destination was created successfully. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 404 | NotFoundException | The requested resource wasn't found. |
| 409 | AlreadyExistsException | The resource you tried to create already exists. |
| 412 | LimitExceededException | You've tried to create a number of resources that exceeds the maximum number of resources for your account. For more information, see [Amazon Pinpoint Quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/limits.html) in the *Amazon Pinpoint Developer Guide*. |
| 429 | TooManyRequestsException | You've issued too many requests to the resource. Wait a few minutes, and then try again. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### OPTIONS
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinationsoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-schemas"></a>

### Request bodies
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-request-examples"></a>

#### POST schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-request-body-post-example"></a>

```
{
  "EventDestinationName": "string",
  "EventDestination": {
    "SnsDestination": {
      "TopicArn": "string"
    },
    "Enabled": boolean,
    "MatchingEventTypes": [
      enum
    ],
    "CloudWatchLogsDestination": {
      "IamRoleArn": "string",
      "LogGroupArn": "string"
    },
    "KinesisFirehoseDestination": {
      "DeliveryStreamArn": "string",
      "IamRoleArn": "string"
    }
  }
}
```

### Response bodies
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-examples"></a>

#### GetConfigurationSetEventDestinationsResponse schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-getconfigurationseteventdestinationsresponse-example"></a>

```
{
  "EventDestinations": [
    {
      "SnsDestination": {
        "TopicArn": "string"
      },
      "Enabled": boolean,
      "MatchingEventTypes": [
        enum
      ],
      "CloudWatchLogsDestination": {
        "IamRoleArn": "string",
        "LogGroupArn": "string"
      },
      "KinesisFirehoseDestination": {
        "DeliveryStreamArn": "string",
        "IamRoleArn": "string"
      },
      "Name": "string"
    }
  ]
}
```

#### CreateConfigurationSetEventDestinationResponse schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-createconfigurationseteventdestinationresponse-example"></a>

```
{
}
```

#### BadRequestException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-badrequestexception-example"></a>

```
{
  "Message": "string"
}
```

#### NotFoundException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-notfoundexception-example"></a>

```
{
  "Message": "string"
}
```

#### AlreadyExistsException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-alreadyexistsexception-example"></a>

```
{
  "Message": "string"
}
```

#### LimitExceededException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-limitexceededexception-example"></a>

```
{
  "Message": "string"
}
```

#### TooManyRequestsException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-toomanyrequestsexception-example"></a>

```
{
  "Message": "string"
}
```

#### InternalServiceErrorException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-response-body-internalserviceerrorexception-example"></a>

```
{
  "Message": "string"
}
```

## Properties
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-properties"></a>

### AlreadyExistsException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-alreadyexistsexception"></a>

The resource that you specified in your request already exists.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### BadRequestException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-badrequestexception"></a>

The input that you provided to the API is invalid.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### CloudWatchLogsDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-cloudwatchlogsdestination"></a>

An object that contains information about an event destination that sends data to Amazon CloudWatch Logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| IamRoleArn | string | True | The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination. |
| LogGroupArn | string | True | The name of the Amazon CloudWatch Log Group that you want to record events in. |

### CreateConfigurationSetEventDestinationRequest
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-createconfigurationseteventdestinationrequest"></a>

An object that is used to define an event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EventDestination | [EventDestinationDefinition](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventdestinationdefinition) | True | An `EventDestinationDefinition` object that includes information about the event destination itself. |
| EventDestinationName | string | True | A name that identifies the event destination. |

### CreateConfigurationSetEventDestinationResponse
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-createconfigurationseteventdestinationresponse"></a>

An empty object that indicates that the event destination was created successfully.

### EventDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventdestination"></a>

An object that defines an event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CloudWatchLogsDestination | [CloudWatchLogsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-cloudwatchlogsdestination) | False | An object that contains information about an event destination that sends data to Amazon CloudWatch Logs. |
| Enabled | boolean | False | Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination. |
| KinesisFirehoseDestination | [KinesisFirehoseDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-kinesisfirehosedestination) | False | An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose. |
| MatchingEventTypes | Array of type [EventType](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventtype) | False | The types of events that you want to send to the event destination. Possible values:   `INITIATED_CALL` - Amazon Pinpoint started trying to deliver the message to the recipient.    `RINGING` - Amazon Pinpoint initiated the phone call, and the recipient's phone is ringing.    `ANSWERED` - Amazon Pinpoint established a connection with the recipient.  This status doesn't necessarily mean that Amazon Pinpoint made a connection with a human recipient. For example, it could indicate that Amazon Pinpoint established a connection with a voicemail system.     `COMPLETED_CALL` - Amazon Pinpoint played the audio message to the recipient.  This status doesn't necessarily mean that the message was delivered to a human recipient. For example, it could indicate that the audio message was delivered to a voicemail system.     `BUSY` - Amazon Pinpoint attempted to deliver the voice message, but received a busy signal.    `FAILED` - Amazon Pinpoint wasn't able to deliver the message.    `NO_ANSWER` - Amazon Pinpoint attempted to deliver the message, but the recipient didn't answer.   |
| Name | string | False | A name that identifies the event destination configuration. |
| SnsDestination | [SnsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-snsdestination) | False | An object that contains information about an event destination that sends data to Amazon SNS. |

### EventDestinationDefinition
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventdestinationdefinition"></a>

An object that defines a single event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CloudWatchLogsDestination | [CloudWatchLogsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-cloudwatchlogsdestination) | False | An object that contains information about an event destination that sends data to Amazon CloudWatch Logs. |
| Enabled | boolean | False | Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination. |
| KinesisFirehoseDestination | [KinesisFirehoseDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-kinesisfirehosedestination) | False | An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose. |
| MatchingEventTypes | Array of type [EventType](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventtype) | True | The types of events that you want to send to the event destination. Possible values:   `INITIATED_CALL` - Amazon Pinpoint started trying to deliver the message to the recipient.    `RINGING` - Amazon Pinpoint initiated the phone call, and the recipient's phone is ringing.    `ANSWERED` - Amazon Pinpoint established a connection with the recipient.  This status doesn't necessarily mean that Amazon Pinpoint made a connection with a human recipient. For example, it could indicate that Amazon Pinpoint established a connection with a voicemail system.     `COMPLETED_CALL` - Amazon Pinpoint played the audio message to the recipient.  This status doesn't necessarily mean that the message was delivered to a human recipient. For example, it could indicate that the audio message was delivered to a voicemail system.     `BUSY` - Amazon Pinpoint attempted to deliver the voice message, but received a busy signal.    `FAILED` - Amazon Pinpoint wasn't able to deliver the message.    `NO_ANSWER` - Amazon Pinpoint attempted to deliver the message, but the recipient didn't answer.   |
| SnsDestination | [SnsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-snsdestination) | False | An object that contains information about an event destination that sends data to Amazon SNS. |

### EventType
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventtype"></a>

The types of events that are sent to the event destination. Possible values are:
+ `INITIATED_CALL`
+ `RINGING`
+ `ANSWERED`
+ `COMPLETED_CALL`
+ `BUSY`
+ `FAILED`
+ `NO_ANSWER`

### GetConfigurationSetEventDestinationsResponse
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-getconfigurationseteventdestinationsresponse"></a>

An object that contains information about an event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EventDestinations | Array of type [EventDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-eventdestination) | False | An array of `EventDestination` objects. Each `EventDestination` object includes ARNs and other information that define an event destination. |

### InternalServiceErrorException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-internalserviceerrorexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### KinesisFirehoseDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-kinesisfirehosedestination"></a>

An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryStreamArn | string | True | The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination. |
| IamRoleArn | string | True | The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream. |

### LimitExceededException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-limitexceededexception"></a>

There are too many instances of the specified resource type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### NotFoundException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-notfoundexception"></a>

The resource you attempted to access doesn't exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### SnsDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-snsdestination"></a>

An object that contains information about an event destination that sends data to Amazon SNS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| TopicArn | string | True | The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to. |

### TooManyRequestsException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-model-toomanyrequestsexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

## See also
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetConfigurationSetEventDestinations
<a name="GetConfigurationSetEventDestinations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for Python](/goto/boto3/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/GetConfigurationSetEventDestinations)

### CreateConfigurationSetEventDestination
<a name="CreateConfigurationSetEventDestination-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for Python](/goto/boto3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSetEventDestination)
