---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-security.html
---

# Security controls for the development stage
<a name="dev-security"></a>

The development stage requires foundational security controls that establish essential protections without impeding the rapid iteration and experimentation that characterizes the PoC objectives. At this stage, security focuses on building secure practices into the development workflow while maintaining the agility needed for innovation.

During system design, threat modelling provides the foundation for all subsequent security decisions. Conducting threat modelling early identifies security requirements before they become costly to implement. This helps teams understand the unique attack surface of generative AI applications across input processing, reasoning, and output generation. This analysis directly informs the implementation of basic guardrails. Adopting solutions such as [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with [prompt injection filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html) can help provide immediate protection against common attack vectors while remaining lightweight enough for experimental environments.

Fundamental access controls can protect development environments, training data, and model artifacts through appropriate authentication mechanisms. They also help you securely store sensitive data and credentials. Development environments should implement role-based access controls that limit access to training datasets, model configurations, and experimental outputs based on team member responsibilities. Secure credential management and encrypted storage of sensitive artifacts can prevent unauthorized access while maintaining the collaborative nature essential for effective development work. Finally, development environments should be integrated with a [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) to support organizational security observability needs.

Supply chain security assessment and basic data validation for training complete the development stage security posture. These controls address the integrity of third-party models, libraries, and data sources. They also implement validation processes to detect potential data poisoning or bias. The lightweight nature of these controls helps teams to establish security foundations early. This can help you avoid costly retrofitting while preparing for the more rigorous requirements of subsequent stages.

For more information, see the following resources:
+ AWS Well-Architected Framework best practices:
  + [Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_data_rest_encrypt.html)
  + [Identify threats and prioritize mitigations using a threat model](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_securely_operate_threat_model.html)
  + [Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html)
  + [Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_data_rest_key_mgmt.html)
  + [Understand your data classification scheme](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_data_classification_identify_data.html)
  + [Use strong sign-in mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_identities_enforce_mechanisms.html)
+ [Threat modeling your generative AI workload to evaluate security risk](https://aws.amazon.com/blogs/security/threat-modeling-your-generative-ai-workload-to-evaluate-security-risk/) (AWS blog post)
