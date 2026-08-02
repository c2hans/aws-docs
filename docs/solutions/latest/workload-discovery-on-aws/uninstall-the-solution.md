---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

To uninstall the solution, use the AWS Management Console or the AWS Command Line Interface (AWS CLI). First, [stop all running tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-task-console-v2.html) from the Amazon ECS cluster. Otherwise, stack deletion can fail.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Select the stack with the name provided during deployment.

1. Choose **Delete stack**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS CLI is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*.

After confirming that the AWS CLI is available, run the following command:

```
$ aws cloudformation delete-stack --stack-name <customer-defined-stack-name>
```
