---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_Deployment.html
---

# Deployment
<a name="API_Deployment"></a>

Information about an application version deployment.

## Contents
<a name="API_Deployment_Contents"></a>

 ** DeploymentId **
The ID of the deployment. This number increases by one each time that you deploy source code or change instance configuration settings.
Type: Long
Required: No

 ** DeploymentTime **
For in-progress deployments, the time that the deployment started.
For completed deployments, the time that the deployment ended.
Type: Timestamp
Required: No

 ** Status **
The status of the deployment:
+  `In Progress` : The deployment is in progress.
+  `Deployed` : The deployment succeeded.
+  `Failed` : The deployment failed.
Type: String
Required: No

 ** VersionLabel **
The version label of the application version in the deployment.
Type: String
Required: No

## See Also
<a name="API_Deployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/Deployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/Deployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/Deployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
