---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-core-pipeline-failure.html
---

# Problem: Core pipeline failure
<a name="problem-core-pipeline-failure"></a>

## Resolution
<a name="resolution-1"></a>

To determine the cause of a deployment failure, use the following steps:

1. Sign in to the AWS Management Console and navigate to the **AWS CodePipeline** console. Select **AWSAccelerator-Pipeline** and find the pipeline stage that failed.

1. The pipeline stage has a CodeBuild project as an action provider. Select the **Details** link under the failed status indicator for the action, then choose **Link to execution details**. This opens the failed processing of the CodeBuild project.

1. Select the **Build logs** tab. This shows the output of the CodeBuild project run. Scrolling to the bottom of this output, you will see an error message. Some common examples are:
   + Misconfiguration or missing properties in the Landing Zone Accelerator on AWS configuration files. This causes the Core pipeline to fail in the **Build** stage. The configuration validator provides a specific error message indicating what caused the property validation to fail.
   + CloudFormation deployment error. This can occur in any stack. CloudFormation provides a specific error message indicating what caused the deployment failure.

**Note**
Regardless of the failure that occurs, build logs will show the following error message at the end:
 `[Container] Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: yarn run ts-node --transpile-only cdk.ts --require-approval never $CDK_OPTIONS --config-dir $CODEBUILD_SRC_DIR_Config --partition aws --app cdk.out. Reason: exit status 1`
This is a generic error message that CodeBuild outputs when the CDK application fails to complete successfully. When troubleshooting deployment errors, the text before this error message indicates which resource(s) failed to deploy.
