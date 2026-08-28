---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GroupByResult.html
---

# GroupByResult
<a name="API_GroupByResult"></a>

Represents finding statistics grouped by `GroupedByField`.

## Contents
<a name="API_GroupByResult_Contents"></a>

 ** GroupByField **   <a name="securityhub-Type-GroupByResult-GroupByField"></a>
The attribute by which filtered security findings should be grouped.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupByValues **   <a name="securityhub-Type-GroupByResult-GroupByValues"></a>
An array of grouped values and their respective counts for each `GroupByField`.
Type: Array of [GroupByValue](API_GroupByValue.md) objects
Required: No

## See Also
<a name="API_GroupByResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GroupByResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GroupByResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GroupByResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
