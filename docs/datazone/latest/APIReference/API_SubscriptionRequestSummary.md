---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscriptionRequestSummary.html
---

# SubscriptionRequestSummary
<a name="API_SubscriptionRequestSummary"></a>

The details of the subscription request.

## Contents
<a name="API_SubscriptionRequestSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-SubscriptionRequestSummary-createdAt"></a>
The timestamp of when a subscription request was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="datazone-Type-SubscriptionRequestSummary-createdBy"></a>
The Amazon DataZone user who created the subscription request.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-SubscriptionRequestSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which a subscription request exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-SubscriptionRequestSummary-id"></a>
The identifier of the subscription request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** requestReason **   <a name="datazone-Type-SubscriptionRequestSummary-requestReason"></a>
The reason for the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** status **   <a name="datazone-Type-SubscriptionRequestSummary-status"></a>
The status of the subscription request.
Type: String
Valid Values: `PENDING | ACCEPTED | REJECTED`
Required: Yes

 ** subscribedListings **   <a name="datazone-Type-SubscriptionRequestSummary-subscribedListings"></a>
The listings included in the subscription request.
Type: Array of [SubscribedListing](API_SubscribedListing.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** subscribedPrincipals **   <a name="datazone-Type-SubscriptionRequestSummary-subscribedPrincipals"></a>
The principals included in the subscription request.
Type: Array of [SubscribedPrincipal](API_SubscribedPrincipal.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** updatedAt **   <a name="datazone-Type-SubscriptionRequestSummary-updatedAt"></a>
The timestamp of when the subscription request was updated.
Type: Timestamp
Required: Yes

 ** decisionComment **   <a name="datazone-Type-SubscriptionRequestSummary-decisionComment"></a>
The decision comment of the subscription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** existingSubscriptionId **   <a name="datazone-Type-SubscriptionRequestSummary-existingSubscriptionId"></a>
The ID of the existing subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** metadataFormsSummary **   <a name="datazone-Type-SubscriptionRequestSummary-metadataFormsSummary"></a>
The summary of the metadata forms.
Type: Array of [MetadataFormSummary](API_MetadataFormSummary.md) objects
Required: No

 ** reviewerId **   <a name="datazone-Type-SubscriptionRequestSummary-reviewerId"></a>
The identifier of the subscription request reviewer.
Type: String
Required: No

 ** updatedBy **   <a name="datazone-Type-SubscriptionRequestSummary-updatedBy"></a>
The identifier of the Amazon DataZone user who updated the subscription request.
Type: String
Required: No

## See Also
<a name="API_SubscriptionRequestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscriptionRequestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscriptionRequestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscriptionRequestSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
