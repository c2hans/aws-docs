---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

Contains information about actions.

## Contents
<a name="API_Action_Contents"></a>

 ** actionType **   <a name="guardduty-Type-Action-actionType"></a>
The GuardDuty finding activity type.
Type: String
Required: No

 ** awsApiCallAction **   <a name="guardduty-Type-Action-awsApiCallAction"></a>
Information about the AWS\_API\_CALL action described in this finding.
Type: [AwsApiCallAction](API_AwsApiCallAction.md) object
Required: No

 ** dnsRequestAction **   <a name="guardduty-Type-Action-dnsRequestAction"></a>
Information about the DNS\_REQUEST action described in this finding.
Type: [DnsRequestAction](API_DnsRequestAction.md) object
Required: No

 ** kubernetesApiCallAction **   <a name="guardduty-Type-Action-kubernetesApiCallAction"></a>
Information about the Kubernetes API call action described in this finding.
Type: [KubernetesApiCallAction](API_KubernetesApiCallAction.md) object
Required: No

 ** kubernetesPermissionCheckedDetails **   <a name="guardduty-Type-Action-kubernetesPermissionCheckedDetails"></a>
Information whether the user has the permission to use a specific Kubernetes API.
Type: [KubernetesPermissionCheckedDetails](API_KubernetesPermissionCheckedDetails.md) object
Required: No

 ** kubernetesRoleBindingDetails **   <a name="guardduty-Type-Action-kubernetesRoleBindingDetails"></a>
Information about the role binding that grants the permission defined in a Kubernetes role.
Type: [KubernetesRoleBindingDetails](API_KubernetesRoleBindingDetails.md) object
Required: No

 ** kubernetesRoleDetails **   <a name="guardduty-Type-Action-kubernetesRoleDetails"></a>
Information about the Kubernetes role name and role type.
Type: [KubernetesRoleDetails](API_KubernetesRoleDetails.md) object
Required: No

 ** networkConnectionAction **   <a name="guardduty-Type-Action-networkConnectionAction"></a>
Information about the NETWORK\_CONNECTION action described in this finding.
Type: [NetworkConnectionAction](API_NetworkConnectionAction.md) object
Required: No

 ** portProbeAction **   <a name="guardduty-Type-Action-portProbeAction"></a>
Information about the PORT\_PROBE action described in this finding.
Type: [PortProbeAction](API_PortProbeAction.md) object
Required: No

 ** rdsLoginAttemptAction **   <a name="guardduty-Type-Action-rdsLoginAttemptAction"></a>
Information about `RDS_LOGIN_ATTEMPT` action described in this finding.
Type: [RdsLoginAttemptAction](API_RdsLoginAttemptAction.md) object
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
