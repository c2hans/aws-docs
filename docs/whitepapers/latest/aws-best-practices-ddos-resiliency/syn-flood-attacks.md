---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/syn-flood-attacks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SYN flood attacks
<a name="syn-flood-attacks"></a>

 When a user connects to a Transmission Control Protocol (TCP) service, such as a web server, their client sends a SYN packet. The server returns a synchronization-acknowledgement (SYN-ACK) packet, and finally the client responds with an acknowledgement (ACK) packet, which completes the expected three-way handshake. The following image illustrates this typical handshake.

![A diagram depicting a SYN three-way handshake](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/syn-three-way-handshake.png)

 In a SYN flood attack, a malicious client sends a large number of SYN packets, but never sends the final ACK packets to complete the handshakes. The server is left waiting for a response to the half-open TCP connections and the idea is that the target eventually runs out of capacity to accept new TCP connections which prevents new users from connecting to the server, however the actual impact is more nuanced. Modern operating systems all implement SYN cookies by default as a mechanism to counter state table exhaustion from SYN flood attacks. Once the SYN queue length reaches a pre-determined threshold, the server responds with a SYN-ACK containing a crafted initial sequence number, without creating an entry in its SYN queue. If the server then receives an ACK containing a correctly incremented acknowledgement number it’s able to add the entry to its state table and proceed as normal. The actual impact of SYN floods on target devices tends to be network capacity and CPU exhaustion, however intermediate stateful devices such as firewalls (or EC2 security group [connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html)) may suffer TCP state table exhaustion and drop new connections.
