---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Evaluation.html
---

# Evaluation
<a name="API_Evaluation"></a>

 Represents the output of `GetEvaluation` operation.

The content consists of the detailed metadata and data file information and the current status of the `Evaluation`.

## Contents
<a name="API_Evaluation_Contents"></a>

 ** ComputeTime **   <a name="amazonml-Type-Evaluation-ComputeTime"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** CreatedAt **   <a name="amazonml-Type-Evaluation-CreatedAt"></a>
The time that the `Evaluation` was created. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** CreatedByIamUser **   <a name="amazonml-Type-Evaluation-CreatedByIamUser"></a>
The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`
Required: No

 ** EvaluationDataSourceId **   <a name="amazonml-Type-Evaluation-EvaluationDataSourceId"></a>
The ID of the `DataSource` that is used to evaluate the `MLModel`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** EvaluationId **   <a name="amazonml-Type-Evaluation-EvaluationId"></a>
The ID that is assigned to the `Evaluation` at creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** FinishedAt **   <a name="amazonml-Type-Evaluation-FinishedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** InputDataLocationS3 **   <a name="amazonml-Type-Evaluation-InputDataLocationS3"></a>
The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is used in the evaluation.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** LastUpdatedAt **   <a name="amazonml-Type-Evaluation-LastUpdatedAt"></a>
The time of the most recent edit to the `Evaluation`. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** Message **   <a name="amazonml-Type-Evaluation-Message"></a>
A description of the most recent details about evaluating the `MLModel`.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** MLModelId **   <a name="amazonml-Type-Evaluation-MLModelId"></a>
The ID of the `MLModel` that is the focus of the evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Name **   <a name="amazonml-Type-Evaluation-Name"></a>
A user-supplied name or description of the `Evaluation`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** PerformanceMetrics **   <a name="amazonml-Type-Evaluation-PerformanceMetrics"></a>
Measurements of how well the `MLModel` performed, using observations referenced by the `DataSource`. One of the following metrics is returned, based on the type of the `MLModel`:
+ BinaryAUC: A binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance.
+ RegressionRMSE: A regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.
+ MulticlassAvgFScore: A multiclass `MLModel` uses the F1 score technique to measure performance.
 For more information about performance metrics, please see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg).
Type: [PerformanceMetrics](API_PerformanceMetrics.md) object
Required: No

 ** StartedAt **   <a name="amazonml-Type-Evaluation-StartedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** Status **   <a name="amazonml-Type-Evaluation-Status"></a>
The status of the evaluation. This element can have one of the following values:
+  `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an `MLModel`.
+  `INPROGRESS` - The evaluation is underway.
+  `FAILED` - The request to evaluate an `MLModel` did not run to completion. It is not usable.
+  `COMPLETED` - The evaluation process completed successfully.
+  `DELETED` - The `Evaluation` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/Evaluation)
