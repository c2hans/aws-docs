---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AccountAggregationSource.html
---

# AccountAggregationSource
<a name="API_AccountAggregationSource"></a>

A collection of accounts and regions.

## Contents
<a name="API_AccountAggregationSource_Contents"></a>

 ** AccountIds **   <a name="config-Type-AccountAggregationSource-AccountIds"></a>
The 12-digit account ID of the account being aggregated.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** AllAwsRegions **   <a name="config-Type-AccountAggregationSource-AllAwsRegions"></a>
If true, aggregate existing AWS Config regions and future regions.
Type: Boolean
Required: No

 ** AwsRegions **   <a name="config-Type-AccountAggregationSource-AwsRegions"></a>
The source regions being aggregated.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_AccountAggregationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AccountAggregationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AccountAggregationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AccountAggregationSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
