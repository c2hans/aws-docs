---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetItem.html
---

# AssetItem
<a name="API_AssetItem"></a>

A Amazon DataZone inventory asset.

## Contents
<a name="API_AssetItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-AssetItem-domainId"></a>
The identifier of the Amazon DataZone domain in which the inventory asset exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** identifier **   <a name="datazone-Type-AssetItem-identifier"></a>
the identifier of the Amazon DataZone inventory asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-AssetItem-name"></a>
The name of the Amazon DataZone inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-AssetItem-owningProjectId"></a>
The identifier of the Amazon DataZone project that owns the inventory asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** typeIdentifier **   <a name="datazone-Type-AssetItem-typeIdentifier"></a>
The identifier of the asset type of the specified Amazon DataZone inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** typeRevision **   <a name="datazone-Type-AssetItem-typeRevision"></a>
The revision of the inventory asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** additionalAttributes **   <a name="datazone-Type-AssetItem-additionalAttributes"></a>
The additional attributes of a Amazon DataZone inventory asset.
Type: [AssetItemAdditionalAttributes](API_AssetItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-AssetItem-createdAt"></a>
The timestamp of when the Amazon DataZone inventory asset was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-AssetItem-createdBy"></a>
The Amazon DataZone user who created the inventory asset.
Type: String
Required: No

 ** description **   <a name="datazone-Type-AssetItem-description"></a>
The description of an Amazon DataZone inventory asset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** externalIdentifier **   <a name="datazone-Type-AssetItem-externalIdentifier"></a>
The external identifier of the Amazon DataZone inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: No

 ** firstRevisionCreatedAt **   <a name="datazone-Type-AssetItem-firstRevisionCreatedAt"></a>
The timestamp of when the first revision of the inventory asset was created.
Type: Timestamp
Required: No

 ** firstRevisionCreatedBy **   <a name="datazone-Type-AssetItem-firstRevisionCreatedBy"></a>
The Amazon DataZone user who created the first revision of the inventory asset.
Type: String
Required: No

 ** glossaryTerms **   <a name="datazone-Type-AssetItem-glossaryTerms"></a>
The glossary terms attached to the Amazon DataZone inventory asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** governedGlossaryTerms **   <a name="datazone-Type-AssetItem-governedGlossaryTerms"></a>
The restricted glossary terms accociated with an asset.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_AssetItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
