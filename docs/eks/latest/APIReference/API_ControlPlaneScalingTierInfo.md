---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ControlPlaneScalingTierInfo.html
---

# ControlPlaneScalingTierInfo
<a name="API_ControlPlaneScalingTierInfo"></a>

Information about a provisioned control plane scaling tier.

## Contents
<a name="API_ControlPlaneScalingTierInfo_Contents"></a>

 ** apiRequestConcurrency **   <a name="AmazonEKS-Type-ControlPlaneScalingTierInfo-apiRequestConcurrency"></a>
The maximum API request concurrency supported by this tier.
Type: Integer
Required: No

 ** clusterDatabaseSizeGb **   <a name="AmazonEKS-Type-ControlPlaneScalingTierInfo-clusterDatabaseSizeGb"></a>
The maximum cluster database size in GB supported by this tier.
Type: Integer
Required: No

 ** controlPlaneComponentConfigOverrides **   <a name="AmazonEKS-Type-ControlPlaneScalingTierInfo-controlPlaneComponentConfigOverrides"></a>
The control plane component configuration overrides specific to this scaling tier.
Type: [ControlPlaneConfigInfo](API_ControlPlaneConfigInfo.md) object
Required: No

 ** podSchedulingRatePerSecond **   <a name="AmazonEKS-Type-ControlPlaneScalingTierInfo-podSchedulingRatePerSecond"></a>
The maximum pod scheduling rate per second supported by this tier.
Type: Integer
Required: No

 ** tierName **   <a name="AmazonEKS-Type-ControlPlaneScalingTierInfo-tierName"></a>
The name of the scaling tier.
Type: String
Required: No

## See Also
<a name="API_ControlPlaneScalingTierInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ControlPlaneScalingTierInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ControlPlaneScalingTierInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ControlPlaneScalingTierInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
