---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The Generative AI Application Builder on AWS solution provides the following features:

 **Rapid experimentation**

This solution allows users to experiment quickly by removing the heavy lifting required to deploy multiple instances with different configurations and compare outputs and performance. Experiment with multiple configurations of various LLMs, prompt engineering, enterprise knowledge bases, guardrails, AI agents, and other parameters.

 **Choice and configurability**

With pre-built connectors to a variety of LLMs, such as models available through Amazon Bedrock, this solution gives you the flexibility to deploy the model of your choice, as well as the AWS and leading FM services you prefer. You can also enable Amazon Bedrock Agents to fulfill various tasks and workflows.

 **Agent Builder**

Build and deploy production-ready AI agents with full lifecycle management. Configure system prompts, integrate Model Context Protocol (MCP) servers for enterprise tools and data access, and enable memory capabilities for context retention across conversations. Agents are deployed on Amazon Bedrock AgentCore with extended runtime support and real-time streaming responses.

 **Workflow Builder**

Orchestrate multiple Agent Builder agents into complex workflows using hierarchical delegation. Create a supervisor agent that autonomously selects and coordinates specialized Agent Builder agents to handle multi-step tasks. Configure agent descriptions, delegation strategies, and workflow-level memory while reusing existing Agent Builder deployments.

 **Production-ready**

Built with AWS Well-Architected design principles, this solution offers enterprise-grade security and scalability with high availability and low latency, ensuring seamless integration into your applications with high performance standards.

 **Extensible modular architecture**

Extend this solution’s functionality by integrating your existing projects or natively connecting additional AWS services. Because this is an open-source application, you can use the included LangChain orchestration layer or Lambda functions to connect with the services of your choice.

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both AWS Service Catalog AppRegistry and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources.
