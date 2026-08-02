---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_planning_network_topology_ha_conn_users.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP01 Use highly available network connectivity for your workload public endpoints
<a name="rel_planning_network_topology_ha_conn_users"></a>

 These endpoints and the routing to them must be highly available. To achieve this, use highly available DNS, content delivery networks (CDNs), API Gateway, load balancing, or reverse proxies.

 Amazon Route 53, AWS Global Accelerator, Amazon CloudFront, Amazon API Gateway, and Elastic Load Balancing (ELB) all provide highly available public endpoints. You might also choose to evaluate AWS Marketplace software appliances for load balancing and proxying.

 Consumers of the service your workload provides, whether they are end-users or other services, make requests on these service endpoints. Several AWS resources are available to enable you to provide highly available endpoints.

 Elastic Load Balancing provides load balancing across Availability Zones, performs Layer 4 (TCP) or Layer 7 (http/https) routing, integrates with AWS WAF, and integrates with AWS Auto Scaling to help create a self-healing infrastructure and absorb increases in traffic while releasing resources when traffic decreases.

 Amazon Route 53 is a scalable and highly available Domain Name System (DNS) service that connects user requests to infrastructure running in AWS such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets–and can also be used to route users to infrastructure outside of AWS.

 AWS Global Accelerator is a network layer service that you can use to direct traffic to optimal endpoints over the AWS global network.

 Distributed Denial of Service (DDoS) attacks risk shutting out legitimate traffic and lowering availability for your users. AWS Shield provides automatic protection against these attacks at no extra cost for AWS service endpoints on your workload. You can augment these features with virtual appliances from APN Partners and the AWS Marketplace to meet your needs.

 **Common anti-patterns:**
+  Using public internet addresses on instances or containers and managing the connectivity to them via DNS.
+  Using Internet Protocol addresses instead of domain names for locating services.
+  Providing content (web pages, static assets, media files) to a large geographic area and not using a content delivery network.

 **Benefits of establishing this best practice:** By implementing highly available services in your workload, you know that your workload will be available to your users.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Ensure that you have highly available connectivity for users of the workload Amazon Route 53, AWS Global Accelerator, Amazon CloudFront, Amazon API Gateway, and Elastic Load Balancing (ELB) all provide highly available public facing endpoints. You may also choose to evaluate AWS Marketplace software appliances for load-balancing and proxying.
+  Ensure that you have a highly available connection to your users.
+  Ensure that you are using a highly available DNS to manage the domain names of your application endpoints.
  +  If your users access your application via the internet, use service API operations to confirm the correct usage of Internet Gateways. Also confirm that the route tables entries for the subnets hosting your application endpoints are correct.
    +  [DescribeInternetGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInternetGateways.html)
    +  [DescribeRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html)
+  Ensure that you are using a highly available reverse proxy or load balancer in front of your application.
  +  If your users access your application via your on-premises environment, ensure that your connectivity between AWS and your on-premises environment is highly available.
  +  Use Route 53 to manage your domain names.
    +  [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
  +  Use a third-party DNS provider that meets your requirements.
  +  Use Elastic Load Balancing.
    +  [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
  +  Use an AWS Marketplace appliance that meets your requirements.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)
+  [Amazon Virtual Private Cloud Connectivity Options Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html)
+  [Multiple data center HA network connectivity](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/)
+  [Using the Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency_toolkit.html)
+  [VPC Endpoints and VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)
+  [What Is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
+  [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+  [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+  [What is Amazon Route 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
+  [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
+  [Working with Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)

 **Related videos:**
+  [AWS re:Invent 2018: Advanced VPC Design and New Capabilities for Amazon VPC (NET303)](https://youtu.be/fnxXNZdf6ew)
+  [AWS re:Invent 2019: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)](https://youtu.be/9Nikqn_02Oc)
