---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_KubernetesClusterRoleUpdate.html
---

# KubernetesClusterRoleUpdate
<a name="API_KubernetesClusterRoleUpdate"></a>

The kubernetes Cluster Role Update.

## Contents
<a name="API_KubernetesClusterRoleUpdate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** remove **   <a name="continuum-Type-KubernetesClusterRoleUpdate-remove"></a>
The remove.
Type: [RemoveKubernetesClusterRole](API_RemoveKubernetesClusterRole.md) object
Required: No

 ** set **   <a name="continuum-Type-KubernetesClusterRoleUpdate-set"></a>
The set.
Type: [KubernetesClusterRoleConfiguration](API_KubernetesClusterRoleConfiguration.md) object
Required: No

## See Also
<a name="API_KubernetesClusterRoleUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/KubernetesClusterRoleUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/KubernetesClusterRoleUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/KubernetesClusterRoleUpdate)
