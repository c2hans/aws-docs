---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesUserDetails.html
---

# KubernetesUserDetails
<a name="API_KubernetesUserDetails"></a>

Details about the Kubernetes user involved in a Kubernetes finding.

## Contents
<a name="API_KubernetesUserDetails_Contents"></a>

 ** groups **   <a name="guardduty-Type-KubernetesUserDetails-groups"></a>
The groups that include the user who called the Kubernetes API.
Type: Array of strings
Required: No

 ** impersonatedUser **   <a name="guardduty-Type-KubernetesUserDetails-impersonatedUser"></a>
Information about the impersonated user.
Type: [ImpersonatedUser](API_ImpersonatedUser.md) object
Required: No

 ** sessionName **   <a name="guardduty-Type-KubernetesUserDetails-sessionName"></a>
Entity that assumes the IAM role when Kubernetes RBAC permissions are assigned to that role.
Type: Array of strings
Required: No

 ** uid **   <a name="guardduty-Type-KubernetesUserDetails-uid"></a>
The user ID of the user who called the Kubernetes API.
Type: String
Required: No

 ** username **   <a name="guardduty-Type-KubernetesUserDetails-username"></a>
The username of the user who called the Kubernetes API.
Type: String
Required: No

## See Also
<a name="API_KubernetesUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesUserDetails)
