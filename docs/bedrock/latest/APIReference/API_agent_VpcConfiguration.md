---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_agent_VpcConfiguration"></a>

Contains the details of a VPC configuration, including its connection settings, resolution mode, and current lifecycle status.

## Contents
<a name="API_agent_VpcConfiguration_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-agent_VpcConfiguration-createdAt"></a>
The time at which the VPC configuration was created.
Type: Timestamp
Required: Yes

 ** port **   <a name="bedrock-Type-agent_VpcConfiguration-port"></a>
The port on which the resource is reached.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** protocol **   <a name="bedrock-Type-agent_VpcConfiguration-protocol"></a>
The protocol used to connect to the resource.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

 ** resolutionMode **   <a name="bedrock-Type-agent_VpcConfiguration-resolutionMode"></a>
Specifies how the resource target is resolved.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: Yes

 ** resourceTarget **   <a name="bedrock-Type-agent_VpcConfiguration-resourceTarget"></a>
The private IPv4 address or DNS name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** status **   <a name="bedrock-Type-agent_VpcConfiguration-status"></a>
The current lifecycle status of the VPC configuration.
Type: String
Valid Values: `CREATING | CREATED | DELETING | CREATE_FAILED | DELETE_FAILED`
Required: Yes

 ** subnetIds **   <a name="bedrock-Type-agent_VpcConfiguration-subnetIds"></a>
The subnets that the knowledge base uses to connect to the resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `subnet-[a-zA-Z0-9]+`
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_VpcConfiguration-updatedAt"></a>
The time at which the VPC configuration was last updated.
Type: Timestamp
Required: Yes

 ** vpcConfigurationId **   <a name="bedrock-Type-agent_VpcConfiguration-vpcConfigurationId"></a>
The unique identifier of the VPC configuration.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9](?:[a-z0-9-]{30}[a-z0-9])`
Required: Yes

 ** vpcId **   <a name="bedrock-Type-agent_VpcConfiguration-vpcId"></a>
The identifier of the VPC that the knowledge base connects through to reach the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `vpc-[a-zA-Z0-9]+`
Required: Yes

 ** description **   <a name="bedrock-Type-agent_VpcConfiguration-description"></a>
The description of the VPC configuration, if provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^\p{C}]*`
Required: No

 ** hostHeader **   <a name="bedrock-Type-agent_VpcConfiguration-hostHeader"></a>
The HTTP `Host` header value sent when invoking the resource, if configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._:\[\]-]{1,255}`
Required: No

 ** name **   <a name="bedrock-Type-agent_VpcConfiguration-name"></a>
The human-readable name of the VPC configuration, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9 _-]*[a-zA-Z0-9])?`
Required: No

 ** statusMessage **   <a name="bedrock-Type-agent_VpcConfiguration-statusMessage"></a>
Additional detail about the current status, such as the cause of a `CREATE_FAILED` or `DELETE_FAILED` status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** tlsServerName **   <a name="bedrock-Type-agent_VpcConfiguration-tlsServerName"></a>
The expected TLS server name that the service matches against the Subject Alternative Names on the resource's TLS certificate. Present when `protocol` is `HTTPS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(\*\.)?([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)*[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?`
Required: No

## See Also
<a name="API_agent_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VpcConfiguration)
