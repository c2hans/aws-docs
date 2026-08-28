---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

Contains the results of a successful invocation of the `DescribeEventSubscriptions` action.

## Contents
<a name="API_EventSubscription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomerAwsId **
The AWS customer account associated with the RDS event notification subscription.
Type: String
Required: No

 ** CustSubscriptionId **
The RDS event notification subscription Id.
Type: String
Required: No

 ** Enabled **
Specifies whether the subscription is enabled. True indicates the subscription is enabled.
Type: Boolean
Required: No

 ** EventCategoriesList.EventCategory.N **
A list of event categories for the RDS event notification subscription.
Type: Array of strings
Required: No

 ** EventSubscriptionArn **
The Amazon Resource Name (ARN) for the event subscription.
Type: String
Required: No

 ** SnsTopicArn **
The topic ARN of the RDS event notification subscription.
Type: String
Required: No

 ** SourceIdsList.SourceId.N **
A list of source IDs for the RDS event notification subscription.
Type: Array of strings
Required: No

 ** SourceType **
The source type for the RDS event notification subscription.
Type: String
Required: No

 ** Status **
The status of the RDS event notification subscription.
Constraints:
Can be one of the following: creating \| modifying \| deleting \| active \| no-permission \| topic-not-exist
The status "no-permission" indicates that RDS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
Type: String
Required: No

 ** SubscriptionCreationTime **
The time the RDS event notification subscription was created.
Type: String
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/EventSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
