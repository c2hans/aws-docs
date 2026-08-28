---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html
---

# Subscribe
<a name="API_Subscribe"></a>

Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same AWS account, the endpoint owner must run the `ConfirmSubscription` action to confirm the subscription.

You call the `ConfirmSubscription` action with the token from the subscription response. Confirmation tokens are valid for two days.

This action is throttled at 100 transactions per second (TPS).

## Request Parameters
<a name="API_Subscribe_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that the `Subscribe` action uses:
+  `DeliveryPolicy` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
+  `FilterPolicy` – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
+  `FilterPolicyScope` – This attribute lets you choose the filtering scope by using one of the following string value types:
  +  `MessageAttributes` (default) – The filter is applied on the message attributes.
  +  `MessageBody` – The filter is applied on the message body.
+  `RawMessageDelivery` – When set to `true`, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
+  `RedrivePolicy` – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:
+  `SubscriptionRoleArn` – The ARN of the IAM role that has the following:
  + Permission to write to the Firehose delivery stream
  + Amazon SNS listed as a trusted entity

  Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see [Fanout to Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html) in the *Amazon SNS Developer Guide*.
The following attributes apply only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html):
+  `ReplayPolicy` – Adds or updates an inline policy document for a subscription to replay messages stored in the specified Amazon SNS topic.
+  `ReplayStatus` – Retrieves the status of the subscription message replay, which can be one of the following:
  +  `Completed` – The replay has successfully redelivered all messages, and is now delivering newly published messages. If an ending point was specified in the `ReplayPolicy` then the subscription will no longer receive newly published messages.
  +  `In progress` – The replay is currently replaying the selected messages.
  +  `Failed` – The replay was unable to complete.
  +  `Pending` – The default state while the replay initiates.
Type: String to string map
Required: No

 ** Endpoint **
The endpoint that you want to receive notifications. Endpoints vary by protocol:
+ For the `http` protocol, the (public) endpoint is a URL beginning with `http://`.
+ For the `https` protocol, the (public) endpoint is a URL beginning with `https://`.
+ For the `email` protocol, the endpoint is an email address.
+ For the `email-json` protocol, the endpoint is an email address.
+ For the `sms` protocol, the endpoint is a phone number of an SMS-enabled device.
+ For the `sqs` protocol, the endpoint is the ARN of an Amazon SQS queue.
+ For the `application` protocol, the endpoint is the EndpointArn of a mobile app and device.
+ For the `lambda` protocol, the endpoint is the ARN of an AWS Lambda function.
+ For the `firehose` protocol, the endpoint is the ARN of an Amazon Data Firehose delivery stream.
Type: String
Required: No

 ** Protocol **
The protocol that you want to use. Supported protocols include:
+  `http` – delivery of JSON-encoded message via HTTP POST
+  `https` – delivery of JSON-encoded message via HTTPS POST
+  `email` – delivery of message via SMTP
+  `email-json` – delivery of JSON-encoded message via SMTP
+  `sms` – delivery of message via SMS
+  `sqs` – delivery of JSON-encoded message to an Amazon SQS queue
+  `application` – delivery of JSON-encoded message to an EndpointArn for a mobile app and device
+  `lambda` – delivery of JSON-encoded message to an AWS Lambda function
+  `firehose` – delivery of JSON-encoded message to an Amazon Data Firehose delivery stream.
Type: String
Required: Yes

 ** ReturnSubscriptionArn **
Sets whether the response from the `Subscribe` request includes the subscription ARN, even if the subscription is not yet confirmed.
If you set this parameter to `true`, the response includes the ARN in all cases, even if the subscription is not yet confirmed. In addition to the ARN for confirmed subscriptions, the response also includes the `pending subscription` ARN value for subscriptions that aren't yet confirmed. A subscription becomes confirmed when the subscriber calls the `ConfirmSubscription` action with a confirmation token.

The default value is `false`.
Type: Boolean
Required: No

 ** TopicArn **
The ARN of the topic you want to subscribe to.
Type: String
Required: Yes

## Response Elements
<a name="API_Subscribe_ResponseElements"></a>

The following element is returned by the service.

 ** SubscriptionArn **
The ARN of the subscription if it is confirmed, or the string "pending confirmation" if the subscription requires confirmation. However, if the API request parameter `ReturnSubscriptionArn` is true, then the value is always the subscription ARN, even if the subscription requires confirmation.
Type: String

## Errors
<a name="API_Subscribe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** FilterPolicyLimitExceeded **
Indicates that the number of filter polices in your AWS account exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase case in the AWS Support Center.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

 ** ReplayLimitExceeded **
Indicates that the request parameter has exceeded the maximum number of concurrent message replays.
HTTP Status Code: 403

 ** SubscriptionLimitExceeded **
Indicates that the customer already owns the maximum allowed number of subscriptions.
HTTP Status Code: 403

## Examples
<a name="API_Subscribe_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example of an Amazon SQS subscription
<a name="API_Subscribe_Example_1"></a>

The following example Query request subscribes an Amazon SQS queue to an SNS topic. For more information, see [Subscribe Queue to Amazon SNS Topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqssubscribe.html) in the *Amazon SQS Developer Guide*.

#### Sample Request
<a name="API_Subscribe_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=Subscribe
&TopicArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3AMyTopic
&Endpoint=arn%3Aaws%3Asqs%3Aus-west-2%3A123456789012%3AMyQueue
&Protocol=sqs
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Subscribe_Example_1_Response"></a>

```
<SubscribeResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <SubscribeResult>
        <SubscriptionArn>arn:aws:sns:us-west-2:123456789012:MyTopic:6b0e71bd-7e97-4d97-80ce-4a0994e55286</SubscriptionArn>
    </SubscribeResult>
    <ResponseMetadata>
        <RequestId>c4407779-24a4-56fa-982c-3d927f93a775</RequestId>
    </ResponseMetadata>
</SubscribeResponse>
```

### Example of an Amazon Data Firehose delivery stream subscription
<a name="API_Subscribe_Example_2"></a>

This example illustrates one usage of Subscribe.

#### Sample Request
<a name="API_Subscribe_Example_2_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=Subscribe
&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic
&Endpoint=arn:aws:firehose:us-west-2:123456789012:deliverystream/MyStream
&Protocol=firehose
&Attributes.entry.1.key=SubscriptionRoleArn
&Attributes.entry.1.value=arn:aws:iam::123456789012:role/FirehoseRoleArn
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Subscribe_Example_2_Response"></a>

```
<SubscribeResponse xmlns="http://sns.amazonaws.com/doc/2010-03-31/">
    <SubscribeResult>
        <SubscriptionArn>
            arn:aws:sns:us-west-2:123456789012:MyTopic:
            6b0e71bd-7e97-4d97-80ce-4a0994e55286
        </SubscriptionArn>
    </SubscribeResult>
    <ResponseMetadata>
        <RequestId>c4407779-24a4-56fa-982c-3d927f93a775</RequestId>
    </ResponseMetadata>
</SubscribeResponse>
```

## See Also
<a name="API_Subscribe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/Subscribe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/Subscribe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/Subscribe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/Subscribe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/Subscribe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/Subscribe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/Subscribe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/Subscribe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/Subscribe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/Subscribe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
