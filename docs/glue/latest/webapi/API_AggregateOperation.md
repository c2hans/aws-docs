---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AggregateOperation.html
---

# AggregateOperation
<a name="API_AggregateOperation"></a>

Specifies the set of parameters needed to perform aggregation in the aggregate transform.

## Contents
<a name="API_AggregateOperation_Contents"></a>

 ** AggFunc **   <a name="Glue-Type-AggregateOperation-AggFunc"></a>
Specifies the aggregation function to apply.
Possible aggregation functions include: avg countDistinct, count, first, last, kurtosis, max, min, skewness, stddev\_samp, stddev\_pop, sum, sumDistinct, var\_samp, var\_pop
Type: String
Valid Values: `avg | countDistinct | count | first | last | kurtosis | max | min | skewness | stddev_samp | stddev_pop | sum | sumDistinct | var_samp | var_pop`
Required: Yes

 ** Column **   <a name="Glue-Type-AggregateOperation-Column"></a>
Specifies the column on the data set on which the aggregation function will be applied.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_AggregateOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AggregateOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AggregateOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AggregateOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
