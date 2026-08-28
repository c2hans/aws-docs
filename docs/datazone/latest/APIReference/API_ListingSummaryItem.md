---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListingSummaryItem.html
---

# ListingSummaryItem
<a name="API_ListingSummaryItem"></a>

The results of the data product summary.

## Contents
<a name="API_ListingSummaryItem_Contents"></a>

 ** glossaryTerms **   <a name="datazone-Type-ListingSummaryItem-glossaryTerms"></a>
The glossary terms of the data product listing.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** listingId **   <a name="datazone-Type-ListingSummaryItem-listingId"></a>
The ID of the data product listing.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** listingRevision **   <a name="datazone-Type-ListingSummaryItem-listingRevision"></a>
The revision of the data product listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ListingSummaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListingSummaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListingSummaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListingSummaryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
