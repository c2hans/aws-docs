---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetListing.html
---

# AssetListing
<a name="API_AssetListing"></a>

An asset published in an Amazon DataZone catalog.

## Contents
<a name="API_AssetListing_Contents"></a>

 ** assetId **   <a name="datazone-Type-AssetListing-assetId"></a>
The identifier of an asset published in an Amazon DataZone catalog.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** assetRevision **   <a name="datazone-Type-AssetListing-assetRevision"></a>
The revision of an asset published in an Amazon DataZone catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** assetType **   <a name="datazone-Type-AssetListing-assetType"></a>
The type of an asset published in an Amazon DataZone catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: No

 ** createdAt **   <a name="datazone-Type-AssetListing-createdAt"></a>
The timestamp of when an asset published in an Amazon DataZone catalog was created.
Type: Timestamp
Required: No

 ** forms **   <a name="datazone-Type-AssetListing-forms"></a>
The metadata forms attached to an asset published in an Amazon DataZone catalog.
Type: String
Required: No

 ** glossaryTerms **   <a name="datazone-Type-AssetListing-glossaryTerms"></a>
The glossary terms attached to an asset published in an Amazon DataZone catalog.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** governedGlossaryTerms **   <a name="datazone-Type-AssetListing-governedGlossaryTerms"></a>
The restricted glossary terms associated with an asset.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** latestTimeSeriesDataPointForms **   <a name="datazone-Type-AssetListing-latestTimeSeriesDataPointForms"></a>
The latest time series data points forms included in the additional attributes of an asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects
Required: No

 ** owningProjectId **   <a name="datazone-Type-AssetListing-owningProjectId"></a>
The identifier of the project where an asset published in an Amazon DataZone catalog exists.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_AssetListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetListing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
