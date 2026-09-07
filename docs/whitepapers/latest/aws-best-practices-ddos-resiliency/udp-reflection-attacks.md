---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/udp-reflection-attacks.html
---

# UDP reflection attacks
<a name="udp-reflection-attacks"></a>

 UDP reflection attacks exploit the fact that UDP is a stateless protocol. Attackers can craft a valid UDP request packet listing the attack target's IP address as the UDP source IP address. The attacker has now falsified (spoofed) the UDP request packet's source IP. The UDP packet contains the spoofed source IP and is sent by the attacker to an intermediate server. The server is tricked into sending its UDP response packets to the targeted victim IP rather than back to the attacker's IP address. The intermediate server is used because it generates a response that is several times larger than the request packet, effectively amplifying the amount of attack traffic sent to the target IP address.

 The amplification factor is the ratio of response size to request size, and it varies depending on which protocol the attacker uses: DNS, Network Time Protocol (NTP), Simple Service Directory Protocol (SSDP), Connectionless Lightweight Directory Access Protocol (CLDAP), [Memcached](https://memcached.org/), Character Generator Protocol (CharGen), or Quote of the Day (QOTD).

 For example, the amplification factor for DNS can be 28 to 54 times the original number of bytes. So, if an attacker sends a request payload of 64 bytes to a DNS server, they can generate over 3400 bytes of unwanted traffic to an attack target. UDP reflection attacks are accountable for larger volume of traffic in comparison to other attacks. The following figure illustrates the reflection tactic and amplification effect.

![A diagram depicting a UDP reflection attack](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/udp-reflection-attack.png)

 It should be noted that reflection attacks, while they provide attackers with amplification, require IP spoofing capability and as increasing numbers of network providers adopt Source Address Validation Everywhere (SAVE) or [BCP38](https://www.rfc-editor.org/info/bcp38/), this capability is removed, requiring DDoS attackers to cease reflection attacks or to relocate to data centers and network providers who don't implement source address validation.
