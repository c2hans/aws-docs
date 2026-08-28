---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_NativeIndexConfiguration.html
---

# NativeIndexConfiguration
<a name="API_NativeIndexConfiguration"></a>

Configuration information for an Amazon Q Business index.

## Contents
<a name="API_NativeIndexConfiguration_Contents"></a>

 ** indexId **   <a name="qbusiness-Type-NativeIndexConfiguration-indexId"></a>
The identifier for the Amazon Q Business index.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** boostingOverride **   <a name="qbusiness-Type-NativeIndexConfiguration-boostingOverride"></a>
Overrides the default boosts applied by Amazon Q Business to supported document attribute data types.
Type: String to [DocumentAttributeBoostingConfiguration](API_DocumentAttributeBoostingConfiguration.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 200.
Key Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: No

 ** version **   <a name="qbusiness-Type-NativeIndexConfiguration-version"></a>
A read-only field that specifies the version of the `NativeIndexConfiguration`.
Amazon Q Business introduces enhanced document retrieval capabilities in version 2 of `NativeIndexConfiguration`, focusing on streamlined metadata boosting that prioritizes recency and source relevance to deliver more accurate responses to your queries. Version 2 has the following differences from version 1:
+ Version 2 supports a single Date field (created\_at OR last\_updated\_at) for recency boosting
+ Version 2 supports a single String field with an ordered list of up to 5 values
+ Version 2 introduces number-based boost levels (ONE, TWO) alongside the text-based levels
+ Version 2 allows specifying prioritization between Date and String fields
+ Version 2 maintains backward compatibility with existing configurations
Type: Long
Required: No

## See Also
<a name="API_NativeIndexConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/NativeIndexConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/NativeIndexConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/NativeIndexConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
