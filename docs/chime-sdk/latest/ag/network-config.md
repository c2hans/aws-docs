---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/network-config.html
---

# Network configuration and bandwidth requirements
<a name="network-config"></a>

The Amazon Chime SDK requires the destinations and ports described in this topic to support various services. If inbound or outbound traffic is blocked, this blockage might affect the ability to use various services, including audio, video, screen sharing, or chat.

The Amazon Chime SDK uses Amazon Elastic Compute Cloud (Amazon EC2) and other AWS services on port TCP/443. If your firewall blocks port TCP/443, you must put `*.amazonaws.com` on an allow list, or put [AWS IP address ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *AWS General Reference* for the following services:
+ Amazon EC2
+ Amazon CloudFront
+ Amazon Route 53

## Common
<a name="common"></a>

The following destinations and ports are required when running the Amazon Chime SDK in your environment.

| Destination | Ports |
| --- | --- |
| \*.chime.aws | TCP:443 |
| \*.amazonaws.com | TCP:443 |

## Amazon Chime SDK WebRTC media sessions
<a name="web-rtc"></a>

| Domain | Subnet | Ports |
| --- | --- | --- |
| \*.chime.aws | 99.77.128.0/18 | TCP:443 UDP:3478 |
| \*.sdkassets.chime.aws |  | TCP:443 |

## Amazon Chime SDK Voice Connector
<a name="cvc"></a>

The following destinations and ports are recommended if you use Amazon Chime SDK Voice Connectors.

### SIP Signaling
<a name="cvc-signaling"></a>

| AWS Region | IPv4 Subnet | IPv6 Subnet | Ports |
| --- | --- | --- | --- |
| US East (N. Virginia) | 3.80.16.0/23 | 2600:f0f0:c040::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| US West (Oregon) | 99.77.253.0/24 | 2600:f0f0:c041::/48  | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Asia Pacific (Seoul) | 99.77.242.0/24 | 2600:f0f0:c046::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Asia Pacific (Singapore) | 99.77.240.0/24 | 2600:f0f0:c048::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Asia Pacific (Sydney) | 99.77.239.0/24 | 2600:f0f0:c049::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Asia Pacific (Tokyo) | 99.77.244.0/24 | 2600:f0f0:c047::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Canada (Central) | 99.77.233.0/24 | 2600:f0f0:c042::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Europe (Frankfurt) | 99.77.247.0/24 | 2600:f0f0:c044::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Europe (Ireland) | 99.77.250.0/24 | 2600:f0f0:c043::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Europe (London) | 99.77.249.0/24 | 2600:f0f0:c045::/48 | UDP/5060<br />TCP/5060<br />TLS/5061 |
| Global |  | 2600:f0f0:c040::/42 |  |

### Media
<a name="cvc-media"></a>

| AWS Region | IPv4 Subnet | IPv6 Subnet | Ports |
| --- | --- | --- | --- |
| Asia Pacific (Seoul) | 99.77.242.0/24 | 2600:f0f0:c046::/48 | UDP/5000:65000 |
| Asia Pacific (Singapore) | 99.77.240.0/24 |  2600:f0f0:c048::/48 | UDP/5000:65000 |
| Asia Pacific (Sydney) | 99.77.239.0/24 |  2600:f0f0:c049::/48 | UDP/5000:65000 |
| Asia Pacific (Tokyo) | 99.77.244.0/24 |  2600:f0f0:c047::/48 | UDP/5000:65000 |
| Canada (Central) | 99.77.233.0/24 |  2600:f0f0:c042::/48 | UDP/5000:65000 |
| Europe (Frankfurt) | 99.77.247.0/24 |  2600:f0f0:c044::/48 | UDP/5000:65000 |
| Europe (Ireland) | 99.77.250.0/24 |  2600:f0f0:c043::/48 | UDP/5000:65000 |
| Europe (London) | 99.77.249.0/24 | 2600:f0f0:c045::/48 | UDP/5000:65000 |
| US East (N. Virginia) | 3.80.16.0/23 | 2600:f0f0:c040::/48 | UDP/5000:65000 |
| US West (Oregon) | 99.77.253.0/24 | 2600:f0f0:c041::/48 | UDP/5000:65000 |
| Global |  | 2600:f0f0:c040::/42 | UDP/5000:65000 |

### Amazon Voice Focus for carriers media destinations and ports
<a name="carrier-vf"></a>

| AWS Region | Destination | Ports |
| --- | --- | --- |
| US East (N. Virginia) | 99.77.254.0/24 | UDP/5000:65000 |
| US West (Oregon) | 99.77.232.0/24 | UDP/5000:65000 |

## Bandwidth requirements
<a name="bandwidth"></a>

The Amazon Chime SDK has the following bandwidth requirements for the media that it provides:
+ Audio
  + 1:1 call: 54 kbps up and down
  + Large call: no more than 32 kbps extra down for 50 callers
+ Video
  + 1:1 call: 650 kbps up and down
  + HD mode: 1400 kbps up and down
  + 3–4 people: 450 kbps up and (N-1)\*400 kbps down
  + 5–16 people: 184 kbps up and (N-1)\*134 kbps down
  + Up and down bandwidth adapts lower based on network conditions
+ Screen
  + 1.2 mbps up (when presenting) and down (when viewing) for high quality. This adapts as low as 320 kbps based on network conditions.
  + Remote control: 800 kbps fixed

Amazon Chime SDK Voice Connectors have the following bandwidth requirements:
+ Audio
  + Call: \~90 kbps up and down. This includes media payload and packet overhead.
+ T.38 fax
  + With V.34: \~40 kbps. This includes media payload and packet overhead.
  + Without V.34: \~20 kbps. This includes media payload and packet overhead.
