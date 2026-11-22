---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnAdditionalKeyExchange.html
---

# VpnAdditionalKeyExchange

Describes an additional key exchange round that is permitted for the VPN tunnel.

## Contents
<a name="API_VpnAdditionalKeyExchange_Contents"></a>

 ** additionalKeyExchangeRound **
The additional key exchange round number.
Type: Integer
Required: No

 ** KeyExchangeMethodSet.N **
The key exchange method numbers permitted for this round.
Type: Array of [AdditionalKeyExchangeMethodsListValue](API_AdditionalKeyExchangeMethodsListValue.md) objects
Required: No

 ** requirement **
Indicates whether this round is mandatory.
Type: String
Valid Values: `required | optional`
Required: No

## See Also
<a name="API_VpnAdditionalKeyExchange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnAdditionalKeyExchange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnAdditionalKeyExchange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnAdditionalKeyExchange)
