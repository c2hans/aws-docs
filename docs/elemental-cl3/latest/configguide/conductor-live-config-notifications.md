---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-notifications.html
---

# Configuring notifications for messages
<a name="conductor-live-config-notifications"></a>

AWS Elemental Conductor Live provides status information through alerts and messages. You can configure these notifications so you know when the node might need attention. The following table describes the differences between alerts and messages and how you can access each.

In the table, find a topic in the first column, then read across for information about alerts and about messages available for this topic.

| Topic | Alerts | Messages |
| --- | --- | --- |
| Ways in which you can access alerts and messages  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-notifications.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-notifications.html)  |
| Information conveyed | Alerts are feedback on a problem that must be fixed.<br />The "Channel Error" alert informs you that a channel has moved to an Error state.<br />This can be helpful when you are receiving automatic email notifications, letting you know to check for related messages on the web interface. | There are three types of messages:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-notifications.html) |
| Active or inactive | Alerts are active until the underlying problem is resolved. When the cause of the alert is no longer present, the system clears the alert, and it becomes inactive. | Messages are neither active nor inactive. They are defined as recent when they are less than 24 hours old. |
| Visibility (web interface only) | You can toggle the visibility of active alerts on the web interface. Suppressing an alert this way is similar to marking an email as read.<br />Alerts are available through the other access options, regardless of their visibility in the web interface. | You can toggle the visibility of recent error messages on the web interface. This is similar to marking an email as read.<br />Visibility does not affect the return on SNMP and REST requests. |

The following sections describe how to set up notifications. For information about viewing alerts and messages on the web interface or through the API, see the *Conductor Live User Guide* and *Conductor Live API Guide*.

**Topics**
+ [Email notification](notification-email.md)
+ [Web callback notification](notification-web.md)
+ [SNMP traps](notification-trap.md)
+ [SNMP polling](notification-polling.md)
