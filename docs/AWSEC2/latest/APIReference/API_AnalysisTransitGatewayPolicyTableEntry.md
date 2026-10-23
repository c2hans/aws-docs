---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisTransitGatewayPolicyTableEntry.html
---

# AnalysisTransitGatewayPolicyTableEntry
<a name="API_AnalysisTransitGatewayPolicyTableEntry"></a>

Describes an entry in a transit gateway policy table.

## Contents
<a name="API_AnalysisTransitGatewayPolicyTableEntry_Contents"></a>

 ** destinationCidr **
The destination CIDR block. If this value is not present, the entry matches any destination address.
Type: String
Required: No

 ** destinationPortRange **
The destination port range. If this value is not present, the entry matches any destination port.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** protocol **
The protocol number. A value of `-1` means that the entry matches all protocols.
Type: String
Required: No

 ** ruleNumber **
The rule number for the policy table entry. Entries are evaluated in ascending order of rule number.
Type: Integer
Required: No

 ** sourceCidr **
The source CIDR block. If this value is not present, the entry matches any source address.
Type: String
Required: No

 ** sourcePortRange **
The source port range. If this value is not present, the entry matches any source port.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** targetRouteTableId **
The ID of the transit gateway route table to which the entry routes matching traffic.
Type: String
Required: No

## See Also
<a name="API_AnalysisTransitGatewayPolicyTableEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisTransitGatewayPolicyTableEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisTransitGatewayPolicyTableEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisTransitGatewayPolicyTableEntry)
