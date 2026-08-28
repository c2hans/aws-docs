---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_EndpointNetworkConfiguration.html
---

# EndpointNetworkConfiguration
<a name="API_EndpointNetworkConfiguration"></a>

Specifies network configuration information for the gateway associated with the Amazon FSx file system.

## Contents
<a name="API_EndpointNetworkConfiguration_Contents"></a>

 ** IpAddresses **   <a name="StorageGateway-Type-EndpointNetworkConfiguration-IpAddresses"></a>
A list of gateway IP addresses on which the associated Amazon FSx file system is available.
If multiple file systems are associated with this gateway, this field is required.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}`
Required: No

## See Also
<a name="API_EndpointNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/EndpointNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/EndpointNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/EndpointNetworkConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
