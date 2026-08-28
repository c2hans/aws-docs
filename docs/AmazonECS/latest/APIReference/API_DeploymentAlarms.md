---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentAlarms.html
---

# DeploymentAlarms
<a name="API_DeploymentAlarms"></a>

One of the methods which provide a way for you to quickly identify when a deployment has failed, and then to optionally roll back the failure to the last working deployment.

When the alarms are generated, Amazon ECS sets the service deployment to failed. Set the rollback parameter to have Amazon ECS to roll back your service to the last completed deployment after a failure.

You can only use the `DeploymentAlarms` method to detect failures when the `DeploymentController` is set to `ECS`.

For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the * *Amazon Elastic Container Service Developer Guide* *.

## Contents
<a name="API_DeploymentAlarms_Contents"></a>

 ** alarmNames **   <a name="ECS-Type-DeploymentAlarms-alarmNames"></a>
One or more CloudWatch alarm names. Use a "," to separate the alarms.
Type: Array of strings
Required: Yes

 ** enable **   <a name="ECS-Type-DeploymentAlarms-enable"></a>
Determines whether to use the CloudWatch alarm option in the service deployment process.
Type: Boolean
Required: Yes

 ** rollback **   <a name="ECS-Type-DeploymentAlarms-rollback"></a>
Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.
Type: Boolean
Required: Yes

## See Also
<a name="API_DeploymentAlarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentAlarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentAlarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentAlarms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
