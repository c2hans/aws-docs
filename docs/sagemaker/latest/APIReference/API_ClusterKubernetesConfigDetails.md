---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterKubernetesConfigDetails.html
---

# ClusterKubernetesConfigDetails
<a name="API_ClusterKubernetesConfigDetails"></a>

Detailed Kubernetes configuration showing both the current and desired state of labels and taints for cluster nodes.

## Contents
<a name="API_ClusterKubernetesConfigDetails_Contents"></a>

 ** CurrentLabels **   <a name="sagemaker-Type-ClusterKubernetesConfigDetails-CurrentLabels"></a>
The current labels applied to cluster nodes of an instance group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Value Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

 ** CurrentTaints **   <a name="sagemaker-Type-ClusterKubernetesConfigDetails-CurrentTaints"></a>
The current taints applied to cluster nodes of an instance group.
Type: Array of [ClusterKubernetesTaint](API_ClusterKubernetesTaint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** DesiredLabels **   <a name="sagemaker-Type-ClusterKubernetesConfigDetails-DesiredLabels"></a>
The desired labels to be applied to cluster nodes of an instance group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Value Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

 ** DesiredTaints **   <a name="sagemaker-Type-ClusterKubernetesConfigDetails-DesiredTaints"></a>
The desired taints to be applied to cluster nodes of an instance group.
Type: Array of [ClusterKubernetesTaint](API_ClusterKubernetesTaint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ClusterKubernetesConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterKubernetesConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterKubernetesConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterKubernetesConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
