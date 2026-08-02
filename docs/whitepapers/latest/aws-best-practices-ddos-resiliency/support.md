---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/support.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Support
<a name="support"></a>

 If you experience an attack, you can also benefit from support from AWS in assessing the threat and reviewing the architecture of your application, or you might want to request other assistance. It is important to create a response plan for DDoS attacks before an actual event. The best practices outlined in this paper are intended to be proactive measures that you implement before you launch an application, but DDoS attacks against your application might still occur. Review the options in this section to determine the support resources that are best suited for your scenario. Your account team can evaluate your use case and application, and assist with specific questions or challenges that you have.

 If you’re running production workloads on AWS, consider subscribing to Business Support, which provides you with 24/7 access to Cloud Support Engineers who can assist with DDoS attack issues. If you’re running mission critical workloads, consider Enterprise Support which provides the ability to open critical cases and receive the fastest response from a Senior Cloud Support Engineer.

 If you’re subscribed to AWS Shield Advanced and are also subscribed to either Business Support or Enterprise Support, you can configure Shield proactive engagement. It allows you to configure health checks, associate to your resources, and provide 24/7 operations contact information. When Shield detects signs of DDoS and your application health checks are showing signs of degradation, AWS SRT will proactively reach out to you. This is our recommended engagement model because it allows for the quickest AWS SRT response times and empowers AWS SRT to begin troubleshooting even before contact has been established with you.

 For more information, refer to [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/).

 The proactive engagement feature requires you to configure a Route 53 health check that accurately measures the health of your application and is associated with the resource protected by Shield Advanced. Once a Route 53 health check is associated in the Shield console, the Shield Advanced detection system uses the health check status as an indicator of your application’s health. The health-based detection feature in Shield Advanced will ensure that you are notified and that mitigations are placed more quickly when your application is unhealthy. AWS SRT will contact you to troubleshoot whether the unhealthy application is being targeted by a DDoS attack and place additional mitigations as needed.

 Completing configuration of proactive engagement includes adding contact details in the Shield console. AWS SRT will use this information to contact you. You can configure up to ten contacts, and provide additional notes if you have any specific contact requirements or preferences. Proactive

 engagement contacts should hold a 24/7 role, such as a security operations center or an individual who is immediately available.

 You can enable proactive engagement for all resources or for select key production resources where response time is critical. This is accomplished by assigning health checks only to these resources.

 You can also escalate to AWS SRT by creating an Support case using the [Support console](https://console.aws.amazon.com/support/home) (sign-in required), or [Support API](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) if you have a DDoS-related event that affects your application’s availability.
