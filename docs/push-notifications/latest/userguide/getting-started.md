---
source_url: https://docs.aws.amazon.com/push-notifications/latest/userguide/getting-started.html
---

# Getting started with AWS End User Messaging Push
<a name="getting-started"></a>

In order to set up AWS End User Messaging Push so that it can send push notifications to your apps, you first have to provide the credentials that authorize AWS End User Messaging Push to send messages to your app. The credentials that you provide depend on which push notification system you use:
+ For Apple Push Notification service (APN) credentials, see [Obtain an encryption key and key ID from Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns#Obtain-an-encryption-key-and-key-ID-from-Apple) and [Obtain a provider certificate from Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-certificate-based-connection-to-apns#Obtain-a-provider-certificate-from-Apple) in the Apple Developer documentation.
+ For Firebase Cloud Messaging (FCM) credentials they can be obtained through the Firebase console, see [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging).
+ For Baidu credentials, see [Baidu](https://push.baidu.com/).
+ For Amazon Device Messaging (ADM) credentials, see [Obtain Credentials](https://developer.amazon.com/docs/adm/obtain-credentials.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Push. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query push-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
