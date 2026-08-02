---
source_url: https://docs.aws.amazon.com/generative-ai-on-aws-how-to-choose/index.html
---

# Choosing an AWS generative AI service

Determine which AWS generative AI services are the best fit for your organization.

## Overview of AWS generative AI services

Generative AI is a set of artificial intelligence (AI) systems and models designed to generate content such as code, text, images, music, or other forms of data. These systems can produce new content based on patterns and knowledge learned from existing data.

*This twelve-minute video discusses building generative AI applications on AWS, part one of a four-part series. View [part two](https://www.youtube.com/watch?v=HUuO9eJbOTk), [part three](https://www.youtube.com/watch?v=JbizhCFmC20), and [part four](https://www.youtube.com/watch?v=gNY06JM6m8U).*

[Video](https://www.youtube.com/embed/WEKTpzvJiec?si=39jHcyiMGTfiO2zB)

**Increasingly, organizations and businesses are using generative AI to:**
- **Automate creative workflows:** Use generative AI services to automate the workflows of time-consuming creative processes such as writing, image or video creation, and graphic design.
- **Customize and personalize content:** Generate targeted content, product recommendations, and customized offerings for an audience-specific context.
- **Augment data:** Synthesize large training datasets for other ML models to unlock scenarios where human-labeled data is scarce.
- **Reduce cost:** Potentially lower costs by using synthesized data, content, and digital assets.
- **Faster experimentation:** Test and iterate on more content variations and creative concepts than would be possible manually.

## Key concepts

Amazon offers a range of generative AI services, applications, tools, and supporting infrastructure. Which of these you use depends largely on what you’re trying to accomplish, how much choice you need in foundation models, the degree of customization you need in your generative AI applications, and the expertise within your organization.

**Foundation models and types**

Foundation models (FMs) are the backbone of generative AI. These pre-trained AI models can be customized for specific tasks, and come in various types:

- **Text models:** Process and generate natural language
- **Image models:** Work with visual data for tasks like image generation or analysis
- **Multimodal models:** Handle multiple types of data simultaneously

The capabilities of an FM are often related to its size, measured in parameters. Larger models can capture more complex patterns, but require more computational resources.

After you've decided on a generative AI service, choose the foundation model (FM) that gives you the best results for your use case. Amazon Bedrock has a [model evaluation capability](/bedrock/latest/userguide/evaluation.html) that can assist in evaluating, comparing, and selecting the best FMs for your use case.

- **Public foundation models**: Amazon Bedrock provides access to a variety of foundation models from different companies. These include [Anthropic Claude](https://aws.amazon.com/bedrock/claude/), [Cohere Command & Embed](https://aws.amazon.com/bedrock/cohere-command-embed/), [AI21 Labs Jurassic](https://aws.amazon.com/bedrock/jurassic/), [Meta Llama](https://aws.amazon.com/bedrock/llama/), [Mistral AI](https://aws.amazon.com/bedrock/mistral/), [Stable Diffusion XL](https://aws.amazon.com/bedrock/stable-diffusion/), [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/), and [Amazon Titan](https://aws.amazon.com/bedrock/titan/). With this multi-model approach, you can select and compare different models based on your specific use case requirements. Using Amazon Bedrock and Amazon SageMaker AI, you can experiment with a variety of foundation models, and privately customize them with your data.

[Learn more](https://aws.amazon.com/what-is/foundation-models/)

- **Model customization and enhancement**: Adapting FMs to specific use cases is crucial for optimal performance. Key customization techniques include: - **Fine-tuning**: Further training the model on domain-specific data - **Continuous pre-training**: Extending the model's knowledge with new data over time - **RAG ([retrieval augmented generation](/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html))** : Enhancing responses by retrieving external information Prompt engineering is another vital skill, allowing users to craft inputs that guide the model to produce desired outputs effectively.

[Get started](/bedrock/latest/userguide/custom-models.html)

- **Performance considerations**: When you evaluate generative AI model performance, consider two factors: - **Inference latency**: The speed at which a model generates responses - **Context window**: Amount of text a model can consider at once

[Get started](/prescriptive-guidance/latest/gen-ai-workload-assessment/introduction.html)

- **Data considerations**: The quality and quantity of data significantly impact model performance. Key factors include: - **Proper data handling**: Ensuring data security and privacy, effective annotation and labeling processes, and the right balance between data quantity with quality - **Data relevance**: How well the data matches the intended use case - **Data accuracy and consistency** - **Bias and fairness**: Ensuring training data doesn't perpetuate harmful biases

[Learn more]( https://aws.amazon.com/blogs/big-data/data-governance-in-the-age-of-generative-ai/)

## Use cases

Transform business processes and content creation with AI-powered automation and insights

### Enterprise knowledge management and support

- Querying and analyzing company data across multiple enterprise systems
- Generating summaries and insights from internal documents
- Creating automated responses for customer service
- Accessing and synthesizing information from various business data sources like Salesforce, SharePoint, and Confluence

**Learn more:**[New Amazon Bedrock capabilities enhance data processing and retrieval](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-capabilities-enhance-data-processing-and-retrieval/)

[Amazon Q Business](/amazonq)
[Amazon Bedrock](/bedrock)
[Amazon Sagemaker AI](/sagemaker)

### Software development and DevOps

- Code generation and optimization
- Application testing and debugging
- Infrastructure management and AWS resource optimization
- Automated code upgrades and security fixes
- Technical documentation creation and maintenance

**Get started:**[How generative AI is transforming developer workflows at Amazon](https://aws.amazon.com/blogs/devops/how-generative-ai-is-transforming-developer-workflows-at-amazon/)

[Amazon Q Developer](/amazonq)

### Content creation & customizations

- Automated writing and content generation
- Image and multimedia content creation
- Personalized content and recommendations for specific audiences
- Document classification and analysis
- Converting data into visualizations and reports

**Get started:**[Experiment with Amazon Nova foundation models](https://nova.amazon.com/chat)

[Amazon Bedrock](/bedrock)
[Amazon Nova](/nova)

### Business process automation

- Automating creative workflows and time-consuming manual tasks
- Building conversational AI applications and chatbots
- Data analysis and pattern recognition
- Creating synthetic training data for ML models
- Process automation through multi-step reasoning and planning

**Get started:**[Amazon Q Business is adding new workflow automation capability and 50+ action integrations](https://aws.amazon.com/blogs/aws/amazon-q-business-is-adding-new-workflow-automation-capability-and-50-action-integrations/)

[Amazon Bedrock](/bedrock)
[Amazon SageMaker AI](/sagemaker)
[Amazon Q](/amazonq)

## Compare services

The AWS generative AI stack provides options at every layer of implementation, from ready-to-use applications to foundational infrastructure. This diagram shows how these services relate to each other.

 As you choose services, consider your team’s technical expertise, development timeline, and
            specific use case requirements. The following table helps you match your business needs to the
            appropriate AWS service.

| If you need to... | To get started |
| --- | --- |
| Generate code and get answers to business questions across your enterprise data | [Amazon Q Business](/amazonq/latest/qbusiness-ug/setting-up.html) <br> [Amazon Q Developer in chat applications](/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html) |
| Choose from multiple foundation models, customize them with your data, and build generative AI applications | [Amazon Bedrock](/bedrock/latest/userguide/getting-started.html) <br> [Amazon Nova](/nova/latest/userguide/getting-started.html) <br> [Amazon Titan](/bedrock/latest/userguide/titan-models.html) |
| Build, train, and deploy machine learning models at scale | [Amazon SageMaker AI](/sagemaker/latest/dg/gs.html) |
| Maximize price-performance for foundation model training and inference | [AWS Trainium](/dlami/latest/devguide/trainium.html) <br> [AWS Inferentia](/eks/latest/userguide/inferentia-support.html) |

![Diagram showing the AWS generative AI stack. This diagram shows the infrastructure to build and train AI models at the bottom of the stack, models and tools to build generative AI apps in the middle, and applications that use LLMs and other FMs to boost productivity, at the top.](/images/generative-ai-on-aws-how-to-choose/images/gen-ai-stack.png)

## Start building

Now that we've covered the criteria you need to apply in choosing an AWS generative AI service, you can select which services are optimized for your needs and explore how you might get started using each of them.

### Amazon Q Business

**[What is Amazon Q Business?](/amazonq/latest/qbusiness-ug/what-is.html)**
Get an overview of Amazon Q Business, with explanations of what it is, how it works, and how to get started using it.

**[Create a sample Amazon Q Business application](/amazonq/latest/qbusiness-ug/quick-create-app.html)**
Learn how to create your first Amazon Q Business application in either the AWS Management Console or using the command line interface (CLI).

**[Combine Amazon Q Business and AWS IAM Identity Center to build generative AI](https://aws.amazon.com/blogs/machine-learning/build-private-and-secure-enterprise-generative-ai-apps-with-amazon-q-business-and-aws-iam-identity-center/)**
Build private and secure enterprise generative AI apps with Amazon Q Business and AWS IAM Identity Center.

### Amazon Q Developer

**[What is Amazon Q Developer?](/amazonq/latest/qdeveloper-ug/what-is.html)**
Get an overview of Amazon Q Developer, with explanations of what it is, how it works, and how to get started using it.

**[Understanding tiers of service for Amazon Q Developer](/amazonq/latest/qdeveloper-ug/q-tiers.html)**
Review the following information to understand the tiers of service for Amazon Q Developer, including Amazon Q Developer Pro and Amazon Q Developer at the free tier.

**[Working with Amazon Q Developer](https://builder.aws.com/learn/topics/agentic-ai)**
Use the Amazon Q Developer Center for fast access to key Amazon Q Developer articles, blog posts, videos, and tips.

### Amazon Bedrock

**[What is Amazon Bedrock?](/bedrock/latest/userguide/what-is-bedrock.html)**
Learn how to use this fully managed service to make foundation models (FMs) from Amazon and third parties available for your use through a unified API.

**[Frequently asked questions about Amazon Bedrock](https://aws.amazon.com/bedrock/faqs/)**
Get answers to the most commonly-asked questions about Amazon Bedrock, including how to use agents, security considerations, details on Amazon Bedrock software development kits (SDKs), Retrieval Augmented Generation (RAG), how to use model evaluation, and how billing works.

**[Guidance for generating product descriptions with Amazon Bedrock](https://aws.amazon.com/solutions/guidance/generating-product-descriptions-with-amazon-bedrock/)**
Learn how to use Amazon Bedrock as part of a solution to automate your product review and approval process for an ecommerce marketplace or retail website.

### Amazon Bedrock IDE

Amazon Bedrock Studio, renamed to Amazon Bedrock IDE, is now available in Amazon SageMaker Unified Studio

**[What is Amazon Bedrock IDE?](/sagemaker-unified-studio/latest/userguide/bedrock.html)**
Use Amazon Bedrock IDE to discover Bedrock models, and build generative AI apps that use Bedrock models and features.

**[Build generative AI applications with Amazon Bedrock IDE](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-quickly-with-amazon-bedrock-in-sagemaker-unified-studio/)**
This blog post describes how you can build applications using a wide array of top performing models. It then explains how to evaluate and share your generative AI apps with Amazon Bedrock IDE.

**[Building a chat app with Amazon Bedrock IDE](/sagemaker-unified-studio/latest/userguide/create-chat-app.html)**
Build an Amazon Bedrock IDE chat agent app that allows users to chat with an Amazon Bedrock model through a conversational interface.

### Amazon SageMaker AI

**[What is Amazon SageMaker AI?](/sagemaker/latest/dg/whatis.html)**
Learn how you can use this fully managed machine learning (ML) service to build, train, and deploy ML models into a production-ready hosted environment.

**[Get started with Amazon SageMaker AI](/sagemaker/latest/dg/gs.html)**
Learn how to join an Amazon SageMaker AI domain, giving you access to SageMaker Studio and RStudio on SageMaker.

**[Get started with Amazon SageMaker JumpStart](/sagemaker/latest/dg/studio-jumpstart.html)**
Explore Amazon SageMaker JumpStart solution templates that set up infrastructure for common use cases, and executable example notebooks for machine learning with SageMaker.

### Amazon SageMaker Unified Studio

**[What is Amazon SageMaker Unified Studio?](/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html)**
Learn how you can use Amazon SageMaker Unified Studio to build, deploy, execute, and monitor workflows from a single interface.

**[An integrated experience for all your data and AI with Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/big-data/an-integrated-experience-for-all-your-data-and-ai-with-amazon-sagemaker-unified-studio/)**
Learn about the new Amazon SageMaker Unified Studio and explore how it unifies your analytic workloads.

**[Get started with Amazon SageMaker Unified Studio](/sagemaker-unified-studio/latest/userguide/getting-started.html)**
Learn how to gain access to Amazon SageMaker Unified Studio, create a project, and then add members to the project and use the sample JupyterLab notebook to begin building with a variety of tools and resources.

### Amazon Nova

**[What is Amazon Nova?](/nova/latest/userguide/what-is-nova.html)**
Explore Amazon Nova, a new generation of foundation models available on Amazon Bedrock.

**[Introducing Amazon Nova foundation models: Frontier intelligence and industry leading price performance](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/)**
Learn about the new Amazon Nova models, including examples of using Amazon Nova models to analyze complex documents and videos, understand charts and diagrams, generate engaging video content, and build sophisticated AI agents.

**[Get started with Amazon Nova in the Amazon Bedrock console](/nova/latest/userguide/getting-started-console.html)**
Learn how to use the playgrounds in the console to submit a text prompt to Amazon Nova models and generate a text or image response

### Amazon Titan

**[Amazon Titan in Amazon Bedrock overview](/bedrock/latest/userguide/titan-models.html)**
Get an overview of Amazon Titan foundation models (FMs) to support your use cases.

**[Cost-effective document classification using the Amazon Titan Multimodal Embeddings Model](https://aws.amazon.com/blogs/machine-learning/cost-effective-document-classification-using-the-amazon-titan-multimodal-embeddings-model/)**
Learn how you can use this model to categorize and extract insights from high volumes of documents of different formats. This blog explores how you can use it to help determine the next set of actions to take, depending on the type of document.

**[Build generative AI applications with Amazon Titan Text Premier, Amazon Bedrock, and AWS CDK](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-with-amazon-titan-text-premier-amazon-bedrock-and-aws-cdk/)**
Explore building and deploying two sample applications powered by Amazon Titan Text Premier in this blog post.

### AWS Trainium

**[Overview of AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)**
Learn about AWS Trainium, the second-generation machine learning (ML) accelerator that AWS purpose built for deep learning training of 100B+ parameter models. Each EC2 Trn1 instance deploys up to 16 AWS Trainium accelerators to deliver a high-performance, low-cost solution for deep learning (DL) training in the cloud.

**[Recommended Trainium Instances](/dlami/latest/devguide/trainium.html)**
Explore how AWS Trainium instances are designed to provide high performance and cost efficiency for deep learning model inference workloads.

**[Scaling distributed training with AWS Trainium and Amazon EKS](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/)**
If you're deploying your deep learning (DL) workloads using Amazon Elastic Kubernetes Service (EKS), learn how you can benefit from the general availability of EC2 Trn1 instances powered by Trainium—a purpose-built ML accelerator optimized to provide a high-performance, cost-effective, and massively scalable platform for training DL models in the cloud.

### AWS Inferentia

**[Overview of Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/)**
Understand how AWS designs accelerators to deliver high performance at the lowest cost for your deep learning (DL) inference applications.

**[AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/)**
Understand what Inferentia2 is optimized for and how it was designed to deliver higher performance, while lowering the cost of LLMs and generative AI inference.

**[Machine learning inference using Inferentia](/eks/latest/userguide/inferentia-support.html)**
Learn how to create an Amazon EKS cluster with nodes running EC2 Inf1 instances and optionally deploy a sample application. EC2 Inf1 instances are powered by AWS Inferentia chips, which are custom built by AWS to provide high-performance and low-cost inference in the cloud.

## Resources

- **Learn**: Public foundation models ([Anthropic Claude](https://aws.amazon.com/bedrock/claude/), [Cohere Command Embed](https://aws.amazon.com/bedrock/cohere-command-embed/), [AI21 Labs Jurassic](https://aws.amazon.com/bedrock/jurassic/),[Meta Llama](https://aws.amazon.com/bedrock/llama/), [Mistral AI](https://aws.amazon.com/bedrock/mistral/), [Stable Diffusion XL](https://aws.amazon.com/bedrock/stable-diffusion/), [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/),[Amazon Titan](https://aws.amazon.com/bedrock/titan/)) [PartyRock, an Amazon Bedrock Playground](https://partyrock.aws/) for hands-on prompt engineering experimentation
- **Build**: [Build private and secure enterprise generative AI apps with Amazon Q Business and IAM Identity Center](https://aws.amazon.com/blogs/machine-learning/build-private-and-secure-enterprise-generative-ai-apps-with-amazon-q-business-and-aws-iam-identity-center/) [Fine-tune and deploy language models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/fine-tune-and-deploy-language-models-with-amazon-sagemaker-canvas-and-amazon-bedrock/) [Build generative AI applications with Amazon Bedrock Studio](https://aws.amazon.com/blogs/aws/build-generative-ai-applications-with-amazon-bedrock-studio-preview/) [Build enterprise-grade applications with natural language using AWS App Studio (preview)](https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview/)
- **Discover**: [Amazon Q capabilities to reimagine developer experience](https://aws.amazon.com/blogs/aws/amazon-q-developer-now-generally-available-includes-new-capabilities-to-reimagine-developer-experience/) [Chat about your AWS account resources with Amazon Q](https://aws.amazon.com/blogs/devops/chat-about-your-aws-account-resources-with-amazon-q-developer/) [Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/)
