---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_MinimumHealthyHosts.html
---

# MinimumHealthyHosts
<a name="API_MinimumHealthyHosts"></a>

Information about the minimum number of healthy instances.

## Contents
<a name="API_MinimumHealthyHosts_Contents"></a>

 ** type **   <a name="CodeDeploy-Type-MinimumHealthyHosts-type"></a>
The minimum healthy instance type:
+  `HOST_COUNT`: The minimum number of healthy instances as an absolute value.
+  `FLEET_PERCENT`: The minimum number of healthy instances as a percentage of the total number of instances in the deployment.
In an example of nine instances, if a HOST\_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET\_PERCENT of 40 is specified, deploy to up to five instances at a time. The deployment is successful if four or more instances are deployed to successfully. Otherwise, the deployment fails.
In a call to the `GetDeploymentConfig`, CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST\_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST\_CONCURRENCY, only to HOST\_COUNT or FLEET\_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.
For more information, see [AWS CodeDeploy Instance Health](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html) in the * AWS CodeDeploy User Guide*.
Type: String
Valid Values: `HOST_COUNT | FLEET_PERCENT`
Required: No

 ** value **   <a name="CodeDeploy-Type-MinimumHealthyHosts-value"></a>
The minimum healthy instance value.
Type: Integer
Required: No

## See Also
<a name="API_MinimumHealthyHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/MinimumHealthyHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/MinimumHealthyHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/MinimumHealthyHosts)
