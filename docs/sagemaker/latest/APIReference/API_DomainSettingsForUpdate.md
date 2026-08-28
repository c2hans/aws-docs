---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DomainSettingsForUpdate.html
---

# DomainSettingsForUpdate
<a name="API_DomainSettingsForUpdate"></a>

A collection of `Domain` configuration settings to update.

## Contents
<a name="API_DomainSettingsForUpdate_Contents"></a>

 ** AmazonQSettings **   <a name="sagemaker-Type-DomainSettingsForUpdate-AmazonQSettings"></a>
A collection of settings that configure the Amazon Q experience within the domain.
Type: [AmazonQSettings](API_AmazonQSettings.md) object
Required: No

 ** DockerSettings **   <a name="sagemaker-Type-DomainSettingsForUpdate-DockerSettings"></a>
A collection of settings that configure the domain's Docker interaction.
Type: [DockerSettings](API_DockerSettings.md) object
Required: No

 ** ExecutionRoleIdentityConfig **   <a name="sagemaker-Type-DomainSettingsForUpdate-ExecutionRoleIdentityConfig"></a>
The configuration for attaching a SageMaker AI user profile name to the execution role as a [sts:SourceIdentity key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html). This configuration can only be modified if there are no apps in the `InService` or `Pending` state.
Type: String
Valid Values: `USER_PROFILE_NAME | DISABLED`
Required: No

 ** IpAddressType **   <a name="sagemaker-Type-DomainSettingsForUpdate-IpAddressType"></a>
The IP address type for the domain. Specify `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity. When you specify `dualstack`, the subnet must support IPv6 CIDR blocks.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** RStudioServerProDomainSettingsForUpdate **   <a name="sagemaker-Type-DomainSettingsForUpdate-RStudioServerProDomainSettingsForUpdate"></a>
A collection of `RStudioServerPro` Domain-level app settings to update. A single `RStudioServerPro` application is created for a domain.
Type: [RStudioServerProDomainSettingsForUpdate](API_RStudioServerProDomainSettingsForUpdate.md) object
Required: No

 ** SecurityGroupIds **   <a name="sagemaker-Type-DomainSettingsForUpdate-SecurityGroupIds"></a>
The security groups for the Amazon Virtual Private Cloud that the `Domain` uses for communication between Domain-level apps and user apps.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** TrustedIdentityPropagationSettings **   <a name="sagemaker-Type-DomainSettingsForUpdate-TrustedIdentityPropagationSettings"></a>
The Trusted Identity Propagation (TIP) settings for the SageMaker domain. These settings determine how user identities from IAM Identity Center are propagated through the domain to TIP enabled AWS services.
Type: [TrustedIdentityPropagationSettings](API_TrustedIdentityPropagationSettings.md) object
Required: No

 ** UnifiedStudioSettings **   <a name="sagemaker-Type-DomainSettingsForUpdate-UnifiedStudioSettings"></a>
The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.
Type: [UnifiedStudioSettings](API_UnifiedStudioSettings.md) object
Required: No

## See Also
<a name="API_DomainSettingsForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DomainSettingsForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DomainSettingsForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DomainSettingsForUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
