---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/syn-flood-attacks.html
---

# SYN flood attacks
<a name="syn-flood-attacks"></a>

 When a user connects to a Transmission Control Protocol (TCP) service, such as a web server, their client sends a SYN packet. The server returns a synchronization-acknowledgement (SYN-ACK) packet, and finally the client responds with an acknowledgement (ACK) packet, which completes the expected three-way handshake. The following figure illustrates this typical handshake.

![A diagram depicting a SYN three-way handshake in a SYN flood attack](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/syn-three-way-handshake.png)

 In a SYN flood attack, a malicious client sends a large number of SYN packets but never completes the TCP handshake. Modern operating systems implement SYN cookies by default to counter state table exhaustion.

 You can improve the DDoS resilience of resources in your virtual private cloud (VPC) by ensuring that the security groups assigned to the resource–such as application load balancers (ALBs), classic load balancers (CLBs), and Elastic IPs (EIPs)–aren't configured to require Amazon Elastic Compute Cloud (Amazon EC2) [connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html). If a security group rule permits TCP or UDP flows for all traffic (0.0.0.0/0 or ::/0) to the listening port (80, 443, and so on), and there is a corresponding rule in the other direction that permits all response traffic (0.0.0.0/0 or ::/0) for all ports (0-65535) on both TCP and UDP, then that flow of traffic isn't tracked. This helps to avoid negative effects of this feature on an instance's packet throughput and enables an ALB to detect and scale based on the increase in traffic during a DDoS event.
