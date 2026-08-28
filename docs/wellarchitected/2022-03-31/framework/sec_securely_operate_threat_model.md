---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_securely_operate_threat_model.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP07 Identify and prioritize risks using a threat model
<a name="sec_securely_operate_threat_model"></a>

 Use a threat model to identify and maintain an up-to-date register of potential threats. Prioritize your threats and adapt your security controls to prevent, detect, and respond. Revisit and maintain this in the context of the evolving security landscape.

Threat modeling provides a systematic approach to aid in finding and addressing security issues early in the design process. Earlier is better since mitigations have a lower cost compared to later in the lifecycle.

The typical core steps of the threat modeling process are:

1. Identify assets, actors, entry points, components, use cases, and trust levels, and include these in a design diagram.

1. Identify a list of threats.

1. For each threat, identify mitigations, which might include security control implementations.

1. Create and review a risk matrix to determine if the threat is adequately mitigated.

Threat modeling is most effective when done at the workload (or workload feature) level, ensuring that all context is available for assessment. Revisit and maintain this matrix as your security landscape evolves.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Create a threat model: A threat model can help you identify and address potential security threats.
  +  [NIST: Guide to Data-Centric System Threat Modeling ](https://csrc.nist.gov/publications/detail/sp/800-154/draft)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Security Audit Guidelines ](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)
+  [Security Bulletins ](https://aws.amazon.com/security/security-bulletins/)

 **Related videos:**
+  [Security Best Practices the Well-Architected Way](https://youtu.be/u6BCVkXkPnM)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
