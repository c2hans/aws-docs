---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/notifications.html
---

# Notifications
<a name="notifications"></a>

When deployed, the guidance sets up the following topics in the Amazon SNS:
+ Alarm notification topic - This topic receives the notifications for the CloudWatch alarms.
+ Auto scaling notification topic - This topic receives the scaling event notifications from auto scaling groups.

To receive messages published to the topics, you must subscribe an endpoint to the topic. When you subscribe an endpoint to a topic, the endpoint begins to receive messages published to the associated topic.
