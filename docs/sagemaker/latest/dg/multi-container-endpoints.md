---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html
---

# Multi-container endpoints

SageMaker AI multi-container endpoints enable customers to deploy multiple containers, that use different models or frameworks, on a single SageMaker AI endpoint. The containers can be run in a sequence as an inference pipeline, or each container can be accessed individually by using direct invocation to improve endpoint utilization and optimize costs.

For information about invoking the containers in a multi-container endpoint in sequence, see [Inference pipelines in Amazon SageMaker AI](inference-pipelines.md).

For information about invoking a specific container in a multi-container endpoint, see [Invoke a multi-container endpoint with direct invocation](multi-container-direct.md)

**Topics**
+ [Create a multi-container endpoint (Boto 3)](multi-container-create.md)
+ [Update a multi-container endpoint](multi-container-update.md)
+ [Invoke a multi-container endpoint with direct invocation](multi-container-direct.md)
+ [Security with multi-container endpoints with direct invocation](multi-container-security.md)
+ [Metrics for multi-container endpoints with direct invocation](multi-container-metrics.md)
+ [Autoscale multi-container endpoints](multi-container-auto-scaling.md)
+ [Troubleshoot multi-container endpoints](multi-container-troubleshooting.md)
