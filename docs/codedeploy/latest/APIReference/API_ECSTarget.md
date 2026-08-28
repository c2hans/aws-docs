---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ECSTarget.html
---

# ECSTarget
<a name="API_ECSTarget"></a>

 Information about the target of an Amazon ECS deployment.

## Contents
<a name="API_ECSTarget_Contents"></a>

 ** deploymentId **   <a name="CodeDeploy-Type-ECSTarget-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** lastUpdatedAt **   <a name="CodeDeploy-Type-ECSTarget-lastUpdatedAt"></a>
 The date and time when the target Amazon ECS application was updated by a deployment.
Type: Timestamp
Required: No

 ** lifecycleEvents **   <a name="CodeDeploy-Type-ECSTarget-lifecycleEvents"></a>
 The lifecycle events of the deployment to this target Amazon ECS application.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** status **   <a name="CodeDeploy-Type-ECSTarget-status"></a>
 The status an Amazon ECS deployment's target ECS application.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

 ** targetArn **   <a name="CodeDeploy-Type-ECSTarget-targetArn"></a>
 The Amazon Resource Name (ARN) of the target.
Type: String
Required: No

 ** targetId **   <a name="CodeDeploy-Type-ECSTarget-targetId"></a>
 The unique ID of a deployment target that has a type of `ecsTarget`.
Type: String
Required: No

 ** taskSetsInfo **   <a name="CodeDeploy-Type-ECSTarget-taskSetsInfo"></a>
 The `ECSTaskSet` objects associated with the ECS target.
Type: Array of [ECSTaskSet](API_ECSTaskSet.md) objects
Required: No

## See Also
<a name="API_ECSTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ECSTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ECSTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ECSTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
