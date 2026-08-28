---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples.html
---

# Amazon SNS examples using the AWS SDK for PHP Version 3
<a name="sns-examples"></a>

Amazon Simple Notification Service (Amazon SNS) is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients.

In Amazon SNS, there are two types of clients: publishers (also referred to as producers) and subscribers (also referred to as consumers). Publishers communicate asynchronously with subscribers by producing and sending a message to a topic, which is a logical access point and communication channel. Subscribers (web servers, email addresses, Amazon SQS queues, AWS Lambda functions) consume or receive the message or notification over one of the supported protocols (Amazon SQS, HTTP/HTTPS URLs, email, AWS SMS, Lambda) when they are subscribed to the topic.

All the example code for the AWS SDK for PHP Version 3 is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

**Topics**
+ [Managing topics](sns-examples-managing-topics.md)
+ [Managing subscriptions](sns-examples-subscribing-unsubscribing-topics.md)
+ [Sending amazon SMS messages](sns-examples-sending-sms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
