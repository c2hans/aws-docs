---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksSeccompProfile.html
---

# EksSeccompProfile
<a name="API_EksSeccompProfile"></a>

The Linux seccomp profile for a pod or container. For more information, see [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksSeccompProfile_Contents"></a>

 ** type **   <a name="Batch-Type-EksSeccompProfile-type"></a>
The seccomp profile type can be one of the following values:
RuntimeDefault
The `RuntimeDefault` value uses the container runtime's default seccomp profile.
Unconfined
The `Unconfined` value doesn't filter the container with seccomp.
Localhost
The `Localhost` value uses a custom profile at the path specified by `localhostProfile`.
Type: String
Valid Values: `RuntimeDefault | Localhost | Unconfined`
Required: Yes

 ** localhostProfile **   <a name="Batch-Type-EksSeccompProfile-localhostProfile"></a>
The path of the profile on the node, relative to the configured seccomp profile location. You must specify this parameter when `type` is `Localhost`. Don't set this parameter for any other type. You are responsible for ensuring that the profile exists on every eligible worker node. For information about providing files to Amazon EKS nodes, see [Use a launch template with AWS Batch on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/eks-launch-templates.html) in the * AWS Batch User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Required: No

## See Also
<a name="API_EksSeccompProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksSeccompProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksSeccompProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksSeccompProfile)
