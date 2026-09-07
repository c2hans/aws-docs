---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/creating-highly-available-endpoint-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Creating highly-available endpoint services
<a name="creating-highly-available-endpoint-services"></a>

 The creation of VPC endpoint services goes through four stages, which we develop here. The generation of a DNS hostname, the use of private IP address, the deployment of the endpoint, and its configuration.

 In the following figure, the account owner of VPC B is a service provider and has a service running on instances in subnet B. The owner of VPC B has a service endpoint (vpce-svc-1234) with an associated Network Load Balancer that points to the instances in subnet B as targets. Instances in subnet A of VPC A use an interface endpoint to access the services in subnet B.

![A diagram that depicts detailed Amazon VPC-to-VPC connectivity with AWS PrivateLink.](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/connectivity-with-privatelink.jpeg)

 When an interface endpoint is created, endpoint-specific Domain Name System (DNS) hostnames are generated that can be used to communicate with the service. After creating the endpoint, requests can be submitted to the provider’s service through one of the following methods:

## Endpoint-specific Regional DNS hostname
<a name="endpoint-specific-regional-dns-hostname"></a>

Let's assume there is a network disruption in Availability Zone B, which leads to a backend health check for an Availability Zone B record failure, so now the VPCE-Regional DNS records only give out Availability Zone A records. Customers generate an endpoint-specific DNS hostname which includes all zonal DNS hostnames generated for the interface endpoint. The hostname includes a unique endpoint identifier, service identifier, the Region, and `vpce.amazonaws.com` in its name, for example:

```
vpce-0fe5b17a0707d6abc-29p5708s.ec2.us-east-1.vpce.amazonaws.com
```

## Zonal-specific DNS hostname
<a name="zonal-specific-dns-hostname"></a>

 Customers generate a zonal specific DNS hostname for each Availability Zone in which the endpoint is available. The hostname includes the Availability Zone in its name, for example:

```
vpce-0fe5b17a0707d6abc-29p5708s-us-east-1a.ec2.us-east-1.vpce.amazonaws.com
```

## Private DNS hostname
<a name="private-dns-hostname"></a>

 If enabled, customers can use a private DNS hostname to alias the automatically- created zonal-specific or regional-specific DNS hostnames into a friendly hostname such as:

```
myservice.example.com
```

## Private IP address of the endpoint network interface
<a name="private-ip-address-of-the-endpoint-network-interface"></a>

 The private IP address of the endpoint network interface in the VPC is directly reachable to access the service in and across Availability Zones, in the same way the zonal-specific DNS hostname is.

 Service providers that use zonal DNS hostnames to access the service can help achieve high availability by enabling cross-zone load balancing. Cross-zone load balancing enables the load balancer to distribute traffic across the registered targets in all enabled Availability Zones. Regional data transfer charges may apply to a service provider’s account when they enable cross-zone load balancing, as data could potentially transfer between Availability Zones.

 In the following figure, the owner of VPC B is the service provider, and has configured a Network Load Balancer with targets in two different Availability Zones. The service consumer (VPC A) has created interface endpoints in the same two Availability Zones in their Amazon VPC. Requests to the service from instances in VPC A can use either interface endpoint. The DNS name resolution of the Endpoint Specific Regional DNS Hostname will alternate between the two IP addresses. NLB attribute: Client routing policy (DNS Record) will not influence the DNS name resolution of the Endpoint Specific Regional DNS Hostname.

![A diagram depicting round-robin DNS load balancing.](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/images/round-robin-dns.jpeg)
