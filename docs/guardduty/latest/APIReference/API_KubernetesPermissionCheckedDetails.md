---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesPermissionCheckedDetails.html
---

# KubernetesPermissionCheckedDetails
<a name="API_KubernetesPermissionCheckedDetails"></a>

Information about the Kubernetes API for which you check if you have permission to call.

## Contents
<a name="API_KubernetesPermissionCheckedDetails_Contents"></a>

 ** allowed **   <a name="guardduty-Type-KubernetesPermissionCheckedDetails-allowed"></a>
Information whether the user has the permission to call the Kubernetes API.
Type: Boolean
Required: No

 ** namespace **   <a name="guardduty-Type-KubernetesPermissionCheckedDetails-namespace"></a>
The namespace where the Kubernetes API action will take place.
Type: String
Required: No

 ** resource **   <a name="guardduty-Type-KubernetesPermissionCheckedDetails-resource"></a>
The Kubernetes resource with which your Kubernetes API call will interact.
Type: String
Required: No

 ** verb **   <a name="guardduty-Type-KubernetesPermissionCheckedDetails-verb"></a>
The verb component of the Kubernetes API call. For example, when you check whether or not you have the permission to call the `CreatePod` API, the verb component will be `Create`.
Type: String
Required: No

## See Also
<a name="API_KubernetesPermissionCheckedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesPermissionCheckedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesPermissionCheckedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesPermissionCheckedDetails)
