---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesWorkload.html
---

# KubernetesWorkload
<a name="API_KubernetesWorkload"></a>

Contains information about Kubernetes workloads involved in a GuardDuty finding, including pods, deployments, and other Kubernetes resources.

## Contents
<a name="API_KubernetesWorkload_Contents"></a>

 ** containerUids **   <a name="guardduty-Type-KubernetesWorkload-containerUids"></a>
A list of unique identifiers for the containers that are part of the Kubernetes workload.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **   <a name="guardduty-Type-KubernetesWorkload-type"></a>
The types of Kubernetes resources involved in the workload.
Type: String
Valid Values: `PODS | JOBS | CRONJOBS | DEPLOYMENTS | DAEMONSETS | STATEFULSETS | REPLICASETS | REPLICATIONCONTROLLERS`
Required: No

 ** namespace **   <a name="guardduty-Type-KubernetesWorkload-namespace"></a>
The Kubernetes namespace in which the workload is running, providing logical isolation within the cluster.
Type: String
Required: No

## See Also
<a name="API_KubernetesWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesWorkload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
