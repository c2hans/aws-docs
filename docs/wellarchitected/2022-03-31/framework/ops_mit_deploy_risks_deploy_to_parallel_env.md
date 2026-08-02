---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_mit_deploy_risks_deploy_to_parallel_env.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS06-BP05 Deploy using parallel environments
<a name="ops_mit_deploy_risks_deploy_to_parallel_env"></a>

 Implement changes onto parallel environments, and then transition over to the new environment. Maintain the prior environment until there is confirmation of successful deployment. Doing so minimizes recovery time by enabling rollback to the previous environment.

 **Common anti-patterns:**
+  You perform a mutable deployment by modifying your existing systems. After discovering that the change was unsuccessful, you are forced to modify the systems again to restore the old version extending your time to recovery.
+  During a maintenance window, you decommission the old environment and then start building your new environment. Many hours into the procedure, you discover unrecoverable issues with the deployment. While extremely tired, you are forced to find the previous deployment procedures and start rebuilding the old environment.

 **Benefits of establishing this best practice:** By using parallel environments, you can pre-deploy the new environment and transition over to them when desired. If the new environment is not successful, you can recover quickly by transitioning back to your original environment.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Deploy using parallel environments: Implement changes onto parallel environments, and transition or cut over to the new environment. Maintain the prior environment until there is confirmation of successful deployment. This minimizes recovery time by enabling rollback to the previous environment. For example, use immutable infrastructures with blue/green deployments.
  +  [Working with deployment configurations in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
  +  [Blue/Green deployments with AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html)
  +  [Set up an API Gateway canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)
  +  [Try a Sample Blue/Green Deployment in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-blue-green.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
+  [Blue/Green deployments with AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html)
+  [Set up an API Gateway canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)
+  [Try a Sample Blue/Green Deployment in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-blue-green.html)
+  [Working with deployment configurations in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)

 **Related videos:**
+  [Deep Dive on Advanced Continuous Delivery Techniques Using AWS](https://www.youtube.com/watch?v=Lrrgd0Kemhw)
