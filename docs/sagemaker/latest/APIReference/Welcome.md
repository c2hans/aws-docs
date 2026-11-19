---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html
---

# Welcome

## Amazon SageMaker Service
<a name="Welcome_Amazon_SageMaker_Service"></a>

Provides APIs for creating and managing SageMaker resources.

Other Resources:
+  [SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html#first-time-user)
+  [Amazon Augmented AI Runtime API Reference](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/Welcome.html)

## Amazon SageMaker Runtime
<a name="Welcome_Amazon_SageMaker_Runtime"></a>

 The Amazon SageMaker AI runtime API.

## Amazon Sagemaker Edge Manager
<a name="Welcome_Amazon_Sagemaker_Edge_Manager"></a>

SageMaker Edge Manager dataplane service for communicating with active agents.

## Amazon SageMaker Feature Store Runtime
<a name="Welcome_Amazon_SageMaker_Feature_Store_Runtime"></a>

Contains all data plane API operations and data types for the Amazon SageMaker Feature Store. Use this API to put, delete, and retrieve (get) features from a feature store.

Use the following operations to configure your `OnlineStore` and `OfflineStore` features, and to create and manage feature groups:
+  [CreateFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFeatureGroup.html)
+  [DeleteFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFeatureGroup.html)
+  [DescribeFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html)
+  [ListFeatureGroups](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFeatureGroups.html)

## Amazon SageMaker geospatial capabilities
<a name="Welcome_Amazon_SageMaker_geospatial_capabilities"></a>

Provides APIs for creating and managing SageMaker geospatial resources.

## Amazon SageMaker Inference Router Runtime
<a name="Welcome_Amazon_SageMaker_Inference_Router_Runtime"></a>

Amazon SageMaker Inference Router Runtime is the runtime API for Amazon SageMaker AI inference routers. An inference router sends each request that you make to one of the destinations of a routing target. A destination is a SageMaker AI endpoint or inference component, in your account or in another account, in the router's AWS Region or in another Region in the same AWS partition. The router chooses a healthy destination with capacity, and prefers destinations in its own Region.

Use `InvokeInferenceRouter` to get an inference in real time. Use `InvokeInferenceRouterAsync` to submit a request whose input and response are stored in Amazon S3.

The inference router runtime endpoint supports HTTP/1.1 only. HTTP/2 isn't supported. If you use the AWS SDKs or the AWS CLI, you don't need to change anything.

## Amazon SageMaker Metrics Service
<a name="Welcome_Amazon_SageMaker_Metrics_Service"></a>

Contains all data plane API operations and data types for Amazon SageMaker Metrics. Use these APIs to put and retrieve (get) features related to your training run.
+  [BatchPutMetrics](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_BatchPutMetrics.html)

## Amazon SageMaker Job Runtime Service
<a name="Welcome_Amazon_SageMaker_Job_Runtime_Service"></a>

Amazon SageMaker Job Runtime provides APIs that enable communication between your agent and the policy model during multi-turn reinforcement learning jobs. These APIs support inference requests to the policy model, rollout lifecycle management, and reward submission.

## Amazon SageMaker Training Session Runtime
<a name="Welcome_Amazon_SageMaker_Training_Session_Runtime"></a>

Amazon SageMaker Training Session Runtime provides APIs for executing training operations and sampling operations against a running training session. Use these APIs to submit asynchronous training steps (such as forward-backward passes, optimizer steps, and checkpoint saves) and to generate text samples from the model being trained.
