---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInfo.html
---

# NetworkInfo
<a name="API_NetworkInfo"></a>

Describes the networking features of the instance type.

## Contents
<a name="API_NetworkInfo_Contents"></a>

 ** BandwidthWeightings.N **
A list of valid settings for configurable bandwidth weighting for the instance type, if supported.
Type: Array of strings
Valid Values: `default | vpc-1 | ebs-1`
Required: No

 ** connectionTrackingConfiguration **
Indicates conntrack information for the instance type
Type: [DefaultConnectionTrackingConfiguration](API_DefaultConnectionTrackingConfiguration.md) object
Required: No

 ** defaultNetworkCardIndex **
The index of the default network card, starting at 0.
Type: Integer
Required: No

 ** efaInfo **
Describes the Elastic Fabric Adapters for the instance type.
Type: [EfaInfo](API_EfaInfo.md) object
Required: No

 ** efaSupported **
Indicates whether Elastic Fabric Adapter (EFA) is supported.
Type: Boolean
Required: No

 ** enaSrdSupported **
Indicates whether the instance type supports ENA Express. ENA Express uses AWS Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances.
Type: Boolean
Required: No

 ** enaSupport **
Indicates whether Elastic Network Adapter (ENA) is supported.
Type: String
Valid Values: `unsupported | supported | required`
Required: No

 ** encryptionInTransitSupported **
Indicates whether the instance type automatically encrypts in-transit traffic between instances.
Type: Boolean
Required: No

 ** flexibleEnaQueuesSupport **
Indicates whether changing the number of ENA queues is supported.
Type: String
Valid Values: `unsupported | supported`
Required: No

 ** ipv4AddressesPerInterface **
The maximum number of IPv4 addresses per network interface.
Type: Integer
Required: No

 ** ipv4AddressesPerSecondaryInterface **
The maximum number of IPv4 addresses per secondary interface.
Type: Integer
Required: No

 ** ipv6AddressesPerInterface **
The maximum number of IPv6 addresses per network interface.
Type: Integer
Required: No

 ** ipv6Supported **
Indicates whether IPv6 is supported.
Type: Boolean
Required: No

 ** maximumNetworkCards **
The maximum number of physical network cards that can be allocated to the instance.
Type: Integer
Required: No

 ** maximumNetworkInterfaces **
The maximum number of network interfaces for the instance type.
Type: Integer
Required: No

 ** maximumSecondaryNetworkInterfaces **
The maximum number of secondary interfaces for the instance type.
Type: Integer
Required: No

 ** NetworkCards.N **
Describes the network cards for the instance type.
Type: Array of [NetworkCardInfo](API_NetworkCardInfo.md) objects
Required: No

 ** networkPerformance **
The network performance.
Type: String
Required: No

 ** secondaryNetworkSupported **
Indicates whether secondary interface attachments from secondary network are supported.
Type: Boolean
Required: No

## See Also
<a name="API_NetworkInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInfo)
