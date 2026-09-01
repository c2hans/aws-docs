---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentGroupInfo.html
---

# DeploymentGroupInfo
<a name="API_DeploymentGroupInfo"></a>

Information about a deployment group.

## Contents
<a name="API_DeploymentGroupInfo_Contents"></a>

 ** alarmConfiguration **   <a name="CodeDeploy-Type-DeploymentGroupInfo-alarmConfiguration"></a>
A list of alarms associated with the deployment group.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** applicationName **   <a name="CodeDeploy-Type-DeploymentGroupInfo-applicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: No

 ** autoRollbackConfiguration **   <a name="CodeDeploy-Type-DeploymentGroupInfo-autoRollbackConfiguration"></a>
Information about the automatic rollback configuration associated with the deployment group.
Type: [AutoRollbackConfiguration](API_AutoRollbackConfiguration.md) object
Required: No

 ** autoScalingGroups **   <a name="CodeDeploy-Type-DeploymentGroupInfo-autoScalingGroups"></a>
A list of associated Auto Scaling groups.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects
Required: No

 ** blueGreenDeploymentConfiguration **   <a name="CodeDeploy-Type-DeploymentGroupInfo-blueGreenDeploymentConfiguration"></a>
Information about blue/green deployment options for a deployment group.
Type: [BlueGreenDeploymentConfiguration](API_BlueGreenDeploymentConfiguration.md) object
Required: No

 ** computePlatform **   <a name="CodeDeploy-Type-DeploymentGroupInfo-computePlatform"></a>
The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** deploymentConfigName **   <a name="CodeDeploy-Type-DeploymentGroupInfo-deploymentConfigName"></a>
The deployment configuration name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: No

 ** deploymentGroupId **   <a name="CodeDeploy-Type-DeploymentGroupInfo-deploymentGroupId"></a>
The deployment group ID.
Type: String
Required: No

 ** deploymentGroupName **   <a name="CodeDeploy-Type-DeploymentGroupInfo-deploymentGroupName"></a>
The deployment group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: No

 ** deploymentStyle **   <a name="CodeDeploy-Type-DeploymentGroupInfo-deploymentStyle"></a>
Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.
Type: [DeploymentStyle](API_DeploymentStyle.md) object
Required: No

 ** ec2TagFilters **   <a name="CodeDeploy-Type-DeploymentGroupInfo-ec2TagFilters"></a>
The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.
Type: Array of [EC2TagFilter](API_EC2TagFilter.md) objects
Required: No

 ** ec2TagSet **   <a name="CodeDeploy-Type-DeploymentGroupInfo-ec2TagSet"></a>
Information about groups of tags applied to an Amazon EC2 instance. The deployment group includes only Amazon EC2 instances identified by all of the tag groups. Cannot be used in the same call as ec2TagFilters.
Type: [EC2TagSet](API_EC2TagSet.md) object
Required: No

 ** ecsServices **   <a name="CodeDeploy-Type-DeploymentGroupInfo-ecsServices"></a>
 The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format `<clustername>:<servicename>`.
Type: Array of [ECSService](API_ECSService.md) objects
Required: No

 ** lastAttemptedDeployment **   <a name="CodeDeploy-Type-DeploymentGroupInfo-lastAttemptedDeployment"></a>
Information about the most recent attempted deployment to the deployment group.
Type: [LastDeploymentInfo](API_LastDeploymentInfo.md) object
Required: No

 ** lastSuccessfulDeployment **   <a name="CodeDeploy-Type-DeploymentGroupInfo-lastSuccessfulDeployment"></a>
Information about the most recent successful deployment to the deployment group.
Type: [LastDeploymentInfo](API_LastDeploymentInfo.md) object
Required: No

 ** loadBalancerInfo **   <a name="CodeDeploy-Type-DeploymentGroupInfo-loadBalancerInfo"></a>
Information about the load balancer to use in a deployment.
Type: [LoadBalancerInfo](API_LoadBalancerInfo.md) object
Required: No

 ** onPremisesInstanceTagFilters **   <a name="CodeDeploy-Type-DeploymentGroupInfo-onPremisesInstanceTagFilters"></a>
The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

 ** onPremisesTagSet **   <a name="CodeDeploy-Type-DeploymentGroupInfo-onPremisesTagSet"></a>
Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.
Type: [OnPremisesTagSet](API_OnPremisesTagSet.md) object
Required: No

 ** outdatedInstancesStrategy **   <a name="CodeDeploy-Type-DeploymentGroupInfo-outdatedInstancesStrategy"></a>
Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.
If this option is set to `UPDATE` or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.
If this option is set to `IGNORE`, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.
Type: String
Valid Values: `UPDATE | IGNORE`
Required: No

 ** serviceRoleArn **   <a name="CodeDeploy-Type-DeploymentGroupInfo-serviceRoleArn"></a>
A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf. For more information, see [Create a Service Role for AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html) in the * AWS CodeDeploy User Guide*.
Type: String
Required: No

 ** targetRevision **   <a name="CodeDeploy-Type-DeploymentGroupInfo-targetRevision"></a>
Information about the deployment group's target revision, including type and location.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: No

 ** terminationHookEnabled **   <a name="CodeDeploy-Type-DeploymentGroupInfo-terminationHookEnabled"></a>
Indicates whether the deployment group was configured to have CodeDeploy install a termination hook into an Auto Scaling group.
For more information about the termination hook, see [How Amazon EC2 Auto Scaling works with CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors) in the * AWS CodeDeploy User Guide*.
Type: Boolean
Required: No

 ** triggerConfigurations **   <a name="CodeDeploy-Type-DeploymentGroupInfo-triggerConfigurations"></a>
Information about triggers associated with the deployment group.
Type: Array of [TriggerConfig](API_TriggerConfig.md) objects
Required: No

## See Also
<a name="API_DeploymentGroupInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentGroupInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentGroupInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentGroupInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
