---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_TargetNetwork.html
---

# TargetNetwork
<a name="API_TargetNetwork"></a>

Configuration for the target network topology and addressing.

## Contents
<a name="API_TargetNetwork_Contents"></a>

 ** topology **   <a name="mgn-Type-TargetNetwork-topology"></a>
The network topology type for the target environment.
Type: String
Valid Values: `ISOLATED_VPC | HUB_AND_SPOKE`
Required: Yes

 ** inboundCidr **   <a name="mgn-Type-TargetNetwork-inboundCidr"></a>
The CIDR block for inbound traffic in the target network.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

 ** inspectionCidr **   <a name="mgn-Type-TargetNetwork-inspectionCidr"></a>
The CIDR block for inspection traffic in the target network.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

 ** outboundCidr **   <a name="mgn-Type-TargetNetwork-outboundCidr"></a>
The CIDR block for outbound traffic in the target network.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `((25[0-4]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\/(1[6-9]|2[0-8])`
Required: No

## See Also
<a name="API_TargetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/TargetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/TargetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/TargetNetwork)
