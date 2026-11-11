---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksPodSecurityContext.html
---

# EksPodSecurityContext
<a name="API_EksPodSecurityContext"></a>

The security context for the pod. The settings apply to all containers in the pod when the container does not specify an overriding value. For more information, see [Set the security context for a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) in the *Kubernetes documentation*.

## Contents
<a name="API_EksPodSecurityContext_Contents"></a>

 ** fsGroup **   <a name="Batch-Type-EksPodSecurityContext-fsGroup"></a>
A special supplemental group that is applied to all containers in the pod. Some volume types allow Kubernetes to change the ownership and permissions of the volume contents to this group when the volume is mounted. The supported value range is `0` through `2147483647`.
Type: Long
Required: No

 ** runAsGroup **   <a name="Batch-Type-EksPodSecurityContext-runAsGroup"></a>
The primary group ID that runs containers in the pod when a container does not specify its own group ID. The supported value range is `0` through `2147483647`.
Type: Long
Required: No

 ** runAsNonRoot **   <a name="Batch-Type-EksPodSecurityContext-runAsNonRoot"></a>
Specifies whether Kubernetes validates that containers in the pod don't run as the root user unless a container specifies an overriding value.
Type: Boolean
Required: No

 ** runAsUser **   <a name="Batch-Type-EksPodSecurityContext-runAsUser"></a>
The user ID that runs containers in the pod when a container does not specify its own user ID. The supported value range is `0` through `2147483647`.
Type: Long
Required: No

 ** seccompProfile **   <a name="Batch-Type-EksPodSecurityContext-seccompProfile"></a>
The default seccomp profile for containers in the pod. A container-level seccomp profile overrides this value.
Type: [EksSeccompProfile](API_EksSeccompProfile.md) object
Required: No

## See Also
<a name="API_EksPodSecurityContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPodSecurityContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPodSecurityContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPodSecurityContext)
