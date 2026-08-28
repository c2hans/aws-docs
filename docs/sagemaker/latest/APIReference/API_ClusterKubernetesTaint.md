---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterKubernetesTaint.html
---

# ClusterKubernetesTaint
<a name="API_ClusterKubernetesTaint"></a>

A Kubernetes taint that can be applied to cluster nodes.

## Contents
<a name="API_ClusterKubernetesTaint_Contents"></a>

 ** Effect **   <a name="sagemaker-Type-ClusterKubernetesTaint-Effect"></a>
The effect of the taint. Valid values are `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
Type: String
Valid Values: `NoSchedule | PreferNoSchedule | NoExecute`
Required: Yes

 ** Key **   <a name="sagemaker-Type-ClusterKubernetesTaint-Key"></a>
The key of the taint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 317.
Pattern: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Required: Yes

 ** Value **   <a name="sagemaker-Type-ClusterKubernetesTaint-Value"></a>
The value of the taint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
Required: No

## See Also
<a name="API_ClusterKubernetesTaint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterKubernetesTaint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterKubernetesTaint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterKubernetesTaint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
