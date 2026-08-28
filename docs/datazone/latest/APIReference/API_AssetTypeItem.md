---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetTypeItem.html
---

# AssetTypeItem
<a name="API_AssetTypeItem"></a>

The details of the asset type.

## Contents
<a name="API_AssetTypeItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-AssetTypeItem-domainId"></a>
The identifier of the Amazon DataZone domain where the asset type exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** formsOutput **   <a name="datazone-Type-AssetTypeItem-formsOutput"></a>
The forms included in the details of the asset type.
Type: String to [FormEntryOutput](API_FormEntryOutput.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** name **   <a name="datazone-Type-AssetTypeItem-name"></a>
The name of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-AssetTypeItem-owningProjectId"></a>
The identifier of the Amazon DataZone project that owns the asset type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** revision **   <a name="datazone-Type-AssetTypeItem-revision"></a>
The revision of the asset type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** createdAt **   <a name="datazone-Type-AssetTypeItem-createdAt"></a>
The timestamp of when the asset type was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-AssetTypeItem-createdBy"></a>
The Amazon DataZone user who created the asset type.
Type: String
Required: No

 ** description **   <a name="datazone-Type-AssetTypeItem-description"></a>
The description of the asset type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** originDomainId **   <a name="datazone-Type-AssetTypeItem-originDomainId"></a>
The identifier of the Amazon DataZone domain where the asset type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** originProjectId **   <a name="datazone-Type-AssetTypeItem-originProjectId"></a>
The identifier of the Amazon DataZone project where the asset type exists.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** updatedAt **   <a name="datazone-Type-AssetTypeItem-updatedAt"></a>
The timestamp of when the asset type was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-AssetTypeItem-updatedBy"></a>
The Amazon DataZone user who updated the asset type.
Type: String
Required: No

## See Also
<a name="API_AssetTypeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetTypeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetTypeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetTypeItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
