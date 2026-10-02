---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksConfiguration.html
---

# EksConfiguration
<a name="API_EksConfiguration"></a>

Configuration for the Amazon EKS cluster that supports the AWS Batch compute environment. The cluster must exist before the compute environment can be created.

## Contents
<a name="API_EksConfiguration_Contents"></a>

 ** eksClusterArn **   <a name="Batch-Type-EksConfiguration-eksClusterArn"></a>
The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is `arn:aws:eks:us-east-1:123456789012:cluster/ClusterForBatch `.
Type: String
Required: Yes

 ** kubernetesNamespace **   <a name="Batch-Type-EksConfiguration-kubernetesNamespace"></a>
The namespace of the Amazon EKS cluster. AWS Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to `default`, can't start with "`kube-`," and must match this regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`. For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.
Type: String
Required: Yes

 ** accessEntry **   <a name="Batch-Type-EksConfiguration-accessEntry"></a>
The AWS Batch-managed Amazon EKS access entry for the compute environment. Set `desiredState` to declare whether AWS Batch manages an access entry on the cluster. In a `DescribeComputeEnvironments` response, `desiredState` is the value that AWS Batch recorded for the compute environment and `status` is the observed state of the access entry on the cluster. To change the access entry on an existing compute environment, use [`EksConfigurationUpdate.accessEntry`](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksConfigurationUpdate.html#Batch-Type-EksConfigurationUpdate-accessEntry).
Whether the entry is provisioned on the cluster depends on the cluster's `authenticationMode` and the `desiredState` recorded for each AWS Batch compute environment targeting the cluster. For more information, see [Amazon EKS access entry authentication](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html) in the * AWS Batch User Guide*.
If you don't specify this field, AWS Batch doesn't record a `desiredState` for the compute environment and `DescribeComputeEnvironments` doesn't return one. For the purpose of provisioning the access entry, AWS Batch behaves as it does for `INHERIT_FROM_CLUSTER`.
Type: [EksAccessEntry](API_EksAccessEntry.md) object
Required: No

## See Also
<a name="API_EksConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksConfiguration)
