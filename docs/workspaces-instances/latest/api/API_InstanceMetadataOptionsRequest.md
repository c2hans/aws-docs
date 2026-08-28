---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceMetadataOptionsRequest.html
---

# InstanceMetadataOptionsRequest
<a name="API_InstanceMetadataOptionsRequest"></a>

Defines instance metadata service configuration.

## Contents
<a name="API_InstanceMetadataOptionsRequest_Contents"></a>

 ** HttpEndpoint **   <a name="workspacesinstances-Type-InstanceMetadataOptionsRequest-HttpEndpoint"></a>
Enables or disables HTTP endpoint for instance metadata.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** HttpProtocolIpv6 **   <a name="workspacesinstances-Type-InstanceMetadataOptionsRequest-HttpProtocolIpv6"></a>
Configures IPv6 support for instance metadata HTTP protocol.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** HttpPutResponseHopLimit **   <a name="workspacesinstances-Type-InstanceMetadataOptionsRequest-HttpPutResponseHopLimit"></a>
Sets maximum number of network hops for metadata PUT responses.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 64.
Required: No

 ** HttpTokens **   <a name="workspacesinstances-Type-InstanceMetadataOptionsRequest-HttpTokens"></a>
Configures token requirement for instance metadata retrieval.
Type: String
Valid Values: `optional | required`
Required: No

 ** InstanceMetadataTags **   <a name="workspacesinstances-Type-InstanceMetadataOptionsRequest-InstanceMetadataTags"></a>
Enables or disables instance metadata tags retrieval.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_InstanceMetadataOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/InstanceMetadataOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/InstanceMetadataOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/InstanceMetadataOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
