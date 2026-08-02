---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/rolling-deployments.html
---

# Rolling deployments
<a name="rolling-deployments"></a>

 A rolling deployment is a deployment strategy that slowly replaces previous versions of an application with new versions of an application by completely replacing the infrastructure on which the application is running. For example, in a rolling deployment in Amazon ECS, containers running previous versions of the application will be replaced one-by-one with containers running new versions of the application.

 A rolling deployment is generally faster than a blue/green deployment; however, unlike a blue/green deployment, in a rolling deployment there is no environment isolation between the old and new application versions. This allows rolling deployments to complete more quickly, but also increases risks and complicates the process of rollback if a deployment fails.

 Rolling deployment strategies can be used with most deployment solutions. Refer to [CloudFormation Update Policies](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html) for more information on rolling deployments with CloudFormation; [Rolling Updates with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) for more details on rolling deployments with Amazon ECS; [Elastic Beanstalk Rolling Environment Configuration Updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rollingupdates.html) for more details on rolling deployments with Elastic Beanstalk; and [Using a Rolling Deployment in AWS OpsWorks](https://docs.aws.amazon.com/opsworks/latest/userguide/best-deploy.html#best-deploy-rolling) for more details on rolling deployments with OpsWorks.
