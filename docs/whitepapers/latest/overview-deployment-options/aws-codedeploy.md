---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/aws-codedeploy.html
---

# AWS CodeDeploy
<a name="aws-codedeploy"></a>

 [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) is a fully managed deployment service that automates application deployments to compute services such as Amazon EC2, [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS), [AWS Lambda](https://aws.amazon.com/lambda/), or on-premises servers. Organizations can use CodeDeploy to automate deployments of an application and remove error prone manual operations from the deployment process. CodeDeploy can be used with a wide variety of application content including code, serverless functions, configuration files, and more.

 CodeDeploy is intended to be used as a *building block* service that is focused on helping application developers deploy and update software that is running on existing infrastructure. It is not an end-to-end application management solution, and is intended to be used in conjunction with other AWS deployment services such as [AWS CodeStar](https://aws.amazon.com/codestar/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), other [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/), and third-party services (see [AWS CodeDeploy Product Integrations](https://aws.amazon.com/codedeploy/product-integrations/) for a complete list of product integrations) as part of a complete CI/CD pipeline. Additionally, CodeDeploy does not manage the creation of resources on behalf of the user.

* Table 3: AWS CodeDeploy deployment features *

|  Capability  |  Description  |
| --- | --- |
|  Provision  |  CodeDeploy is intended for use with existing compute resources and does not create resources on your behalf. CodeDeploy requires compute resources to be organized into a construct called a *deployment group* in order to deploy application content. <br /> Refer to [Working with Deployment Groups in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups.html) for more details on linking CodeDeploy to compute resources.  |
|  Configure  |  CodeDeploy uses an application specification file to define customizations for compute resources. <br /> Refer to [CodeDeploy AppSpec File Reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html) for more details on the resource customizations with CodeDeploy.  |
|  Deploy  |  Depending on the type of compute resource that CodeDeploy is used with, CodeDeploy offers different strategies for deploying your application. <br /> Refer to [Working with Deployments in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html) for more details on the types of deployment processes that are supported.  |
|  Scale  |  CodeDeploy does not support scaling of your underlying application infrastructure; however, depending on your [deployment configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html), it might create additional resources to support blue/green deployments.  |
|  Monitor  |  CodeDeploy can monitor the success or failure of deployments and offers a history of all deployments, but does not provide performance or application-level metrics. <br /> Refer to [Monitoring Deployments in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring.html) for more details on the types of monitoring capabilities offered by CodeDeploy  |

 The following diagram illustrates a general use case for CodeDeploy as part of a complete CI/CD solution. In this example, CodeDeploy is used in conjunction with additional AWS Developer Tools, namely AWS CodePipeline (automate CI/CD pipelines), [AWS CodeBuild](https://aws.amazon.com/codebuild/) (build and test application components), and [AWS CodeCommit](https://aws.amazon.com/codecommit/) (source code repository) to deploy an application onto a group of Amazon EC2 instances. CodeDeploy is used with other tools as part of a complete CI/CD pipeline. CodeDeploy manages deployment of application components onto compute resources that are part of a deployment group. All infrastructure components are created outside of CodeDeploy.

![AWS CodePipeline workflow showing CodeCommit, CodeBuild, CodeDeploy, and EC2 with Auto Scaling.](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image4.png)

* AWS CodeDeploy use case *

## AWS CodeDeploy for AWS Lambda
<a name="codedeploy-for-lambda"></a>

 AWS CodeDeploy for AWS Lambda enables you to automate your serverless deployments, giving you greater control and visibility over your application releases. You can use CodeDeploy to deploy a new version of your serverless function to a small percentage of users or traffic and gradually increase traffic as you gain confidence in the new version. With CodeDeploy, you can define deployment groups, which represent a set of Lambda functions that receive traffic from the same event source. For example, you can create a deployment group for a set of Lambda functions that are initiated by API Gateway or an Amazon EventBridge rule. You can then create a deployment using CodeDeploy, which deploys the new version of your erverless function to a specified deployment group.

 CodeDeploy also enables you to define a deployment configuration, which specifies the settings for a deployment, such as the deployment type, deployment strategy, and traffic shifting rules. You can use the Canary deployment strategy to deploy the new version of your serverless function to a small percentage of traffic and monitor the health and performance of the new version before increasing traffic to it.

 By using CodeDeploy for serverless, you can automate your deployment process, reduce the time and effort required to release new versions of your application, and increase the stability and reliability of your serverless functions.
