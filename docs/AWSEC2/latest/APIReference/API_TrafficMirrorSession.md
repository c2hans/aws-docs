---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TrafficMirrorSession.html
---

# TrafficMirrorSession
<a name="API_TrafficMirrorSession"></a>

Describes a Traffic Mirror session.

## Contents
<a name="API_TrafficMirrorSession_Contents"></a>

 ** description **
The description of the Traffic Mirror session.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the Traffic Mirror session's network interface.
Type: String
Required: No

 ** ownerId **
The ID of the account that owns the Traffic Mirror session.
Type: String
Required: No

 ** packetLength **
The number of bytes in each packet to mirror. These are the bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet
Type: Integer
Required: No

 ** sessionNumber **
The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.
Valid values are 1-32766.
Type: Integer
Required: No

 ** TagSet.N **
The tags assigned to the Traffic Mirror session.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficMirrorFilterId **
The ID of the Traffic Mirror filter.
Type: String
Required: No

 ** trafficMirrorSessionId **
The ID for the Traffic Mirror session.
Type: String
Required: No

 ** trafficMirrorTargetId **
The ID of the Traffic Mirror target.
Type: String
Required: No

 ** virtualNetworkId **
The virtual network ID associated with the Traffic Mirror session.
Type: Integer
Required: No

## See Also
<a name="API_TrafficMirrorSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TrafficMirrorSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TrafficMirrorSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TrafficMirrorSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
