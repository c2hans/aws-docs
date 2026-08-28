---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlossaryTermItem.html
---

# GlossaryTermItem
<a name="API_GlossaryTermItem"></a>

The details of a business glossary term.

## Contents
<a name="API_GlossaryTermItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-GlossaryTermItem-domainId"></a>
The identifier of the Amazon DataZone domain in which the business glossary exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** glossaryId **   <a name="datazone-Type-GlossaryTermItem-glossaryId"></a>
The identifier of the business glossary to which the term belongs.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-GlossaryTermItem-id"></a>
The identifier of the business glossary term.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-GlossaryTermItem-name"></a>
The name of the business glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** status **   <a name="datazone-Type-GlossaryTermItem-status"></a>
The status of the business glossary term.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** additionalAttributes **   <a name="datazone-Type-GlossaryTermItem-additionalAttributes"></a>
The additional attributes of an Amazon DataZone glossary term.
Type: [GlossaryTermItemAdditionalAttributes](API_GlossaryTermItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-GlossaryTermItem-createdAt"></a>
The timestamp of when a business glossary term was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-GlossaryTermItem-createdBy"></a>
The Amazon DataZone user who created the business glossary.
Type: String
Required: No

 ** longDescription **   <a name="datazone-Type-GlossaryTermItem-longDescription"></a>
The long description of the business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** shortDescription **   <a name="datazone-Type-GlossaryTermItem-shortDescription"></a>
The short description of the business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** termRelations **   <a name="datazone-Type-GlossaryTermItem-termRelations"></a>
The relations of the business glossary term.
Type: [TermRelations](API_TermRelations.md) object
Required: No

 ** updatedAt **   <a name="datazone-Type-GlossaryTermItem-updatedAt"></a>
The timestamp of when a business glossary term was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-GlossaryTermItem-updatedBy"></a>
The Amazon DataZone user who updated the business glossary term.
Type: String
Required: No

 ** usageRestrictions **   <a name="datazone-Type-GlossaryTermItem-usageRestrictions"></a>
The usage restrictions associated with a goverened glossary term.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`
Required: No

## See Also
<a name="API_GlossaryTermItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlossaryTermItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlossaryTermItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlossaryTermItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
