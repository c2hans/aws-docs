---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_AmazonMachineImageSecurityGroup.html
---

# AmazonMachineImageSecurityGroup
<a name="API_marketplace-discovery_AmazonMachineImageSecurityGroup"></a>

Contains a recommended security group configuration for an AMI fulfillment option.

## Contents
<a name="API_marketplace-discovery_AmazonMachineImageSecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cidrIpAddresses **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageSecurityGroup-cidrIpAddresses"></a>
The IP address ranges in CIDR format.
Type: Array of strings
Required: Yes

 ** fromPort **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageSecurityGroup-fromPort"></a>
The start of the port range.
Type: Integer
Required: Yes

 ** protocol **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageSecurityGroup-protocol"></a>
The IP protocol name, such as `tcp`.
Type: String
Required: Yes

 ** toPort **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageSecurityGroup-toPort"></a>
The end of the port range.
Type: Integer
Required: Yes

## See Also
<a name="API_marketplace-discovery_AmazonMachineImageSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/AmazonMachineImageSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/AmazonMachineImageSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/AmazonMachineImageSecurityGroup)
