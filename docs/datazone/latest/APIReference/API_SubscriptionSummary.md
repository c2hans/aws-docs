---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscriptionSummary.html
---

# SubscriptionSummary
<a name="API_SubscriptionSummary"></a>

The details of the subscription.

## Contents
<a name="API_SubscriptionSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-SubscriptionSummary-createdAt"></a>
The timestamp of when the subscription was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="datazone-Type-SubscriptionSummary-createdBy"></a>
The Amazon DataZone user who created the subscription.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-SubscriptionSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which a subscription exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-SubscriptionSummary-id"></a>
The identifier of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-SubscriptionSummary-status"></a>
The status of the subscription.
Type: String
Valid Values: `APPROVED | REVOKED | CANCELLED`
Required: Yes

 ** subscribedListing **   <a name="datazone-Type-SubscriptionSummary-subscribedListing"></a>
The listing included in the subscription.
Type: [SubscribedListing](API_SubscribedListing.md) object
Required: Yes

 ** subscribedPrincipal **   <a name="datazone-Type-SubscriptionSummary-subscribedPrincipal"></a>
The principal included in the subscription.
Type: [SubscribedPrincipal](API_SubscribedPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** updatedAt **   <a name="datazone-Type-SubscriptionSummary-updatedAt"></a>
The timestamp of when the subscription was updated.
Type: Timestamp
Required: Yes

 ** retainPermissions **   <a name="datazone-Type-SubscriptionSummary-retainPermissions"></a>
The retain permissions included in the subscription.
Type: Boolean
Required: No

 ** subscriptionRequestId **   <a name="datazone-Type-SubscriptionSummary-subscriptionRequestId"></a>
The identifier of the subscription request for the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** updatedBy **   <a name="datazone-Type-SubscriptionSummary-updatedBy"></a>
The Amazon DataZone user who updated the subscription.
Type: String
Required: No

## See Also
<a name="API_SubscriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscriptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscriptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscriptionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
