---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Event Destination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname"></a>

A *configuration set* is a set of rules that you apply to the voice messages that you send. In a configuration set, you can specify an *event destination* for specific types of events related to voice messages. An *event destination* is a location that you publish information about your voice calls to. For example, when a message is successfully delivered, you can log that event to an Amazon CloudWatch destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.

Each configuration set can contain between 0 and 10 event destinations. Each event destination can contain a reference to one (and only one) destination, such as an Amazon CloudWatch log or Amazon Kinesis Data Firehose destination.

## URI
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-url"></a>

`/v1/sms-voice/configuration-sets/{{ConfigurationSetName}}/event-destinations/{{EventDestinationName}}`

## HTTP methods
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-http-methods"></a>

### PUT
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnameput"></a>

**Operation ID:** `UpdateConfigurationSetEventDestination`

Updates an event destination in a configuration set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{EventDestinationName}} | String | True | The name of the event destination that you want to update. |
| {{ConfigurationSetName}} | String | True | The name of the configuration set that contains the event destination that you want to update. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateConfigurationSetEventDestinationResponse | An empty object that indicates that the event destination was updated successfully. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 404 | NotFoundException | The requested resource wasn't found. |
| 429 | TooManyRequestsException | You've made too many PUT requests in one second. Requests are limited to 1 per second. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### DELETE
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnamedelete"></a>

**Operation ID:** `DeleteConfigurationSetEventDestination`

Deletes an event destination from a configuration set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{EventDestinationName}} | String | True | The name of the event destination that you want to delete. |
| {{ConfigurationSetName}} | String | True | The name of the configuration set that you want to delete. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteConfigurationSetEventDestinationResponse | An empty object that indicates that the event destination was deleted successfully. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 404 | NotFoundException | The requested resource wasn't found. |
| 429 | TooManyRequestsException | You've made too many DELETE requests in one second. Requests are limited to 1 per second. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### OPTIONS
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnameoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-schemas"></a>

### Request bodies
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-request-examples"></a>

#### PUT schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-request-body-put-example"></a>

```
{
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
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-examples"></a>

#### UpdateConfigurationSetEventDestinationResponse schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-updateconfigurationseteventdestinationresponse-example"></a>

```
{
}
```

#### DeleteConfigurationSetEventDestinationResponse schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-deleteconfigurationseteventdestinationresponse-example"></a>

```
{
}
```

#### BadRequestException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-badrequestexception-example"></a>

```
{
  "Message": "string"
}
```

#### NotFoundException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-notfoundexception-example"></a>

```
{
  "Message": "string"
}
```

#### TooManyRequestsException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-toomanyrequestsexception-example"></a>

```
{
  "Message": "string"
}
```

#### InternalServiceErrorException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-response-body-internalserviceerrorexception-example"></a>

```
{
  "Message": "string"
}
```

## Properties
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-properties"></a>

### BadRequestException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-badrequestexception"></a>

The input that you provided to the API is invalid.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### CloudWatchLogsDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-cloudwatchlogsdestination"></a>

An object that contains information about an event destination that sends data to Amazon CloudWatch Logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| IamRoleArn | string | True | The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination. |
| LogGroupArn | string | True | The name of the Amazon CloudWatch Log Group that you want to record events in. |

### DeleteConfigurationSetEventDestinationResponse
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-deleteconfigurationseteventdestinationresponse"></a>

An empty object that indicates that the event destination was deleted successfully.

### EventDestinationDefinition
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-eventdestinationdefinition"></a>

An object that defines a single event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CloudWatchLogsDestination | [CloudWatchLogsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-cloudwatchlogsdestination) | False | An object that contains information about an event destination that sends data to Amazon CloudWatch Logs. |
| Enabled | boolean | False | Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination. |
| KinesisFirehoseDestination | [KinesisFirehoseDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-kinesisfirehosedestination) | False | An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose. |
| MatchingEventTypes | Array of type [EventType](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-eventtype) | True | The types of events that you want to send to the event destination. Possible values:+   `INITIATED_CALL` - Amazon Pinpoint started trying to deliver the message to the recipient. <br />+   `RINGING` - Amazon Pinpoint initiated the phone call, and the recipient's phone is ringing. <br />+   `ANSWERED` - Amazon Pinpoint established a connection with the recipient.  This status doesn't necessarily mean that Amazon Pinpoint made a connection with a human recipient. For example, it could indicate that Amazon Pinpoint established a connection with a voicemail system.  <br />+   `COMPLETED_CALL` - Amazon Pinpoint played the audio message to the recipient.  This status doesn't necessarily mean that the message was delivered to a human recipient. For example, it could indicate that the audio message was delivered to a voicemail system.  <br />+   `BUSY` - Amazon Pinpoint attempted to deliver the voice message, but received a busy signal. <br />+   `FAILED` - Amazon Pinpoint wasn't able to deliver the message. <br />+   `NO_ANSWER` - Amazon Pinpoint attempted to deliver the message, but the recipient didn't answer.  |
| SnsDestination | [SnsDestination](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-snsdestination) | False | An object that contains information about an event destination that sends data to Amazon SNS. |

### EventType
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-eventtype"></a>

The types of events that are sent to the event destination. Possible values are:
+ `INITIATED_CALL`
+ `RINGING`
+ `ANSWERED`
+ `COMPLETED_CALL`
+ `BUSY`
+ `FAILED`
+ `NO_ANSWER`

### InternalServiceErrorException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-internalserviceerrorexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### KinesisFirehoseDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-kinesisfirehosedestination"></a>

An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryStreamArn | string | True | The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination. |
| IamRoleArn | string | True | The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream. |

### NotFoundException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-notfoundexception"></a>

The resource you attempted to access doesn't exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### SnsDestination
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-snsdestination"></a>

An object that contains information about an event destination that sends data to Amazon SNS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| TopicArn | string | True | The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to. |

### TooManyRequestsException
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-toomanyrequestsexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### UpdateConfigurationSetEventDestinationRequest
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-updateconfigurationseteventdestinationrequest"></a>

An object that defines a request to update an existing event destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EventDestination | [EventDestinationDefinition](#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-eventdestinationdefinition) | True | An object that defines a single event destination. |

### UpdateConfigurationSetEventDestinationResponse
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-model-updateconfigurationseteventdestinationresponse"></a>

An empty object that indicates that the event destination was updated successfully.

## See also
<a name="v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateConfigurationSetEventDestination
<a name="UpdateConfigurationSetEventDestination-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/UpdateConfigurationSetEventDestination)

### DeleteConfigurationSetEventDestination
<a name="DeleteConfigurationSetEventDestination-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSetEventDestination)
