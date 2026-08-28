---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_NetworkingRequest.html
---

# NetworkingRequest
<a name="API_NetworkingRequest"></a>

The networking configuration for the cluster's control plane.

## Contents
<a name="API_NetworkingRequest_Contents"></a>

 ** networkType **   <a name="PCS-Type-NetworkingRequest-networkType"></a>
The IP address version the cluster uses. The default is `IPV4`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** securityGroupIds **   <a name="PCS-Type-NetworkingRequest-securityGroupIds"></a>
A list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.
Type: Array of strings
Pattern: `sg-\w{8,17}`
Required: No

 ** subnetIds **   <a name="PCS-Type-NetworkingRequest-subnetIds"></a>
The list of subnet IDs where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources. Subnet IDs have the form `subnet-0123456789abcdef0`.
Subnets can't be in AWS Outposts, AWS Wavelength or an AWS Local Zone.
 AWS PCS currently supports only 1 subnet in this list.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `subnet-\w{8,17}`
Required: No

## See Also
<a name="API_NetworkingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/NetworkingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/NetworkingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/NetworkingRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
