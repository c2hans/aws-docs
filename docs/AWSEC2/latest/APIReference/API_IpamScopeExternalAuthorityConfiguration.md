---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamScopeExternalAuthorityConfiguration.html
---

# IpamScopeExternalAuthorityConfiguration
<a name="API_IpamScopeExternalAuthorityConfiguration"></a>

The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.

In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to AWS while using Amazon VPC IPAM to manage subnets within those ranges.

## Contents
<a name="API_IpamScopeExternalAuthorityConfiguration_Contents"></a>

 ** externalResourceIdentifier **
The identifier for the external resource managing this scope. For Infoblox integrations, this is the Infoblox resource identifier in the format `<version>.identity.account.<entity_realm>.<entity_id>`.
Type: String
Required: No

 ** type **
The type of external authority managing this scope. Currently supports `Infoblox` for integration with Infoblox Universal DDI.
Type: String
Valid Values: `infoblox`
Required: No

## See Also
<a name="API_IpamScopeExternalAuthorityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamScopeExternalAuthorityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamScopeExternalAuthorityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamScopeExternalAuthorityConfiguration)
