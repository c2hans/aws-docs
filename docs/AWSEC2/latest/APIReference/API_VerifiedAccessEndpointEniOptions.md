---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessEndpointEniOptions.html
---

# VerifiedAccessEndpointEniOptions
<a name="API_VerifiedAccessEndpointEniOptions"></a>

Options for a network-interface type endpoint.

## Contents
<a name="API_VerifiedAccessEndpointEniOptions_Contents"></a>

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** port **
The IP port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PortRangeSet.N **
The port ranges.
Type: Array of [VerifiedAccessEndpointPortRange](API_VerifiedAccessEndpointPortRange.md) objects
Required: No

 ** protocol **
The IP protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

## See Also
<a name="API_VerifiedAccessEndpointEniOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessEndpointEniOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessEndpointEniOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessEndpointEniOptions)
