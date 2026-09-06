---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-infrastructure.html
---

# 6. Infrastructure security for agentic AI systems on AWS
<a name="best-practices-infrastructure"></a>

Infrastructure security for agentic AI systems requires isolation strategies and immutable deployment practices to contain potential compromises. Account separation and automated deployment pipelines reduce both the attack surface and operational risk.

**This section contains the following best practices:**
+ [6.1 Use the AWS Security Reference Architecture for AI systems (AI-specific)](#best-practices-6-sec-ref-arch)
+ [6.2 Apply defense-in-depth principles (General)](#best-practices-6-defense-in-depth)
+ [6.3 Reduce human access to infrastructure (General)](#best-practices-6-human-access)
+ [6.4 Deploy adequate edge protection (General)](#best-practices-6-edge-protection)

## 6.1 Use the AWS Security Reference Architecture for AI systems (AI-specific)
<a name="best-practices-6-sec-ref-arch"></a>

The [AWS Security Reference Architecture (AWS SRA)](https://aws.amazon.com/prescriptive-guidance/security-reference-architecture/) is a holistic set of guidelines for deploying the full complement of AWS security services in a multi-account environment. Use the latest [AWS SRA – generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/introduction.html) guide to align with AWS security best practices for generative AI systems. These best practices form a solid foundation for agentic AI systems. Specifically, use AWS account structures to separate agents from data sources that are not directly related to their operational functions. For example, make sure that fine-tuning data is isolated from any operational runtime environments. This reduces the scope of potential compromise and improves access control granularity.

## 6.2 Apply defense-in-depth principles (General)
<a name="best-practices-6-defense-in-depth"></a>

Apply defense-in-depth principles throughout the infrastructure to create multiple security barriers that help protect against various attack vectors. This approach reduces the likelihood of any single control failure resulting in a system breach. For more information, see [Architect defense-in-depth security for generative AI applications using the OWASP Top 10 for LLMs](https://aws.amazon.com/blogs/machine-learning/architect-defense-in-depth-security-for-generative-ai-applications-using-the-owasp-top-10-for-llms/) (AWS blog post).

## 6.3 Reduce human access to infrastructure (General)
<a name="best-practices-6-human-access"></a>

The AWS Well-Architected Framework recommends that you [automate generative AI application lifecycle with infrastructure as code](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops04-bp01.html) and that you [use runbooks for standard activities such as deployment](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_tracking_change_management_planned_changemgmt.html). Make sure that your infrastructure deployment includes tested, standardized runbooks. This reduces the likelihood of human error introducing vulnerabilities during the deployment process. Deploy immutable infrastructure and [implement break-glass-procedures](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html) to prevent unauthorized modifications and promote consistent security configurations across environments. For more information about controlling changes, see [How do you implement change?](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-08.html) in the AWS Well-Architected Framework.

The AWS Well-Architected Framework also recommends that you [deploy software programmatically](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_deploy_software_programmatically.html) and that you [use multiple environments](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_multi_env.html). Use automated pipelines to deploy code across environments, and [regularly assess the security properties of the pipeline](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_regularly_assess_security_properties_of_pipelines.html).

## 6.4 Deploy adequate edge protection (General)
<a name="best-practices-6-edge-protection"></a>

Deploy edge protections that help protect against common web application threats, such as those outlined in the [OWASP Web Application Security Project](https://owasp.org/www-project-top-ten/) (OWASP website). This can help protect agentic AI systems from internet-based attacks. Implement controls to limit unreasonable request volumes and filter requests from known threats. This can prevent denial-of-service attacks and reduce exposure to malicious actors. Establish capabilities for rapid rule updates to protect against emerging threats. Make sure that security controls can adapt quickly to new attack patterns and vulnerabilities. For more information about limiting request volumes, see [Applying rate limiting to requests in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html).
