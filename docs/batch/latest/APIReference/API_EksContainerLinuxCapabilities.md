---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksContainerLinuxCapabilities.html
---

# EksContainerLinuxCapabilities
<a name="API_EksContainerLinuxCapabilities"></a>

The Linux capabilities for the container. For more information, see [Set capabilities for a container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) in the *Kubernetes documentation*.

## Contents
<a name="API_EksContainerLinuxCapabilities_Contents"></a>

 ** add **   <a name="Batch-Type-EksContainerLinuxCapabilities-add"></a>
The Linux capabilities to add to the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the `CAP_` prefix.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** drop **   <a name="Batch-Type-EksContainerLinuxCapabilities-drop"></a>
The Linux capabilities to remove from the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the `CAP_` prefix.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_EksContainerLinuxCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksContainerLinuxCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksContainerLinuxCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksContainerLinuxCapabilities)
