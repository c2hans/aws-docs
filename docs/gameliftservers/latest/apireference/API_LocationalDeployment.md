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
+  `IN_PROGRESS` -- The deployment is in progress.
+  `IMPAIRED` -- The deployment failed and the fleet has some impaired containers.
+  `COMPLETE` -- The deployment has completed successfully.
+  `ROLLBACK_IN_PROGRESS` -- The deployment failed and rollback has been initiated.
+  `ROLLBACK_IN_COMPLETE` -- The deployment failed and rollback has been completed.
+  `CANCELLED` -- The deployment was cancelled.
Type: String
Valid Values: `IN_PROGRESS | IMPAIRED | COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETE | CANCELLED | PENDING`
Required: No

## See Also
<a name="API_LocationalDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LocationalDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LocationalDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LocationalDeployment)
