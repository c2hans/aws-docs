---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscriptionGrantSummary.html
---

# SubscriptionGrantSummary
<a name="API_SubscriptionGrantSummary"></a>

The details of the subscription grant.

## Contents
<a name="API_SubscriptionGrantSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-SubscriptionGrantSummary-createdAt"></a>
The timestamp of when a subscription grant was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="datazone-Type-SubscriptionGrantSummary-createdBy"></a>
The datazone user who created the subscription grant.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-SubscriptionGrantSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which a subscription grant exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** grantedEntity **   <a name="datazone-Type-SubscriptionGrantSummary-grantedEntity"></a>
The entity to which the subscription is granted.
Type: [GrantedEntity](API_GrantedEntity.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="datazone-Type-SubscriptionGrantSummary-id"></a>
The identifier of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-SubscriptionGrantSummary-status"></a>
The status of the subscription grant.
Type: String
Valid Values: `PENDING | IN_PROGRESS | GRANT_FAILED | REVOKE_FAILED | GRANT_AND_REVOKE_FAILED | COMPLETED | INACCESSIBLE`
Required: Yes

 ** subscriptionTargetId **   <a name="datazone-Type-SubscriptionGrantSummary-subscriptionTargetId"></a>
The identifier of the target of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** updatedAt **   <a name="datazone-Type-SubscriptionGrantSummary-updatedAt"></a>
The timestamp of when the subscription grant was updated.
Type: Timestamp
Required: Yes

 ** assets **   <a name="datazone-Type-SubscriptionGrantSummary-assets"></a>
The assets included in the subscription grant.
Type: Array of [SubscribedAsset](API_SubscribedAsset.md) objects
Required: No

 ** environmentId **   <a name="datazone-Type-SubscriptionGrantSummary-environmentId"></a>
The environment ID of the subscription grant.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** subscriptionId **   <a name="datazone-Type-SubscriptionGrantSummary-subscriptionId"></a>
 *This member has been deprecated.*
The ID of the subscription.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** updatedBy **   <a name="datazone-Type-SubscriptionGrantSummary-updatedBy"></a>
The Amazon DataZone user who updated the subscription grant.
Type: String
Required: No

## See Also
<a name="API_SubscriptionGrantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscriptionGrantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscriptionGrantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscriptionGrantSummary)
