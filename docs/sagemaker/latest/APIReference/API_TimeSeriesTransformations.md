---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesTransformations.html
---

# TimeSeriesTransformations
<a name="API_TimeSeriesTransformations"></a>

Transformations allowed on the dataset. Supported transformations are `Filling` and `Aggregation`. `Filling` specifies how to add values to missing values in the dataset. `Aggregation` defines how to aggregate data that does not align with forecast frequency.

## Contents
<a name="API_TimeSeriesTransformations_Contents"></a>

 ** Aggregation **   <a name="sagemaker-Type-TimeSeriesTransformations-Aggregation"></a>
A key value pair defining the aggregation method for a column, where the key is the column name and the value is the aggregation method.
The supported aggregation methods are `sum` (default), `avg`, `first`, `min`, `max`.
Aggregation is only supported for the target column.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Valid Values: `sum | avg | first | min | max`
Required: No

 ** Filling **   <a name="sagemaker-Type-TimeSeriesTransformations-Filling"></a>
A key value pair defining the filling method for a column, where the key is the column name and the value is an object which defines the filling logic. You can specify multiple filling methods for a single column.
The supported filling methods and their corresponding options are:
+  `frontfill`: `none` (Supported only for target column)
+  `middlefill`: `zero`, `value`, `median`, `mean`, `min`, `max`
+  `backfill`: `zero`, `value`, `median`, `mean`, `min`, `max`
+  `futurefill`: `zero`, `value`, `median`, `mean`, `min`, `max`
To set a filling method to a specific value, set the fill parameter to the chosen filling method value (for example `"backfill" : "value"`), and define the filling value in an additional parameter prefixed with "\_value". For example, to set `backfill` to a value of `2`, you must include two parameters: `"backfill": "value"` and `"backfill_value":"2"`.
Type: String to string to string map map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Map Entries: Maximum number of 6 items.
Valid Keys: `frontfill | middlefill | backfill | futurefill | frontfill_value | middlefill_value | backfill_value | futurefill_value`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\_\-]+`
Required: No

## See Also
<a name="API_TimeSeriesTransformations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TimeSeriesTransformations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TimeSeriesTransformations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TimeSeriesTransformations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
