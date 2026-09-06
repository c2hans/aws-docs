---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessEndpointCidrOptions.html
---

# VerifiedAccessEndpointCidrOptions
<a name="API_VerifiedAccessEndpointCidrOptions"></a>

Describes the CIDR options for a Verified Access endpoint.

## Contents
<a name="API_VerifiedAccessEndpointCidrOptions_Contents"></a>

 ** cidr **
The CIDR.
Type: String
Required: No

 ** PortRangeSet.N **
The port ranges.
Type: Array of [VerifiedAccessEndpointPortRange](API_VerifiedAccessEndpointPortRange.md) objects
Required: No

 ** protocol **
The protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

 ** SubnetIdSet.N **
The IDs of the subnets.
Type: Array of strings
Required: No

## See Also
<a name="API_VerifiedAccessEndpointCidrOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessEndpointCidrOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessEndpointCidrOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessEndpointCidrOptions)
