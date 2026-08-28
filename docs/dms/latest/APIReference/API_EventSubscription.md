---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

Describes an event notification subscription created by the `CreateEventSubscription` operation.

## Contents
<a name="API_EventSubscription_Contents"></a>

 ** CustomerAwsId **   <a name="DMS-Type-EventSubscription-CustomerAwsId"></a>
The AWS customer account associated with the AWS DMS event notification subscription.
Type: String
Required: No

 ** CustSubscriptionId **   <a name="DMS-Type-EventSubscription-CustSubscriptionId"></a>
The AWS DMS event notification subscription Id.
Type: String
Required: No

 ** Enabled **   <a name="DMS-Type-EventSubscription-Enabled"></a>
Boolean value that indicates if the event subscription is enabled.
Type: Boolean
Required: No

 ** EventCategoriesList **   <a name="DMS-Type-EventSubscription-EventCategoriesList"></a>
A lists of event categories.
Type: Array of strings
Required: No

 ** SnsTopicArn **   <a name="DMS-Type-EventSubscription-SnsTopicArn"></a>
The topic ARN of the AWS DMS event notification subscription.
Type: String
Required: No

 ** SourceIdsList **   <a name="DMS-Type-EventSubscription-SourceIdsList"></a>
A list of source Ids for the event subscription.
Type: Array of strings
Required: No

 ** SourceType **   <a name="DMS-Type-EventSubscription-SourceType"></a>
 The type of AWS DMS resource that generates events.
Valid values: replication-instance \| replication-server \| security-group \| replication-task
Type: String
Required: No

 ** Status **   <a name="DMS-Type-EventSubscription-Status"></a>
The status of the AWS DMS event notification subscription.
Constraints:
Can be one of the following: creating \| modifying \| deleting \| active \| no-permission \| topic-not-exist
The status "no-permission" indicates that AWS DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
Type: String
Required: No

 ** SubscriptionCreationTime **   <a name="DMS-Type-EventSubscription-SubscriptionCreationTime"></a>
The time the AWS DMS event notification subscription was created.
Type: String
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/EventSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
