---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedAsset.html
---

# SubscribedAsset
<a name="API_SubscribedAsset"></a>

The details of the asset for which the subscription grant is created.

## Contents
<a name="API_SubscribedAsset_Contents"></a>

 ** assetId **   <a name="datazone-Type-SubscribedAsset-assetId"></a>
The identifier of the asset for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** assetRevision **   <a name="datazone-Type-SubscribedAsset-assetRevision"></a>
The revision of the asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** status **   <a name="datazone-Type-SubscribedAsset-status"></a>
The status of the asset for which the subscription grant is created.
Type: String
Valid Values: `GRANT_PENDING | REVOKE_PENDING | GRANT_IN_PROGRESS | REVOKE_IN_PROGRESS | GRANTED | REVOKED | GRANT_FAILED | REVOKE_FAILED`
Required: Yes

 ** assetScope **   <a name="datazone-Type-SubscribedAsset-assetScope"></a>
The asset scope of the subscribed asset.
Type: [AssetScope](API_AssetScope.md) object
Required: No

 ** failureCause **   <a name="datazone-Type-SubscribedAsset-failureCause"></a>
The failure cause included in the details of the asset for which the subscription grant is created.
Type: [FailureCause](API_FailureCause.md) object
Required: No

 ** failureTimestamp **   <a name="datazone-Type-SubscribedAsset-failureTimestamp"></a>
The failure timestamp included in the details of the asset for which the subscription grant is created.
Type: Timestamp
Required: No

 ** grantedTimestamp **   <a name="datazone-Type-SubscribedAsset-grantedTimestamp"></a>
The timestamp of when the subscription grant to the asset is created.
Type: Timestamp
Required: No

 ** permissions **   <a name="datazone-Type-SubscribedAsset-permissions"></a>
The asset permissions.
Type: [Permissions](API_Permissions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** targetName **   <a name="datazone-Type-SubscribedAsset-targetName"></a>
The target name of the asset for which the subscription grant is created.
Type: String
Required: No

## See Also
<a name="API_SubscribedAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedAsset)
