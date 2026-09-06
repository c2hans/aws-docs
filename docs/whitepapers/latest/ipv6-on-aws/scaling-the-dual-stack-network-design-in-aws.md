---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/scaling-the-dual-stack-network-design-in-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scaling the dual-stack network design in AWS
<a name="scaling-the-dual-stack-network-design-in-aws"></a>

## Elastic Load Balancing
<a name="elastic-load-balancing"></a>

 [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It supports the following types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers.

**Note**
 Application Load Balancers and Network Load Balancers are purpose-built load balancers replacing the functionality of Classic Load Balancers. You can review the benefits of using Application Load Balancers and Network Load Balancers over Classic Load Balancers in [Benefits of migrating from a Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html#application-load-balancer-benefits) (for Application Load Balancers) and [Benefits of migrating from a Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#network-load-balancer-benefits) (for Network Load Balancers). This whitepaper focuses only on Application Load Balancers and Network Load Balancers.

 Both load balancer types support internet-facing and internal load balancer schemes. You create both internet-facing and internal Application Load Balancers and Network Load Balancers when you have clients communicating using IPv4 and IPv6. You associate IPv6 CIDR blocks with your VPC and choose the subnets where you launch both internet-facing and internal Application Load Balancers or Network Load Balancers.

 To support IPv6, configure your Application Load Balancers or Network Load Balancers with the *dualstack* IP address type. This means that clients can communicate with the load balancers using both IPv4 and IPv6 addresses. In a dual-stack IP address type, the DNS name of the load balancer provides both IPv4 and IPv6 addresses, and creates A and AAAA records respectively.

 Application Load Balancers and Network Load Balancers can have both IPv4 or IPv6 targets. They communicate with their IPv4 targets using IPv4, and with the IPv6 targets using IPv6. When you configure the target groups, you cannot mix IPv4 and IPv6 targets. Also, note that with IPv6 targets, only the IP-type targets are supported and the IPv6 addresses need to be from the VPC IPv6 Space. You cannot point to IPv6 addresses from peered VPCs, on-premises, or that are reachable through the AWS Transit Gateway.

 The Application Load Balancer supports both HTTP and HTTPS listeners to support IPv6. The Network Load Balancer supports IPv6 on frontend connections for only TCP and TLS listeners.

 The following table outlines IPv6 support for both listeners and targets across currently existing ELB variants: Classic Load Balancers, Network Load Balancers, Application Load Balancers, and Gateway Load Balancers.

* Table - ELB IPv6 support *

|   |  Public IPv6 listeners  |  Private IPv6 listeners  |  IPv6 targets  |
| --- | --- | --- | --- |
|  Classic Load Balancers  |  No  |  No  |  No  |
|  Network Load Balancers  |  Yes\*  |  Yes  |  Yes  |
|  Application Load Balancers  |  Yes  |  Yes  |  Yes  |
|  Gateway Load Balancers  |  No  |  No  |  No  |

 **\**** TCP and TLS only*

 When you enable dual-stack mode on Network Load Balancers, and have the IPv4 targets, Network Load Balancing does the IPv6 to IPv4 conversion and therefore, the source IP is not preserved. However, the load balancer will add the IPv6 source IP to the proxy protocol (PPv2) header and send it to the targets. In this case, the targets need to parse the PPv2 header to obtain the actual source IP of the client.

![This is a diagram that displays a dual-stack IPv4/IPv6 internet-facing Network Load Balancer.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/dual-stack-ipv4ipv6-internet-facing-network-load-balancer.png)

 For the Network Load Balancer with IPv6 targets, source IP preservation is enabled for IPv6 connections to the dual stack load balancer with IPv6 targets. Client IP preservation has no effect on traffic converted from IPv6 to IPv4 or IPv4 to IPv6. The source IP of this type of traffic is always the private IP address of the Network Load Balancer. The following table summarizes the protocol – IPv4 or IPv6 – used by NLB clients and for target connectivity, and the Client IP visibility the targets have, based on client IP preservation settings:

 **Table 1 – NLB Client IP visibility**

|   |   |  IPv4 Client  |  IPv6 Client  |
| --- | --- | --- | --- |
|  Target Type / Protocol  |  Client IP Preservation  |  Client IP address visibility  |   |
|  Instance Type / IPv4  |  Enabled  |  Client IPv4  |  NLB private IPv4  |
|   |  Disabled  |  NLB private IPv4  |  NLB private IPv4  |
|  IP Type / IPv4 target group  |  Enabled  |  Client IPv4  |  NLB private IPv4  |
|   |  Disabled  |  NLB private IPv4  |  NLB private IPv4  |
|  IP Type / IPv6 target group  |  Enabled  |  NLB IPv6  |  Client IPv6  |
|   |  Disabled  |  NLB IPv6  |  NLB IPv6  |

## AWS Global Accelerator
<a name="aws-global-accelerator"></a>

AWS Global Accelerator supports IPv6 dual-stack implementations.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. CloudFront delivers the content through a worldwide network of data centers called edge locations or points of presence (PoPs) that are interconnected via the AWS backbone delivering ultra-low latency performance and high availability to your viewers (end users). It supports both IPv4 and IPv6 from viewer to CloudFront edge locations. This means that a viewer can establish either an IPv4 or IPv6 connection with an edge location.

 When a viewer makes an HTTP/HTTPS request over IPv6 to CloudFront, Amazon CloudFront automatically maps network conditions and intelligently routes the user’s traffic to the most performant AWS edge location to serve up cached or dynamic content. This edge location responds to the end user natively over IPv6. Clients receive the same content and same security, availability, performance, and scalability whether they are using IPv4 or IPv6.

 CloudFront communicates with origin server using IPv4 only. IPv6 origins are not supported. This applies to all types of origins for CloudFront distribution, including Amazon S3 buckets, AWS Elemental MediaStore containers, an AWS Elemental MediaPackage channel, and custom origins.

 Following is the request flow for life of an HTTP request in IPv6:

1.  An IPv6 viewer (for example, a browser) accesses your website or application and requests an object such as an image file from Amazon CloudFront distribution with FQDN `d111111abcdef8.cloudfront.net` over IPv6.

1.  The DNS query first lands at a recursive resolver. This resolver queries Amazon Route 53 for AAAA records for `d111111abcdef8.cloudfront.net`, as Route 53 is the authoritative name server for the `cloudfront.net` domain.

1.  Amazon Route 53 name servers are accessible over IPv4 or IPv6. DNS resolves AAAA query and routes the request to the CloudFront POP (edge location) that can best serve the request. Amazon CloudFront automatically maps network conditions and intelligently routes your user’s traffic to the most performant AWS edge location to serve up cached or dynamic content.

1.  The viewer connects to the respective CloudFront POP.

1.  In the POP, CloudFront checks its cache for the requested content. If the image file is in the cache, CloudFront returns them to the viewer. If the files are not in the cache, CloudFront compares the request with the specifications in your distribution and forwards the HTTP request to your origin server over IPv4 for the image file.

1.  The origin server responds the image file request back to the edge location.

1.  As soon as the first byte arrives from the origin, CloudFront begins to respond the files to the viewer. CloudFront also adds the image file to the cache in the edge location based on the cache headers.

![This is a diagram that illustrates Amazon CloudFront dual-stack IPv4/IPv6 support.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/amazon-cloudfront-dual-stack-ipv4ipv6-support.png)
