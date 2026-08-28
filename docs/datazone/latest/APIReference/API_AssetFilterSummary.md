---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetFilterSummary.html
---

# AssetFilterSummary
<a name="API_AssetFilterSummary"></a>

The summary of the asset filter.

## Contents
<a name="API_AssetFilterSummary_Contents"></a>

 ** assetId **   <a name="datazone-Type-AssetFilterSummary-assetId"></a>
The ID of the data asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** domainId **   <a name="datazone-Type-AssetFilterSummary-domainId"></a>
The ID of the domain where the asset filter lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-AssetFilterSummary-id"></a>
The ID of the asset filter.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-AssetFilterSummary-name"></a>
The name of the asset filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** createdAt **   <a name="datazone-Type-AssetFilterSummary-createdAt"></a>
The timestamp at which the asset filter was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-AssetFilterSummary-description"></a>
The description of the asset filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** effectiveColumnNames **   <a name="datazone-Type-AssetFilterSummary-effectiveColumnNames"></a>
The effective column names of the asset filter.
Type: Array of strings
Required: No

 ** effectiveRowFilter **   <a name="datazone-Type-AssetFilterSummary-effectiveRowFilter"></a>
The effective row filter of the asset filter.
Type: String
Required: No

 ** errorMessage **   <a name="datazone-Type-AssetFilterSummary-errorMessage"></a>
The error message that is displayed if the action does not succeed.
Type: String
Required: No

 ** status **   <a name="datazone-Type-AssetFilterSummary-status"></a>
The status of the asset filter.
Type: String
Valid Values: `VALID | INVALID`
Required: No

## See Also
<a name="API_AssetFilterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetFilterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetFilterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetFilterSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
