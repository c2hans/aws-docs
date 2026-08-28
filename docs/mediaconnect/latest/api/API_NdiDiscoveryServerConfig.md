---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiDiscoveryServerConfig.html
---

# NdiDiscoveryServerConfig
<a name="API_NdiDiscoveryServerConfig"></a>

Specifies the configuration settings for individual NDI® discovery servers. A maximum of 3 servers is allowed.

## Contents
<a name="API_NdiDiscoveryServerConfig_Contents"></a>

 ** discoveryServerAddress **   <a name="mediaconnect-Type-NdiDiscoveryServerConfig-discoveryServerAddress"></a>
The unique network address of the NDI discovery server.
Type: String
Required: Yes

 ** vpcInterfaceAdapter **   <a name="mediaconnect-Type-NdiDiscoveryServerConfig-vpcInterfaceAdapter"></a>
The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.
Type: String
Required: Yes

 ** discoveryServerPort **   <a name="mediaconnect-Type-NdiDiscoveryServerConfig-discoveryServerPort"></a>
The port for the NDI discovery server. Defaults to 5959 if a custom port isn't specified.
Type: Integer
Required: No

## See Also
<a name="API_NdiDiscoveryServerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiDiscoveryServerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiDiscoveryServerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiDiscoveryServerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
