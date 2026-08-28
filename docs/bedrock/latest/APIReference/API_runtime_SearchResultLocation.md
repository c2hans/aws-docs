---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_SearchResultLocation.html
---

# SearchResultLocation
<a name="API_runtime_SearchResultLocation"></a>

Specifies a search result location within the content array, providing positioning information for cited content using search result index and block positions.

## Contents
<a name="API_runtime_SearchResultLocation_Contents"></a>

 ** end **   <a name="bedrock-Type-runtime_SearchResultLocation-end"></a>
The ending position in the content array where the cited content ends.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** searchResultIndex **   <a name="bedrock-Type-runtime_SearchResultLocation-searchResultIndex"></a>
The index of the search result content block where the cited content is found.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** start **   <a name="bedrock-Type-runtime_SearchResultLocation-start"></a>
The starting position in the content array where the cited content begins.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_runtime_SearchResultLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/SearchResultLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/SearchResultLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/SearchResultLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
