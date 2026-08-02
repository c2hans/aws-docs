---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PacketHeaderStatement.html
---

# PacketHeaderStatement
<a name="API_PacketHeaderStatement"></a>

Describes a packet header statement.

## Contents
<a name="API_PacketHeaderStatement_Contents"></a>

 ** DestinationAddressSet.N **
The destination addresses.
Type: Array of strings
Required: No

 ** DestinationPortSet.N **
The destination ports.
Type: Array of strings
Required: No

 ** DestinationPrefixListSet.N **
The destination prefix lists.
Type: Array of strings
Required: No

 ** ProtocolSet.N **
The protocols.
Type: Array of strings
Valid Values: `tcp | udp`
Required: No

 ** SourceAddressSet.N **
The source addresses.
Type: Array of strings
Required: No

 ** SourcePortSet.N **
The source ports.
Type: Array of strings
Required: No

 ** SourcePrefixListSet.N **
The source prefix lists.
Type: Array of strings
Required: No

## See Also
<a name="API_PacketHeaderStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PacketHeaderStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PacketHeaderStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PacketHeaderStatement)
