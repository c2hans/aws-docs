---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/introduction-denial-of-service-attacks.html
---

# Introduction to denial of service attacks
<a name="introduction-denial-of-service-attacks"></a>

 A Denial of Service (DoS) attack, or event, is a deliberate attempt to make a website or application unavailable to users, such as by flooding it with network traffic. Attackers use a variety of techniques that consume large amounts of network bandwidth or tie up other system resources, disrupting access for legitimate users. In its simplest form, a lone attacker uses a single source to carry out a DoS attack against a target, as shown in the following figure.

![A diagram depicting a DoS attack](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/dos-attack.png)

In a DDoS attack, an attacker uses multiple sources to orchestrate an attack against a target. These sources can include distributed groups of malware infected computers, routers, IoT devices, and other endpoints. The following figure shows a network of compromised hosts that participate in the attack, generating a flood of packets or requests to overwhelm the target.

![A diagram depicting a DDoS attack](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-attack.png)

 There are seven layers in the Open Systems Interconnection (OSI) model, described in the following table. DDoS attacks are most common at layers 3, 4, and 7.
+  Layer 3 and 4 attacks correspond to the Network and Transport layers of the OSI model. Within this whitepaper, AWS refers to these collectively as *infrastructure layer attacks*.
+  Layer 7 attacks correspond to the Application layer of the OSI model.

 This paper discusses these attack types in the sections that follow.

 *Table 1 – OSI model*

|  \#  |  Layer  |   Unit   |   Description   |   Vector examples   |
| --- | --- | --- | --- | --- |
|  7  |  Application  |  Data  |  Network process to application  |  HTTP floods, DNS query floods  |
|  6  |  Presentation  |  Data  |  Data representation and encryption  |  Transport Layer Security (TLS) abuse  |
|  5  |  Session  |  Data  |  Interhost communication  |  N/A  |
|  4  |  Transport  |  Segments  |  End-to-end connections and reliability  |  Synchronize (SYN) floods  |
|  3  |  Network  |  Packets  |  Path determination and logical addressing  |  User Datagram Protocol (UDP) reflection attacks  |
|  2  |  Data Link  |  Frames  |  Physical addressing  |  N/A  |
|  1  |  Physical  |  Bits  |  Media, signal, and binary transmission  |  N/A  |
