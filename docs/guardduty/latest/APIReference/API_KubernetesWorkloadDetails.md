---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesWorkloadDetails.html
---

# KubernetesWorkloadDetails
<a name="API_KubernetesWorkloadDetails"></a>

Details about the Kubernetes workload involved in a Kubernetes finding.

## Contents
<a name="API_KubernetesWorkloadDetails_Contents"></a>

 ** containers **   <a name="guardduty-Type-KubernetesWorkloadDetails-containers"></a>
Containers running as part of the Kubernetes workload.
Type: Array of [Container](API_Container.md) objects
Required: No

 ** hostIPC **   <a name="guardduty-Type-KubernetesWorkloadDetails-hostIPC"></a>
Whether the host IPC flag is enabled for the pods in the workload.
Type: Boolean
Required: No

 ** hostNetwork **   <a name="guardduty-Type-KubernetesWorkloadDetails-hostNetwork"></a>
Whether the hostNetwork flag is enabled for the pods included in the workload.
Type: Boolean
Required: No

 ** hostPID **   <a name="guardduty-Type-KubernetesWorkloadDetails-hostPID"></a>
Whether the host PID flag is enabled for the pods in the workload.
Type: Boolean
Required: No

 ** name **   <a name="guardduty-Type-KubernetesWorkloadDetails-name"></a>
Kubernetes workload name.
Type: String
Required: No

 ** namespace **   <a name="guardduty-Type-KubernetesWorkloadDetails-namespace"></a>
Kubernetes namespace that the workload is part of.
Type: String
Required: No

 ** serviceAccountName **   <a name="guardduty-Type-KubernetesWorkloadDetails-serviceAccountName"></a>
The service account name that is associated with a Kubernetes workload.
Type: String
Required: No

 ** type **   <a name="guardduty-Type-KubernetesWorkloadDetails-type"></a>
Kubernetes workload type (e.g. Pod, Deployment, etc.).
Type: String
Required: No

 ** uid **   <a name="guardduty-Type-KubernetesWorkloadDetails-uid"></a>
Kubernetes workload ID.
Type: String
Required: No

 ** volumes **   <a name="guardduty-Type-KubernetesWorkloadDetails-volumes"></a>
Volumes used by the Kubernetes workload.
Type: Array of [Volume](API_Volume.md) objects
Required: No

## See Also
<a name="API_KubernetesWorkloadDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesWorkloadDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesWorkloadDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesWorkloadDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
