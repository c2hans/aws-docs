---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-limitations.html
---

# Limitations of customizing Amazon Nova models
<a name="nova-model-limitations"></a>

Amazon Nova customization doesn't support the following capabilities on SageMaker.
+ **SSH into the instance to find the metrics**

  Due to security controls in place, you can't SSH into the master node in the training algo-1 instance to find memory stats or NVIDIA stats and validate the training steps.
+ **Warm pools are not accessible to SageMaker training jobs**

  Due to security controls in place, the SageMaker warm pools can't be used to keep the instance in the warm pool till the time to live.
+ **Custom model merging**

  Merging multiple models is not currently supported. This means that creating multiple LoRA adapters and perform a multi-merge operation with the base model is not available.
+ **Supported observability tool**

  [TensorBoard](https://www.tensorflow.org/tensorboard) and [MLflow](https://mlflow.org/) are the only supported observability tools to view metrics for SageMaker training jobs. For more information, see [TensorBoard in SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/tensorboard-on-sagemaker.html) and [MLflow in SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
