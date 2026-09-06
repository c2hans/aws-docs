---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-machine-learning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Machine Learning
<a name="amazon-machine-learning"></a>

AWS offers the broadest and deepest set of [machine learning services](https://aws.amazon.com/machine-learning/#Explore_AWS_Machine_Learning_services) and supporting cloud [infrastructure](https://aws.amazon.com/machine-learning/infrastructure/?c=ml&sec=int), putting machine learning in the hands of every developer, data scientist, and expert practitioner. When you build an ML-based workload in AWS, you can choose from three different levels of ML services to balance speed-to-market with level of customization and ML skill level:
+ [Artificial Intelligence (AI) services](https://aws.amazon.com/machine-learning/ai-services/)
+ [ML services](https://aws.amazon.com/machine-learning/)
+ [ML frameworks and infrastructure](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-stack.html)

The AI Services level provides fully managed services that enable you to quickly add ML capabilities to your workloads using API calls. This gives you the ability to build powerful, intelligent applications with capabilities such as computer vision, speech, natural language, chatbots, predictions, and recommendations. Services at this level are based on pre-trained or automatically trained machine learning and deep learning models, so you don’t need ML knowledge to use them.

You can use:
+ [Amazon Translate](https://aws.amazon.com/translate/) to translate or localize text content
+ [Amazon Polly](https://aws.amazon.com/polly/) for text-to-speech conversion
+ [Amazon Lex](https://aws.amazon.com/lex/) for building conversational chat bots
+ [Amazon Comprehend](https://aws.amazon.com/comprehend/?c=ml&sec=srv) to extract insights and relationships from unstructured data
+ [Amazon Forecast](https://aws.amazon.com/forecast/?c=ml&sec=srv) to build accurate forecasting models
+ [Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/?c=ml&sec=srv) to identify potentially fraudulent online activities,
+ [Amazon CodeGuru](https://aws.amazon.com/codeguru/?c=ml&sec=srv) to automate code reviews and to identify most expensive lines of code
+ [Amazon Textract](https://aws.amazon.com/textract/?c=ml&sec=srv) to extract text and data from documents automatically
+ [Amazon Rekognition](https://aws.amazon.com/rekognition/?blog-cards.sort-by=item.additionalFields.createdDate&blog-cards.sort-order=desc) to add image and video analysis to your applications
+ [Amazon Kendra](https://aws.amazon.com/kendra/?c=ml&sec=srv) to reimagines enterprise search for your websites and applications
+ [Amazon Personalize](https://aws.amazon.com/personalize/?c=ml&sec=srv) for real-time personalized recommendations
+ [Amazon Transcribe](https://aws.amazon.com/transcribe/?c=ml&sec=srv) to add speech to text capabilities to your applications

The ML Services level provides managed services and resources for machine learning to developers, data scientists, and researchers.
+ [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) enables developers and data scientists to quickly and easily build, train, and deploy ML models at any scale.
+ [Amazon SageMaker AI Ground Truth](https://aws.amazon.com/sagemaker/groundtruth/) helps you build highly accurate ML training datasets quickly.
+ [Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) is the first integrated development environment for machine learning to build, train, and deploy ML models at scale.
+ [Amazon SageMaker AI Autopilot](https://aws.amazon.com/sagemaker/autopilot/) automatically builds, trains, and tunes the best ML models based on your data, while enabling you to maintain full control and visibility.
+ [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/getting-started/) helps you quickly and easily get started with ML.
+ [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) reduces the time it takes to aggregate and prepare data for ML from weeks to minutes.
+ [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) is a fully managed, purpose-built repository to store, update, retrieve, and share ML features.
+ [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) provides ML developers with greater visibility into your training data and models so you can identify and limit bias and explain predictions.
+ [Amazon SageMaker AI Debugger](https://aws.amazon.com/sagemaker/debugger/) optimizes ML models with real-time monitoring of training metrics and system resources.
+ [Amazon SageMaker AI's distributed training libraries](https://aws.amazon.com/sagemaker/distributed-training/) automatically split large deep learning models and training datasets across AWS graphics processing unit (GPU) instances in a fraction of the time it takes to do manually.
+ [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) is the first purpose-built, easy-to-use continuous integration and continuous delivery (CI/CD) service for ML.
+ [Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/) enables developers to train ML models once, and then run them anywhere in the cloud or at the edge.

The [ML Frameworks and Infrastructure](https://aws.amazon.com/machine-learning/infrastructure/?c=ml&sec=int) level is intended for expert ML practitioners. These people are comfortable with designing their own tools and workflows to build, train, tune, and deploy models, and are accustomed to working at the framework and infrastructure level. In AWS, you can use open-source ML frameworks such as TensorFlow, PyTorch, and Apache MXNet. The Deep Learning AMI and Deep Learning Containers in this level have multiple ML frameworks preinstalled that are optimized for performance. This optimization means that they are always ready to be launched on powerful, ML-optimized compute infrastructure, such as Amazon EC2 P3 and P3dn instances, that provides a boost of speed and efficiency to ML workloads.

Amazon ML can create ML models based on data stored in S3, Amazon Redshift, or Amazon RDS. Built-in wizards guide you through the steps of interactively exploring your data to training the ML model, evaluate the model quality, and adjust outputs to align with business goals. After a model is ready, you can request predictions in batches, or using the low-latency real-time API.

Workloads often use services from multiple levels of the ML stack. Depending on the business use case, services and infrastructure from the different levels can be combined to satisfy multiple requirements and achieve multiple business goals. For example, you can use AI services for sentiment analysis of customer reviews on your retail website, and use managed ML services to build a custom model using your own data to predict future sales.

## Ideal usage patterns
<a name="ideal-usage-patterns-aml"></a>

 Amazon ML is ideal for discovering patterns in your data and using these patterns to create ML models that can generate predictions on new, unseen data points. For example, you can:
+  **Enable applications to flag suspicious transactions** – Build an ML model that predicts whether a new transaction is legitimate or fraudulent.
+  **Forecast product demand** – Input historical order information to predict future order quantities.
+  **Media intelligence ** – Maximize the value of media content by adding machine learning to media workflows such as search and discovery, content localization, compliance, monetization, and more.
+  **Personalize application content** – Predict which items a user will be most interested in, and retrieve these predictions from your application in real-time.
+  **Predict user activity** – Analyze user behavior to customize your website and provide a better user experience.
+  **Listen to social media** – Ingest and analyze social media feeds that potentially impact business decisions.
+  **Intelligent contact center** – Enhance your customer service experience and reduce costs by integrating ML into your contact center.
+  **Intelligent search** – Boost business productivity and customer satisfaction by delivering accurate and useful information faster from siloed and unstructured information sources across the organization.

## Cost model
<a name="cost-model-aml"></a>

With Amazon Machine Learning services, you pay only for what you use. There are no minimum fees and no upfront commitments.

AWS pre-trained AI Services cost model varies depending upon the AI service you are planning to integrate with your applications. For details, see pricing details of the respective AI services:
+ [Amazon Comprehend](https://aws.amazon.com/comprehend/pricing/)
+ [Amazon Forecast](https://aws.amazon.com/forecast/pricing/)
+ [Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/pricing/)
+ [Amazon Translate](https://aws.amazon.com/translate/pricing/)
+ [Amazon CodeGuru](https://aws.amazon.com/codeguru/pricing/)
+ [Amazon Textract](https://aws.amazon.com/textract/pricing/)
+ [Amazon Rekognition](https://aws.amazon.com/rekognition/pricing/?nc=sn&loc=4)
+ [Amazon Polly](https://aws.amazon.com/polly/pricing/?nc=sn&loc=4)
+ [Amazon Lex](https://aws.amazon.com/lex/pricing/?nc=sn&loc=3)
+ [Amazon Kendra](https://aws.amazon.com/kendra/pricing/)
+ [Amazon Personalize](https://aws.amazon.com/personalize/pricing/)
+ [Amazon Transcribe](https://aws.amazon.com/transcribe/pricing/?nc=sn&loc=3)

With [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), you have two choices to pay, and you only pay for what you use:
+ **On-demand pricing** is billed by the second, with no minimum fees and no upfront commitments.
+ **SageMaker Savings Plans** offer a flexible, usage-based pricing model in exchange for a commitment to a consistent amount of usage. For details, see [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/).

The ML Frameworks and Infrastructure level is intended for expert ML practitioners. ML training and inference workloads can exhibit characteristics that are steady state (such as hourly batch tagging of photos for a large population), spiky (such as kicking off new training jobs or search recommendations during promotional periods), or both. AWS has pricing options and solutions to help you optimize your infrastructure performance and costs.

For details, see the [AWS Machine Learning Infrastructure](https://aws.amazon.com/machine-learning/infrastructure/).

## Performance
<a name="performance-aml"></a>

The time it takes to create models and to request predictions from ML models depends on the number of input data records, and the types and distribution of attributes that you specify. There are a number of principles designed to help increase performance specifically for ML workloads:
+ **Optimize compute for your ML workload** — Most ML workloads are very compute-intensive, because large amounts of vector multiplications and additions need to be performed on a multitude of data and parameters. Especially in Deep Learning, there is a need to scale to chipsets that provide larger queue depth, higher Arithmetic Logic Units and Register counts, to allow for massively parallel processing. Because of that, GPUs are the preferred processor type to train a Deep Learning model.
+  **Define latency and network bandwidth performance requirements for your models ** — Some of your ML applications might require near-instantaneous inference results to satisfy your business requirements. Offering the lowest latency possible may require the removal of costly round trips to the nearest API endpoints. This reduction in latency can be achieved by running the inference directly on the device itself. This is known as *Machine Learning at the Edge*. A common use case for such a requirement is predictive maintenance in factories. This form of low latency and near-real-time inference at the edge allows for early indications of failure, potentially mitigating costly repairs of machinery before the failure actually happens.
+ **Continuously monitor and measure system performance ** — The practice of identifying and regularly collecting key metrics related to the building, training, hosting, and running predictions against a model ensures that you are able to continuously monitor the holistic success across key evaluation criteria. To validate system level resources used to support the phases of ML workloads, it’s key to continuously collect and monitor system level resources such as compute, memory, and network. Requirements for ML workloads change in different phases, as training jobs are more memory intensive, while inference jobs are more compute intensive.

## Durability and availability
<a name="durability-and-availability-aml"></a>

There are key principles designed to help increase availability and durability specifically for ML workloads:
+ **Manage changes to model inputs through automation ** — ML workloads have additional requirements to manage changes to the data that is used to train a model to be able to recreate the exact version of a model in the event of failure or human error. Managing versions and changes through automation provides for a reliable and consistent recovery method.
+ **Train once and deploy across environments ** — When deploying the same version of an ML model across multiple accounts or environments, the same practice of build once that is applied to application code should be applied for model training. A specific version of a model should only be trained once and the output model artifacts should be utilized to deploy across multiple environments to avoid bringing in any unexpected changes to the model across environments.

## Scalability and elasticity
<a name="scalability-and-elasticity-aml"></a>

There are key principles designed to help increase availability and durability specifically for ML workloads:
+ **Identify the end-to-end architecture and operational model early** — Early in the ML development lifecycle, identify the end-to-end architecture and operational model for model training and hosting. This allows for early identification of architectural and operational considerations that will be required for the development, deployment, management and integration of ML workloads.
+ **Version machine learning inputs and artifacts** — Versioned inputs and artifacts enable you to recreate artifacts for previous versions of your ML workload. Version inputs are used to create models, including training data and training source code, and model artifacts.
+ **Automate machine learning deployment pipelines** — Minimize human touch points in ML deployment pipelines to ensure that ML models are consistently and repeatedly deployed using a pipeline that defines how models move from development to production. Identify and implement a deployment strategy that satisfies the requirements of your use case and business problem. If required, include human quality gates in your pipeline to have humans evaluate if a model is ready to deploy to a target environment.

## Interfaces
<a name="interfaces-aml"></a>

Creating a data source is as simple as adding your data to S3. To ingest data, you can use Direct Connect to privately connect your data center directly to an AWS Region. To physically transfer petabytes of data in batches, use AWS Snowball Edge, or, if you have exabytes of data, use AWS Snowmobile. You can integrate your existing on-premises storage using Storage Gateway, or add cloud capabilities using AWS Snowball Edge Edge. Use Amazon Data Firehose to collect and ingest multiple streaming-data sources.

## Anti-patterns
<a name="anti-patterns-aml"></a>

 Amazon ML has the following anti-patterns:
+ **Big data processing** – Data processing activities are well suited for tools like Apache Spark, which provide SQL support for data discovery, among other useful utilities. On AWS, Amazon EMR facilitates the management of Spark clusters, and enables capabilities like elastic scaling while minimizing costs through Spot Instance pricing.
+ **Real-time analytics** – Collecting, processing, and analyzing the streaming data to respond in real time are well suited for tools like Kafka. On AWS, [Amazon Kinesis](https://aws.amazon.com/kinesis/?c=a&sec=uc) makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information and [Amazon MSK](https://aws.amazon.com/msk/?c=a&sec=uc) is a fully managed service that makes it easy for you to build and run applications that use [Apache Kafka](https://aws.amazon.com/streaming-data/what-is-kafka/) to process streaming data. Apache Kafka is an open-source platform for building real-time streaming data pipelines and applications.
