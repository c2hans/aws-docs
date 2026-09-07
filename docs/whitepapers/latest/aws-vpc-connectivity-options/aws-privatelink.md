---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html
---

# AWS PrivateLink
<a name="aws-privatelink"></a>

 AWS PrivateLink enables you to connect to some AWS services, services hosted by other AWS accounts (referred to as *endpoint services*), and supported AWS Marketplace partner services, via private IP addresses in your VPC. The interface endpoints are created directly inside of your VPC, using elastic network interfaces and IP addresses in your VPC’s subnets. That means that VPC Security Groups can be used to manage access to the endpoints.

![A diagram showing AWS Privatelink.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-privatelink.png)

We recommend this approach if you want to use services offered by another VPC securely within an AWS network, using private IP addresses. Alternatively, AWS PrivateLink is a good solution when the VPCs have overlapped IP addresses.

 AWS PrivateLink fully supports IPv6, but both of the destination VPCs, VPC Subnets, the Network Load Balancer, and the DNS names have to be enabled or modified to use dual-stack. After these pre-requisites are met, IPv6 can be enabled at the service configuration for the endpoint.

## Access controls to AWS PrivateLink
<a name="access-controls-to-privatelink"></a>

 The interface endpoints are created directly inside of your VPC by using elastic network interfaces and IP addresses in your VPC’s subnets. That means that VPC Security Groups can be used to manage network access to the endpoints.

 When you create an interface endpoint or a gateway endpoint, you can also attach an endpoint policy. The endpoint policy controls which AWS principals (AWS accounts, IAM users, and roles) can use the VPC endpoint to access the endpoint service.

 You cannot attach more than one policy to an endpoint. However, you can modify an endpoint policy at any time.

 An endpoint policy does not override or replace IAM user policies or service-specific policies (such as Amazon S3 bucket policies). If you're using an interface endpoint to connect to Amazon S3, you can also use Amazon S3 bucket policies to control access to buckets from specific endpoints or specific VPCs.

## Additional resources
<a name="additional-resources-13"></a>
+  [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html)
+  [VPC endpoint services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html)
+  [Blog post: Expedite your IPv6 adoption with PrivateLink services and endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/)
+  [Blog post: Connecting Networks with Overlapping IP Ranges](https://aws.amazon.com/blogs/networking-and-content-delivery/connecting-networks-with-overlapping-ip-ranges/)
+  [AWS PrivateLink Partners](https://aws.amazon.com/privatelink/partners/)
