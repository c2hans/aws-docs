---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/layered-approach.html
---

# Adopting a layered approach for generative AI development
<a name="layered-approach"></a>

To build a robust and scalable generative AI platform, organizations need a comprehensive environment that enables innovation while maintaining control and security. This strategy document recommends an enterprise-ready environment that consists of four essential layers, which are shown in the following image.

![The four layers of an enterprise-ready generative AI environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/images/guide-img/d1de6eb7-906b-4581-b4e9-93e995f9bb3c/images/d0d911df-cc0e-4b04-b200-879f64735e35.png)

Each of the following layers plays a crucial role in successful generative AI adoption and scaling across the enterprise:

1. **Data and compute infrastructure** – Reliable infrastructure provides the foundation for developing, training, and deploying generative AI applications. This layer makes sure that organizations have the necessary computational resources and data management capabilities to support various use cases, from small experiments to large-scale production deployments. For Amazon Elastic Compute Cloud (Amazon EC2), consider using [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/), [UltraClusters](https://aws.amazon.com/ec2/ultraclusters/), [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html), [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html), [AWS Nitro System](https://aws.amazon.com/ec2/nitro/), and [AWS Neuron](https://aws.amazon.com/ai/machine-learning/neuron/).

1. **Approved foundation models and tools** – This layer allows your organization to access approved, pretrained models while maintaining security and compliance. Teams can experiment with different models, evaluate their effectiveness, and select the most appropriate ones for specific use cases. You can use [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) to establish guardrails, build agents, customize models, or import your own custom model.

1. **Security and governance** – This layer helps you make sure that generative AI applications adhere to organizational policies, compliance requirements, legal and privacy requirements, and ethical guidelines. In this layer, you implement consistent security controls and governance mechanisms across all generative AI initiatives.

1. **Repeatable application patterns** – This layer accelerates development and promotes consistency by providing standardized templates and best practices for common generative AI use cases. Providing repeatable patterns helps prevent duplication of effort and enables rapid scaling of successful solutions. Examples of repeatable patterns include intelligent document processing, Retrieval Augmented Generation (RAG), chat-based assistants, and agentic workflows.

This layered approach provides the following key benefits:
+ It clearly separates the different aspects of generative AI implementation.
+ It promotes consistent security and governance across all generative AI initiatives.
+ It helps you build scalable infrastructure that grows with organizational needs.
+ It standardizes approaches that accelerate development.
+ It reduces risk through proven patterns and practices.

By implementing these four layers, organizations can create a solid foundation for their generative AI initiatives while maintaining the flexibility to adapt to new requirements and opportunities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
