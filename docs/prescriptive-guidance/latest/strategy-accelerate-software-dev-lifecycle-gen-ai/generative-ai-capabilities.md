---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-software-dev-lifecycle-gen-ai/generative-ai-capabilities.html
---

# Foundational capabilities for an AI-powered software development experience
<a name="generative-ai-capabilities"></a>

To successfully implement a generative AI-powered software development experience, you need to establish a set of foundational capabilities that span multiple personas in your organization. These capabilities represent your ability to effectively deploy resources, implement processes, and achieve desired outcomes in the context of AI-powered software development. By cultivating these capabilities, you create a robust foundation that helps you seamlessly integrate generative AI across all stages of the SDLC.

AWS provides key services to help you implement these capabilities. For example, [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) helps accelerate software development by acting as an AI-powered assistant. [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) helps you get fast, relevant answers to pressing questions, solve problems, and generate content. It can also act on your behalf by integrating tools related to software development. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) provides access to foundation models and broad set of capabilities to customize specific development workflows and requirements.

By cultivating these capabilities through AWS services, you create a robust foundation that helps you seamlessly integrate generative AI across all stages of the SDLC.

The following are the foundational capabilities that you should focus on:
+ [Project management](generative-ai-capabilities-proj-mgmt.md)
+ [Requirement management](generative-ai-capabilities-req-mgmt.md)
+ [Architecture and design](generative-ai-capabilities-arch-design.md)
+ [Collaboration](generative-ai-capabilities-collaboration.md)
+ [DevSecOps](generative-ai-capabilities-devsecops.md)
+ [Operation and maintenance](generative-ai-capabilities-ops-maintenance.md)
+ [AI assistants](generative-ai-capabilities-assistants.md)
+ [Analytics and insights](generative-ai-capabilities-analytics.md)
+ [Knowledge management](generative-ai-capabilities-knowledge-mgmt.md)
+ [Extensibility](generative-ai-capabilities-extensibility.md)

Each foundational capability integrates with the framework dimensions and the different stages of the SDLC. This integration helps you use AI capabilities effectively throughout your software development process. It enhances efficiency, quality, and innovation at every step. The synergy between these foundational capabilities, the framework, and the SDLC stages creates a comprehensive ecosystem for AI-powered software development. This helps you harness the full potential of generative AI, drive continuous improvement, accelerate development cycles, and deliver quality software products.

The following table shows how the foundational capabilities and subcapabilities map to the framework dimensions and the SDLC phases.

|
|
| **Capability: subcapability** | **Investigate** | **Integrate** | **Interact** | **Iterate** | **Impact** |
| --- |--- |--- |--- |--- |--- |
| **Project management: **Issue management | Requirements and planning | None | None | None | None |
| **Project management: **Sprint and task management | Requirements and planning | Requirements and planning | None | None | None |
| **Project management: **Product backlog management | Requirements and planning | None | None | Requirements and planning | None |
| **Project management: **User stories mapping | Requirements and planning | None | None | None | None |
| **Project management: **Reporting and analytics | Requirements and planning | None | None | None | Requirements and planning |
| **Project management: **Product roadmap management | Requirements and planning | None | Requirements and planning | None | None |
| **Project management: **Feedback loops | None | None | None | Requirements and planning | None |
| **Project management: **Retrospectives | None | None | None | Requirements and planning | None |
| **Requirement management** | Requirements and planning | Requirements and planning | None | None | None |
| **Architecture and design: **Solution design | Design and architecture | Design and architecture | None | None | None |
| **Collaboration: **Documentation management | All SDLC phases | None | All SDLC phases | None | None |
| **Collaboration: **Knowledge sharing | All SDLC phases | None | All SDLC phases | None | None |
| **Collaboration: **Project asset management | None | All SDLC phases | All SDLC phases | None | None |
| **DevSecOps: **CI/CD | Testing, Deployment | Implementation, Testing, Deployment | Deployment | None | None |
| **DevSecOps: **DevOps security | Implementation | Implementation, Testing, Operation and maintenance | None | Implementation, Testing, Operation and maintenance | None |
| **DevSecOps: **Application performance monitoring | None | Operation and maintenance | None | None | None |
| **DevSecOps: **Log aggregation and analytics | Operation and maintenance | Operation and maintenance | None | None | None |
| **DevSecOps: **AIOps | Operation and maintenance | None | None | Operation and maintenance | None |
| **DevSecOps: **Continuous improvement | None | None | None | Operation and maintenance | None |
| **DevSecOps: **Dashboard monitoring | None | Operation and maintenance | None | None | None |
| **DevSecOps: **Performance insights | Operation and maintenance | None | None | Operation and maintenance | None |
| **Operation and maintenance: **Incident management | None | None | None | Operation and maintenance | None |
| **Operation and maintenance: **Code upgrades | None | Operation and maintenance | None | None | None |
| **Operation and maintenance: **Code optimization | Operation and maintenance | Operation and maintenance | None | None | None |
| **Operation and maintenance: **Technical debt management | None | Operation and maintenance | Operation and maintenance | None | None |
| **Operation and maintenance: **Change management | None | Implementation, Deployment | None | None | None |
| **Operation and maintenance: **Reverse engineering | Operation and maintenance | None | None | None | None |
| **Operation and maintenance: **Code modernization | None | Implementation | None | None | None |
| **Operation and maintenance: **Performance optimization | None | Operation and maintenance | None | Operation and maintenance | None |
| **Analytics and insights** | None | Requirements and planning | None | None | All SDLC phases |
| **AI assistant** | None | None | All SDLC phases | None | None |
| **Knowledge management** | None | None | All SDLC phases | None | None |
| **Extensibility** | None | Deployment | None | None | None |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
