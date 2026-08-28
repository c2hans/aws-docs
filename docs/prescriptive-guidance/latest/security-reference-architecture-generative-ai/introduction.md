---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – AI security
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

AI solutions span multiple use cases, each with distinct security requirements. The [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/) defines security scope and disciplines for different use cases, and the [Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/) defines the autonomy and agency given to an agent.

Depending on your use case, you can use a managed service where the provider handles operations, or build your own. AWS offers a wide range of services to help you build, run, and integrate artificial intelligence and machine learning (AI/ML) solutions of any size, complexity, or use case. These services operate at all [three layers of the generative AI stack](https://aws.amazon.com/blogs/machine-learning/welcome-to-a-new-era-of-building-in-the-cloud-with-generative-ai-on-aws/): infrastructure, large language models (LLMs), and applications.

This guide focuses on the middle layer, which provides access to all the models and tools you need to build and scale generative AI applications and applications on AWS. Although AI (machine learning and LLMs) can be used for security purposes, this guide focuses on the foundational security controls to protect AI workloads deployed on AWS.

## Intended audience
<a name="intended-audience.3509e8c7-6c15-55c2-b32a-bd9dbbc00e76"></a>

The intended audience for this guidance is security professionals, architects, and developers who are responsible for securely integrating generative AI capabilities into their organizations and applications using AWS services.

**In this guide:**
+ About the AWS SRA library
+ AWS SRA for AI
+ Generative AI capabilities
+ Integrating a traditional cloud workload with Amazon Bedrock
+ Conclusion

### Attachments
<a name="attachments-a349f18f-a9fd-43a3-9a48-27534bf6412a"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
