---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key components of an AWS web hosting architecture
<a name="key-components-of-an-aws-web-hosting-architecture"></a>

The following sections outline some of the key components of a web hosting architecture deployed in the AWS Cloud, and explain how they differ from a traditional web hosting architecture.

## Network management
<a name="network-management"></a>

 In the AWS Cloud, the ability to segment your network from that of other customers enables a more secure and scalable architecture. While security groups provide host-level security (see the [Host Security](#host-security) section), [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) enables you to launch resources in a logically isolated and virtual network that you define.

 Amazon VPC is a service that gives you full control over the details of your networking setup in AWS. Examples of this control include creating public-facing subnets for web servers, and private subnets with no internet access for your databases. Additionally, Amazon VPC enables you to create hybrid architectures by using hardware virtual private networks (VPNs), and use the AWS Cloud as an extension of your own data center.

 Amazon VPC also includes [IPv6](https://en.wikipedia.org/wiki/IPv6) support in addition to traditional [IPv4](https://en.wikipedia.org/wiki/IPv4) support for your network.

## Content delivery
<a name="content-delivery"></a>

When your web traffic is geo-dispersed, it’s not always feasible and certainly not cost effective to replicate your entire infrastructure across the globe. A [Content Delivery Network](https://aws.amazon.com/caching/cdn/) (CDN) provides you the ability to utilize its global network of edge locations to deliver a cached copy of web content such as videos, webpages, images and so on to your customers. To reduce response time, the CDN utilizes the nearest edge location to the customer or originating request location to reduce the response time. Throughput is dramatically increased given that the web assets are delivered from cache. For dynamic data, many CDNs can be configured to retrieve data from the origin servers.

You can use CloudFront to deliver your website, including dynamic, static, and streaming content, using a global network of edge locations. CloudFront automatically routes requests for your content to the nearest edge location, so content is delivered with the best possible performance. CloudFront is optimized to work with other AWS services, like [Amazon S3](https://aws.amazon.com/s3/) and [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2). CloudFront also works seamlessly with any origin server that is not an AWS origin server, which stores the original, definitive versions of your files.

 Like other AWS services, there are no contracts or monthly commitments for using CloudFront – you pay only for as much or as little content as you actually deliver through the service.

Additionally, any existing solutions for edge caching in your web application infrastructure should work well in the AWS Cloud.

## Managing public DNS
<a name="managing-public-dns"></a>

Moving a web application to the AWS Cloud requires some [Domain Name System](https://aws.amazon.com/route53/what-is-dns/) (DNS) changes. To help you manage DNS routing, AWS provides [Amazon Route 53](https://aws.amazon.com/route53/), a highly available and scalable cloud DNS web service. Route 53 is designed to give developers and businesses an extremely reliable and cost-effective way to route end users to internet applications by translating names such as “www.example.com” into numeric IP addresses such as 192.0.2.1, that computers use to connect to each other. Route 53 is fully compliant with [IPv6](https://en.wikipedia.org/wiki/IPv6) as well.

## Host security
<a name="host-security"></a>

In addition to inbound network traffic filtering at the edge, AWS also recommends web applications apply network traffic filtering at the host level. [Amazon EC2](https://aws.amazon.com/ec2/) provides a feature named *security groups*. A security group is analogous to an inbound network firewall, for which you can specify the protocols, ports, and source IP ranges that are allowed to reach your EC2 instances.

You can assign one or more security groups to each EC2 instance. Each security group allows appropriate traffic in to each instance. Security groups can be configured so that only specific subnets, IP addresses, and resources have access to an EC2 instance. Alternatively, they can reference other security groups to limit access to EC2 instances that are in specific groups.

In the AWS web hosting architecture in Figure 3, the security group for the web server cluster might allow access only from the web-layer Load Balancer and only over TCP on ports 80 and 443 (HTTP and HTTPS). The application server security group, on the other hand, might allow access only from the application-layer Load Balancer. In this model, your support engineers would also need to access the EC2 instances, what can be achieved with [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html). For a deeper discussion on security, see [AWS Cloud Security](https://aws.amazon.com/security/), which contains security bulletins, certification information, and security whitepapers that explain the security capabilities of AWS.

## Load balancing across clusters
<a name="load-balancing-across-clusters"></a>

 Hardware load balancers are a common network appliance used in traditional web application architectures. AWS provides this capability through the [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) service. ELB automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, IP addresses, [AWS Lambda](https://aws.amazon.com/lambda/) functions, and virtual appliances. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones. Elastic Load Balancing offers four types of load balancers that all feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant.

## Finding other hosts and services
<a name="finding-other-hosts-and-services"></a>

In the traditional web hosting architecture, most of your hosts have static IP addresses. In the AWS Cloud, most of your hosts have dynamic IP addresses. Although every EC2 instance can have both public and private DNS entries and will be addressable over the internet, the DNS entries and the IP addresses are assigned dynamically when you launch the instance. They cannot be manually assigned. Static IP addresses (Elastic IP addresses in AWS terminology) can be assigned to running instances after they are launched. You should use Elastic IP addresses for instances and services that require consistent endpoints, such as primary databases, central file servers, and EC2-hosted load balancers.

## Caching within the web application
<a name="caching-within-the-web-application"></a>

 In-memory application caches can reduce load on services and improve performance and scalability on the database tier by caching frequently used information. [Amazon ElastiCache](https://aws.amazon.com/elasticache/) is a web service that makes it easy to deploy, operate, and scale an in-memory cache in the cloud. You can configure the in-memory cache you create to automatically scale with load and to automatically replace failed nodes. ElastiCache is protocol-compliant with Memcached and Redis, which simplifies migration from your current on-premises solution.
