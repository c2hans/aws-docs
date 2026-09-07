---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/best-practices-from-the-field.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best practices from the field
<a name="best-practices-from-the-field"></a>

 This section summarizes the best practices that have been implemented by some of largest and most successful AWS customers that run large real-time Session Initiation Protocol (SIP) workloads. AWS customers wanting to run their own SIP infrastructure in the public cloud would find these best practices valuable as they can help increase the reliability and resiliency of the system in case of different kinds of failures. Although some of these best practices are SIP specific, most of them are applicable to any real-time communication application running on AWS.

## Create a SIP overlay
<a name="create-a-sip-overlay"></a>

 AWS has a robust, scalable and redundant network backbone that provides connectivity between different AWS Regions. When a network event, such as a fiber cut, degrades an AWS backbone link, traffic is quickly failed over to redundant paths using network level routing protocols, such as Border Gateway Protocol (BGP). This network level traffic engineering is a black box to AWS customers and most do not even notice these failover events. However, customers that run real-time workloads, such as voice, high quality video, and low latency messaging, do sometimes notice these events. So, how can an AWS customer implement their own traffic engineering on top of what is provided by AWS at the network level? The solution is deploying SIP infrastructure at many different AWS Regions. As part of the call control features, SIP also provides the ability to route calls through specific SIP proxies.

![A diagram depicting using SIP routing to override network routing .](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/using-sip-to-override.png)

 In the preceding figure, SIP infrastructure (represented by green dots inside the cubes) is running in all four US Regions. The solid blue lines represent a fictional depiction of the AWS backbone. If no SIP routing is implemented, a call originating in the US west coast and destined for the US east coast goes over the backbone link that is directly connecting the Oregon and Virginia regions. The diagram shows how a customer might override the network level routing and make the same call between Oregon and Virginia routed through California using SIP routing. This type of SIP traffic engineering can be implemented using SIP proxies and media gateways based on network metrics such as SIP retransmissions and customer specific business preferences.
