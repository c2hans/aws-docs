---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReferenceStoreFilter.html
---

# ReferenceStoreFilter
<a name="API_ReferenceStoreFilter"></a>

A filter for reference stores.

## Contents
<a name="API_ReferenceStoreFilter_Contents"></a>

 ** createdAfter **   <a name="omics-Type-ReferenceStoreFilter-createdAfter"></a>
The filter's start date.
Type: Timestamp
Required: No

 ** createdBefore **   <a name="omics-Type-ReferenceStoreFilter-createdBefore"></a>
The filter's end date.
Type: Timestamp
Required: No

 ** name **   <a name="omics-Type-ReferenceStoreFilter-name"></a>
The name to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ReferenceStoreFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReferenceStoreFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReferenceStoreFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReferenceStoreFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
