---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeploymentTarget.html
---

# DeploymentTarget
<a name="API_DeploymentTarget"></a>

 Information about the deployment target.

## Contents
<a name="API_DeploymentTarget_Contents"></a>

 ** cloudFormationTarget **   <a name="CodeDeploy-Type-DeploymentTarget-cloudFormationTarget"></a>
 Information about the target to be updated by an CloudFormation blue/green deployment. This target type is used for all deployments initiated by a CloudFormation stack update.
Type: [CloudFormationTarget](API_CloudFormationTarget.md) object
Required: No

 ** deploymentTargetType **   <a name="CodeDeploy-Type-DeploymentTarget-deploymentTargetType"></a>
The deployment type that is specific to the deployment's compute platform or deployments initiated by a CloudFormation stack update.
Type: String
Valid Values: `InstanceTarget | LambdaTarget | ECSTarget | EKSTarget | CloudFormationTarget`
Required: No

 ** ecsTarget **   <a name="CodeDeploy-Type-DeploymentTarget-ecsTarget"></a>
 Information about the target for a deployment that uses the Amazon ECS compute platform.
Type: [ECSTarget](API_ECSTarget.md) object
Required: No

 ** instanceTarget **   <a name="CodeDeploy-Type-DeploymentTarget-instanceTarget"></a>
 Information about the target for a deployment that uses the EC2/On-premises compute platform.
Type: [InstanceTarget](API_InstanceTarget.md) object
Required: No

 ** lambdaTarget **   <a name="CodeDeploy-Type-DeploymentTarget-lambdaTarget"></a>
 Information about the target for a deployment that uses the AWS Lambda compute platform.
Type: [LambdaTarget](API_LambdaTarget.md) object
Required: No

## See Also
<a name="API_DeploymentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeploymentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeploymentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeploymentTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
