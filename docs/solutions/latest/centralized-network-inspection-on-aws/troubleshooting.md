---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

 This section provides known issue resolution when deploying the guidance.

## Problem: Missing Network Firewall resources
<a name="problem-missing-network-firewall-resources"></a>

 The CloudFormation stack has completed successfully, but not all the Network Firewall resources are created.

### Resolution
<a name="resolution"></a>

 After the CloudFormation stack is complete, the CodePipeline stage created by the solution might still be in the `In-Progress` state. Once the CodePipeline stage is completed, all the Network Firewall resources will be available in the AWS Network Firewall console.

## Problem: Failed CodePipeline stage
<a name="problem-failed-codepipeline-stage"></a>

 The CodePipeline stage is failing.

### Resolution
<a name="resolution-1"></a>

 If the CodePipeline stage is in `Failed` state, it means that this guidance hasn't been able to complete the create or update network firewall resources operation. Refer to the logs in the CodePipeline stages to ensure that the CodeBuild stages are successful.

 If a JSON file is not valid or has incorrect information, the CodeBuild stage that validates the files will list the errors along with the file names.

 For more information, refer to the [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html).
