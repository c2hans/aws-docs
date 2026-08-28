---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SyntheticDataColumnProperties.html
---

# SyntheticDataColumnProperties
<a name="API_SyntheticDataColumnProperties"></a>

Properties that define how a specific data column should be handled during synthetic data generation, including its name, type, and role in predictive modeling.

## Contents
<a name="API_SyntheticDataColumnProperties_Contents"></a>

 ** columnName **   <a name="API-Type-SyntheticDataColumnProperties-columnName"></a>
The name of the data column as it appears in the dataset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_]+-)*([a-z0-9_]+))?`
Required: Yes

 ** columnType **   <a name="API-Type-SyntheticDataColumnProperties-columnType"></a>
The data type of the column, which determines how the synthetic data generation algorithm processes and synthesizes values for this column.
Type: String
Valid Values: `CATEGORICAL | NUMERICAL`
Required: Yes

 ** isPredictiveValue **   <a name="API-Type-SyntheticDataColumnProperties-isPredictiveValue"></a>
Indicates if this column contains predictive values that should be treated as target variables in machine learning models. This affects how the synthetic data generation preserves statistical relationships.
Type: Boolean
Required: Yes

## See Also
<a name="API_SyntheticDataColumnProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SyntheticDataColumnProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SyntheticDataColumnProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SyntheticDataColumnProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
