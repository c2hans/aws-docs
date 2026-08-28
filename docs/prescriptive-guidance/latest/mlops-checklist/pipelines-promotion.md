---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/pipelines-promotion.html
---

# 4. Robust pipelines and promotion
<a name="pipelines-promotion"></a>

Pipelines provide many options for hyperparameter tuning, AutoML, and processing routines. Pipelines are logged from end to end. Robust pipelines can run training in parallel across multiple instances and frameworks, scaling load sizes as needed. Robust pipelines can promote models into production, deploying in real-time, streaming, and batch. These deployments can support single-model or multi-model inference.

|  |
| --- |
| 4.1 Large-scale and distributed training | A mature ML system supports the ability to run training on large compute-optimized instances in parallel. It has the tooling in place to help ensure that these resources are fully used and that the training scales evenly across the compute cluster. |
| --- |--- |
| **4.2 Support for multiple frameworks** | Developers can port different platform frameworks, such as PyTorch or Flax, to run training and inference jobs. Likewise, different languages and versions are supported and usable. Switching to another framework will not break the system. |
| **4.3 Hyperparameter tuning** | A hyperparameter tuning step is a part of the training pipeline. Deployed models have their hyperparameters tuned. Multiple options are available to tune hyperparameters. For accuracy improvement, at least one of the tuning options should have a Bayesian inference or approach. |
| **4.4 AutoML option** | To reduce manual experimentation and comparison, a mature ML system supports running AutoML, which automatically selects the best feature pipeline, hyperparameters, and model. Note that AutoML is a feature to use pragmatically, but it's not a panacea. |
| **4.5 Inference support: real time** | This is commonly called model as a service (MaaS). The system supports real-time inference with REST API operations, for inference request on demand. It's able to ship MaaS infrastructure on which the model can scale both horizontally and vertically as a standalone API or as an endpoint associated with other applications. Alternatively, it's possible to deploy by using serverless technology. |
| **4.6 Inference support: streaming** | Models can be promoted to a real-time inference format such as Amazon Kinesis or Amazon Managed Streaming for Apache Kafka, whereby inference is run in streaming fashion on the model. This requires at least 90 percent of the checklist to be complete, because guardrails, observability, and monitoring are essential for real-time inference. |
| **4.7 Inference support: batch** | The system supports batch deployment of models as scheduled or initiated jobs. The system can run models as part of an extract, transform, and load (ETL) process or in isolation. Batch jobs record the state from each step and run in an ordered pattern, such as a directed acyclic graph. Alternatively, jobs can write to a database, which acts as the server of model inference. |
| **4.8 Preprocessing and post-processing routines** | When needed, data is featurized as part of the model intake process or the batch jobs. If there are multiple models or multiple steps at play, post-processing routines take care of featurizing the data. |
| **4.9 Ability to invoke hierarchical or simultaneous models** | The ML system can deploy many models together or run them in a sequential fashion. The former means hosting on a single model endpoint across a fleet of resources. The latter implies that multiple models need to run in a chained fashion one after the other. The system can handle both these types of complexity resiliently. |
| **4.10 Horizontal and vertical scaling strategies** | A pipeline should have the ability to support both types of scaling strategies for training and inference. The ML system can increase its size and distribute traffic across multiple machines when either latency or throughput increases. Policies for this type of behavior are set, and they consider optimal resource allocation. |
| **4.11 End-to-end logging** | The development team should have logging set inside all pipeline code so that logging can capture inputs, outputs, and intermediate steps in the system. Logging should support tracing runs in the pipeline and debugging errors. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
