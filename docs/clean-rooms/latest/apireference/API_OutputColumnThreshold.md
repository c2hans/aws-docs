---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_OutputColumnThreshold.html
---

# OutputColumnThreshold
<a name="API_OutputColumnThreshold"></a>

Specifies the minimum number of distinct identities for an individual output column. This value overrides the table-wide `minimumIdentityCount` that you set in `AggregationThreshold`.

## Contents
<a name="API_OutputColumnThreshold_Contents"></a>

 ** minimumIdentityCount **   <a name="API-Type-OutputColumnThreshold-minimumIdentityCount"></a>
The minimum number of distinct identities that each query output group must represent for this column. Specify 0 to exempt the column from the threshold, or a value of 2 or greater to enforce a threshold.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: Yes

 ** outputColumnName **   <a name="API-Type-OutputColumnThreshold-outputColumnName"></a>
The name of the output column that the override applies to. You can specify each column only once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

## See Also
<a name="API_OutputColumnThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/OutputColumnThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/OutputColumnThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/OutputColumnThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
