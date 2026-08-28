---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RuleDetail.html
---

# RuleDetail
<a name="API_RuleDetail"></a>

The details of a rule.

## Contents
<a name="API_RuleDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glossaryTermEnforcementDetail **   <a name="datazone-Type-RuleDetail-glossaryTermEnforcementDetail"></a>
The enforcement details of a glossary term that's part of the metadata rule.
Type: [GlossaryTermEnforcementDetail](API_GlossaryTermEnforcementDetail.md) object
Required: No

 ** metadataFormEnforcementDetail **   <a name="datazone-Type-RuleDetail-metadataFormEnforcementDetail"></a>
The enforcement detail of the metadata form.
Type: [MetadataFormEnforcementDetail](API_MetadataFormEnforcementDetail.md) object
Required: No

## See Also
<a name="API_RuleDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RuleDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RuleDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RuleDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
