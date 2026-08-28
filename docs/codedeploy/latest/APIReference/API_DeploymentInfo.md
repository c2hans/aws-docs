---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentInfo.html
---

# DeploymentInfo
<a name="API_DeploymentInfo"></a>

Information about a deployment.

## Contents
<a name="API_DeploymentInfo_Contents"></a>

 ** additionalDeploymentStatusInfo **   <a name="CodeDeploy-Type-DeploymentInfo-additionalDeploymentStatusInfo"></a>
 *This member has been deprecated.*
Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.
Type: String
Required: No

 ** applicationName **   <a name="CodeDeploy-Type-DeploymentInfo-applicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** autoRollbackConfiguration **   <a name="CodeDeploy-Type-DeploymentInfo-autoRollbackConfiguration"></a>
Information about the automatic rollback configuration associated with the deployment.
Type: [AutoRollbackConfiguration](API_AutoRollbackConfiguration.md) object
Required: No

 ** blueGreenDeploymentConfiguration **   <a name="CodeDeploy-Type-DeploymentInfo-blueGreenDeploymentConfiguration"></a>
Information about blue/green deployment options for this deployment.
Type: [BlueGreenDeploymentConfiguration](API_BlueGreenDeploymentConfiguration.md) object
Required: No

 ** completeTime **   <a name="CodeDeploy-Type-DeploymentInfo-completeTime"></a>
A timestamp that indicates when the deployment was complete.
Type: Timestamp
Required: No

 ** computePlatform **   <a name="CodeDeploy-Type-DeploymentInfo-computePlatform"></a>
The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** createTime **   <a name="CodeDeploy-Type-DeploymentInfo-createTime"></a>
A timestamp that indicates when the deployment was created.
Type: Timestamp
Required: No

 ** creator **   <a name="CodeDeploy-Type-DeploymentInfo-creator"></a>
The means by which the deployment was created:
+  `user`: A user created the deployment.
+  `autoscaling`: Amazon EC2 Auto Scaling created the deployment.
+  `codeDeployRollback`: A rollback process created the deployment.
+  `CodeDeployAutoUpdate`: An auto-update process created the deployment when it detected outdated Amazon EC2 instances.
Type: String
Valid Values: `user | autoscaling | codeDeployRollback | CodeDeploy | CodeDeployAutoUpdate | CloudFormation | CloudFormationRollback | autoscalingTermination`
Required: No

 ** deploymentConfigName **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentConfigName"></a>
 The deployment configuration name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** deploymentGroupName **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentGroupName"></a>
 The deployment group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** deploymentId **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** deploymentOverview **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentOverview"></a>
A summary of the deployment status of the instances in the deployment.
Type: [DeploymentOverview](API_DeploymentOverview.md) object
Required: No

 ** deploymentStatusMessages **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentStatusMessages"></a>
Messages that contain information about the status of a deployment.
Type: Array of strings
Required: No

 ** deploymentStyle **   <a name="CodeDeploy-Type-DeploymentInfo-deploymentStyle"></a>
Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.
Type: [DeploymentStyle](API_DeploymentStyle.md) object
Required: No

 ** description **   <a name="CodeDeploy-Type-DeploymentInfo-description"></a>
A comment about the deployment.
Type: String
Required: No

 ** errorInformation **   <a name="CodeDeploy-Type-DeploymentInfo-errorInformation"></a>
Information about any error associated with this deployment.
Type: [ErrorInformation](API_ErrorInformation.md) object
Required: No

 ** externalId **   <a name="CodeDeploy-Type-DeploymentInfo-externalId"></a>
The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.
Type: String
Required: No

 ** fileExistsBehavior **   <a name="CodeDeploy-Type-DeploymentInfo-fileExistsBehavior"></a>
Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.
+  `DISALLOW`: The deployment fails. This is also the default behavior if no option is specified.
+  `OVERWRITE`: The version of the file from the application revision currently being deployed replaces the version already on the instance.
+  `RETAIN`: The version of the file already on the instance is kept and used as part of the new deployment.
Type: String
Valid Values: `DISALLOW | OVERWRITE | RETAIN`
Required: No

 ** ignoreApplicationStopFailures **   <a name="CodeDeploy-Type-DeploymentInfo-ignoreApplicationStopFailures"></a>
 If true, then if an `ApplicationStop`, `BeforeBlockTraffic`, or `AfterBlockTraffic` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if `ApplicationStop` fails, the deployment continues with DownloadBundle. If `BeforeBlockTraffic` fails, the deployment continues with `BlockTraffic`. If `AfterBlockTraffic` fails, the deployment continues with `ApplicationStop`.
 If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.
 During a deployment, the AWS CodeDeploy agent runs the scripts specified for `ApplicationStop`, `BeforeBlockTraffic`, and `AfterBlockTraffic` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.
 If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use `ignoreApplicationStopFailures` to specify that the `ApplicationStop`, `BeforeBlockTraffic`, and `AfterBlockTraffic` failures should be ignored.
Type: Boolean
Required: No

 ** instanceTerminationWaitTimeStarted **   <a name="CodeDeploy-Type-DeploymentInfo-instanceTerminationWaitTimeStarted"></a>
Indicates whether the wait period set for the termination of instances in the original environment has started. Status is 'false' if the KEEP\_ALIVE option is specified. Otherwise, 'true' as soon as the termination wait period starts.
Type: Boolean
Required: No

 ** loadBalancerInfo **   <a name="CodeDeploy-Type-DeploymentInfo-loadBalancerInfo"></a>
Information about the load balancer used in the deployment.
Type: [LoadBalancerInfo](API_LoadBalancerInfo.md) object
Required: No

 ** overrideAlarmConfiguration **   <a name="CodeDeploy-Type-DeploymentInfo-overrideAlarmConfiguration"></a>
Information about alarms associated with a deployment or deployment group.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** previousRevision **   <a name="CodeDeploy-Type-DeploymentInfo-previousRevision"></a>
Information about the application revision that was deployed to the deployment group before the most recent successful deployment.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: No

 ** relatedDeployments **   <a name="CodeDeploy-Type-DeploymentInfo-relatedDeployments"></a>
Information about deployments related to the specified deployment.
Type: [RelatedDeployments](API_RelatedDeployments.md) object
Required: No

 ** revision **   <a name="CodeDeploy-Type-DeploymentInfo-revision"></a>
Information about the location of stored application artifacts and the service from which to retrieve them.
Type: [RevisionLocation](API_RevisionLocation.md) object
Required: No

 ** rollbackInfo **   <a name="CodeDeploy-Type-DeploymentInfo-rollbackInfo"></a>
Information about a deployment rollback.
Type: [RollbackInfo](API_RollbackInfo.md) object
Required: No

 ** startTime **   <a name="CodeDeploy-Type-DeploymentInfo-startTime"></a>
A timestamp that indicates when the deployment was deployed to the deployment group.
In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.
Type: Timestamp
Required: No

 ** status **   <a name="CodeDeploy-Type-DeploymentInfo-status"></a>
The current state of the deployment as a whole.
Type: String
Valid Values: `Created | Queued | InProgress | Baking | Succeeded | Failed | Stopped | Ready`
Required: No

 ** targetInstances **   <a name="CodeDeploy-Type-DeploymentInfo-targetInstances"></a>
Information about the instances that belong to the replacement environment in a blue/green deployment.
Type: [TargetInstances](API_TargetInstances.md) object
Required: No

 ** updateOutdatedInstancesOnly **   <a name="CodeDeploy-Type-DeploymentInfo-updateOutdatedInstancesOnly"></a>
Indicates whether only instances that are not running the latest application revision are to be deployed to.
Type: Boolean
Required: No

## See Also
<a name="API_DeploymentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
