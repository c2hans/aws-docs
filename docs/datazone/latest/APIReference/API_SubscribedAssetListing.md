---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedAssetListing.html
---

# SubscribedAssetListing
<a name="API_SubscribedAssetListing"></a>

The details of the published asset for which the subscription grant is created.

## Contents
<a name="API_SubscribedAssetListing_Contents"></a>

 ** assetScope **   <a name="datazone-Type-SubscribedAssetListing-assetScope"></a>
The asset scope of the subscribed asset listing.
Type: [AssetScope](API_AssetScope.md) object
Required: No

 ** entityId **   <a name="datazone-Type-SubscribedAssetListing-entityId"></a>
The identifier of the published asset for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** entityRevision **   <a name="datazone-Type-SubscribedAssetListing-entityRevision"></a>
The revision of the published asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** entityType **   <a name="datazone-Type-SubscribedAssetListing-entityType"></a>
The type of the published asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: No

 ** forms **   <a name="datazone-Type-SubscribedAssetListing-forms"></a>
The forms attached to the published asset for which the subscription grant is created.
Type: String
Required: No

 ** glossaryTerms **   <a name="datazone-Type-SubscribedAssetListing-glossaryTerms"></a>
The glossary terms attached to the published asset for which the subscription grant is created.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** permissions **   <a name="datazone-Type-SubscribedAssetListing-permissions"></a>
The asset permissions.
Type: [Permissions](API_Permissions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_SubscribedAssetListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedAssetListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedAssetListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedAssetListing)
