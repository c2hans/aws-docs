---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_PerformanceMetrics.html
---

# PerformanceMetrics
<a name="API_PerformanceMetrics"></a>

Measurements of how well the `MLModel` performed on known observations. One of the following metrics is returned, based on the type of the `MLModel`:
+ BinaryAUC: The binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance.
+ RegressionRMSE: The regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.
+ MulticlassAvgFScore: The multiclass `MLModel` uses the F1 score technique to measure performance.

 For more information about performance metrics, please see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg).

## Contents
<a name="API_PerformanceMetrics_Contents"></a>

 ** Properties **   <a name="amazonml-Type-PerformanceMetrics-Properties"></a>
Specific performance metric information.
Type: String to string map
Required: No

## See Also
<a name="API_PerformanceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/PerformanceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/PerformanceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/PerformanceMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
