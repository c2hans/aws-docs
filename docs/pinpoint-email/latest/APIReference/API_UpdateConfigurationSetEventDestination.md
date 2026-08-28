---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.html
---

# UpdateConfigurationSetEventDestination
<a name="API_UpdateConfigurationSetEventDestination"></a>

Update the configuration of an event destination for a configuration set.

In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

## Request Syntax
<a name="API_UpdateConfigurationSetEventDestination_RequestSyntax"></a>

```
PUT /v1/email/configuration-sets/{{ConfigurationSetName}}/event-destinations/{{EventDestinationName}} HTTP/1.1
Content-type: application/json

{
   "EventDestination": {
      "CloudWatchDestination": {
         "DimensionConfigurations": [
            {
               "DefaultDimensionValue": "{{string}}",
               "DimensionName": "{{string}}",
               "DimensionValueSource": "{{string}}"
            }
         ]
      },
      "Enabled": {{boolean}},
      "KinesisFirehoseDestination": {
         "DeliveryStreamArn": "{{string}}",
         "IamRoleArn": "{{string}}"
      },
      "MatchingEventTypes": [ "{{string}}" ],
      "PinpointDestination": {
         "ApplicationArn": "{{string}}"
      },
      "SnsDestination": {
         "TopicArn": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationSetEventDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_UpdateConfigurationSetEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateConfigurationSetEventDestination-request-uri-ConfigurationSetName"></a>
The name of the configuration set that contains the event destination that you want to modify.
Required: Yes

 ** [EventDestinationName](#API_UpdateConfigurationSetEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateConfigurationSetEventDestination-request-uri-EventDestinationName"></a>
The name of the event destination that you want to modify.
Required: Yes

## Request Body
<a name="API_UpdateConfigurationSetEventDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EventDestination](#API_UpdateConfigurationSetEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateConfigurationSetEventDestination-request-EventDestination"></a>
An object that defines the event destination.
Type: [EventDestinationDefinition](API_EventDestinationDefinition.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateConfigurationSetEventDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateConfigurationSetEventDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConfigurationSetEventDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_UpdateConfigurationSetEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
