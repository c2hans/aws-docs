---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscriptionTargetSummary.html
---

# SubscriptionTargetSummary
<a name="API_SubscriptionTargetSummary"></a>

The details of the subscription target.

## Contents
<a name="API_SubscriptionTargetSummary_Contents"></a>

 ** applicableAssetTypes **   <a name="datazone-Type-SubscriptionTargetSummary-applicableAssetTypes"></a>
The asset types included in the subscription target.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: Yes

 ** authorizedPrincipals **   <a name="datazone-Type-SubscriptionTargetSummary-authorizedPrincipals"></a>
The authorized principals included in the subscription target.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9:/._-]*`
Required: Yes

 ** createdAt **   <a name="datazone-Type-SubscriptionTargetSummary-createdAt"></a>
The timestamp of when the subscription target was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="datazone-Type-SubscriptionTargetSummary-createdBy"></a>
The Amazon DataZone user who created the subscription target.
Type: String
Required: Yes

 ** domainId **   <a name="datazone-Type-SubscriptionTargetSummary-domainId"></a>
The identifier of the Amazon DataZone domain in which the subscription target exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** environmentId **   <a name="datazone-Type-SubscriptionTargetSummary-environmentId"></a>
The identifier of the environment of the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-SubscriptionTargetSummary-id"></a>
The identifier of the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-SubscriptionTargetSummary-name"></a>
The name of the subscription target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** projectId **   <a name="datazone-Type-SubscriptionTargetSummary-projectId"></a>
The identifier of the project specified in the subscription target.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** provider **   <a name="datazone-Type-SubscriptionTargetSummary-provider"></a>
The provider of the subscription target.
Type: String
Required: Yes

 ** subscriptionTargetConfig **   <a name="datazone-Type-SubscriptionTargetSummary-subscriptionTargetConfig"></a>
The configuration of the subscription target.
Type: Array of [SubscriptionTargetForm](API_SubscriptionTargetForm.md) objects
Required: Yes

 ** type **   <a name="datazone-Type-SubscriptionTargetSummary-type"></a>
The type of the subscription target.
Type: String
Required: Yes

 ** manageAccessRole **   <a name="datazone-Type-SubscriptionTargetSummary-manageAccessRole"></a>
The manage access role specified in the subscription target.
Type: String
Pattern: `arn:aws(|-cn|-us-gov):iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*`
Required: No

 ** subscriptionGrantCreationMode **   <a name="datazone-Type-SubscriptionTargetSummary-subscriptionGrantCreationMode"></a>
 Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** updatedAt **   <a name="datazone-Type-SubscriptionTargetSummary-updatedAt"></a>
The timestamp of when the subscription target was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-SubscriptionTargetSummary-updatedBy"></a>
The Amazon DataZone user who updated the subscription target.
Type: String
Required: No

## See Also
<a name="API_SubscriptionTargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscriptionTargetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscriptionTargetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscriptionTargetSummary)
