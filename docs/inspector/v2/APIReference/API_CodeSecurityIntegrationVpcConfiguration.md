---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityIntegrationVpcConfiguration.html
---

# CodeSecurityIntegrationVpcConfiguration

The VPC configuration that Amazon Inspector uses to connect to a source code repository provider that is hosted in a private network.

## Contents
<a name="API_CodeSecurityIntegrationVpcConfiguration_Contents"></a>

 ** vpcEndpointId **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-vpcEndpointId"></a>
The ID of the VPC endpoint used for the connection.
Type: String
Pattern: `vpce-[0-9a-f]{8}([0-9a-f]{9})?`
Required: Yes

 ** vpcId **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-vpcId"></a>
The ID of the VPC that Amazon Inspector connects through to reach the repository provider.
Type: String
Pattern: `vpc-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: Yes

 ** codeConnectionsHostArn **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-codeConnectionsHostArn"></a>
The Amazon Resource Name (ARN) of the AWS CodeConnections host used for the connection.
Type: String
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: No

 ** securityGroups **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-securityGroups"></a>
The IDs of the security groups used for the connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Pattern: `sg-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** subnetIds **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-subnetIds"></a>
The IDs of the subnets used for the connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Pattern: `subnet-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** tlsCertificate **   <a name="inspector2-Type-CodeSecurityIntegrationVpcConfiguration-tlsCertificate"></a>
The TLS certificate used to establish a trusted connection to the repository provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CodeSecurityIntegrationVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSecurityIntegrationVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSecurityIntegrationVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSecurityIntegrationVpcConfiguration)
