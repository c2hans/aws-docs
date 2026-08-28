---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_KubeApiServerVersionConfig.html
---

# KubeApiServerVersionConfig
<a name="API_KubeApiServerVersionConfig"></a>

The Kubernetes API server version-specific configuration defaults and constraints.

## Contents
<a name="API_KubeApiServerVersionConfig_Contents"></a>

 ** eventTtl **   <a name="AmazonEKS-Type-KubeApiServerVersionConfig-eventTtl"></a>
The event TTL configuration with default value and constraints.
Type: [DurationParameterConfig](API_DurationParameterConfig.md) object
Required: No

 ** serviceNodePortRange **   <a name="AmazonEKS-Type-KubeApiServerVersionConfig-serviceNodePortRange"></a>
The service node port range configuration with default value and constraints.
Type: [PortRangeParameterConfig](API_PortRangeParameterConfig.md) object
Required: No

## See Also
<a name="API_KubeApiServerVersionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubeApiServerVersionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubeApiServerVersionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubeApiServerVersionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
