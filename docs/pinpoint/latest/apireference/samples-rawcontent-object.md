---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/samples-rawcontent-object.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Schema sample: RawContent object for a push notification
<a name="samples-rawcontent-object"></a>

When you send a push notification through a push notification channel, you have the option of using a `RawContent` object to specify the settings and contents of the notification. Using a `RawContent` object can be helpful when you want to send custom data to an app for processing, as part of sending a notification. If you use a `RawContent` object to define the settings and contents of a push notification, the settings and content that you specify in the object override all other settings and content for the notification.

## Overview
<a name="samples-rawcontent-object-overview"></a>

A `RawContent` object is a raw, JSON-formatted string that contains the payload for a push notification. The data in the payload is formatted as a set of key-value pairs, with the quotation marks escaped.

The contents of a `RawContent` object vary, depending primarily on the target platform and push notification service. For each platform and service, the contents of this object maps to a specific message object of the Amazon Pinpoint API:
+ **Amazon Device Messaging** – For push notifications that you want to send through the ADM channel to the Amazon Device Messaging (ADM) service, use the fields and options defined by the [ADMMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-admmessage) object. Enclose the `RawContent` object in that object.
+ **Apple Push Notification service** – For push notifications that you want to send through an APNs channel to the Apple Push Notification (APNs) service, use the fields and options defined by the [APNSMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-apnsmessage) object. Enclose the `RawContent` object in that object.
+ **Baidu Cloud Push** – For push notifications that you want to send through the Baidu channel to the Baidu Cloud Push service, use the fields and options defined by the [BaiduMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-baidumessage) object. Enclose the `RawContent` object in that object.
+ **Firebase Cloud Messaging** – For push notifications that you want to send through the GCM channel to the Firebase Cloud Messaging (FCM) service, use the fields and options defined by the [GCMMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-gcmmessage) object. Enclose the `RawContent` object in that object.

The preceding links go to the object definitions for the `SendMessages` operation, which corresponds to sending a POST request to the [Messages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html) resource. However, you can use these objects with other Amazon Pinpoint API operations that send push notifications.

The structure and design of these objects aligns with the requirements and options that are provided by the corresponding platform and push notification service. For detailed information about the options for a particular platform or service, see the documentation for the platform or service.

**Important**
Avoid putting sensitive data, such as credit card numbers, in `RawContent` objects. If you have to include sensitive data in an object, make sure that you encrypt the data before you send it and use the decryption features provided by the target platform.

## Samples
<a name="samples-rawcontent-object-samples"></a>

The samples in this topic use comparable example data to show the structure of two `RawContent` objects. The objects specify the settings and contents of a standard push notification. The notification congratulates an existing user of a fitness app because the user reported a new personal record for a running time.

The first sample is designed to be sent to APNs for delivery to the app on an iOS device:

```
{
    "APNSMessage":{
        "RawContent":"{\n\"aps\":{\n \"alert\":{\n\"title\":\"Hello\",\n\"subtitle\":\"Hello from Pinpoint!\",\n\"body\":\"Have a good day!\"\n},\n\"category\":\"Notification\"\n},\n\"customKey\":\"12345678\"\n}\n"
    }
}
```

For a list of keys, see [Payload key reference](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference) in the Apple developer guide.

The second sample is designed to be sent to FCM for delivery to the app on an Android device:

```
{
    "GCMMessage":{
        "RawContent":"{\n \"collapse_key\":\"string\",\n\"priority\":\"string\",\n\"time_to_live\":1234,\n\"notification\": {\n\"title\":\"Hello\",\n\"body\":\"Hello from Pinpoint!\",\n \"android_channel_id\":\"string\",\n\"body_loc_args\":[\n\"string\"\n],\n\"body_loc_key\":\"string\",\n\"click_action\":\"string\",\n\"color\": \"string\",\n\"icon\":\"string\",\n\"sound\":\"string\",\n\"tag\":\"string\",\n\"title_loc_args\":[\n\"string\"\n],\n\"title_loc_key\":\"string\"\n},\n\"data\":{\n\"customKey\":\"customValue\"\n}\n}"
    }
}
```

Amazon Pinpoint also supports FCM v1 payloads in the raw content, see [Using Google Firebase Cloud Messaging (FCM) v1 payloads](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-v1-payloads.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
