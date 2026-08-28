---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ControlPlaneConfigInfo.html
---

# ControlPlaneConfigInfo
<a name="API_ControlPlaneConfigInfo"></a>

The control plane component configuration defaults and constraints.

## Contents
<a name="API_ControlPlaneConfigInfo_Contents"></a>

 ** kubeApiServerConfig **   <a name="AmazonEKS-Type-ControlPlaneConfigInfo-kubeApiServerConfig"></a>
The Kubernetes API server configuration defaults and constraints.
Type: [KubeApiServerVersionConfig](API_KubeApiServerVersionConfig.md) object
Required: No

 ** kubeControllerManagerConfig **   <a name="AmazonEKS-Type-ControlPlaneConfigInfo-kubeControllerManagerConfig"></a>
The Kubernetes controller manager configuration defaults and constraints.
Type: [KubeControllerManagerVersionConfig](API_KubeControllerManagerVersionConfig.md) object
Required: No

 ** kubeSchedulerConfig **   <a name="AmazonEKS-Type-ControlPlaneConfigInfo-kubeSchedulerConfig"></a>
The Kubernetes scheduler configuration defaults and constraints.
Type: [KubeSchedulerVersionConfig](API_KubeSchedulerVersionConfig.md) object
Required: No

## See Also
<a name="API_ControlPlaneConfigInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ControlPlaneConfigInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ControlPlaneConfigInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ControlPlaneConfigInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
