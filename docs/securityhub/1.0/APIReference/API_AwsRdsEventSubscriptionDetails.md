---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsEventSubscriptionDetails.html
---

# AwsRdsEventSubscriptionDetails
<a name="API_AwsRdsEventSubscriptionDetails"></a>

Details about an Amazon RDS event notification subscription. The subscription allows Amazon RDS to post events to an SNS topic.

## Contents
<a name="API_AwsRdsEventSubscriptionDetails_Contents"></a>

 ** CustomerAwsId **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-CustomerAwsId"></a>
The identifier of the event notification subscription.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CustSubscriptionId **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-CustSubscriptionId"></a>
The identifier of the account that is associated with the event notification subscription.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Enabled **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-Enabled"></a>
Whether the event notification subscription is enabled.
Type: Boolean
Required: No

 ** EventCategoriesList **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-EventCategoriesList"></a>
The list of event categories for the event notification subscription.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** EventSubscriptionArn **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-EventSubscriptionArn"></a>
The ARN of the event notification subscription.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnsTopicArn **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-SnsTopicArn"></a>
The ARN of the SNS topic to post the event notifications to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceIdsList **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-SourceIdsList"></a>
A list of source identifiers for the event notification subscription.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SourceType **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-SourceType"></a>
The source type for the event notification subscription.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-Status"></a>
The status of the event notification subscription.
Valid values: `creating` \| `modifying` \| `deleting` \| `active` \| `no-permission` \| `topic-not-exist`
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubscriptionCreationTime **   <a name="securityhub-Type-AwsRdsEventSubscriptionDetails-SubscriptionCreationTime"></a>
The datetime when the event notification subscription was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsEventSubscriptionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsEventSubscriptionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsEventSubscriptionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsEventSubscriptionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
