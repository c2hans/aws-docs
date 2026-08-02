---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/edge-ai.html
---

# Edge AI and global inference distribution
<a name="edge-ai"></a>

Although cloud-based inference serves most enterprise use cases, certain scenarios require real-time responses, offline capabilities, or proximity to the data source or user. For these cases, *edge AI*, executing AI logic on or near the device, offers a powerful complement to serverless cloud architecture.

AWS supports edge AI through two key serverless technologies:
+ [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) runs inference logic globally at AWS edge locations by using Amazon CloudFront.

  **Example** – A global ecommerce site uses a Lambda@Edge function to personalize homepage content based on user location and language. As a result, it delivers tailored experiences instantly from the nearest CloudFront edge location.
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) enables local AI execution on connected devices.

  **Example** – A smart appliance uses a model deployed with AWS IoT Greengrass for real-time diagnostics, syncing insights to the cloud when needed or when connectivity permits.

Together, these technologies extend the reach of serverless AI to low-latency, bandwidth-sensitive, or offline environments, and globally distributed user bases.

## Lambda@Edge: Global inference at the CDN layer
<a name="9999999999999999lam--edge--global-inference-at-the-cdn-layer.2df75225-99b0-5ef6-a862-dd9e8b656a1a"></a>

By using Lambda@Edge, developers can run AWS Lambda functions at CloudFront edge locations. This approach reduces latency for end users and enables AI experiences that are context-aware and ultra- fast.

Key capabilities of Lambda@Edge include the following:
+ Runs logic at the CDN layer in response to CloudFront events such as viewer request and origin response
+ Customizes content such as webpage personalization and recommendations according to user, location, and device
+ Integrates AI inference directly into content delivery without routing to a central AWS Region
+ Deploys globally without provisioning infrastructure

### Use case examples of Lambda@Edge
<a name="use-case-examples-of-9999999999999999lam--edge.1d97f556-7818-53ea-af39-f85e2d4b5e38"></a>

Lambda@Edge enables the following key use cases:
+ **Ecommerce personalization** – Deliver dynamic product recommendations based on user ID and behavior.
+ **Media streaming** – Adjust recommendations and parental controls based on regional policies.
+ **Marketing campaigns **– Customize banners, content, and offers for each location.
+ **Multilingual user experience (UX)** – Detect user location and language to serve Amazon Bedrock LLM-translated content inline.

By placing inference logic as close to the user as possible, Lambda@Edge supports hyper-personalized, AI-driven front-end delivery, which is ideal for high-scale consumer applications.

Lambda@Edge is often used in tandem with Amazon Bedrockor SageMaker Serverless Inference by using asynchronous routing and caching strategies to combine speed with intelligence.

## AWS IoT Greengrass: Local inference at the edge
<a name="9999999999999999gglong---local-inference-at-the-edge.7215f3fb-432f-54b2-b3ed-dd99bb9b2193"></a>

AWS IoT Greengrass is a lightweight runtime that customers can use to run Lambda functions, ML inference, and custom code. It operates on edge devices such as industrial controllers, cameras, medical devices, or smart appliances.

Key capabilities of AWS IoT Greengrass include the following:
+ Runs Lambda functions locally even when disconnected from the cloud.
+ Packages ML models (through SageMaker or custom training) to perform inference directly on the device.
+ Streamlines updates through secure over-the-air deployment and configuration management.
+ Integrates with AWS services (for example, Amazon S3, AWS IoT Core, and Amazon CloudWatch) for centralized monitoring.

### Use case examples of AWS IoT Greengrass
<a name="use-case-examples-of-9999999999999999gglong-.7408646f-5e05-57d7-b14d-2d062f95d49d"></a>

AWS IoT Greengrass enables inference applications at the edge across multiple industries, such as the following:
+ **Manufacturing** – Detect defects from camera input without cloud round trips.
+ **Healthcare** – Monitor patients and perform diagnostics in clinics with intermittent connectivity.
+ **Agriculture** – Classify crop conditions using drone footage.
+ **Energy** – Monitor pipelines and turbines using anomaly detection models.

AWS IoT Greengrass enables these workloads to be fast, resilient, and independent of cloud latency, while still providing cloud-side management, observability, and synchronization. By using AWS IoT Greengrass, developers can deploy the same Lambda functions used in the cloud, creating continuity across centralized and distributed systems.

## Global and local AI: A tiered execution strategy
<a name="global-and-local-ai--a-tiered-execution-strategy.2911bae0-cdde-5ef1-9b4b-2660539162ec"></a>

Enterprises can combine Lambda@Edge and AWS IoT Greengrass to create a tiered edge AI system. This hybrid architecture enables intelligent decisions to be made at the right layer, depending on latency sensitivity, model size, connectivity, and compliance requirements. The following table describes the tiers, AWS technologies, and roles in this architecture.

|
|
| Tier | AWS technology | Technology role |
| --- |--- |--- |
| Device edge | AWS IoT Greengrass | On-deviceOffline-capableAI logicSensor data processing |
| Network edge | Lambda@Edge | Content personalizationLightweight AI near the userUltra-low latency |
| Cloud core | Amazon Bedrock, Amazon SageMaker Serverless Inference, and AWS Step Functions | Heavy AI inferenceOrchestrationAgent reasoningRAG pipelines |

## Summary of edge AI
<a name="summary-of-edge-ai.58514f52-5f09-5008-a4ed-adf71a3a1bd6"></a>

Edge AI is a natural evolution of serverless architecture, bringing low-latency inference, contextual personalization, and resilience to connectivity challenges. With AWS IoT Greengrass and Lambda@Edge, organizations can achieve the following:
+ Developers can extend serverless principles beyond the data center.
+ Enterprises can deploy and maintain AI pipelines closer to users and data sources.
+ AI logic becomes location-aware, autonomous, and highly scalable.

AI is becoming pervasive across sectors, from smart cities to field robotics to global media delivery. To support this evolution, these AWS services can play a foundational role in building distributed, intelligent applications that run anywhere.
