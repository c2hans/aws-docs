---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/additional-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Additional considerations
<a name="additional-considerations"></a>

 This section describes additional aspects that you should consider on top of the previously presented solutions. For example, DNS logging, or DNS server resiliency.

## DNS logging
<a name="dns-logging"></a>

 DNS logging refers to logging specific DNS query from individual host. Typically, these logs are stored for security forensics and compliance. [Amazon GuardDuty](https://aws.amazon.com/guardduty/) provides machine learning (ML)-based forensics and anomaly detection on recursive queries originating from local VPC resources. If raw historical logging is not required, GuardDuty might satisfy your requirements without any additional heavy lifting.

 Route 53 provides query logs for public hosted zones. If customers require logging for Private Hosted Zones and queries that originate from resources within a VPC, they have several options while still following the Well-Architected Framework and DNS best practices.

 Centralized query logging, distributed (on-instance) query logging, and a hybrid approach to log a percentage of queries based on user-defined domain allowlisting, are three of the most popular and scalable methods for query logging currently available.

### Centralized query logging
<a name="centralized-query-logging"></a>

 Query logging is accomplished in a centralized fashion when all queries are forwarded to a resolver that is not the Route 53 Resolver (Amazon-provided DNS). This resolver can be local to the VPC, such as several instances running unbound, or an on-premises resource over Direct Connect, VPN, or the Internet Gateway. The latter adds additional latency and dependencies outside of the VPC, and is typically not recommended for that reason. As with any centralized or distributed system, it comes with pros and cons.

 Centralization of query logs allows for easy aggregation and a single plane of glass to view and parse DNS client queries. With centralization, additional attention needs be directed at the scale of the instances acting as resolvers and number of queries that are directed at any single instance. These instances become single points of failure and can become a barrier due to DNS packets per second limits. Each EC2 instance is limited to 1024 packets per second for DNS queries toward the Route 53 Resolver. If the requests being sent to the customer managed instance-based DNS resolvers are not distributed effectively and are not implementing caching techniques, with high volume the DNS instances may exceed the 1024 per instance packet per second limit to the Route 53 Resolver DNS resolver with the VPC.

### Distributed query logging
<a name="distributed-query-logging"></a>

 Another approach is logging DNS queries in a distributed fashion on instance. This is accomplished by running unbound or another logging capable resolver or forwarder on each instance that requires logging. With the distributed model of logging DNS queries, each instance runs a local resolver in order to capture all DNS queries locally on each instance. These logs can then be aggregated upstream to a centralized [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket for historical collection and centralized parsing. Depending on the aggregation process, this might create a delayed ability for centralized parsing and forensics, but removes any single points of failure and reduces the overall blast radius of any given upstream instance-based resolver failure. If On-Demand Instance parsing is required, the delivery window can be shorted. Depending on your operational model, you might want to allow on-box forensics or external access, so the logging delivery schedule should be considered.

 VPC traffic mirroring is an alternative off-instance distributed logging mechanism that can be achieved for supported instance types. At this time, all [AWS Nitro](https://aws.amazon.com/ec2/nitro/)-based instances support VPC traffic mirroring. By enabling traffic mirroring for Transmission Control Protocol (TCP)- and User Diagram Protocol (UDP)-based traffic on port 53 on individual instance ENIs, you have the ability to capture DNS requests in [pcap](https://en.wikipedia.org/wiki/Pcap) format. Traffic mirroring for DNS logs shares similar availability and scalability constructs as other distributed methods, but increases simplicity and flexibility because it does not require the application or [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) to incorporate any additional DNS logic. A traffic mirroring session can be attached and detached to instance ENIs as needed. Traffic mirroring is priced per elastic network interface that traffic mirroring is enabled on, and the customer is responsible for configuring and managing the traffic mirror target.

 For more information on Amazon VPC traffic mirroring, refer to [Traffic Mirroring concepts](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html).

### Hybrid query logging
<a name="hybrid-query-logging"></a>

 The third option is a hybrid approach that allows more granularity on what queries are filtered. Companies that are able to define “trusted” zones and “untrusted” zones might prefer this approach.

 *Trusted zones* are approved by the organization and might not require logging. Anything unapproved falls under the *untrusted* category, to be logged and possibly acted upon, such as a deny list of the response. For example, any zones that are owned and operated by the organization and VPC local resources are trusted, and everything else should be logged and controlled. This hybrid approach is now possible with the release of the Amazon Route 53 Resolver service, because of its ability to provide conditional forwarding rules by zone. In this approach, all local VPC resources resolve to Route 53 Resolver as usual, but when a query is made to an untrusted zone that matches an Amazon Route 53 Resolver conditional forwarding rule, it’s forwarded to a specified instance or on-premises-based resolver such as the previously mentioned centralized DNS resolver. This approach does not require any modifications on the instance, and removes any single points of failure for all trusted zones.

## Custom EC2 DNS Resolver
<a name="custom-ec2-dns-resolver"></a>

 You can choose to host your own custom DNS resolver on Amazon EC2 that uses public DNS servers to perform recursive public DNS resolution instead of using Route 53 Resolver. This is a good choice because of the nature of the application and the ability to have more control and flexibility over the DNS environment. You could also do this if the PPS per network interface limit is a hindrance to your ability to scale and none of the solutions discussed thus far suit your needs.

 This whitepaper does not describe the details of architecting such a solution, but we point out some caveats that will help you plan better in such a scenario. The following diagram illustrates an approach to a hybrid VPC DNS setup where you have your own DNS resolver on Amazon EC2.

![A diagram depicting Amazon EC2 DNS instances with segregated resolver and forwarder.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/segregated.jpeg)

1.  DNS queries for internal EC2 names and Route 53 PHZs are forwarded to Route 53 Resolver.

1.  DNS queries bound for on-premises servers are conditionally forwarded to on-premises DNS servers.

1.  DNS queries for public domains are conditionally forwarded to the custom DNS resolver in the public subnet. The resolver then recursively resolves public domains using the latest root hints available from the Internet Assigned Number Authority (IANA).

 For security reasons, we recommend that the conditional forwarder instance that requires connectivity to on-premises sits separately in a private subnet of the VPC. Because the custom DNS resolver must be able to query public DNS servers, it runs in its own public subnet of the VPC.

 Ideally, you would have security group rules on the EC2 instance running the custom DNS resolver, but if this custom DNS resolver has high rates of querying out to the internet, then there is a possibility that you will hit connection tracking limits, as discussed in the [*Connection tracking*](key-concepts.md#connection-tracking) section. To avoid this scenario, avoid connection tracking by itself by opening up all ports, TCP and UDP, to the whole world at the security group level, both inbound and outbound.

 Because this grants permissive rules to the instance-level security group, you will have to handle the security of the instance at a different layer. At the least, we recommend you control the traffic entering into the entire public subnet by using [*Network Access Control Lists*](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) (network ACLs), which thereby restricts access to the instance. Alternatively, you could use application-level control mechanisms such as access-control provided by a DNS resolver such as unbound.

 Custom DNS resolvers might develop a reputation upstream on the internet. If the instance is assigned a dynamic public IP address that belonged to another customer and previously earned a bad reputation, requests upstream could be throttled or even blocked. To avoid being throttled or blocked, consider assigning Elastic IP addresses to these resolver instances. This provides these IP addresses that talk to the upstream servers with the opportunity to build a good reputation over time that can be owned and maintained. Scaling concerns can be mitigated through the use of a DNS server fleet sitting behind a Network Load Balancer (NLB) that is configured with both TCP and UDP listener on port 53.

## Microsoft Windows instances
<a name="microsoft-windows-instances"></a>

 Typically, Microsoft Windows instances are joined using Active Directory Domain Services (AD DS). In scenarios where you use the Amazon VPC DHCP options set, unlike the Linux resolver, you can set the full set of four DNS servers. You can set the DNS servers independently from the DHCP supplied IP address similar to the supersede option discussed earlier. This can be accomplished using Active Directory Group Policy or configuration management tools such as [Amazon EC2 Run Command](https://aws.amazon.com/ec2/run-command/) or [AWS OpsWorks for Chef Automate](https://aws.amazon.com/opsworks/chefautomate/) mentioned earlier. In addition, the Windows DNS client also enables you to cache recently resolved queries, which reduces the overall demand on the primary DNS server.

 The Windows DNS client service is designed to prompt a dynamic update from the DNS server if a change is made to its IP address information. When prompted, the DNS server updates the host record IP address for that computer (according to RFC 2136).

 Microsoft DNS provides support for dynamic updates and this is enabled by default in any Active Directory integrated DNS zone. When you use a lightweight forwarder such as unbound for Windows instances, note that there isn’t any support for these dynamic updates, and it can’t support RFC 2126. If you want to do this, you should use the Microsoft DNS server as a primary for these instances.

## Unbound – additional options
<a name="unbound-additional-options"></a>

 Unbound caches the results for subsequent queries until the time to live (TTL) expires, after which it forwards the request. By enabling the *prefetch* option in unbound, you can ensure that frequently used records are pre-fetched before they expire to keep the cache up-to-date. Also, if the on-premises DNS server is not available when the cache expires, unbound returns `SERVFAIL`. To protect yourself against such a situation, you can enable the serve-expired option to serve old responses from the cache with a TTL of zero in the response without waiting for the actual resolution to finish. After the resolution is completed, the response is cached for subsequent use.

## DNS forwarder – forward first
<a name="dns-forwarder-forward-first"></a>

 Some DNS servers (notably `BIND`) include a *forward first* option enabled by default, which causes the server to query the forwarder first and, if there is no response, to recursively retry the internet DNS servers. For private DNS domains in this scenario, the internet DNS servers return an authoritative `NXDOMAIN`, which is a non-existent internet or intranet domain name. They might also return the public address if you’re using split horizon DNS for public zones, which is used to provided different answers for private vs. public IP addresses. Therefore, it is critical to specify the `forward only` option, which specifies that retries are made against the forwarders, which means that you avoid ever seeing the response from public name servers. The unbound DNS server has the `forward first` option disabled by default.

## DNS server resiliency
<a name="dns-server-resiliency"></a>

 The solutions in this whitepaper are intended to provide high availability in the event that there is an issue with your primary DNS server. However, there are factors that can prevent or delay this failover from occurring. These factors include, but are not limited to, the timeout value in `resolv.conf`, configuration issues with the superseded DNS, or incorrect DHCP options settings. In some cases, these factors could impact the availability of applications that are dependent on name resolution. There are a few simple approaches to ensure the resilience of your forwarders in case there is an issue with the underlying hardware or instance software. While these approaches don’t eliminate the need for Well-Architected design, they can help you increase the overall resiliency of your solution.

### EC2 instance recovery
<a name="ec2-instance-recovery"></a>

 In the case of an underlying hardware failure of a DNS forwarder instance, you can use EC2 instance recovery to start the instance on a new host. A recovered instance is identical to the original instance, including the instance ID, private IP addresses, Elastic IP addresses, and all instance metadata. To do this, you can create a CloudWatch alarm that monitors an EC2 instance and automatically recovers the instance if it becomes impaired. You can use the CloudWatch alarm to monitor issues like loss of network connectivity, loss of system power, software issues on the physical host, or hardware issues on the physical host that affect network reachability.

 For more information about instance recovery, refer to [*Recover your instance*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) in the *Amazon EC2 User Guide for Linux Instances*. For step-by-step instructions on using CloudWatch alarms to recover an instance, refer to [*Create alarms that stop, terminate, reboot, or recover an instance*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html) in the *Amazon EC2 User Guide for Linux Instances*.

### Secondary IP address
<a name="secondary-ip-address"></a>

 In an Amazon VPC, instances can be assigned secondary IP addresses, which are transferrable. If an instance fails, the secondary IP can be transferred to a standby instance and this avoids the need for every instance to reconfigure their resolver IP addresses. This approach redirects traffic to the healthy instance so that it can respond to DNS queries. This approach is appropriate for scenarios where EC2 instance recovery might not provide fast enough recovery, or might not be appropriate (for example, an operating system fault or software issue). For more information about working with multiple IP addresses, refer to [*Multiple IP addresses*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/MultipleIP.html) in the *Amazon EC2 User Guide for Linux Instances*.
