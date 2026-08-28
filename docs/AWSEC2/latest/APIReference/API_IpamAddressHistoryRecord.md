---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamAddressHistoryRecord.html
---

# IpamAddressHistoryRecord
<a name="API_IpamAddressHistoryRecord"></a>

The historical record of a CIDR within an IPAM scope. For more information, see [View the history of IP addresses](https://docs.aws.amazon.com/vpc/latest/ipam/view-history-cidr-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Contents
<a name="API_IpamAddressHistoryRecord_Contents"></a>

 ** resourceCidr **
The CIDR of the resource.
Type: String
Required: No

 ** resourceComplianceStatus **
The compliance status of a resource. For more information on compliance statuses, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `compliant | noncompliant | unmanaged | ignored`
Required: No

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceName **
The name of the resource.
Type: String
Required: No

 ** resourceOverlapStatus **
The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `overlapping | nonoverlapping | ignored`
Required: No

 ** resourceOwnerId **
The ID of the resource owner.
Type: String
Required: No

 ** resourceRegion **
The AWS Region of the resource.
Type: String
Required: No

 ** resourceType **
The type of the resource.
Type: String
Valid Values: `eip | vpc | subnet | network-interface | instance`
Required: No

 ** sampledEndTime **
Sampled end time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the end time may have occurred before this specific time.
Type: Timestamp
Required: No

 ** sampledStartTime **
Sampled start time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the start time may have occurred before this specific time.
Type: Timestamp
Required: No

 ** vpcId **
The VPC ID of the resource.
Type: String
Required: No

## See Also
<a name="API_IpamAddressHistoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamAddressHistoryRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamAddressHistoryRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamAddressHistoryRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
