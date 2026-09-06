---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns-send-sms.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Send and Receive SMS Notifications
<a name="sns-send-sms"></a>

You can use Amazon Simple Notification Service (Amazon SNS) to send and receive Short Message Service (SMS) notifications to SMS-enabled mobile phones and smart phones.

**Note**
SMS notifications are currently supported for phone numbers in the United States. SMS messages can be sent only from topics created in the US East (N. Virginia) region. However, you can publish messages to topics that you create in the US East (N. Virginia) region from any other region.

## Create a Topic
<a name="create-a-topic"></a>

To create a topic:

1. In the Amazon SNS console, click **Create new topic**. The Create new topic dialog box appears.

1. In the Topic name box, type a topic name.

1. In the Display name box, type a display name. The topic must have a display name assigned to it because the first ten (10) characters of the display name are used as the initial part of the text message prefix. The display name you enter will appear in the confirmation message that SNS sends to the user (the display name below is “AMZN SMS”).

![](http://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/sns-display-name.png)

1. Click **Create topic**. The new topic appears in the Topics page.

1. Select the new topic and then click the topic ARN. The Topic Details page appears.

1. Copy the topic ARN, as you will need it when you subscribe to a topic in the next step.

   ```
   arn:aws:sns:us-west-2:111122223333:MyTopic
   ```

## Subscribe to a Topic Using the SMS Protocol
<a name="subscribe-to-a-topic-using-the-sms-protocol"></a>

Create an SNS client, passing your credentials object and the region of your identity pool:

```
var snsClient = new AmazonSimpleNotificationServiceClient(credentials, region);
```

To subscribe to a topic, invoke `SubscribeAsync` and pass it the ARN of the topic that you want to subscribe to, the protocol (“sms”), and the phone number:

```
var response = await snsClient.SubscribeAsync(topicArn, "sms", "1234567890");
```

You will receive a subscribe arn in the subscribe response object. Your subscribe arn looks like this:

```
arn:aws:sns:us-west-2:123456789012:MyTopic:6b0e71bd-7e97-4d97-80ce-4a0994e55286
```

When a device subscribes to a topic, SNS will send a confirmation message to the device, and the user will have to confirm that they want to receive notifications, as shown below:

![](http://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/sns-subscribe.png)

After the user subscribes to the topic, they will receive SMS messages when you publish them to that topic.

## Publish a Message
<a name="publish-a-message"></a>

To publish a message to a topic:

1. Sign in to the AWS Management Console and open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home).

1. In the left navigation pane, click **Topics** and then select the topic you want to publish to.

1. Click **Publish to topic**.

1. In the Subject box, type a subject.

1. In the Message box, type a message. Amazon SNS sends text that you enter in the Message box to SMS subscribers unless you also enter text into the Subject box. Because Amazon SNS includes a display name prefix with all SMS messages that you send, the sum of the display name prefix and the message payload cannot exceed 140 ASCII characters or 70 Unicode characters. Amazon SNS truncates messages that exceed these limits.

1. Click **Publish message**. Amazon SNS displays a confirmation dialog box. The SMS message appears on your SMS-enabled device, as shown below.
![](http://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/sns-publish.png)
