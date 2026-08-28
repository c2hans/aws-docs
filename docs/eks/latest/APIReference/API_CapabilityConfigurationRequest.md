---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilityConfigurationRequest.html
---

# CapabilityConfigurationRequest
<a name="API_CapabilityConfigurationRequest"></a>

Configuration settings for a capability. The structure of this object varies depending on the capability type.

## Contents
<a name="API_CapabilityConfigurationRequest_Contents"></a>

 ** argoCd **   <a name="AmazonEKS-Type-CapabilityConfigurationRequest-argoCd"></a>
Configuration settings specific to Argo CD capabilities. This field is only used when creating or updating an Argo CD capability.
Type: [ArgoCdConfigRequest](API_ArgoCdConfigRequest.md) object
Required: No

## See Also
<a name="API_CapabilityConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CapabilityConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CapabilityConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CapabilityConfigurationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
