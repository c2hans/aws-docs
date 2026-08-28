---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DomainDeliverabilityTrackingOption.html
---

# DomainDeliverabilityTrackingOption
<a name="API_DomainDeliverabilityTrackingOption"></a>

An object that contains information about the Deliverability dashboard subscription for a verified domain that you use to send email and currently has an active Deliverability dashboard subscription. If a Deliverability dashboard subscription is active for a domain, you gain access to reputation, inbox placement, and other metrics for the domain.

## Contents
<a name="API_DomainDeliverabilityTrackingOption_Contents"></a>

 ** Domain **   <a name="pinpoint-Type-DomainDeliverabilityTrackingOption-Domain"></a>
A verified domain that’s associated with your AWS account and currently has an active Deliverability dashboard subscription.
Type: String
Required: No

 ** InboxPlacementTrackingOption **   <a name="pinpoint-Type-DomainDeliverabilityTrackingOption-InboxPlacementTrackingOption"></a>
An object that contains information about the inbox placement data settings for the domain.
Type: [InboxPlacementTrackingOption](API_InboxPlacementTrackingOption.md) object
Required: No

 ** SubscriptionStartDate **   <a name="pinpoint-Type-DomainDeliverabilityTrackingOption-SubscriptionStartDate"></a>
The date, in Unix time format, when you enabled the Deliverability dashboard for the domain.
Type: Timestamp
Required: No

## See Also
<a name="API_DomainDeliverabilityTrackingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DomainDeliverabilityTrackingOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DomainDeliverabilityTrackingOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DomainDeliverabilityTrackingOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
