---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAclEntry.html
---

# CreateNetworkAclEntry
<a name="API_CreateNetworkAclEntry"></a>

Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules.

We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules.

After you add an entry, you can't modify it; you must either replace it, or create an entry and delete the old one.

For more information about network ACLs, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateNetworkAclEntry_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrBlock**
The IPv4 network range to allow or deny, in CIDR notation (for example `172.16.0.0/24`). We modify the specified CIDR block to its canonical form; for example, if you specify `100.68.0.18/18`, we modify it to `100.68.0.0/18`.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Egress**
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).
Type: Boolean
Required: Yes

 **Icmp**
ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.
Type: [IcmpTypeCode](API_IcmpTypeCode.md) object
Required: No

 **Ipv6CidrBlock**
The IPv6 network range to allow or deny, in CIDR notation (for example `2001:db8:1234:1a00::/64`).
Type: String
Required: No

 **NetworkAclId**
The ID of the network ACL.
Type: String
Required: Yes

 **PortRange**
TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).
Type: [PortRange](API_PortRange.md) object
Required: No

 **Protocol**
The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), "17" (UDP), or "1" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.
Type: String
Required: Yes

 **RuleAction**
Indicates whether to allow or deny the traffic that matches the rule.
Type: String
Valid Values: `allow | deny`
Required: Yes

 **RuleNumber**
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.
Type: Integer
Required: Yes

## Response Elements
<a name="API_CreateNetworkAclEntry_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_CreateNetworkAclEntry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateNetworkAclEntry_Examples"></a>

### Example 1
<a name="API_CreateNetworkAclEntry_Example_1"></a>

This example creates an entry with rule number 110 in the specified network ACL. The rule allows ingress traffic from any IPv4 address (`0.0.0.0/0`) on UDP port 53.

#### Sample Request
<a name="API_CreateNetworkAclEntry_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkAclEntry
&NetworkAclId=acl-2cb85d45
&RuleNumber=110
&Protocol="17"
&RuleAction=allow
&Egress=false
&CidrBlock=0.0.0.0/0
&PortRange.From=53
&PortRange.To=53
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkAclEntry_Example_1_Response"></a>

```
<CreateNetworkAclEntryResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</CreateNetworkAclEntryResponse>
```

### Example 2
<a name="API_CreateNetworkAclEntry_Example_2"></a>

This example creates an entry with rule number 120 in the specified network ACL. The rule allows ingress traffic from any IPv6 address (`::/0`) on TCP port 80.

#### Sample Request
<a name="API_CreateNetworkAclEntry_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkAclEntry
&NetworkAclId=acl-2cb85d45
&RuleNumber=120
&Protocol="6"
&RuleAction=allow
&Egress=false
&Ipv6CidrBlock=::/0
&PortRange.From=80
&PortRange.To=80
&AUTHPARAMS
```

## See Also
<a name="API_CreateNetworkAclEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateNetworkAclEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateNetworkAclEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
