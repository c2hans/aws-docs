---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceTarget.html
---

# InstanceTarget
<a name="API_InstanceTarget"></a>

 A target Amazon EC2 or on-premises instance during a deployment that uses the EC2/On-premises compute platform.

## Contents
<a name="API_InstanceTarget_Contents"></a>

 ** deploymentId **   <a name="CodeDeploy-Type-InstanceTarget-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** instanceLabel **   <a name="CodeDeploy-Type-InstanceTarget-instanceLabel"></a>
 A label that identifies whether the instance is an original target (`BLUE`) or a replacement target (`GREEN`).
Type: String
Valid Values: `Blue | Green`
Required: No

 ** lastUpdatedAt **   <a name="CodeDeploy-Type-InstanceTarget-lastUpdatedAt"></a>
 The date and time when the target instance was updated by a deployment.
Type: Timestamp
Required: No

 ** lifecycleEvents **   <a name="CodeDeploy-Type-InstanceTarget-lifecycleEvents"></a>
 The lifecycle events of the deployment to this target instance.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** status **   <a name="CodeDeploy-Type-InstanceTarget-status"></a>
 The status an EC2/On-premises deployment's target instance.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

 ** targetArn **   <a name="CodeDeploy-Type-InstanceTarget-targetArn"></a>
 The Amazon Resource Name (ARN) of the target.
Type: String
Required: No

 ** targetId **   <a name="CodeDeploy-Type-InstanceTarget-targetId"></a>
 The unique ID of a deployment target that has a type of `instanceTarget`.
Type: String
Required: No

## See Also
<a name="API_InstanceTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/InstanceTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/InstanceTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/InstanceTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
