---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LocationalDeployment.html
---

# LocationalDeployment
<a name="API_LocationalDeployment"></a>

For a multi-location container fleet, describes the progress of a deployment across all fleet locations.

## Contents
<a name="API_LocationalDeployment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DeploymentStatus **   <a name="gameliftservers-Type-LocationalDeployment-DeploymentStatus"></a>
The status of fleet deployment activity in the location.
+  `IN_PROGRESS` -- The deployment is in progress in the location. This status covers validation as well as the replacement of the location's containers.
+  `IMPAIRED` -- The deployment failed validation in the location, and the location kept the containers that failed validation so that you can inspect them. A location reaches this status when the deployment's impairment strategy is `MAINTAIN`.
+  `COMPLETE` -- The deployment has completed successfully in the location.
+  `ROLLBACK_IN_PROGRESS` -- The deployment failed and rollback has been initiated in the location. A location reaches this status when the deployment's impairment strategy is `ROLLBACK`.
+  `ROLLBACK_COMPLETE` -- The deployment failed and rollback has been completed in the location. The location is running the configuration from the last successful deployment.
+  `CANCELLED` -- The deployment was cancelled because a new deployment started for the same fleet.
Type: String
Valid Values: `IN_PROGRESS | IMPAIRED | COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | CANCELLED | PENDING`
Required: No

## See Also
<a name="API_LocationalDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationalDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationalDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationalDeployment)
