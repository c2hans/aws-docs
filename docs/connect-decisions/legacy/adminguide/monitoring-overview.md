---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/monitoring-overview.html
---

# Logging and Monitoring AWS Supply Chain
<a name="monitoring-overview"></a>

Logging and Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Supply Chain and your other AWS solutions. AWS provides the AWS CloudTrail monitoring tool to watch AWS Supply Chain, report when something is wrong, and take automatic actions when appropriate.

**Note**
APIs called only from the AWS Supply Chain console are captured in AWS CloudTrail.

*AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. You can view the AWS Supply Chain events under *scn.amazonaws.com*. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Note**
Note the following with AWS Supply Chain:
When you invite users that don't have access to AWS Supply Chain, these users don't receive information in the notifications that they receive from the web application. Invited users receive an email notification with a link to the web application. They can only log in and view the content in the notification if they have the required user permissions.
All users with or without user permissions to a particular Insight can view the Insights chat messages.
As an application admin, when you are add users to the AWS Supply Chain instance, they have access to the AWS KMS key. You can manage the user permissions to add or remove users. For more information on user permissions, see [Managing user permission roles](adding-users-groups.md).

## AWS Supply Chain data events in CloudTrail
<a name="service-name-data-events-cloudtrail"></a>

**Note**
The web application APIs listed under [AWS Supply Chain web application APIs](webappi.md) are listed in the data events in CloudTrail.

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the AWS Supply Chain resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations.
+ To log data events using the CloudTrail console, create a [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html#creating-a-trail-in-the-console) or [event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.html) to log data events, or [update an existing trail or event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) to log data events.

  1. Choose **Data events** to log data events.

  1. From the **Data event type** list, choose the resource type for which you want to log data events.

  1. Choose the log selector template you want to use. You can log all data events for the resource type, log all `readOnly` events, log all `writeOnly` events, or create a custom log selector template to filter on the `readOnly`, `eventName`, and `resources.ARN` fields.
+ To log data events using the AWS CLI, configure the `--advanced-event-selectors` parameter to set the `eventCategory` field equal to `Data` and the `resources.type` field equal to the resource type value . You can add conditions to filter on the values of the `readOnly`, `eventName`, and `resources.ARN` fields.
  + To configure a trail to log data events, run the [put-event-selectors](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) command. For more information, see [Logging data events for trails with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-CLI-trail-examples).
  + To configure an event data store to log data events, run the [create-event-data-store](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/create-event-data-store.html) command to create a new event data store to log data events, or run the [update-event-data-store](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-event-data-store.html) command to update an existing event data store. For more information, see [Logging data events for event data stores with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-CLI-eds-examples).

\*You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html).

## AWS Supply Chain management events in CloudTrail
<a name="service-name-management-events-cloudtrail"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Supply Chain logs all control plane operations to CloudTrail as management events.
