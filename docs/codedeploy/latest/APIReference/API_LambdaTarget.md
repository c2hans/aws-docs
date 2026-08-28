---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LambdaTarget.html
---

# LambdaTarget
<a name="API_LambdaTarget"></a>

 Information about the target AWS Lambda function during an AWS Lambda deployment.

## Contents
<a name="API_LambdaTarget_Contents"></a>

 ** deploymentId **   <a name="CodeDeploy-Type-LambdaTarget-deploymentId"></a>
 The unique ID of a deployment.
Type: String
Required: No

 ** lambdaFunctionInfo **   <a name="CodeDeploy-Type-LambdaTarget-lambdaFunctionInfo"></a>
 A `LambdaFunctionInfo` object that describes a target Lambda function.
Type: [LambdaFunctionInfo](API_LambdaFunctionInfo.md) object
Required: No

 ** lastUpdatedAt **   <a name="CodeDeploy-Type-LambdaTarget-lastUpdatedAt"></a>
 The date and time when the target Lambda function was updated by a deployment.
Type: Timestamp
Required: No

 ** lifecycleEvents **   <a name="CodeDeploy-Type-LambdaTarget-lifecycleEvents"></a>
 The lifecycle events of the deployment to this target Lambda function.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** status **   <a name="CodeDeploy-Type-LambdaTarget-status"></a>
 The status an AWS Lambda deployment's target Lambda function.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

 ** targetArn **   <a name="CodeDeploy-Type-LambdaTarget-targetArn"></a>
 The Amazon Resource Name (ARN) of the target.
Type: String
Required: No

 ** targetId **   <a name="CodeDeploy-Type-LambdaTarget-targetId"></a>
 The unique ID of a deployment target that has a type of `lambdaTarget`.
Type: String
Required: No

## See Also
<a name="API_LambdaTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/LambdaTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/LambdaTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/LambdaTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
