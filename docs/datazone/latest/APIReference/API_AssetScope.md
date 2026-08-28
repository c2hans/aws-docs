---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetScope.html
---

# AssetScope
<a name="API_AssetScope"></a>

The asset scope.

## Contents
<a name="API_AssetScope_Contents"></a>

 ** assetId **   <a name="datazone-Type-AssetScope-assetId"></a>
The asset ID of the asset scope.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** filterIds **   <a name="datazone-Type-AssetScope-filterIds"></a>
The filter IDs of the asset scope.
Type: Array of strings
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-AssetScope-status"></a>
The status of the asset scope.
Type: String
Required: Yes

 ** errorMessage **   <a name="datazone-Type-AssetScope-errorMessage"></a>
The error message of the asset scope.
Type: String
Required: No

## See Also
<a name="API_AssetScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
