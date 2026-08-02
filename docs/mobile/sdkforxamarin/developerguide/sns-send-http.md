---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns-send-http.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Send Messages to HTTP/HTTPS Endpoints
<a name="sns-send-http"></a>

You can use Amazon SNS to send notification messages to one or more HTTP or HTTPS endpoints. The process is as follows:

1. Configure your endpoint to receive Amazon SNS messages.

1. Subscribe an HTTP/HTTPS endpoint to a topic.

1. Confirm your subscription.

1. Publish a notification to the topic. Amazon SNS then sends an HTTP POST request delivering the contents of the notification to the subscribed endpoint.

## Configure Your HTTP/HTTPS Endpoint to Receive Amazon SNS Messages
<a name="configure-your-http-https-endpoint-to-receive-amazon-sns-messages"></a>

Follow the instructions in Step 1 of [Sending Amazon SNS Messages to HTTP/HTTPS Endpoints](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) to configure your endpoint.

## Subscribe Your HTTP/HTTPS endpoint to Your Amazon SNS Topic
<a name="subscribe-your-http-https-endpoint-to-your-amazon-sns-topic"></a>

Create an SNS client, passing your credentials object and the region of your identity pool:

```
var snsClient = new AmazonSimpleNotificationServiceClient(credentials, region);
```

To send messages to an HTTP or HTTPS endpoint through a topic, you must subscribe the endpoint to the Amazon SNS topic. You specify the endpoint using its URL:

```
var response = await snsClient.SubscribeAsync(
  "topicArn",
  "http",  /* "http" or "https" */
  "endpointUrl" /* endpoint url beginning with http or https */
);
```

## Confirm Your Subscription
<a name="confirm-your-subscription"></a>

After you subscribe to an endpoint, Amazon SNS will send a subscription confirmation message to the endpoint. The code at the endpoint must retrieve the `SubscribeURL` value from the subscription confirmation message and either visit the location specified by the `SubscribeURL` itself or make it available to you so that you can manually visit the `SubscribeURL` (for example, if using a web browser).

Amazon SNS will not send messages to the endpoint until the subscription is confirmed. When you visit the `SubscribeURL`, the response will contain an XML document containing an element `SubscriptionArn` that specifies the ARN for the subscription.

## Send Messages to the HTTP/HTTPS Endpoint
<a name="send-messages-to-the-http-https-endpoint"></a>

You can send a message to a topic’s subscriptions by publishing to the topic. Invoke `PublishAsync` and pass it the topic ARN and your message.

```
var response = await snsClient.PublishAsync(topicArn, "This is your message");
```
