---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/use-dns-for-load-balancing-and-floating-ips-for-failover.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Use DNS for load balancing and floating IPs for failover
<a name="use-dns-for-load-balancing-and-floating-ips-for-failover"></a>

 IP telephony clients that support DNS SRV capability can efficiently use the redundancy built into the infrastructure by load balancing clients to different SBCs/PBXs.

![A diagram depicting using DNS SRV records to load balance SIP clients .](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/using-dns-srv-records.png)

The preceding figure shows how customers can use the SRV records to load balance SIP traffic. Any IP telephony client that supports the SRV standard will look for the sip. `<transport protocol>` prefix in an SRV type DNS record. In the example, the answer section from DNS contains both of the PBXs running in different AWS Availability Zones. However, in addition to the endpoint URIs, the SRV record contains three additional pieces of information:
+  The first number is the **Priority** (1 in the example above). A lower priority is preferred over higher.
+  The second number is the **Weight** (10 in the example above).
+  And the third number is the **Port** to be used (5060).

 Since the priority is the same (1) for both PBXs servers, the clients use the weight to load balance between the two PBXs. In this case, since the weights are the same, SIP traffic should be load balanced equally between the two PBXs.

 DNS can be a good solution for client load balancing, but what about implementing failover by changing/updating DNS ‘A’ records? This method is discouraged because of inconsistency found in DNS caching behavior within the client and intermediate nodes. A better approach for intra-AZ failover between a cluster of SIP nodes is to use the EC2 IP reassignment where an impaired host’s IP address is instantly reassigned to a healthy host by using the EC2 API. Paired with a detailed monitoring and health check solution, IP reassignment of a failed node ensures that traffic is moved over to a healthy host in a timely manner that minimizes end user disruption.
