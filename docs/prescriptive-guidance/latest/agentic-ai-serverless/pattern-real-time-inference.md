---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-real-time-inference.html
---

# Pattern 3: Real-time inference at the edge
<a name="pattern-real-time-inference"></a>

Many enterprise use cases demand intelligent decision-making at the point of interaction, whether that interaction is with a customer, a machine, a vehicle, or an IoT device. In these scenarios, cloud-only inference is not enough because of the following issues:
+ **Latency constraints** – Milliseconds matter in user experiences such as personalization, recommendations, and fraud checks.
+ **Intermittent or no connectivity** – Remote environments such as industrial, agricultural, and healthcare often lack consistent access to cloud APIs.
+ **High data volume** – Sending large sensor or image payloads to the cloud for inference is inefficient and costly.
+ **Regulatory requirements** – In some jurisdictions, sensitive data must remain local.

Traditional architectures that rely solely on centralized ML inference introduce delays, increase costs, and can fail to serve users or systems effectively in edge-first environments.

## The edge inference pattern: Real-time intelligence at the edge
<a name="the-edge-inference-pattern--real-time-intelligence-at-the-edge.64c38587-3759-5c21-bdac-d63025d30fab"></a>

The real-time edge inference pattern enables organizations to run inference workloads closer to the user or device, using services managed by AWS. These services include [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html), which allows for localized, offline-capable inference on physical edge devices. Additionally, [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works.html) enables the execution of lightweight AI logic at [Amazon CloudFront edge locations](https://awsfundamentals.com/blog/aws-edge-locations) globally.

These serverless services enable distributed AI experiences that are instantaneous, resilient to connectivity issues, and compliant with regional and latency-sensitive requirements.

The reference architecture implements each layer as follows:
+ **Event trigger** – Uses edge events (such as sensor readings and device state changes) or viewer requests through CloudFront.
+ **Processing** – Implements a local Lambda function on AWS IoT Greengrass to format input, extract metadata, or filter noise. Uses Lambda@Edge to inspect headers or geolocation.
+ **Inference** – Deploys an ML model through an AWS IoT Greengrass component (for example, PyTorch or ONNX) or makes remote API calls to Amazon Bedrock or [Amazon SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) through Lambda@Edge.
+ **Post–processing** – Uses AWS IoT Greengrass to publish anomaly detection to MQTT or [AWS IoT device shadows](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html). Employs Lambda@Edge to personalize responses and set cookies.
+ **Output** – Synchronizes to AWS IoT Core, [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Serves responses through CloudFront to either browser or device dashboard.

**Note**
Each tier plays a role in reducing response time, optimizing bandwidth, and localizing intelligence.

## Use cases for the edge inference pattern
<a name="use-cases-for-the-edge-inference-pattern.91088703-add5-501a-896f-b127a83040fc"></a>

The real-time inference at the edge pattern supports various implementations across different industries. Here are two representative examples:
+ **Factory equipment monitoring and AWS IoT Greengrass** – A manufacturing plant deploys gateways that are enabled by AWS IoT Greengrass to detect anomalies in equipment vibrations. The model runs locally, alerting the operator in real time and only sending summary data to the cloud.
+ **Personalized web content and Lambda@Edge** – An ecommerce site uses Lambda@Edge to analyze cookies and headers on incoming requests. Lambda@Edge helps the site to deliver personalized recommendations and product images in under 50ms, without backend round trips.

## Security and management best practices at the edge
<a name="security-and-management-best-practices-at-the-edge.218c5a8b-1f5c-5c89-a736-93be0b83b6f5"></a>

Both IoT Greengrass and Lambda@Edge are fully integrated with [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM), AWS IoT Core, and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). Key best practices include the following:
+ Code signing and verification for AWS IoT Greengrass components
+ Regional traffic inspection and logging for Lambda@Edge
+ Secure over-the-air (OTA) model updates using Amazon S3 buckets and continuous integration and continuous deployment (CI/CD) pipelines
+ Fine-grained IAM roles to limit data access at the edge

## Comparing AWS IoT Greengrass and Lambda@Edge
<a name="comparing-9999999999999999gg--and-9999999999999999lam--edge.5c6aa954-a352-5ca6-9492-9846af95a5f5"></a>

The following table compares key operational aspects of AWS IoT Greengrass and Lambda@Edge in the context of edge inference.

|
|
| Consideration | AWS IoT Greengrass | Lambda@Edge |
| --- |--- |--- |
| Works offline | Yes | No |
| Handles local sensor and actuator data | Yes | No |
| Good for global web personalization | No | Yes |
| Supports AI models | Full local inference | Lightweight logic and cloud API calls |
| Integration with Amazon Bedrock or SageMaker Serverless Inference | Through async sync and logging | Through Amazon API Gateway fallback or caching |

By using this pattern, enterprises can embed AI where it's needed most, on the shop floor, in the field, in the browser, or across the globe. The real-time inference at the edge pattern is essential for:
+ Applications with low-latency, high-availability requirements
+ Edge devices in remote or high-throughput environments
+ Global consumer experiences where location matters

By combining AWS IoT Greengrass for on-device intelligence with Lambda@Edge for proximity to users, AWS enables a powerful, serverless approach to scalable, resilient, and cost-effective edge AI.

## Business value of the edge inference pattern
<a name="business-value-of-the-edge-inference-pattern.183d04fc-2906-5b8f-936a-cf8bddac2766"></a>

The edge inference pattern delivers value in the following areas:
+ **Performance** – Achieves sub-100ms inference for user-facing apps or time-critical automation
+ **Reliability** – Works without connectivity, which is especially important for IoT or remote deployments
+ **Bandwidth savings** – Keeps raw data local and pushes only meaningful events to the cloud
+ **Compliance** – Maintains inference and data locally to comply with regional governance such as General Data Protection Regulation (GDPR) and Health Insurance Portability and Accountability Act of 1996 (HIPAA)
+ **Cost control** – Minimizes cloud resource usage and network traffic where not essential
