---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceDeployment.html
---

# ServiceDeployment
<a name="API_ServiceDeployment"></a>

Information about the service deployment.

Service deployments provide a comprehensive view of your deployments. For information about service deployments, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html) in the * *Amazon Elastic Container Service Developer Guide* *.

## Contents
<a name="API_ServiceDeployment_Contents"></a>

 ** alarms **   <a name="ECS-Type-ServiceDeployment-alarms"></a>
The CloudWatch alarms that determine when a service deployment fails.
Type: [ServiceDeploymentAlarms](API_ServiceDeploymentAlarms.md) object
Required: No

 ** clusterArn **   <a name="ECS-Type-ServiceDeployment-clusterArn"></a>
The ARN of the cluster that hosts the service.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-ServiceDeployment-createdAt"></a>
The time the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** deploymentCircuitBreaker **   <a name="ECS-Type-ServiceDeployment-deploymentCircuitBreaker"></a>
The circuit breaker configuration that determines a service deployment failed.
Type: [ServiceDeploymentCircuitBreaker](API_ServiceDeploymentCircuitBreaker.md) object
Required: No

 ** deploymentConfiguration **   <a name="ECS-Type-ServiceDeployment-deploymentConfiguration"></a>
Optional deployment parameters that control how many tasks run during a deployment and the ordering of stopping and starting tasks.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** finishedAt **   <a name="ECS-Type-ServiceDeployment-finishedAt"></a>
The time the service deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** lifecycleHookDetails **   <a name="ECS-Type-ServiceDeployment-lifecycleHookDetails"></a>
The details of the lifecycle hooks for the current service deployment.
Type: Array of [DeploymentLifecycleHookDetail](API_DeploymentLifecycleHookDetail.md) objects
Required: No

 ** lifecycleStage **   <a name="ECS-Type-ServiceDeployment-lifecycleStage"></a>
The current lifecycle stage of the deployment. Possible values include:
+ RECONCILE\_SERVICE

  The reconciliation stage that only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state.
+ PRE\_SCALE\_UP

  The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic.
+ SCALE\_UP

  The stage when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point.
+ POST\_SCALE\_UP

  The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic.
+ TEST\_TRAFFIC\_SHIFT

  The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic.
+ POST\_TEST\_TRAFFIC\_SHIFT

  The test traffic shift is complete. The green service revision handles 100% of the test traffic.
+ PRE\_PRODUCTION\_TRAFFIC\_SHIFT

  Occurs before production traffic shift. For linear and canary deployments, this stage is invoked before every traffic shift step.
+ PRODUCTION\_TRAFFIC\_SHIFT

  Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic. For linear and canary deployments, this stage is invoked at every traffic shift step.
+ POST\_PRODUCTION\_TRAFFIC\_SHIFT

  The production traffic shift is complete.
+ BAKE\_TIME

  The stage when both blue and green service revisions are running simultaneously after the production traffic has shifted.
+ CLEAN\_UP

  The stage when the blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage.
Type: String
Valid Values: `RECONCILE_SERVICE | PRE_SCALE_UP | SCALE_UP | POST_SCALE_UP | TEST_TRAFFIC_SHIFT | POST_TEST_TRAFFIC_SHIFT | PRODUCTION_TRAFFIC_SHIFT | POST_PRODUCTION_TRAFFIC_SHIFT | BAKE_TIME | CLEAN_UP`
Required: No

 ** rollback **   <a name="ECS-Type-ServiceDeployment-rollback"></a>
The rollback options the service deployment uses when the deployment fails.
Type: [Rollback](API_Rollback.md) object
Required: No

 ** serviceArn **   <a name="ECS-Type-ServiceDeployment-serviceArn"></a>
The ARN of the service for this service deployment.
Type: String
Required: No

 ** serviceDeploymentArn **   <a name="ECS-Type-ServiceDeployment-serviceDeploymentArn"></a>
The ARN of the service deployment.
Type: String
Required: No

 ** sourceServiceRevisions **   <a name="ECS-Type-ServiceDeployment-sourceServiceRevisions"></a>
The currently deployed workload configuration.
Type: Array of [ServiceRevisionSummary](API_ServiceRevisionSummary.md) objects
Required: No

 ** startedAt **   <a name="ECS-Type-ServiceDeployment-startedAt"></a>
The time the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** status **   <a name="ECS-Type-ServiceDeployment-status"></a>
The service deployment state.
Type: String
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_REQUESTED | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

 ** statusReason **   <a name="ECS-Type-ServiceDeployment-statusReason"></a>
Information about why the service deployment is in the current status. For example, the circuit breaker detected a failure.
Type: String
Required: No

 ** stoppedAt **   <a name="ECS-Type-ServiceDeployment-stoppedAt"></a>
The time the service deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
The service deployment stops when any of the following actions happen:
+ A user manually stops the deployment
+ The rollback option is not in use for the failure detection mechanism (the circuit breaker or alarm-based) and the service fails.
Type: Timestamp
Required: No

 ** targetServiceRevision **   <a name="ECS-Type-ServiceDeployment-targetServiceRevision"></a>
The workload configuration being deployed.
Type: [ServiceRevisionSummary](API_ServiceRevisionSummary.md) object
Required: No

 ** updatedAt **   <a name="ECS-Type-ServiceDeployment-updatedAt"></a>
The time that the service deployment was last updated. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

## See Also
<a name="API_ServiceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceDeployment)
