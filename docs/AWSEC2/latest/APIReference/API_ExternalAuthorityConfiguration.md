---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExternalAuthorityConfiguration.html
---

# ExternalAuthorityConfiguration
<a name="API_ExternalAuthorityConfiguration"></a>

The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.

For more information, see [Integrate VPC IPAM with Infoblox infrastructure](https://docs.aws.amazon.com/vpc/latest/ipam/integrate-infoblox-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Contents
<a name="API_ExternalAuthorityConfiguration_Contents"></a>

 ** ExternalResourceIdentifier **
The identifier for the external resource managing this scope. For Infoblox integrations, this is the Infoblox resource identifier in the format `<version>.identity.account.<entity_realm>.<entity_id>`.
Type: String
Required: No

 ** Type **
The type of external authority.
Type: String
Valid Values: `infoblox`
Required: No

## See Also
<a name="API_ExternalAuthorityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExternalAuthorityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExternalAuthorityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExternalAuthorityConfiguration)
