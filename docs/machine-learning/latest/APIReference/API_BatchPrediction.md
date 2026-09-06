---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_BatchPrediction.html
---

# BatchPrediction
<a name="API_BatchPrediction"></a>

 Represents the output of a `GetBatchPrediction` operation.

 The content consists of the detailed metadata, the status, and the data file information of a `Batch Prediction`.

## Contents
<a name="API_BatchPrediction_Contents"></a>

 ** BatchPredictionDataSourceId **   <a name="amazonml-Type-BatchPrediction-BatchPredictionDataSourceId"></a>
The ID of the `DataSource` that points to the group of observations to predict.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** BatchPredictionId **   <a name="amazonml-Type-BatchPrediction-BatchPredictionId"></a>
The ID assigned to the `BatchPrediction` at creation. This value should be identical to the value of the `BatchPredictionID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** ComputeTime **   <a name="amazonml-Type-BatchPrediction-ComputeTime"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** CreatedAt **   <a name="amazonml-Type-BatchPrediction-CreatedAt"></a>
The time that the `BatchPrediction` was created. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** CreatedByIamUser **   <a name="amazonml-Type-BatchPrediction-CreatedByIamUser"></a>
The AWS user account that invoked the `BatchPrediction`. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`
Required: No

 ** FinishedAt **   <a name="amazonml-Type-BatchPrediction-FinishedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** InputDataLocationS3 **   <a name="amazonml-Type-BatchPrediction-InputDataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** InvalidRecordCount **   <a name="amazonml-Type-BatchPrediction-InvalidRecordCount"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** LastUpdatedAt **   <a name="amazonml-Type-BatchPrediction-LastUpdatedAt"></a>
The time of the most recent edit to the `BatchPrediction`. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** Message **   <a name="amazonml-Type-BatchPrediction-Message"></a>
A description of the most recent details about processing the batch prediction request.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** MLModelId **   <a name="amazonml-Type-BatchPrediction-MLModelId"></a>
The ID of the `MLModel` that generated predictions for the `BatchPrediction` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Name **   <a name="amazonml-Type-BatchPrediction-Name"></a>
A user-supplied name or description of the `BatchPrediction`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** OutputUri **   <a name="amazonml-Type-BatchPrediction-OutputUri"></a>
The location of an Amazon S3 bucket or directory to receive the operation results. The following substrings are not allowed in the `s3 key` portion of the `outputURI` field: ':', '//', '/./', '/../'.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** StartedAt **   <a name="amazonml-Type-BatchPrediction-StartedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** Status **   <a name="amazonml-Type-BatchPrediction-Status"></a>
The status of the `BatchPrediction`. This element can have one of the following values:
+  `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
+  `INPROGRESS` - The process is underway.
+  `FAILED` - The request to perform a batch prediction did not run to completion. It is not usable.
+  `COMPLETED` - The batch prediction process completed successfully.
+  `DELETED` - The `BatchPrediction` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`
Required: No

 ** TotalRecordCount **   <a name="amazonml-Type-BatchPrediction-TotalRecordCount"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

## See Also
<a name="API_BatchPrediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/BatchPrediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/BatchPrediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/BatchPrediction)
