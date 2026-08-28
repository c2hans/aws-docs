---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_MLModel.html
---

# MLModel
<a name="API_MLModel"></a>

 Represents the output of a `GetMLModel` operation.

The content consists of the detailed metadata and the current status of the `MLModel`.

## Contents
<a name="API_MLModel_Contents"></a>

 ** Algorithm **   <a name="amazonml-Type-MLModel-Algorithm"></a>
The algorithm used to train the `MLModel`. The following algorithm is supported:
+  `SGD` -- Stochastic gradient descent. The goal of `SGD` is to minimize the gradient of the loss function.
Type: String
Valid Values: `sgd`
Required: No

 ** ComputeTime **   <a name="amazonml-Type-MLModel-ComputeTime"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** CreatedAt **   <a name="amazonml-Type-MLModel-CreatedAt"></a>
The time that the `MLModel` was created. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** CreatedByIamUser **   <a name="amazonml-Type-MLModel-CreatedByIamUser"></a>
The AWS user account from which the `MLModel` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`
Required: No

 ** EndpointInfo **   <a name="amazonml-Type-MLModel-EndpointInfo"></a>
The current endpoint of the `MLModel`.
Type: [RealtimeEndpointInfo](API_RealtimeEndpointInfo.md) object
Required: No

 ** FinishedAt **   <a name="amazonml-Type-MLModel-FinishedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** InputDataLocationS3 **   <a name="amazonml-Type-MLModel-InputDataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** LastUpdatedAt **   <a name="amazonml-Type-MLModel-LastUpdatedAt"></a>
The time of the most recent edit to the `MLModel`. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** Message **   <a name="amazonml-Type-MLModel-Message"></a>
A description of the most recent details about accessing the `MLModel`.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** MLModelId **   <a name="amazonml-Type-MLModel-MLModelId"></a>
The ID assigned to the `MLModel` at creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** MLModelType **   <a name="amazonml-Type-MLModel-MLModelType"></a>
Identifies the `MLModel` category. The following are the available types:
+  `REGRESSION` - Produces a numeric result. For example, "What price should a house be listed at?"
+  `BINARY` - Produces one of two possible results. For example, "Is this a child-friendly web site?".
+  `MULTICLASS` - Produces one of several possible results. For example, "Is this a HIGH-, LOW-, or MEDIUM-risk trade?".
Type: String
Valid Values: `REGRESSION | BINARY | MULTICLASS`
Required: No

 ** Name **   <a name="amazonml-Type-MLModel-Name"></a>
A user-supplied name or description of the `MLModel`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** ScoreThreshold **   <a name="amazonml-Type-MLModel-ScoreThreshold"></a>
The score threshold for the `MLModel`.
Type: Float
Required: No

 ** ScoreThresholdLastUpdatedAt **   <a name="amazonml-Type-MLModel-ScoreThresholdLastUpdatedAt"></a>
The time of the most recent edit to the `ScoreThreshold`. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** SizeInBytes **   <a name="amazonml-Type-MLModel-SizeInBytes"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** StartedAt **   <a name="amazonml-Type-MLModel-StartedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** Status **   <a name="amazonml-Type-MLModel-Status"></a>
The current status of an `MLModel`. This element can have one of the following values:
+  `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to create an `MLModel`.
+  `INPROGRESS` - The creation process is underway.
+  `FAILED` - The request to create an `MLModel` didn't run to completion. The model isn't usable.
+  `COMPLETED` - The creation process completed successfully.
+  `DELETED` - The `MLModel` is marked as deleted. It isn't usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`
Required: No

 ** TrainingDataSourceId **   <a name="amazonml-Type-MLModel-TrainingDataSourceId"></a>
The ID of the training `DataSource`. The `CreateMLModel` operation uses the `TrainingDataSourceId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** TrainingParameters **   <a name="amazonml-Type-MLModel-TrainingParameters"></a>
A list of the training parameters in the `MLModel`. The list is implemented as a map of key-value pairs.
The following is the current set of training parameters:
+  `sgd.maxMLModelSizeInBytes` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

   The value is an integer that ranges from `100000` to `2147483648`. The default value is `33554432`.
+  `sgd.maxPasses` - The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `100`. The default value is `10`.
+  `sgd.shuffleType` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`.
+  `sgd.l1RegularizationAmount` - The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L1 normalization. This parameter can't be used when `L2` is specified. Use this parameter sparingly.
+  `sgd.l2RegularizationAmount` - The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L2 normalization. This parameter can't be used when `L1` is specified. Use this parameter sparingly.
Type: String to string map
Required: No

## See Also
<a name="API_MLModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/MLModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/MLModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/MLModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
