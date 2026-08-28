---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/model-execution-strategies.html
---

# Model execution strategies for AI workloads
<a name="model-execution-strategies"></a>

At the core of any AI architecture is the model execution layer, the component that performs inference, powers predictions, or generates content. AWS offers two powerful, serverless-ready paths for executing AI workloads:
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) provides access to foundation models (FMs) for generative AI use cases.
+ [Amazon SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) enables scalable deployment of custom-trained models for traditional machine learning (ML) workloads.

By understanding when and how to use each AWS service, enterprises can optimize for both business needs and operational efficiency.

## Amazon Bedrock: Foundation models as a service
<a name="9999999999999999brlong---foundation-models-as-a-service.1a3207bb-dc2f-51ce-a065-c96caeaa5ee5"></a>

Amazon Bedrock is a fully managed service that provides serverless access to FMs from leading AI providers such as Anthropic (Claude), Meta (Llama), Mistral, Cohere, and Amazon Titan and [Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html). You can interact with these models using simple API calls, without needing to provision infrastructure, manage GPUs, or fine-tune models.

Key capabilities of Amazon Bedrock include the following:
+ **Text generation** – Summarization, rewriting, content creation, and Q&A.
+ **Code generation** – Natural language to code.
+ **Classification and extraction** – Labeling, parsing, and semantic tagging.
+ **RAG workflows** – Integrate with knowledge bases for grounded responses.
+ **Agents** – Enable autonomous orchestration and tool use.
+ **Multimodal intelligence** – Through Amazon Nova, understand and generate across text, image, and video.
+ **Fine-tuning and distillation support** – Through Amazon Nova Premier, train task-specific models or create compact student models.
+ **Tiered performance and cost** – Select from Amazon Nova Micro, Nova Lite, Nova Pro, and Nova Premier models to balance latency, accuracy, and price.

Operational benefits of Amazon Bedrock include the following:
+ **Model management** – No model hosting or versioning required.
+ **Secure data handling** – Isolated tenant environment and no training on user data.
+ **Token-based billing** – Provides predictable cost modeling.
+ **Multimodal API unification** – Handles input/output across images, video, and text through the same Amazon Bedrock interface.
+ **Low-latency options** – Available with Amazon Nova Micro and Nova Lite that are ideal for edge and user-facing generative AI apps.
+ **Enterprise grounding compatibility** – All Amazon Nova models are compatible with Amazon Bedrock Knowledge Bases and Retrieval Augmented Generation (RAG) architectures.

Amazon Bedrock integrates with other AWS services and features in the following ways:
+ Triggered from Lambda, Step Functions, or API Gateway
+ Integrated with Amazon Bedrock Agents for goal-driven orchestration
+ Works seamlessly with [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) and RAG pipelines

### Ideal use cases for Amazon Bedrock
<a name="ideal-use-cases-for-9999999999999999brlong-.0c69d78a-ecd2-5987-a0fa-440a21555750"></a>

Amazon Bedrock is well-suited for a variety of scenarios, such as the following:
+ **Generative AI tasks** - Create marketing content and documentation and power chatbots.
+ **Conversational assistants** - Build support bots and internal copilots.
+ **Knowledge retrieval** – Use for summarization and semantic search tasks.
+ **Dynamic planning** - Power agent-based decision systems.
+ **Multimodal generation** – Use [Amazon Nova Canvas](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html) to generate images, and use [Amazon Nova Reel](https://docs.aws.amazon.com/nova/latest/userguide/video-generation.html) to produce videos from prompts and structured context.
+ **Enterprise assistants** – Use [Amazon Nova Pro](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) to enable goal-driven decision-making tools that are grounded in proprietary data.
+ **Real-time user experience feedback** - Analyze and respond to customer actions with under 100ms latency by using Amazon Nova Micro.

## Amazon SageMaker Serverless Inference: Custom model hosting
<a name="9999999999999999smkrlong--serverless-inference--custom-model-hosting.fe8eba7d-c67e-5a8d-897b-2a9cfd3060e4"></a>

Amazon SageMaker Serverless Inference is designed for developers and data scientists who have trained their own models (for example, XGBoost, PyTorch, Scikit-learn, and TensorFlow). By using SageMaker Serverless Inference, they can deploy their models in a scalable, serverless environment.

Unlike Amazon Bedrock, SageMaker Serverless Inference gives you control over the model architecture, training data, and logic.

Key capabilities of SageMaker Serverless Inference include the following:
+ Hosts traditional ML models such as classification, regression, natural language processing (NLP), and forecasting
+ Supports multi-model endpoints
+ Supports automatic scaling so that compute is provisioned on-demand and shut down when idle
+ Runs inference on custom container images or prebuilt ML frameworks

Operational benefits of SageMaker Serverless Inference include the following:
+ Pay-per-inference model with zero idle costs
+ Fully managed endpoints and no server setup
+ Integrates with training pipelines and notebooks

SageMaker Serverless Inference integrates with other AWS services and features in the following ways:
+ Invoked by using AWS LambdaStep Functions, or SDK and API calls
+ Works with SageMaker Pipelines for end-to-end machine learning operations (MLOps)
+ Logs and metrics integrated with Amazon CloudWatch

### Ideal use cases for SageMaker Serverless Inference
<a name="ideal-use-cases-for-9999999999999999smkr--serverless-inference.2174b625-dbc4-57db-b65f-f92014bf6ea7"></a>

SageMaker Serverless Inference is a good choice for various machine learning applications:
+ **Predictive analytics** - Use for sales forecasting and churn prediction models.
+ **Text classification** - Supports tasks like spam detection and sentiment analysis.
+ **Image classification** - Enables document optical character recognition (OCR) and medical imaging applications.
+ **Custom natural language processing (NLP)** - Handles entity recognition and document tagging tasks.

## Choosing between Amazon Bedrock and SageMaker Serverless Inference
<a name="choosing-between-9999999999999999br--and-9999999999999999smkr--serverless-inference.39f03e11-c36e-5e5f-8db8-bfad22071c46"></a>

Both Amazon Bedrock and SageMaker Serverless Inference offer serverless paths to scalable, production-ready AI execution. Together, they form the core execution layer of modern, event-driven, serverless AI architectures on AWS. The following table compares these services across key dimensions.

|
|
| Dimension | Amazon Bedrock | SageMaker Serverless Inference |
| --- |--- |--- |
| Model type | Foundation models (LLMs) | Custom-trained ML models |
| Setup effort | Minimal (no training or hosting) | Requires model training and packaging |
| Use case | Generative, conversational, and semantic | Predictive, numerical, and structured data |
| Scalability | Fully serverless and auto-scaled | Fully serverless and auto-scaled |
| Cost model | Pay per token | Pay per inference |
| Integration | API Gateway, Lambda, Amazon Bedrock Agents, and RAG | Lambda, Step Functions, and CI/CD pipelines |
| Tuning required | None (zero-shot or few-shot) | Full control (hyperparameters and retraining) |

Choosing the right service depends on the nature of your AI workload:
+ Use Amazon Bedrock when you need semantic flexibility, goal-driven workflows, and rapid iteration with foundation models.
+ Use SageMaker Serverless Inference when you have proprietary models, structured inputs, or need full control over training and deployment.
+ Use SageMaker JumpStart to choose from hundreds of [built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) with pretrained models from model hubs, including TensorFlow Hub, PyTorch Hub, Hugging Face, and MxNet GluonCV.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
