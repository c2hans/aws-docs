---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetRevision.html
---

# AssetRevision
<a name="API_AssetRevision"></a>

The revision of an inventory asset.

## Contents
<a name="API_AssetRevision_Contents"></a>

 ** createdAt **   <a name="datazone-Type-AssetRevision-createdAt"></a>
The timestamp of when an inventory asset revison was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-AssetRevision-createdBy"></a>
The Amazon DataZone user who created the asset revision.
Type: String
Required: No

 ** domainId **   <a name="datazone-Type-AssetRevision-domainId"></a>
The Amazon DataZone user who created the inventory asset.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** id **   <a name="datazone-Type-AssetRevision-id"></a>
The identifier of the inventory asset revision.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** revision **   <a name="datazone-Type-AssetRevision-revision"></a>
The revision details of the inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_AssetRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetRevision)
