---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterKubernetesConfigNodeDetails.html
---

# ClusterKubernetesConfigNodeDetails
<a name="API_ClusterKubernetesConfigNodeDetails"></a>

Node-specific Kubernetes configuration showing both current and desired state of labels and taints for an individual cluster node.

## Contents
<a name="API_ClusterKubernetesConfigNodeDetails_Contents"></a>

 ** CurrentLabels **   <a name="sagemaker-Type-ClusterKubernetesConfigNodeDetails-CurrentLabels"></a>
The current labels applied to the cluster node.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Value Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

 ** CurrentTaints **   <a name="sagemaker-Type-ClusterKubernetesConfigNodeDetails-CurrentTaints"></a>
The current taints applied to the cluster node.
Type: Array of [ClusterKubernetesTaint](API_ClusterKubernetesTaint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** DesiredLabels **   <a name="sagemaker-Type-ClusterKubernetesConfigNodeDetails-DesiredLabels"></a>
The desired labels to be applied to the cluster node.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Value Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

 ** DesiredTaints **   <a name="sagemaker-Type-ClusterKubernetesConfigNodeDetails-DesiredTaints"></a>
The desired taints to be applied to the cluster node.
Type: Array of [ClusterKubernetesTaint](API_ClusterKubernetesTaint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ClusterKubernetesConfigNodeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterKubernetesConfigNodeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterKubernetesConfigNodeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterKubernetesConfigNodeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
