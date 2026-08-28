---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_EligibleDataSource.html
---

# EligibleDataSource
<a name="API_EligibleDataSource"></a>

The identifier of the data source Amazon Q Business will generate responses from.

## Contents
<a name="API_EligibleDataSource_Contents"></a>

 ** dataSourceId **   <a name="qbusiness-Type-EligibleDataSource-dataSourceId"></a>
The identifier of the data source.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** indexId **   <a name="qbusiness-Type-EligibleDataSource-indexId"></a>
The identifier of the index the data source is attached to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

## See Also
<a name="API_EligibleDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/EligibleDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/EligibleDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/EligibleDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
