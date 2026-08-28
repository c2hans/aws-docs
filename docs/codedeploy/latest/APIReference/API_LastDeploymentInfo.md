---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LastDeploymentInfo.html
---

# LastDeploymentInfo
<a name="API_LastDeploymentInfo"></a>

Information about the most recent attempted or successful deployment to a deployment group.

## Contents
<a name="API_LastDeploymentInfo_Contents"></a>

 ** createTime **   <a name="CodeDeploy-Type-LastDeploymentInfo-createTime"></a>
A timestamp that indicates when the most recent deployment to the deployment group started.
Type: Timestamp
Required: No

 ** deploymentId **   <a name="CodeDeploy-Type-LastDeploymentInfo-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** endTime **   <a name="CodeDeploy-Type-LastDeploymentInfo-endTime"></a>
A timestamp that indicates when the most recent deployment to the deployment group was complete.
Type: Timestamp
Required: No

 ** status **   <a name="CodeDeploy-Type-LastDeploymentInfo-status"></a>
The status of the most recent deployment.
Type: String
Valid Values: `Created | Queued | InProgress | Baking | Succeeded | Failed | Stopped | Ready`
Required: No

## See Also
<a name="API_LastDeploymentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/LastDeploymentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/LastDeploymentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/LastDeploymentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
