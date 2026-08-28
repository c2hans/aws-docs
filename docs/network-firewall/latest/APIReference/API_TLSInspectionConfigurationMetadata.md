---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TLSInspectionConfigurationMetadata.html
---

# TLSInspectionConfigurationMetadata
<a name="API_TLSInspectionConfigurationMetadata"></a>

High-level information about a TLS inspection configuration, returned by `ListTLSInspectionConfigurations`. You can use the information provided in the metadata to retrieve and manage a TLS configuration.

## Contents
<a name="API_TLSInspectionConfigurationMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-TLSInspectionConfigurationMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** Name **   <a name="networkfirewall-Type-TLSInspectionConfigurationMetadata-Name"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## See Also
<a name="API_TLSInspectionConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TLSInspectionConfigurationMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
