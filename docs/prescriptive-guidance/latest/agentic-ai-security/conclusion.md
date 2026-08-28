---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/conclusion.html
---

# Conclusion and resources
<a name="conclusion"></a>

Securing agentic AI systems requires applying established security practices with AI-specific adaptations rather than entirely new approaches. The autonomous nature of these systems demands particular attention to input validation, access controls, and system recovery capabilities. Ongoing threat-modeling activities support safe expansion of system features, new model inference, wider user bases, and version uplifts. Continuous monitoring remains important as threat landscapes evolve. Organizations that establish these security foundations and establish them into ongoing operational schedules are better positioned to implement agentic AI systems safely and effectively.

## Resources
<a name="resources"></a>

The follow frameworks and publications were used as reference in developing this guide. They are also relevant to developing and operating agentic AI systems safely and securely on AWS.

### AWS resources
<a name="9999999999999999aws--resources.a8637df0-bd32-51d6-bbb3-5c2727bb0b1b"></a>
+ [Agentic AI on AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) – This documentation series can help you implement agentic AI systems on AWS, including information about how to plan, design, and build these systems.
+ [AWS Security Reference Architecture](https://aws.amazon.com/prescriptive-guidance/security-reference-architecture/) – This library provides [technical guidance](https://aws.amazon.com/prescriptive-guidance/security-reference-architecture/), [implementation code](https://github.com/aws-samples/aws-security-reference-architecture-examples), and a [validation tool](https://github.com/awslabs/sra-verify) that can help you build a multi-account security architecture on AWS.
+ [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) – This framework provides architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the AWS Cloud.
+ [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) – This AWS service can help you implement AWS best practices.
+ [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) – This agentic platform can help you build, deploy, and operate AI agents securely at scale by using any framework and foundation model.
+ [Security in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html) – This section of the Amazon Bedrock documentation can help you meet security and compliance objectives when building with Amazon Bedrock.

### NIST resources
<a name="nist-resources.f9334538-ab89-5383-9e24-0a62115f4f14"></a>
+ [NIST AI risk management framework (RMF) playbook](https://airc.nist.gov/airmf-resources/playbook/) – This playbook provides practical guidance and resources for implementing AI-specific risk-management practices and helps you comply with the NIST AI RMF standards.
+ [Secure software development practices for generative AI and dual-use foundation models](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf) – This publication provides secure software development practices specifically for generative AI and dual-use foundation models as a community profile of the Secure Software Development Framework (SSDF).
+ [Security and privacy controls for information systems and organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) – This publication provides a catalog of security and privacy controls for federal information systems and organizations to help protect against cybersecurity threats and privacy risks.

### OWASP resources
<a name="owasp-resources.f8921281-8c99-5ced-9ab3-85ca373feb27"></a>
+ [Agentic AI threats and mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) – This resource documents key security threats and mitigation strategies specifically for agentic AI systems and focuses on vulnerabilities and risks.
+ [OWASP top 10 for LLM applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) – This lists critical security vulnerabilities and risks that are specific to LLM applications and provides essential guidance for securing AI systems against emerging threats.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
