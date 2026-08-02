---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_NetworkProfile.html
---

# NetworkProfile
<a name="API_NetworkProfile"></a>

An array of settings that describes characteristics of a network profile.

## Contents
<a name="API_NetworkProfile_Contents"></a>

 ** arn **   <a name="devicefarm-Type-NetworkProfile-arn"></a>
The Amazon Resource Name (ARN) of the network profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** description **   <a name="devicefarm-Type-NetworkProfile-description"></a>
The description of the network profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** downlinkBandwidthBits **   <a name="devicefarm-Type-NetworkProfile-downlinkBandwidthBits"></a>
The data throughput rate in bits per second, as an integer from 0 to 104857600.
Type: Long
Required: No

 ** downlinkDelayMs **   <a name="devicefarm-Type-NetworkProfile-downlinkDelayMs"></a>
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** downlinkJitterMs **   <a name="devicefarm-Type-NetworkProfile-downlinkJitterMs"></a>
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** downlinkLossPercent **   <a name="devicefarm-Type-NetworkProfile-downlinkLossPercent"></a>
Proportion of received packets that fail to arrive from 0 to 100 percent.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** name **   <a name="devicefarm-Type-NetworkProfile-name"></a>
The name of the network profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **   <a name="devicefarm-Type-NetworkProfile-type"></a>
The type of network profile. Valid values are listed here.
Type: String
Valid Values: `CURATED | PRIVATE`
Required: No

 ** uplinkBandwidthBits **   <a name="devicefarm-Type-NetworkProfile-uplinkBandwidthBits"></a>
The data throughput rate in bits per second, as an integer from 0 to 104857600.
Type: Long
Required: No

 ** uplinkDelayMs **   <a name="devicefarm-Type-NetworkProfile-uplinkDelayMs"></a>
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** uplinkJitterMs **   <a name="devicefarm-Type-NetworkProfile-uplinkJitterMs"></a>
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
Type: Long
Required: No

 ** uplinkLossPercent **   <a name="devicefarm-Type-NetworkProfile-uplinkLossPercent"></a>
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_NetworkProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/NetworkProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/NetworkProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/NetworkProfile)
