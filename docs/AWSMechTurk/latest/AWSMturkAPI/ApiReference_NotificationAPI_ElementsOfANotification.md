---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationAPI_ElementsOfANotification.html
---

# Elements of a Notification Message
<a name="ApiReference_NotificationAPI_ElementsOfANotification"></a>

Notification messages contain one or more `Event` data structures that describe recent activity for HITs of a HIT type.

## The Notification API Version
<a name="ApiReference_NotificationAPI_ElementsOfANotification-the-notification-api-version"></a>

Similar to how a REST request that is sent to the Amazon Mechanical Turk Requester service must include a `Version` parameter to indicate which version of the service API the client is expecting to use, a notification message must also include a `Version` parameter. This version string is identical to the version that is included in the notification specification for the HIT type.

**Tip**
 Your application may need to accommodate receiving notification messages of different versions at the same time if you want to upgrade your notification specifications to a new version without missing messages. You can avoid having to accommodate multiple API versions by first disabling the notification specifications that use the old version, upgrading your application to use the new version, then updating the notification specifications to use the new version and re-enable notifications.

 When a new version of the notification API is made available, all existing notification specifications will continue to use the API versions they were using previously. You must update your notification specifications to use a new version of the API.

## Events
<a name="ApiReference_NotificationAPI_ElementsOfANotification-events"></a>

 A notification message describes one or more events that happened in regards to a HIT type. Each event includes:
+ the event type (`EventType`), a value corresponding to the `EventType` value in the [notification specification data structure](ApiReference_NotificationDataStructureArticle.md)
+ the time of the event (`EventTime`), as a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) in the Coordinated Universal Time time zone, such as **2005-01-31T23:59:59Z**
+ the HIT type ID for the event (`HITTypeId`)
+ the HIT ID for the event (`HITId`)
+ the assignment ID for the event, if applicable (`AssignmentId`)

 Multiple events may be batched into a single notification message.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
