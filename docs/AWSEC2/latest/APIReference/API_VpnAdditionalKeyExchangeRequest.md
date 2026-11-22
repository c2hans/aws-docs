---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnAdditionalKeyExchangeRequest.html
---

# VpnAdditionalKeyExchangeRequest

Specifies an additional key exchange round for the VPN tunnel, as defined in RFC 9370.

## Contents
<a name="API_VpnAdditionalKeyExchangeRequest_Contents"></a>

 ** AdditionalKeyExchangeRound **
The additional key exchange round number.
Valid range: Minimum value of 1. Maximum value of 7.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 7.
Required: Yes

 ** KeyExchangeMethod.N **
The key exchange method numbers that are permitted for this round. The method numbers are the IANA IKEv2 key exchange method transform IDs.
A `required` round must specify at least one method. An `optional` round can omit this parameter or specify an empty list. If omitted or empty for an optional round, the round is disabled.
IKEv2 requires that the initial Diffie-Hellman exchange and each required round use a different key exchange method. The permitted methods must allow a distinct method to be selected for each of them.
Valid values: `2` \| `5` \| `14` \| `15` \| `16` \| `17` \| `18` \| `19` \| `20` \| `21` \| `22` \| `23` \| `24` \| `35` \| `36` \| `37`
Type: Array of [AdditionalKeyExchangeMethodsRequestListValue](API_AdditionalKeyExchangeMethodsRequestListValue.md) objects
Required: No

 ** Requirement **
Indicates whether this round is mandatory. If `required`, the tunnel isn't established unless the customer gateway device negotiates this round. If `optional`, the round is negotiated only if the customer gateway device supports it.
Valid values: `required` \| `optional`
Default: `required`
Type: String
Valid Values: `required | optional`
Required: No

## See Also
<a name="API_VpnAdditionalKeyExchangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnAdditionalKeyExchangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnAdditionalKeyExchangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnAdditionalKeyExchangeRequest)
