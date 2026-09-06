---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlossaryItem.html
---

# GlossaryItem
<a name="API_GlossaryItem"></a>

The details of a business glossary.

## Contents
<a name="API_GlossaryItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-GlossaryItem-domainId"></a>
The identifier of the Amazon DataZone domain in which the business glossary exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-GlossaryItem-id"></a>
The identifier of the glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-GlossaryItem-name"></a>
The name of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-GlossaryItem-owningProjectId"></a>
The identifier of the project that owns the business glosary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-GlossaryItem-status"></a>
The business glossary status.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: Yes

 ** additionalAttributes **   <a name="datazone-Type-GlossaryItem-additionalAttributes"></a>
The additional attributes of an Amazon DataZone glossary.
Type: [GlossaryItemAdditionalAttributes](API_GlossaryItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-GlossaryItem-createdAt"></a>
The timestamp of when the glossary was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-GlossaryItem-createdBy"></a>
The Amazon DataZone user who created the glossary.
Type: String
Required: No

 ** description **   <a name="datazone-Type-GlossaryItem-description"></a>
The business glossary description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** updatedAt **   <a name="datazone-Type-GlossaryItem-updatedAt"></a>
The timestamp of when the business glossary was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-GlossaryItem-updatedBy"></a>
The Amazon DataZone user who updated the business glossary.
Type: String
Required: No

 ** usageRestrictions **   <a name="datazone-Type-GlossaryItem-usageRestrictions"></a>
The usage restrictions associated with a goverened glossary term.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`
Required: No

## See Also
<a name="API_GlossaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlossaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlossaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlossaryItem)
