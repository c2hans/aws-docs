---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-and-destinations.html
---

# Amazon SNS event sources and destinations
<a name="sns-event-sources-and-destinations"></a>

Amazon SNS connects AWS services and external systems by routing event-driven notifications. Amazon SNS receives events from various AWS services, such as data pipeline updates, Amazon EC2 scaling actions, or security alerts, and publishes these events to Amazon SNS topics. These topics then send notifications to designated destinations.

Amazon SNS supports two main types of destinations: [Application-to-Application (A2A)](sns-system-to-system-messaging.md) and [Application-to-Person (A2P)](sns-user-notifications.md). In A2A messaging, Amazon SNS can send events to Lambda to trigger custom business logic, to Amazon SQS for queuing messages, and to Amazon Data Firehose for streaming data to storage and analytics services. For A2P messaging, Amazon SNS can send notifications via SMS, email, and push notifications to mobile devices, ensuring that users or teams receive timely alerts.

By acting as a central hub, Amazon SNS routes notifications to the right places, helping you automate and manage your AWS infrastructure more effectively. This setup allows for seamless integration between services and reliable communication with users and systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
