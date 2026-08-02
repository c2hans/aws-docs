---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PacketHeaderStatementRequest.html
---

# PacketHeaderStatementRequest
<a name="API_PacketHeaderStatementRequest"></a>

Describes a packet header statement.

## Contents
<a name="API_PacketHeaderStatementRequest_Contents"></a>

 ** DestinationAddress.N **
The destination addresses.
Type: Array of strings
Required: No

 ** DestinationPort.N **
The destination ports.
Type: Array of strings
Required: No

 ** DestinationPrefixList.N **
The destination prefix lists.
Type: Array of strings
Required: No

 ** Protocol.N **
The protocols.
Type: Array of strings
Valid Values: `tcp | udp`
Required: No

 ** SourceAddress.N **
The source addresses.
Type: Array of strings
Required: No

 ** SourcePort.N **
The source ports.
Type: Array of strings
Required: No

 ** SourcePrefixList.N **
The source prefix lists.
Type: Array of strings
Required: No

## See Also
<a name="API_PacketHeaderStatementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PacketHeaderStatementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PacketHeaderStatementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PacketHeaderStatementRequest)
