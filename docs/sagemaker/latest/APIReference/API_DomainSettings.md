---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DomainSettings.html
---

# DomainSettings
<a name="API_DomainSettings"></a>

A collection of settings that apply to the `SageMaker Domain`. These settings are specified through the `CreateDomain` API call.

## Contents
<a name="API_DomainSettings_Contents"></a>

 ** AmazonQSettings **   <a name="sagemaker-Type-DomainSettings-AmazonQSettings"></a>
A collection of settings that configure the Amazon Q experience within the domain. The `AuthMode` that you use to create the domain must be `SSO`.
Type: [AmazonQSettings](API_AmazonQSettings.md) object
Required: No

 ** DockerSettings **   <a name="sagemaker-Type-DomainSettings-DockerSettings"></a>
A collection of settings that configure the domain's Docker interaction.
Type: [DockerSettings](API_DockerSettings.md) object
Required: No

 ** ExecutionRoleIdentityConfig **   <a name="sagemaker-Type-DomainSettings-ExecutionRoleIdentityConfig"></a>
The configuration for attaching a SageMaker AI user profile name to the execution role as a [sts:SourceIdentity key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html).
Type: String
Valid Values: `USER_PROFILE_NAME | DISABLED`
Required: No

 ** IpAddressType **   <a name="sagemaker-Type-DomainSettings-IpAddressType"></a>
The IP address type for the domain. Specify `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity. When you specify `dualstack`, the subnet must support IPv6 CIDR blocks. If not specified, defaults to `ipv4`.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** RStudioServerProDomainSettings **   <a name="sagemaker-Type-DomainSettings-RStudioServerProDomainSettings"></a>
A collection of settings that configure the `RStudioServerPro` Domain-level app.
Type: [RStudioServerProDomainSettings](API_RStudioServerProDomainSettings.md) object
Required: No

 ** SecurityGroupIds **   <a name="sagemaker-Type-DomainSettings-SecurityGroupIds"></a>
The security groups for the Amazon Virtual Private Cloud that the `Domain` uses for communication between Domain-level apps and user apps.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** TrustedIdentityPropagationSettings **   <a name="sagemaker-Type-DomainSettings-TrustedIdentityPropagationSettings"></a>
The Trusted Identity Propagation (TIP) settings for the SageMaker domain. These settings determine how user identities from IAM Identity Center are propagated through the domain to TIP enabled AWS services.
Type: [TrustedIdentityPropagationSettings](API_TrustedIdentityPropagationSettings.md) object
Required: No

 ** UnifiedStudioSettings **   <a name="sagemaker-Type-DomainSettings-UnifiedStudioSettings"></a>
The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.
Type: [UnifiedStudioSettings](API_UnifiedStudioSettings.md) object
Required: No

## See Also
<a name="API_DomainSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DomainSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DomainSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DomainSettings)
