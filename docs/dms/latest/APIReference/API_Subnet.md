---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Subnet.html
---

# Subnet
<a name="API_Subnet"></a>

In response to a request by the `DescribeReplicationSubnetGroups` operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

## Contents
<a name="API_Subnet_Contents"></a>

 ** SubnetAvailabilityZone **   <a name="DMS-Type-Subnet-SubnetAvailabilityZone"></a>
The Availability Zone of the subnet.
Type: [AvailabilityZone](API_AvailabilityZone.md) object
Required: No

 ** SubnetIdentifier **   <a name="DMS-Type-Subnet-SubnetIdentifier"></a>
The subnet identifier.
Type: String
Required: No

 ** SubnetStatus **   <a name="DMS-Type-Subnet-SubnetStatus"></a>
The status of the subnet.
Type: String
Required: No

## See Also
<a name="API_Subnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Subnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Subnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Subnet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
