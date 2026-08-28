---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides known issue resolution when deploying the solution.

If these instructions don’t address your issue, [Contact AWS Support](contact-aws-support.md) provides instructions for opening an Support case for this solution.

## Problem: Handling intermittent issues during solution deployment
<a name="problem-handling-intermittent-issues-during-solution-deployment"></a>

You receive a **CREATE\_FAILED** message for the single stack or the underlying module’s CloudFormation stacks during the stack deployment.

## Resolution
<a name="resolution"></a>

Complete the following steps to resolve this issue:

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. From the list of CloudFormation stacks, select any stack that is in **ROLLBACK\_COMPLETE** state. This could be an underlying module’s specific stack or the single-click `scene-intelligence-with-rosbag-on-aws-create` stack.

1. Delete the stack by following the instructions for [Deleting a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the *AWS CloudFormation User Guide*.

1. Modify the `scene-intelligence-with-rosbag-on-aws-create.template` CloudFormation template by following these steps:

   1. Download the [template](https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-create.template).

   1. Change the [wait condition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html) names. Wait condition names must be unique on every creation of a CloudFormation stack. The following is an example on how to modify the wait condition handler name from `CodeBuildRunWaitConditionHandler01` to `CodeBuildRunWaitConditionHandler02`, and update the `CallbackUrl` to reflect the changed wait condition handler name under `CodeBuildRun` custom resource.

      ```
      ## Update WaitConditionHandle Logical Id

      CodeBuildRun:
       Type: AWS::CloudFormation::CustomResource
       Properties:
       ServiceToken: !GetAtt CodeBuildLambda.Arn
       BuildProjectName: ! Ref CreateUpdateCodeBuildProject
       CallbackUrl: !Ref CodeBuildRunWaitConditionHandler01 # Update Here
      CodeBuildRunWaitConditionHandler01 # Update Here
       Type: AWS::CloudFormation::WaitConditionHandle

      ## Example of Updated Template Content

      CodeBuildRun:
       Type: AWS::CloudFormation::CustomResource
       Properties:
       ServiceToken: !GetAtt CodeBuildLambda.Arn
       BuildProjectName: ! Ref CreateUpdateCodeBuildProject
       CallbackUrl: !Ref CodeBuildRunWaitConditionHandler02 # Update Here
      CodeBuildRunWaitConditionHandler02 # Update Here
       Type: AWS::CloudFormation::WaitConditionHandle
      ```

1. Create a new deployment using the modified `scene-intelligence-with-rosbag-on-aws-create.template` CloudFormation template by following the instructions in [Launch the stack](launch-the-deployment-stack.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
