---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RollbackInfo.html
---

# RollbackInfo
<a name="API_RollbackInfo"></a>

Information about a deployment rollback.

## Contents
<a name="API_RollbackInfo_Contents"></a>

 ** rollbackDeploymentId **   <a name="CodeDeploy-Type-RollbackInfo-rollbackDeploymentId"></a>
The ID of the deployment rollback.
Type: String
Required: No

 ** rollbackMessage **   <a name="CodeDeploy-Type-RollbackInfo-rollbackMessage"></a>
Information that describes the status of a deployment rollback (for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded).
Type: String
Required: No

 ** rollbackTriggeringDeploymentId **   <a name="CodeDeploy-Type-RollbackInfo-rollbackTriggeringDeploymentId"></a>
The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.
Type: String
Required: No

## See Also
<a name="API_RollbackInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RollbackInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RollbackInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RollbackInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
