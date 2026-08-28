---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

Detailed information about an event to which you have subscribed.

## Contents
<a name="API_EventSubscription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomerAwsId **
The AWS customer account that is associated with the Amazon DocumentDB event notification subscription.
Type: String
Required: No

 ** CustSubscriptionId **
The Amazon DocumentDB event notification subscription ID.
Type: String
Required: No

 ** Enabled **
A Boolean value indicating whether the subscription is enabled. A value of `true` indicates that the subscription is enabled.
Type: Boolean
Required: No

 ** EventCategoriesList.EventCategory.N **
A list of event categories for the Amazon DocumentDB event notification subscription.
Type: Array of strings
Required: No

 ** EventSubscriptionArn **
The Amazon Resource Name (ARN) for the event subscription.
Type: String
Required: No

 ** SnsTopicArn **
The topic ARN of the Amazon DocumentDB event notification subscription.
Type: String
Required: No

 ** SourceIdsList.SourceId.N **
A list of source IDs for the Amazon DocumentDB event notification subscription.
Type: Array of strings
Required: No

 ** SourceType **
The source type for the Amazon DocumentDB event notification subscription.
Type: String
Required: No

 ** Status **
The status of the Amazon DocumentDB event notification subscription.
Constraints:
Can be one of the following: `creating`, `modifying`, `deleting`, `active`, `no-permission`, `topic-not-exist`
The `no-permission` status indicates that Amazon DocumentDB no longer has permission to post to the SNS topic. The `topic-not-exist` status indicates that the topic was deleted after the subscription was created.
Type: String
Required: No

 ** SubscriptionCreationTime **
The time at which the Amazon DocumentDB event notification subscription was created.
Type: String
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/EventSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
