---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-sagemaker.html
---

# Amazon SageMaker AI and Application Auto Scaling
<a name="services-that-can-integrate-sagemaker"></a>

You can scale SageMaker AI endpoint variants, provisioned concurrency for serverless endpoints, and inference components using target tracking scaling policies, step scaling policies, and scheduled scaling.

Use the following information to help you integrate SageMaker AI with Application Auto Scaling.

## Service-linked role created for SageMaker AI
<a name="integrate-service-linked-role-sagemaker"></a>

The following service-linked role is automatically created in your AWS account when registering SageMaker AI resources as scalable targets with Application Auto Scaling. This role allows Application Auto Scaling to perform supported operations within your account. For more information, see [Service-linked roles for Application Auto Scaling](application-auto-scaling-service-linked-roles.md).
+ `AWSServiceRoleForApplicationAutoScaling_SageMakerEndpoint`

## Service principal used by the service-linked role
<a name="integrate-service-principal-sagemaker"></a>

The service-linked role in the previous section can be assumed only by the service principal authorized by the trust relationships defined for the role. The service-linked role used by Application Auto Scaling grants access to the following service principal:
+ `sagemaker.application-autoscaling.amazonaws.com`

## Registering SageMaker AI endpoint variants as scalable targets with Application Auto Scaling
<a name="integrate-register-sagemaker"></a>

Application Auto Scaling requires a scalable target before you can create scaling policies or scheduled actions for a SageMaker AI model (variant). A scalable target is a resource that Application Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace.

If you configure auto scaling using the SageMaker AI console, then SageMaker AI automatically registers a scalable target for you.

If you want to configure auto scaling using the AWS CLI or one of the AWS SDKs, you can use the following options:
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for a product variant. The following example registers the desired instance count for a product variant called `my-variant`, running on the `my-endpoint` endpoint, with a minimum capacity of one instance and a maximum capacity of eight instances.

  ```
  aws application-autoscaling register-scalable-target \
    --service-namespace sagemaker \
    --scalable-dimension sagemaker:variant:DesiredInstanceCount \
    --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}} \
    --min-capacity {{1}} \
    --max-capacity {{8}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
  }
  ```
+ AWS SDK:

  Call the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) operation and provide `ResourceId`, `ScalableDimension`, `ServiceNamespace`, `MinCapacity`, and `MaxCapacity` as parameters.

## Registering the provisioned concurrency of serverless endpoints as scalable targets with Application Auto Scaling
<a name="integrate-register-provisioned-concurrency"></a>

Application Auto Scaling also requires a scalable target before you can create scaling policies or scheduled actions for the provisioned concurrency of serverless endpoints.

If you configure auto scaling using the SageMaker AI console, then SageMaker AI automatically registers a scalable target for you.

Otherwise, use one of the following methods to register the scalable target:
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for a product variant. The following example registers the provisioned concurrency for a product variant called `my-variant`, running on the `my-endpoint` endpoint, with a minimum capacity of one and a maximum capacity of ten.

  ```
  aws application-autoscaling register-scalable-target \
    --service-namespace sagemaker \
    --scalable-dimension sagemaker:variant:DesiredProvisionedConcurrency \
    --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}} \
    --min-capacity {{1}} \
    --max-capacity {{10}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
  }
  ```
+ AWS SDK:

  Call the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) operation and provide `ResourceId`, `ScalableDimension`, `ServiceNamespace`, `MinCapacity`, and `MaxCapacity` as parameters.

## Registering inference components as scalable targets with Application Auto Scaling
<a name="integrate-register-inference-components"></a>

Application Auto Scaling also requires a scalable target before you can create scaling policies or scheduled actions for inference components.
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for an inference component. The following example registers the desired copy count for an inference component called `my-inference-component`, with a minimum capacity of zero copies and a maximum capacity of three copies.

  ```
  aws application-autoscaling register-scalable-target \
    --service-namespace sagemaker \
    --scalable-dimension sagemaker:inference-component:DesiredCopyCount \
    --resource-id inference-component/{{my-inference-component}} \
    --min-capacity {{0}} \
    --max-capacity {{3}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
  }
  ```
+ AWS SDK:

  Call the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) operation and provide `ResourceId`, `ScalableDimension`, `ServiceNamespace`, `MinCapacity`, and `MaxCapacity` as parameters.

## Related resources
<a name="sagemaker-related-resources"></a>

If you are just getting started with Application Auto Scaling, you can find additional useful information about scaling your SageMaker AI resources in the *Amazon SageMaker AI Developer Guide*:
+ [Automatically scale Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
+ [Automatically scale Provisioned Concurrency for a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-autoscale.html)
+ [Set auto scaling policies for multi-model endpoint deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints-autoscaling.html)
+ [Autoscale an asynchronous endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-autoscale.html)

**Note**
In 2023, SageMaker AI introduced new inference capabilities built on real-time inference endpoints. You create a SageMaker AI endpoint with an endpoint configuration that defines the instance type and initial instance count for the endpoint. Then, create an inference component, which is a SageMaker AI hosting object that you can use to deploy a model to an endpoint. For information about scaling inference components, see [Amazon SageMaker AI adds new inference capabilities to help reduce foundation model deployment costs and latency](https://aws.amazon.com/blogs/aws/amazon-sagemaker-adds-new-inference-capabilities-to-help-reduce-foundation-model-deployment-costs-and-latency/) and [Reduce model deployment costs by 50% on average using the latest features of Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/reduce-model-deployment-costs-by-50-on-average-using-sagemakers-latest-features/) on the AWS Blog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
