---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewBGPPeer.html
---

# NewBGPPeer
<a name="API_NewBGPPeer"></a>

Information about a new BGP peer.

## Contents
<a name="API_NewBGPPeer_Contents"></a>

 ** addressFamily **   <a name="DX-Type-NewBGPPeer-addressFamily"></a>
The address family for the BGP peer.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** amazonAddress **   <a name="DX-Type-NewBGPPeer-amazonAddress"></a>
The IP address assigned to the Amazon interface.
Type: String
Required: No

 ** asn **   <a name="DX-Type-NewBGPPeer-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
Type: Integer
Required: No

 ** asnLong **   <a name="DX-Type-NewBGPPeer-asnLong"></a>
The long ASN for a new BGP peer. The valid range is from 1 to 4294967294.
Type: Long
Required: No

 ** authKey **   <a name="DX-Type-NewBGPPeer-authKey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
Type: String
Required: No

 ** customerAddress **   <a name="DX-Type-NewBGPPeer-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String
Required: No

## See Also
<a name="API_NewBGPPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/NewBGPPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/NewBGPPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/NewBGPPeer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
