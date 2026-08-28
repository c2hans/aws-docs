---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Amazon Simple Notification Service (SNS)
<a name="sns"></a>

Using SNS and the AWS Mobile SDK for .NET and Xamarin, you can write applications that can receive mobile push notifications. For information about SNS, see [Amazon Simple Notification Service](https://aws.amazon.com/sns/).

## Key Concepts
<a name="key-concepts"></a>

Amazon SNS allows applications and end-users on different devices to receive notifications via Mobile Push notification (Apple, Google and Kindle Fire Devices), HTTP/HTTPS, Email/Email-JSON, SMS or Amazon Simple Queue Service (SQS) queues, or AWS Lambda functions. SNS lets you send individual messages or to fan-out messages to large numbers of recipients subscribed to a single topic.

### Topics
<a name="topics"></a>

A topic is an “access point” for allowing recipients to dynamically subscribe for identical copies of the same notification. One topic can support deliveries to multiple endpoint types – for example, you can group together iOS, Android and SMS recipients.

### Subscriptions
<a name="subscriptions"></a>

To receive messages published to a topic, you have to subscribe an endpoint to that topic. An endpoint is a mobile app, web server, email address, or an Amazon SQS queue that can receive notification messages from Amazon SNS. Once you subscribe an endpoint to a topic and the subscription is confirmed, the endpoint will receive all messages published to that topic.

### Publishing
<a name="publishing"></a>

When you publish to a topic, SNS delivers appropriately formatted copies of your message to each subscriber of that topic. For Mobile Push Notifications, you can publish directly to the endpoint or subscribe the endpoint to a topic.

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

To use SNS in your application, you’ll need to add the SDK to your project. To do so, follow the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md).

#### Set Permissions for SNS
<a name="set-permissions-for-sns"></a>

For information on setting permissions for SNS, see [Managing Access to Your Amazon SNS Topics](https://docs.aws.amazon.com/sns/latest/dg/AccessPolicyLanguage.html).

#### Add NuGet Package for SNS to Your Project
<a name="add-nuget-package-for-sns-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the Amazon Simple Notification Service NuGet package to your project.

## Integrating SNS with Your Application
<a name="integrating-sns-with-your-application"></a>

There are many ways to interact with SNS in your Xamarin application:

**Topics**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Xamarin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
