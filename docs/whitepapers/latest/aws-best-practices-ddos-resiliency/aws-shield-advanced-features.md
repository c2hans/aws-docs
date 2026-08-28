---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-shield-advanced-features.html
---

# AWS Shield Advanced Features
<a name="aws-shield-advanced-features"></a>

**Managed DDoS event response with Shield Response Team support**

 When subscribed to Shield Advanced, you can engage the AWS Shield Response Team (SRT) to help you create rules to mitigate an attack that's reducing your application's availability. For more information, see [Managed DDoS event response with Shield Response Team (SRT)](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html).

**Proactive engagement**

 With proactive engagement, the SRT contacts you directly when the availability or performance of your application is affected because of a possible attack. We recommend this engagement model because it provides the quickest SRT response and allows the SRT to begin troubleshooting even before they've established contact with you. Through proactive engagement, you can configure [health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html), associate to your resources, and provide always available operations contact information. When Shield Advanced detects signs of DDoS and your application health checks are showing signs of degradation, AWS SRT will proactively reach out to you.

 Completing configuration of proactive engagement includes adding contact details in the Shield Advanced console. AWS SRT will use this information to contact you.

 You can enable proactive engagement for all resources or for select key production resources where response time is critical. This is accomplished by assigning health checks only to these resources. For more information, see [Setting up proactive engagement for the SRT to contact you directly](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-proactive-engagement.html).

**Centralized protection management**

 In addition, you can use AWS Firewall Manager to centrally configure and manage security rules, such as AWS Shield Advanced protections and AWS WAF rules, across your organization. Your AWS Organizations management account can designate an administrator account, which is authorized to create Firewall Manager policies. These policies allow you to define criteria, such as resource type and tags, which determine where rules are applied. This is useful when you have multiple accounts and want to standardize your protection. AWS Shield protection policies can be created using AWS Firewall Manager only for Shield Advanced users.

 For more information about:
+  How to manage the deployment of rules across your AWS resources with Firewall Manager, see:
  + [Getting started with Firewall Manager AWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms.html)
  + [Getting started with Firewall Manager Shield Advanced policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-shield.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
