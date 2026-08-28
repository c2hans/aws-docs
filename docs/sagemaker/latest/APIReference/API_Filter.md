---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A conditional statement for a search expression that includes a resource property, a Boolean operator, and a value. Resources that match the statement are returned in the results from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

If you specify a `Value`, but not an `Operator`, SageMaker uses the equals operator.

In search, there are several property types:

Metrics
To define a metric filter, enter a value using the form `"Metrics.<name>"`, where `<name>` is a metric name. For example, the following filter searches for training jobs with an `"accuracy"` metric greater than `"0.9"`:
 `{`
 `"Name": "Metrics.accuracy",`
 `"Operator": "GreaterThan",`
 `"Value": "0.9"`
 `}`

HyperParameters
To define a hyperparameter filter, enter a value with the form `"HyperParameters.<name>"`. Decimal hyperparameter values are treated as a decimal in a comparison if the specified `Value` is also a decimal value. If the specified `Value` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a `"learning_rate"` hyperparameter that is less than `"0.5"`:
 ` {`
 ` "Name": "HyperParameters.learning_rate",`
 ` "Operator": "LessThan",`
 ` "Value": "0.5"`
 ` }`

Tags
To define a tag filter, enter a value with the form `Tags.<key>`.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-Filter-Name"></a>
A resource property name. For example, `TrainingJobName`. For valid property names, see [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html). You must specify a valid property for the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** Operator **   <a name="sagemaker-Type-Filter-Operator"></a>
A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:
Equals
The value of `Name` equals `Value`.
NotEquals
The value of `Name` doesn't equal `Value`.
Exists
The `Name` property exists.
NotExists
The `Name` property does not exist.
GreaterThan
The value of `Name` is greater than `Value`. Not supported for text properties.
GreaterThanOrEqualTo
The value of `Name` is greater than or equal to `Value`. Not supported for text properties.
LessThan
The value of `Name` is less than `Value`. Not supported for text properties.
LessThanOrEqualTo
The value of `Name` is less than or equal to `Value`. Not supported for text properties.
In
The value of `Name` is one of the comma delimited strings in `Value`. Only supported for text properties.
Contains
The value of `Name` contains the string `Value`. Only supported for text properties.
A `SearchExpression` can include the `Contains` operator multiple times when the value of `Name` is one of the following:
+  `Experiment.DisplayName`
+  `Experiment.ExperimentName`
+  `Experiment.Tags`
+  `Trial.DisplayName`
+  `Trial.TrialName`
+  `Trial.Tags`
+  `TrialComponent.DisplayName`
+  `TrialComponent.TrialComponentName`
+  `TrialComponent.Tags`
+  `TrialComponent.InputArtifacts`
+  `TrialComponent.OutputArtifacts`
A `SearchExpression` can include only one `Contains` operator for all other values of `Name`. In these cases, if you include multiple `Contains` operators in the `SearchExpression`, the result is the following error message: "`'CONTAINS' operator usage limit of 1 exceeded.`"
Type: String
Valid Values: `Equals | NotEquals | GreaterThan | GreaterThanOrEqualTo | LessThan | LessThanOrEqualTo | Contains | Exists | NotExists | In`
Required: No

 ** Value **   <a name="sagemaker-Type-Filter-Value"></a>
A value used with `Name` and `Operator` to determine which resources satisfy the filter's condition. For numerical properties, `Value` must be an integer or floating-point decimal. For timestamp properties, `Value` must be an ISO 8601 date-time string of the following format: `YYYY-mm-dd'T'HH:MM:SS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
