---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/event-infra.html
---

# Event infrastructure
<a name="event-infra"></a>

![Diagram showing the event infrastructure producers and consumers including Lambda functions EventBridge schedules and Step Functions workflows](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/event-infrastructure.drawio.png)

**Event infrastructure**
The event infrastructure performs the solution’s monitoring actions and responds to the events produced. The resources in the diagram can be categorized into event **producers** and **consumers**.

Producers:
+ The **lease monitoring** Lambda checks all active leases against their configured terms and generates any alerts or lifecycle events that occur. To check the cost usage, the Lambda function assumes the intermediate role in the Hub account. It then assumes the Spoke role in the Org management account to retrieve cost and usage data from the [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) service. It uses a tag-first approach, querying costs by the `accountTag/ISB-<namespace>:LeaseId` account tag and falling back to the `LINKED_ACCOUNT` dimension for leases without active tags. For more information, see the [Tag-based cost attribution](account-cost-allocation-tagging.md#tag-based-cost-attribution) section. This Lambda runs hourly through an EventBridge schedule.
+ The **drift monitoring** Lambda checks for situations where the internal state of the solution (DynamoDB) does not match the actual location of an account within the org (for instance, an account may be in an active state, but is located in the cleanup OU). In this scenario, an event is produced to move the account into quarantine for manual investigation by an administrator. This Lambda runs every 6 hours on an EventBridge schedule.
+ The **cost report** Lambda generates monthly cost reports aggregated by cost report groups configured in lease templates. This function queries DynamoDB for all lease records from the previous month, retrieves cost and usage data from AWS Cost Explorer, and generates CSV reports with cost breakdowns by cost report group. The reports are stored in a designated S3 bucket and administrators are notified via email when reports are available. This Lambda runs at the beginning of every month.
+ The **account lifecycle** Lambda produces an event to start the account cleanup process after an account has been successfully moved to the CleanUp OU, and produces blueprint deployment request events when a lease with an attached blueprint is approved.
+ The **account cleaner** durable Lambda emits an event once an account has been processed (cleanup succeeded or failed).
+ The **blueprint deployment** Step Functions state machine emits success or failure events once a blueprint deployment process has been completed.
+ The **assignment processing** Step Functions state machine emits events when IAM Identity Center access is granted or removed for shared lease principals.

Consumers:
+ The **account lifecycle** function receives events from the account cleaner, blueprint deployment, and lease monitoring Lambdas to move accounts from one lifecycle state to another. This process involves moving the account between OUs, updating the state in DynamoDB, and revoking/granting user access to an account within the IAM Identity Center.
+ The **account cleaner** durable Lambda receives events indicating that an account should be processed for cleanup.
+ The **assignment processing** Step Functions workflow receives assignment requested events and processes IAM Identity Center account assignment operations (grant or revoke access) for lease sharing.
+ The **email notification** Lambda receives events from all producers and sends human-readable emails to the appropriate users, managers, and administrators for the event. This Lambda uses [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/) for these notifications.
