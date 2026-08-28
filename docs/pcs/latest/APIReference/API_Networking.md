---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_Networking.html
---

# Networking
<a name="API_Networking"></a>

The networking configuration for the cluster's control plane.

## Contents
<a name="API_Networking_Contents"></a>

 ** networkType **   <a name="PCS-Type-Networking-networkType"></a>
The IP address version the cluster uses. The default is `IPV4`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** securityGroupIds **   <a name="PCS-Type-Networking-securityGroupIds"></a>
The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.
The following rules are required:
+ Inbound rule 1
  + Protocol: All
  + Ports: All
  + Source: Self
+ Outbound rule 1
  + Protocol: All
  + Ports: All
  + Destination: 0.0.0.0/0 (IPv4) or ::/0 (IPv6)
+ Outbound rule 2
  + Protocol: All
  + Ports: All
  + Destination: Self
Type: Array of strings
Pattern: `sg-\w{8,17}`
Required: No

 ** subnetIds **   <a name="PCS-Type-Networking-subnetIds"></a>
The ID of the subnet where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources. The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone.
 Example: `subnet-abcd1234`
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `subnet-\w{8,17}`
Required: No

## See Also
<a name="API_Networking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/Networking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/Networking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/Networking)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
