---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesRoleBindingDetails.html
---

# KubernetesRoleBindingDetails
<a name="API_KubernetesRoleBindingDetails"></a>

Contains information about the role binding that grants the permission defined in a Kubernetes role.

## Contents
<a name="API_KubernetesRoleBindingDetails_Contents"></a>

 ** kind **   <a name="guardduty-Type-KubernetesRoleBindingDetails-kind"></a>
The kind of the role. For role binding, this value will be `RoleBinding`.
Type: String
Required: No

 ** name **   <a name="guardduty-Type-KubernetesRoleBindingDetails-name"></a>
The name of the `RoleBinding`.
Type: String
Required: No

 ** roleRefKind **   <a name="guardduty-Type-KubernetesRoleBindingDetails-roleRefKind"></a>
The type of the role being referenced. This could be either `Role` or `ClusterRole`.
Type: String
Required: No

 ** roleRefName **   <a name="guardduty-Type-KubernetesRoleBindingDetails-roleRefName"></a>
The name of the role being referenced. This must match the name of the `Role` or `ClusterRole` that you want to bind to.
Type: String
Required: No

 ** uid **   <a name="guardduty-Type-KubernetesRoleBindingDetails-uid"></a>
The unique identifier of the role binding.
Type: String
Required: No

## See Also
<a name="API_KubernetesRoleBindingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesRoleBindingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesRoleBindingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesRoleBindingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
