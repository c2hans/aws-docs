---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html
---

# Deploy foundation models and custom fine-tuned models
<a name="sagemaker-hyperpod-model-deployment-deploy"></a>

Whether you're deploying pre-trained foundation open-weights or gated models from Amazon SageMaker JumpStart or your own custom or fine-tuned models stored in Amazon S3 or Amazon FSx, SageMaker HyperPod provides the flexible, scalable infrastructure you need for production inference workloads.

****

|  | Deploy open-weights and gated foundation models from JumpStart | Deploy custom and fine-tuned models from Amazon S3 and Amazon FSx | Deploy models from local NVMe storage |
| --- | --- | --- | --- |
| Description | Deploy from a comprehensive catalog of pre-trained foundation models with automatic optimization and scaling policies tailored to each model family. | Bring your own custom and fine-tuned models and use SageMaker HyperPod's enterprise infrastructure for production-scale inference. Choose between cost-effective storage with Amazon S3 or a high-performance file system with Amazon FSx. | Load model weights from a node's local NVMe storage to eliminate network latency during pod startup. Useful for autoscaling events, scale-from-zero workloads, and latency-sensitive failovers. |
| Key benefits | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)  |
| Deployment options |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-deploy.html)  |

The following sections step you through deploying models from Amazon SageMaker JumpStart, from Amazon S3 and Amazon FSx, and from local NVMe storage.

**Topics**
+ [Deploy models from JumpStart using Amazon SageMaker Studio](sagemaker-hyperpod-model-deployment-deploy-js-ui.md)
+ [Deploy models from JumpStart using kubectl](sagemaker-hyperpod-model-deployment-deploy-js-kubectl.md)
+ [Deploy models from Amazon S3, Amazon FSx, or Hugging Face Hub using kubectl](sagemaker-hyperpod-model-deployment-deploy-ftm.md)
+ [Deploy models from local NVMe storage using kubectl](sagemaker-hyperpod-model-deployment-deploy-nvme.md)
+ [Deploy custom fine-tuned models using the Python SDK and HPCLI](deploy-trained-model.md)
+ [Deploy models from Amazon SageMaker JumpStart using the Python SDK and HPCLI](deploy-jumpstart-model.md)
