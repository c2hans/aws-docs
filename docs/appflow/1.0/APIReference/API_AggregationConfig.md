---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_AggregationConfig.html
---

# AggregationConfig
<a name="API_AggregationConfig"></a>

 The aggregation settings that you can use to customize the output format of your flow data.

## Contents
<a name="API_AggregationConfig_Contents"></a>

 ** aggregationType **   <a name="appflow-Type-AggregationConfig-aggregationType"></a>
 Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.
Type: String
Valid Values: `None | SingleFile`
Required: No

 ** targetFileSize **   <a name="appflow-Type-AggregationConfig-targetFileSize"></a>
The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.
Type: Long
Required: No

## See Also
<a name="API_AggregationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/AggregationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/AggregationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/AggregationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
