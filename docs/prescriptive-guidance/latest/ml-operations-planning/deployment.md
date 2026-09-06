---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/deployment.html
---

# Deployment
<a name="deployment"></a>

In software engineering, putting code in production requires due diligence, because code might behave unexpectedly, unforeseen user behavior might break software, and unexpected edge cases can be found. Software engineers and DevOps engineers usually employ unit tests and rollback strategies to mitigate these risks. With ML, putting models in production requires even more planning, because the real environment is expected to drift, and on many occasions, models are validated on metrics that are proxies for the real business metrics they are trying to improve.

Follow the best practices in this section to help address these challenges.

## Automate the deployment cycle
<a name="automate-the-deployment-cycle"></a>

The training and deployment process should be entirely automated to prevent human error and to ensure that build checks are run consistently. Users should not have write access permissions to the production environment.

[Amazon SageMaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/) help create CI/CD pipelines for ML projects. One of the advantages of using a CI/CD pipeline is that all code that is used to ingest data, train a model, and perform monitoring can be version controlled by using a tool such as [Git](https://git-scm.com/). Sometimes you have to retrain a model by using the same algorithm and hyperparameters, but different data. The only way to verify that you're using the correct version of the algorithm is to use source control and tags. You can use the [default project templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-sm.html) provided by SageMaker as a starting point for your MLOps practice.

When you create CI/CD pipelines to deploy your model, make sure to tag your build artifacts with a build identifier, code version or commit, and data version. This practice helps you troubleshoot any deployment issues. Tagging is also sometimes required for models that make predictions in highly regulated fields. The ability to work backward and identify the exact data, code, build, checks, and approvals associated with an ML model can help improve governance significantly.

Part of the job of the CI/CD pipeline is to perform tests on what it is building. Although data unit tests are expected to happen before the data is ingested by a feature store, the pipeline is still responsible for performing tests on the input and output of a given model and for checking key metrics. One example of such a check is to validate a new model on a fixed validation set and to confirm that its performance is similar to the previous model by using an established threshold. If performance is significantly lower than expected, the build should fail and the model should not go into production.

The extensive use of CI/CD pipelines also supports pull requests, which help prevent human error. When you use pull requests, every code change must be reviewed and approved by at least one other team member before it can go to production. Pull requests are also useful for identifying code that doesn't adhere to business rules and for spreading knowledge within the team.

## Choose a deployment strategy
<a name="choose-a-deployment-strategy"></a>

MLOps deployment strategies include blue/green, canary, shadow, and A/B testing.

### Blue/green
<a name="blue-green.868931b8-37b3-5e16-866f-9aba33ed3905"></a>

Blue/green deployments are very common in software development. In this mode, two systems are kept running during development: blue is the old environment (in this case, the model that is being replaced) and green is the newly released model that is going to production. Changes can easily be rolled back with minimum downtime, because the old system is kept alive. For more in-depth information about blue/green deployments in the context of SageMaker, see the blog post [Safely deploying and monitoring Amazon SageMaker endpoints with AWS CodePipeline and AWS CodeDeploy](https://aws.amazon.com/blogs/machine-learning/safely-deploying-and-monitoring-amazon-sagemaker-endpoints-with-aws-codepipeline-and-aws-codedeploy/) on the AWS Machine Learning blog.

### Canary
<a name="canary.5b486b5d-dbfa-597b-8518-35fee66015f7"></a>

Canary deployments are similar to blue/green deployments in that both keep two models running together. However, in canary deployments, the new model is rolled out to users incrementally, until all traffic eventually shifts over to the new model. As in blue/green deployments, risk is mitigated because the new (and potentially faulty) model is closely monitored during the initial rollout, and can be rolled back in case of issues. In SageMaker, you can specify initial traffic distribution by using the [InitialVariantWeight](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html) API`.`

### Shadow
<a name="shadow.a733952e-1d9c-55f9-84cc-858f6f29a4ae"></a>

You can use shadow deployments to safely bring a model to production. In this mode, the new model works alongside an older model or business process, and performs inferences without influencing any decisions. This mode can be useful as a final check or higher fidelity experiment before you promote the model to production.

Shadow mode is useful when you don't need any user inference feedback. You can assess the quality of predictions by performing error analysis and comparing the new model with the old model, and you can monitor the output distribution to verify that it is as expected. To see how to do shadow deployment with SageMaker, see the blog post [Deploy shadow ML models in Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/deploy-shadow-ml-models-in-amazon-sagemaker/) on the AWS Machine Learning blog.

### A/B testing
<a name="a-b-testing.605d48c4-3b0b-51ef-9fcc-df5bc17e0a72"></a>

When ML practitioners develop models in their environments, the metrics that they optimize for are often proxies to the business metrics that really matter. This makes it difficult to tell for certain if a new model will actually improve business outcomes, such as revenue and clickthrough rate, and reduce the number of user complaints.

Consider the case of an e-commerce website in which the business goal is to sell as many products as possible. The review team knows that sales and customer satisfaction correlate directly with informative and accurate reviews. A team member might propose a new review ranking algorithm to improve sales. By using A/B testing, they could roll the old and new algorithms out to different but similar user groups, and monitor the results to see whether users who received predictions from the newer model are more likely to make purchases.

A/B testing also helps gauge the business impact of model staleness and drift. Teams can put new models in production with some recurrence, perform A/B testing with each model, and create an age versus performance chart. This would help the team understand the data drift volatility in their production data.

For more information about how to perform A/B testing with Sage Maker, see the blog post [A/B Testing ML models in production using Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/) on the AWS Machine Learning blog.

## Consider your inference requirements
<a name="consider-your-inference-requirements"></a>

With SageMaker, you can choose the underlying infrastructure to deploy your model in different ways. These inference invocation capabilities support different use cases and cost profiles. Your options include real-time inference, asynchronous inference, and batch transform, as discussed in the following sections.

### Real-time inference
<a name="real-time-inference.926bf6be-b31c-5b23-991a-5e7f680b8b3e"></a>

[Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) is ideal for inference workloads where you have real-time, interactive, low-latency requirements. You can deploy your model to SageMaker hosting services and get an endpoint that can be used for inference. These endpoints are fully managed, support automatic scaling (see [Automatically scale Amazon SageMaker models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)), and can be deployed in multiple [Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html).

If you have a deep learning model built with Apache MXNet, PyTorch, or TensorFlow, you can also use [Amazon SageMaker Elastic Inference (EI)](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html). With EI, you can attach fractional GPUs to any SageMaker instance to accelerate inference. You can select the client instance to run your application and attach an EI accelerator to use the correct amount of GPU acceleration for your inference needs.

Another option is to use [multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html), which provide a scalable and cost-effective solution to deploying large numbers of models. These endpoints use a shared serving container that is enabled to host multiple models. Multi-model endpoints reduce hosting costs by improving endpoint utilization compared with using single-model endpoints. They also reduce deployment overhead, because SageMaker manages loading models in memory and scaling them based on traffic patterns.

For additional best practices for deploying ML models in SageMaker, see [Deployment best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html) in the SageMaker documentation.

### Asynchronous inference
<a name="asynchronous-inference.8110bad9-f39f-5dc7-bbfa-7b86320f9aaf"></a>

[Amazon SageMaker Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) is a capability in SageMaker that queues incoming requests and processes them asynchronously. This option is ideal for requests with large payload sizes up to 1 GB, long processing times, and near real-time latency requirements. Asynchronous inference enables you to save on costs by automatically scaling the instance count to zero when there are no requests to process, so you pay only when your endpoint is processing requests.

### Batch transform
<a name="batch-transform.254e9070-9680-50cc-87c4-6a14818b55ab"></a>

Use [batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) when you want to do the following:
+ Preprocess datasets to remove noise or bias that interferes with training or inference from your dataset.
+ Get inferences from large datasets.
+ Run inference when you don't need a persistent endpoint.
+ Associate input records with inferences to assist the interpretation of results.
