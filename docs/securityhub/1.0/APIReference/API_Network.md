---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Network.html
---

# Network
<a name="API_Network"></a>

The details of network-related information about a finding.

## Contents
<a name="API_Network_Contents"></a>

 ** DestinationDomain **   <a name="securityhub-Type-Network-DestinationDomain"></a>
The destination domain of network-related information about a finding.
Length Constraints: Minimum of 1. Maximum of 128.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationIpV4 **   <a name="securityhub-Type-Network-DestinationIpV4"></a>
The destination IPv4 address of network-related information about a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationIpV6 **   <a name="securityhub-Type-Network-DestinationIpV6"></a>
The destination IPv6 address of network-related information about a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationPort **   <a name="securityhub-Type-Network-DestinationPort"></a>
The destination port of network-related information about a finding.
Type: Integer
Required: No

 ** Direction **   <a name="securityhub-Type-Network-Direction"></a>
The direction of network traffic associated with a finding.
Type: String
Valid Values: `IN | OUT`
Required: No

 ** OpenPortRange **   <a name="securityhub-Type-Network-OpenPortRange"></a>
The range of open ports that is present on the network.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** Protocol **   <a name="securityhub-Type-Network-Protocol"></a>
The protocol of network-related information about a finding.
Length Constraints: Minimum of 1. Maximum of 16.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceDomain **   <a name="securityhub-Type-Network-SourceDomain"></a>
The source domain of network-related information about a finding.
Length Constraints: Minimum of 1. Maximum of 128.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceIpV4 **   <a name="securityhub-Type-Network-SourceIpV4"></a>
The source IPv4 address of network-related information about a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceIpV6 **   <a name="securityhub-Type-Network-SourceIpV6"></a>
The source IPv6 address of network-related information about a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceMac **   <a name="securityhub-Type-Network-SourceMac"></a>
The source media access control (MAC) address of network-related information about a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourcePort **   <a name="securityhub-Type-Network-SourcePort"></a>
The source port of network-related information about a finding.
Type: Integer
Required: No

## See Also
<a name="API_Network_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Network)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Network)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Network)
