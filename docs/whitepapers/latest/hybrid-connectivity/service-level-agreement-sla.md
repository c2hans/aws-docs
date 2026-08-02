---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/service-level-agreement-sla.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service level agreement (SLA)
<a name="service-level-agreement-sla"></a>

## Definition
<a name="definition-sla"></a>

 Enterprise organizations often require a service provider to fulfil an SLA for each service the organization consumes. The organization in turn builds its own services on top and may offer their own consumers an SLA. The SLA is important as it describes how the service is provided and operated, and it often includes specific measurable characteristics, such as availability. Should the service break the defined SLA, a service provider usually offers financial compensation specified by the agreement. An SLA defines the type of measure, the requirement, and the measurement period. As an example, refer to uptime target definition under the [AWS Direct Connect SLA](https://aws.amazon.com/directconnect/sla/).

## Key questions
<a name="key-questions-sla"></a>
+  Is a hybrid connectivity connection SLA with service credits required?
+  Does the entire hybrid network need to adhere to an uptime target?

## Capabilities to consider
<a name="capabilities-to-consider-sla"></a>

 **Connectivity type:** Internet connectivity can be unpredictable. While AWS takes great care with multiple links in place with a diverse set of ISPs, the administration of the internet is simply outside of AWS or a single provider’s administrative domain. There is a limited amount of route engineering and traffic influence a cloud provider can do once traffic has left the border of their network. That said, there is an [AWS Site-to-Site VPN SLA](https://aws.amazon.com/vpn/site-to-site-vpn-sla/) that provides availability targets for AWS Site-to-Site VPN endpoints.

 AWS [Direct Connect offers a formal SLA](https://aws.amazon.com/directconnect/sla/) with service credits calculated as a percentage of the total AWS Direct Connect Port Hour charges paid by you for the applicable connections experiencing unavailability for the monthly billing cycle in which the SLA was not met. This is the recommended transport if an SLA is required. AWS Direct Connect lists [specific minimal configuration requirements](https://aws.amazon.com/directconnect/sla/) for each uptime target such as number of AWS Direct Connect locations, connections, and other configuration details. The failure to satisfy the requirements means that service credits cannot be offered should the service break defined SLAs.

 Importantly, even if the service selected to provide hybrid connectivity is configured to meet the SLA requirements, the rest of the network may not provide the same level of SLA. The AWS responsibility ends at the AWS Direct Connect location at the AWS Direct Connect port. Once AWS hands traffic off to your organization’s network, it is no longer the responsibility of AWS. If you use a service provider between AWS and your on-premises network, connectivity is subject to SLA between yourself and the service provider, if applicable. Keep in mind that the entire hybrid network is just as good as the weakest part of it when designing hybrid connectivity.

 AWS Direct Connect partners offer AWS Direct Connect connectivity. The partner may offer an SLA with service credits based on their product offering up to the demarcation point with AWS. The option should be evaluated and further researched directly with APN Partners. AWS publishes [a list of validated delivery partners](https://aws.amazon.com/directconnect/partners/).

 **Logical design:** In addition to the connectivity type, you also must consider other building blocks as part of your overall design. As an example, [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/sla/) has its own SLA, as does [AWS S2S VPN](https://aws.amazon.com/vpn/site-to-site-vpn-sla/). You might be using AWS Transit Gateway for scale and AWS S2S VPN for security reasons, but you must design both in manner consistent with each SLAs to be eligible for service credits with each respective service.

Review [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/) and [Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html).

![Diagram showing an SLA consideration decision tree](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/sla-decision-tree.png)
