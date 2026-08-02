---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceDeploymentBrief.html
---

# ServiceDeploymentBrief
<a name="API_ServiceDeploymentBrief"></a>

The service deployment properties that are retured when you call `ListServiceDeployments`.

This provides a high-level overview of the service deployment.

## Contents
<a name="API_ServiceDeploymentBrief_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-ServiceDeploymentBrief-clusterArn"></a>
The ARN of the cluster that hosts the service.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-ServiceDeploymentBrief-createdAt"></a>
The time that the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** finishedAt **   <a name="ECS-Type-ServiceDeploymentBrief-finishedAt"></a>
The time that the service deployment completed. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** serviceArn **   <a name="ECS-Type-ServiceDeploymentBrief-serviceArn"></a>
The ARN of the service for this service deployment.
Type: String
Required: No

 ** serviceDeploymentArn **   <a name="ECS-Type-ServiceDeploymentBrief-serviceDeploymentArn"></a>
The ARN of the service deployment.
Type: String
Required: No

 ** startedAt **   <a name="ECS-Type-ServiceDeploymentBrief-startedAt"></a>
The time that the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** status **   <a name="ECS-Type-ServiceDeploymentBrief-status"></a>
The status of the service deployment
Type: String
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_REQUESTED | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

 ** statusReason **   <a name="ECS-Type-ServiceDeploymentBrief-statusReason"></a>
Information about why the service deployment is in the current status. For example, the circuit breaker detected a deployment failure.
Type: String
Required: No

 ** targetServiceRevisionArn **   <a name="ECS-Type-ServiceDeploymentBrief-targetServiceRevisionArn"></a>
The ARN of the service revision being deplyed.
Type: String
Required: No

## See Also
<a name="API_ServiceDeploymentBrief_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceDeploymentBrief)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceDeploymentBrief)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceDeploymentBrief)
