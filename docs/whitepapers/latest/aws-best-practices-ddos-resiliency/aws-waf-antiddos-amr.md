---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-antiddos-amr.html
---

# AWS WAF – Application layer DDoS protection
<a name="aws-waf-antiddos-amr"></a>

 You can use the AWS WAF [AntiDDoS managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html) (Anti-DDoS AMR) to protect your web applications against DDoS events in one place when using AWS WAF. This AMR detection system is designed to distinguish between DDoS events and flash crowds, where many legitimate clients send a limited number of requests.

 When added to your AWS WAF web ACL configuration, it learns your traffic patterns and establishes baselines for each protected resource. The system identifies anomalies by comparing current traffic to these baselines, assigning suspicion scores to requests for use in subsequent mitigations.

 During an event, the [AntiDDoS AMR labels](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html) all requests to the affected resource with an event-detected label and further identifies requests suspected to be part of the DDoS attack. The AntiDDoS AMR applies protections independently for each protected resource, basing its actions on the unique baseline established for that resource. This approach provides tailored and effective protection against DDoS attacks for your web applications.

 AntiDDoS AMR starts detecting attacks after establishing a traffic baseline within minutes of AMR activation for the protected resource. Novel algorithms and techniques used in the ruleset enable time to mitigation within seconds. Furthermore, the logic inside AntiDDoS AMR uses sensitivity level and suspicion scores to minimize both false positives and false negatives to help ensure that only malicious volumetric traffic is blocked.

 The AMR feature offers adjustable configuration, including [sensitivity controls](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-aws-waf-application-layer-ddos-protection/) based on the suspicion levels detected by the system for specific events and requests from suspicious sources. This allows you to customize the protection configuration to suit the needs of your specific application types. One of the benefits of AntiDDoS AMR is its ability to detect and mitigate attacks within seconds.

 To learn more about the AMR, pricing, and how to get started with it, see the [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html).
