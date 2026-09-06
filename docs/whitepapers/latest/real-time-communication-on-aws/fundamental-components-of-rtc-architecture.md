---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/fundamental-components-of-rtc-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Fundamental components of RTC architecture
<a name="fundamental-components-of-rtc-architecture"></a>

 In the telecommunications industry, RTC commonly refers to live media sessions between two endpoints with minimum latency. These sessions could be related to:
+  A voice session between two parties (such as a telephone system, mobile, or Voice over IP (VoIP))
+  Instant messaging (such as chatting and Instant Relay Chat (IRC))
+  Live video session (such as video conferencing and telepresence)

 Each of the preceding solutions has some components in common (such as components that provide authentication, authorization and access control, transcoding, buffering and relay, and so on) and some components unique to the type of media transmitted (such as broadcast service, messaging server and queues, and so on). This section focuses on defining a voice- and video-based RTC system and all of the related components, as illustrated in the following figure.

![A diagram depicting essential architectural components for RTC.](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/essential-rtc-components.png)

## Softswitch/PBX
<a name="softswitchpbx"></a>

 A softswitch or PBX is the brain of a voice telephone system and provides intelligence for establishing, maintaining, and routing of a voice call within or outside the enterprise by using different components. All of the subscribers of the enterprise are required to register with the softswitch to receive or make a call. An important functionality of the softswitch is to keep track of each subscriber and how to reach them by using the other components within the voice network.

## Session border controller (SBC)
<a name="session-border-controller-sbc"></a>

 A session border controller (SBC) sits at the edge of a voice network and keeps track of all incoming and outgoing traffic (both control and data planes). One of the key responsibilities of an SBC is to protect the voice system from malicious use. The SBC can be used to interconnect with session initiation protocol (SIP) trunks for external connectivity. Some SBCs also provide transcoding capabilities for converting [CODECs](https://en.wikipedia.org/wiki/Codec) from one format to another. Most SBCs also provide network address translation (NAT) traversal capabilities, which aids in ensuring calls are established, even across firewalled networks.

## PSTN connectivity
<a name="pstn-connectivity"></a>

 Voice over IP (VoIP) solutions use Public Switched Telephone Network (PSTN) gateways and SIP trunks to connect with legacy PSTN networks.

### PSTN gateway
<a name="pstn-gateway"></a>

 The PSTN gateway converts the signaling between SIP and SS7 and media between Real Time Transport Protocol (RTP) and time division multiplexing (TDM) using CODEC transcoding. PSTN gateways always sit at the edge close to the PSTN network.

### SIP trunk
<a name="sip-trunk"></a>

 In a SIP trunk, the enterprise does not end its calls onto a TDM (SS7 based) network, but rather the flows between enterprise and telco remain over IP. Most of the SIP Trunks are established by using SBCs. The enterprise must agree on the predefined security rules from telco, such as allowing a certain range of IP addresses, ports, and so on.

## Media gateway (transcoder)
<a name="media-gateway-transcoder"></a>

Users communicate in real-time using audio and/or video, as well as optional data and other information. To communicate, the two devices need to be able to agree upon a mutually-understood codec for each media track, so they can successfully communicate and present the shared media. All WebRTC-compatible browsers must support online positioning user support (OPUS) and G711 for audio, [VP8](https://en.wikipedia.org/wiki/VP8), and H.264 Constrained Baseline profile for video.

A typical voice solution outside the WebRTC ecosystem allows various types of CODECs. Some of the common CODECs are G.711 µ-law for North America, G.711 A-law, G.729, and G.722. When two devices that are using two different CODECs communicate with each other, the media gateway translates the CODEC flow between the devices. In other words, a media gateway processes media, and ensures that the end devices are able to communicate with each other.

## Push notifications in WebRTC
<a name="push-notifications-in-webrtc"></a>

WebRTC implementations are very common on mobile devices. Unlike web browsers, a mobile device can’t keep a websocket connectivity open for a long time. Therefore, it needs to rely on push-notifications from the WebRTC server for all ending requests, such as calls and messages.

[Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) lets you send push notifications to apps on mobile devices. These apps could be running on various operating systems such as Apple iOS or Android. The following figure shows a high-level overview of push-notifications flow, from a WebRTC notification server to WebRTC mobile endpoints.

![A diagram depicting Amazon SNS for push notifications.](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/sns-push-notifications.jpg)

## WebRTC and WebRTC gateway
<a name="webrtc-and-webrtc-gateway"></a>

 Web real-time communication (WebRTC) allows you to establish a call from a web browser or request resources from the backend server by using API. The technology is designed with cloud technology in mind and therefore provides various APIs which could be used to establish a call. Because not all of the voice solutions (including SIP) support these APIs, the WebRTC gateway is required to translate API calls into SIP messages and vice versa.

The following figure shows a design pattern for a highly available WebRTC architecture. The incoming traffic from WebRTC clients is balanced by an[ Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB) with WebRTC running on [Amazon Elastic Compute Cloud](https://aws.amazon.com/pm/ec2/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!488982705492!e!!g!!amazon%20ec2&ef_id=CjwKCAjw_tWRBhAwEiwALxFPoZYgo0_abdA7JHP4hKKHfEsy2nGSZLqw3A4AutXy2sgGO6vBD8P7_xoCefAQAvD_BwE:G:s&s_kwcid=AL!4422!3!488982705492!e!!g!!amazon%20ec2) (Amazon EC2) instances that are part of an [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) group.

![A basic topology of an RTC system for voice.](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/rtc-system-for-voice.jpg)

Another design pattern for SIP and RTP traffic is to use pairs of SBCs on Amazon EC2 in active-passive mode across Availability Zones, as seen in the following figure. Here, an Elastic IP address can be dynamically moved between instances upon failure, where the Domain Name Service (DNS) cannot be used.

![A diagram depicting RTC architecture using Amazon EC2 in a virtual private cloud (VPC).](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/rtc-with-ec2.jpg)
