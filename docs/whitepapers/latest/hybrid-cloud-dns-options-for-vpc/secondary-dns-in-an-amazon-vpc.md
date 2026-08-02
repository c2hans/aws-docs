---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/secondary-dns-in-an-amazon-vpc.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secondary DNS in an Amazon VPC
<a name="secondary-dns-in-an-amazon-vpc"></a>

 Alternatively, you might decide to deploy and manage additional DNS infrastructure running on EC2 instances to handle DNS requests either from VPCs or on-premises, where you can still benefit from using AWS Managed Services.

 This approach uses Route 53 private hosted zones with AWS Lambda and [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) to mirror on-premises DNS zones. This can then be natively resolved from within a VPC without conditional forwarding, and without a real-time dependency on on-premises DNS servers.

 For the full solution, refer to [https://aws.amazon.com/blogs/compute/powering-secondary-dns-in-a-vpc-using-aws-lambda-and-amazon-route-53-private-hosted-zones/](https://aws.amazon.com/blogs/compute/powering-secondary-dns-in-a-vpc-using-aws-lambda-and-amazon-route-53-private-hosted-zones/) on the AWS Compute blog.

 The following table outlines this solution:

 *Table 2 – Solution highlights – secondary DNS in an Amazon VPC *

|   Use case   |  Advantages  |   Limitations   |
| --- | --- | --- |
| Customers that cannot use the native Route 53 Resolver forwarding features <br />Customers that don’t want to build or manage conditional forwarder instances <br />Customers that do not have in-house DevOps expertise <br /> Infrequently changing DNS environment  | Low management overhead <br />Low operational cost <br />Highly resilient DNS infrastructure <br />Low possibility for instances to breach the PPS per network interface limit  | On-premises instances can’t query Route 53 Resolver directly for Amazon EC2 hostnames without creating a forwarding target <br />Works well only when on- premises DNS server records must be replicated to Route 53 <br />Requires on-premises DNS server to support full zone transfer query <br />Requires working with the Route 53 API limits  |

 The following diagram represents a sample architecture utilizing a secondary DNS within an Amazon VPC.

![A diagram depciting secondary DNS running on Route 53 private hosted zones.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/secondary-dns.png)

1.  CloudWatch Events invokes a Lambda function. The scheduled event is configured based on a JSON string that is passed to the Lambda function that sets a number of parameters, including the DNS domain, source DNS server, and Route 53 zone ID. This configuration lets you reuse a single Lambda function for multiple zones.

1.  A new network interface is created in the VPC’s subnets and attached to the Lambda function. This allows the function to access any internal network resources based on the security group that you defined.

1.  The Lambda function transfers the source DNS zone from the IP address specified in the JSON parameters. Configure DNS servers to allow full zone transfers, which happen over TCP and UDP port 53.

1.  The Route 53 DNS zone is retrieved using the AWS API.

1.  The two zone files are compared, and then the resulting differences are returned as a set of actions to be performed using Route 53.

1.  Updates to the Route 53 zone are made using the AWS API, and then the Start of Authority (SOA) is updated to match the source version.

 There are several benefits to using this approach. Aside from the initial solution setup, there is little management overhead after the environment is set up as the solution continues working without any manual intervention. Also, there is no client-side setup because the DHCP options that you set configure each instance to use Route 53 Resolver (aka `AmazonProvidedDNS`) by default.

 This solution can be one of the more scalable hybrid DNS solutions in a VPC because queries for any domain go directly to Route 53 Resolver from each instance and then to the Amazon Route 53 infrastructure. This ensures that each instance uses its own PPS per network interface limit. There is also no correlation and impact of implementing this solution in one or more VPCs as you choose to associate the Route 53 hosted zone with multiple VPCs. The possibility of failure of a DNS component is lower because of the highly available and reliable Amazon Route 53 infrastructure. Note, however, that there is a hard limit of 1,000 private hosted zone associations.

 The main disadvantage of this solution is that it requires full zone transfer query so it isn’t appropriate for customers that run DNS servers that don’t support full zone transfer queries. Also, because this solution involves working with the Route 53 APIs, you must stay within the [Route 53 API limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-requests).

 This solution does not provide a method for resolving EC2 records from on premises directly.
