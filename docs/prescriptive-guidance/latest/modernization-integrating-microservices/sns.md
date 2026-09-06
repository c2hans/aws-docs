---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/sns.html
---

# Amazon SNS
<a name="sns"></a>

[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) allows you to create both standard and FIFO topics. Topics are used to implement a publish/subscribe (pub/sub) architecture. Amazon SNS supports a variety of subscription types, including email, SMS (assuming that you've configured an origination identity, such as a toll-free number or 10-digit long code), HTTP(S) endpoints, and SQS queues. End-user subscriptions, such as email messages and SMS messages, to an SNS topic **must be confirmed by the subscriber**. Amazon SNS enables services to *fan out* widely, which means that a single message can be delivered to a potentially large number of subscribers. An SNS standard topic has a default limit of 12.5 million subscriptions.

In a microservices environment, an SNS topic is useful for decoupling message routing and delivery logic from a publisher. This can be implemented by using topic filters. Conceptually, topic filters are somewhat similar to Amazon EventBridge rules, but they are configured for each subscriber instead of being available from a centralized location. For example, let's say you have:
+ An Order service, which processes orders.
+ A Fulfillment service, which handles order fulfillment.
+ A Loyalty service, which awards members loyalty points for orders.

When an order is ready to be fulfilled, it publishes a message to a topic. The Fulfillment service subscribes to the topic but doesn't apply a filter, because it wants to know about all orders. Imagine that you have a Loyalty service, which is responsible for awarding points to members when they place an order. However, not all orders are placed by members. The Loyalty service would subscribe to the topic but would implement a subscription filter to check an attribute that indicates whether the order was for a member or a guest.

Consider the case where a system receives a request from an end user to make a payment, as illustrated in the following diagram. In this case, multiple downstream systems need to know that the request was made so that various actions can be taken. When you use Amazon SNS, payments are published to an SNS topic, and Lambda functions subscribe to the topic to update the customer and sales databases. Additionally, an email subscription (which must be confirmed by the customer) sends an email confirmation to the customer by using a subscription filter.

![Amazon SNS process flow for messaging in microservices.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/2429a4e4-0bcd-402d-93c0-8892f63d6667.png)

## Guidance
<a name="sns-guidance"></a>

Some of the functionality described in this section for Amazon SNS overlaps with the functionality offered by an event bus, such as EventBridge. Consider using Amazon SNS when:
+ You will have a large number of subscribers to a topic.
+ You want to use subscription types (such as email or SMS), which are not natively supported by EventBridge.
+ Subscribers should be able to determine their subscription filter.
+ You require ordered delivery to subscribers (per message group).

If you have many topics, and subscriptions and filters are being used to route messages between microservices, EventBridge is likely the better choice.
