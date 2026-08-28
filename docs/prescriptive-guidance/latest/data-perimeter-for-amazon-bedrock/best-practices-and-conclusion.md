---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/best-practices-and-conclusion.html
---

# Conclusion
<a name="best-practices-and-conclusion"></a>

Implementing AWS data perimeter controls for Amazon Bedrock requires a comprehensive approach that addresses the unique security challenges of generative AI workloads.

The three-layered defense of identity, resource, and network perimeters provides robust protection against data exfiltration, unauthorized access, and compliance violations while maintaining the operational flexibility required for AI innovation.

The key to successful implementation lies in understanding that AI workloads differ fundamentally from traditional applications in their data flows, access patterns, and risk profiles. By implementing the controls outlined in this guide, organizations can apply minimum required security guardrails for an AI solution built on Amazon Bedrock.

Start with organizational boundary controls using SCPs, then implement resource-specific protections for your most sensitive AI data. Layer on network controls and comprehensive monitoring to create defense in depth.

Regular testing and validation ensure your controls remain effective as your AI workloads evolve and new threats emerge.

Remember that data perimeter implementation is an iterative process. Begin with the most critical controls for your highest-risk AI workloads, then expand coverage as you gain experience and confidence with the framework.

The investment in comprehensive data perimeter controls pays dividends in reduced security risk, improved compliance posture, and increased stakeholder confidence in your AI initiatives.

**Beyond data perimeter – operational considerations**

While this guide focuses on establishing security boundaries through identity, resource, and network perimeters, successful Amazon Bedrock deployments require additional operational practices that complement these foundational controls:

**Model lifecycle management**
+ **Version control** – Pin to specific model versions in production environments to ensure consistent behavior and security posture.
+ **Upgrade procedures** – Establish testing and approval workflows before adopting new model versions.
+ **Deprecation planning** – Monitor AWS announcements for model deprecations and plan migrations accordingly.
+ **Custom model governance** – Document training data lineage, implement approval gates for model deployment, and establish retirement procedures.

**Logging and monitoring strategy**
+ **Prompt logging** – Enable model invocation logging with appropriate encryption and retention policies based on data sensitivity.
+ **Performance monitoring** – Establish baseline metrics for model behavior and monitor for drift or unexpected changes.
+ **Cost tracking** – Implement CloudWatch alarms for usage spikes and maintain budget alerts for Amazon Bedrock spending.
+ **Audit trails** – Leverage CloudTrail for comprehensive audit logging of all Amazon Bedrock API calls.

**Knowledge base governance**
+ **Data classification** – Implement classification schemes for all documents in knowledge bases.
+ **Refresh schedules** – Establish procedures for updating knowledge base content and removing stale data.
+ **Access patterns** – Monitor query patterns for unusual data access that might indicate security issues.
+ **Data retention** – Document and enforce retention policies for knowledge base content.

**Agent security practices**
+ **Action group review** – Require security review for all new agent action groups and Lambda integrations.
+ **Input validation** – Implement robust validation in all agent action group Lambda functions..
+ **Capability documentation** – Maintain clear documentation of each agent's capabilities and business justification.
+ **Invocation monitoring** – Monitor agent invocations for unusual patterns or potential abuse.

**Guardrails implementation**
+ **Content filtering** – Configure Amazon Bedrock guardrails based on use case sensitivity and compliance requirements.
+ **Adversarial testing** – Test guardrails with adversarial prompts before production deployment.
+ **Threshold tuning** – Monitor guardrail intervention rates and adjust thresholds based on operational experience.
+ **Bypass procedures** – Document legitimate use cases that may require guardrail adjustments.

**Incident response planning**
+ **AI-specific incidents** – Define response procedures for prompt injection attacks, data leakage, and model abuse.
+ **Automated response** – Implement automated responses for repeated policy violations.
+ **Runbook maintenance** – Maintain detailed runbooks for common AI security incidents.
+ **Access revocation** – Document procedures for emergency model access revocation.

These operational practices, combined with the data perimeter controls outlined in this guide, provide a comprehensive security and operational framework for your Amazon Bedrock deployments.

For detailed guidance on implementing these operational practices, refer to the **Resources **section, which includes links to AWS documentation, best practices guides, and operational tools.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
