---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html
---

# Model Registration Deployment with Model Registry
<a name="model-registry"></a>

With the Amazon SageMaker Model Registry you can do the following:
+ Catalog models for production.
+ Manage model versions.
+ Associate metadata, such as training metrics, with a model.
+ View information from Amazon SageMaker Model Cards in your registered models.
+ View model lineage for traceability and reproducibility.
+ Define a staging construct that models can progress through for your model lifecycle.
+ Manage the approval status of a model.
+ Deploy models to production.
+ Automate model deployment with CI/CD.
+ Share models with other users.

Catalog models by creating SageMaker Model Registry Model (Package) Groups that contain different versions of a model. You can create a Model Group that tracks all of the models that you train to solve a particular problem. You can then register each model you train and the Model Registry adds it to the Model Group as a new model version. Lastly, you can create categories of Model Groups by further organizing them into SageMaker Model Registry Collections. A typical workflow might look like the following:
+ Create a Model Group.
+ Create an ML pipeline that trains a model. For information about SageMaker pipelines, see [Pipelines actions](pipelines-build.md).
+ For each run of the ML pipeline, create a model version that you register in the Model Group you created in the first step.
+ Add your Model Group into one or more Model Registry Collections.

For details about how to create and work with models, model versions, and Model Groups, see [Model Registry Models, Model Versions, and Model Groups](model-registry-models.md). Optionally, if you want to further group your Model Groups into Collections, see [Model Registry Collections](modelcollections.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
