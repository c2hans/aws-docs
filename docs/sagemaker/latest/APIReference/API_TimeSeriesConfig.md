---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesConfig.html
---

# TimeSeriesConfig
<a name="API_TimeSeriesConfig"></a>

The collection of components that defines the time-series.

## Contents
<a name="API_TimeSeriesConfig_Contents"></a>

 ** ItemIdentifierAttributeName **   <a name="sagemaker-Type-TimeSeriesConfig-ItemIdentifierAttributeName"></a>
The name of the column that represents the set of item identifiers for which you want to predict the target value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** TargetAttributeName **   <a name="sagemaker-Type-TimeSeriesConfig-TargetAttributeName"></a>
The name of the column representing the target variable that you want to predict for each item in your dataset. The data type of the target variable must be numerical.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** TimestampAttributeName **   <a name="sagemaker-Type-TimeSeriesConfig-TimestampAttributeName"></a>
The name of the column indicating a point in time at which the target value of a given item is recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** GroupingAttributeNames **   <a name="sagemaker-Type-TimeSeriesConfig-GroupingAttributeNames"></a>
A set of columns names that can be grouped with the item identifier column to create a composite key for which a target value is predicted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_TimeSeriesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TimeSeriesConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TimeSeriesConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TimeSeriesConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
