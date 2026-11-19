---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterOperationSummary.html
---

# ClusterOperationSummary

A summary of an operation performed on a HyperPod cluster.

## Contents
<a name="API_ClusterOperationSummary_Contents"></a>

 ** ClusterArn **   <a name="sagemaker-Type-ClusterOperationSummary-ClusterArn"></a>
The Amazon Resource Name (ARN) of the HyperPod cluster associated with the operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ClusterOperationSummary-CreationTime"></a>
The timestamp when the operation was created.
Type: Timestamp
Required: No

 ** OperationId **   <a name="sagemaker-Type-ClusterOperationSummary-OperationId"></a>
The unique identifier (UUID) of the operation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Status **   <a name="sagemaker-Type-ClusterOperationSummary-Status"></a>
The current status of the operation. Valid values are `InProgress`, `Superseded`, or `Done`.
Type: String
Valid Values: `InProgress | Superseded | Done`
Required: No

 ** Type **   <a name="sagemaker-Type-ClusterOperationSummary-Type"></a>
The type of the operation. Valid values are `Scaling` or `DeepHealthCheck`.
Type: String
Valid Values: `Scaling | DeepHealthCheck`
Required: No

## See Also
<a name="API_ClusterOperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterOperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterOperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterOperationSummary)
