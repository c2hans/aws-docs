---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_FleetDeployment.html
---

# FleetDeployment
<a name="API_FleetDeployment"></a>

Describes a container fleet deployment with updates to the fleet.

## Contents
<a name="API_FleetDeployment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationTime **   <a name="gameliftservers-Type-FleetDeployment-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** DeploymentConfiguration **   <a name="gameliftservers-Type-FleetDeployment-DeploymentConfiguration"></a>
Instructions for how to deploy updates to a container fleet and what actions to take if the deployment fails.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** DeploymentId **   <a name="gameliftservers-Type-FleetDeployment-DeploymentId"></a>
A unique identifier for the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** DeploymentStatus **   <a name="gameliftservers-Type-FleetDeployment-DeploymentStatus"></a>
The status of fleet deployment activity in the location.
+  `IN_PROGRESS` -- The deployment is in progress.
+  `IMPAIRED` -- The deployment failed and the fleet has some impaired containers.
+  `COMPLETE` -- The deployment has completed successfully.
+  `ROLLBACK_IN_PROGRESS` -- The deployment failed and rollback has been initiated.
+  `ROLLBACK_IN_COMPLETE` -- The deployment failed and rollback has been completed.
+  `CANCELLED` -- The deployment was cancelled.
Type: String
Valid Values: `IN_PROGRESS | IMPAIRED | COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | CANCELLED | PENDING`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-FleetDeployment-FleetId"></a>
A unique identifier for the container fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** GameServerBinaryArn **   <a name="gameliftservers-Type-FleetDeployment-GameServerBinaryArn"></a>
The unique identifier for the version of the game server container group definition that is being deployed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** PerInstanceBinaryArn **   <a name="gameliftservers-Type-FleetDeployment-PerInstanceBinaryArn"></a>
The unique identifier for the version of the per-instance container group definition that is being deployed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** RollbackGameServerBinaryArn **   <a name="gameliftservers-Type-FleetDeployment-RollbackGameServerBinaryArn"></a>
The unique identifier for the version of the game server container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

 ** RollbackPerInstanceBinaryArn **   <a name="gameliftservers-Type-FleetDeployment-RollbackPerInstanceBinaryArn"></a>
The unique identifier for the version of the per-instance container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9:/-]+`
Required: No

## See Also
<a name="API_FleetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/FleetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/FleetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/FleetDeployment)
