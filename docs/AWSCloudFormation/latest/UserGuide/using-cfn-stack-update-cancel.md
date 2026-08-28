---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-update-cancel.html
---

# Cancel a stack update
<a name="using-cfn-stack-update-cancel"></a>

After a stack update has begun, you can cancel the stack update if the stack is still in the `UPDATE_IN_PROGRESS` state. After an update has finished, you can't cancel it. You can, however, update a stack again with any previous settings.

If you cancel a stack update, the stack is rolled back to the stack configuration that existed before initiating the stack update.

**Topics**
+ [To cancel a stack update (console)](#using-cfn-stack-update-cancel-console)
+ [To cancel a stack update (AWS CLI)](#using-cfn-stack-update-cancel-cli)

## To cancel a stack update (console)
<a name="using-cfn-stack-update-cancel-console"></a>

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where the stack is located.

1. On the **Stacks** page, choose the stack that's currently being updated. Its status must be `UPDATE_IN_PROGRESS`.

1. Choose **Stack actions** and then **Cancel update stack**.

1. To continue canceling the update, choose **Cancel update**. Otherwise, choose **Cancel** to resume the update.

The stack proceeds to the `UPDATE_ROLLBACK_IN_PROGRESS` state. After the update cancellation is complete, the stack is set to `UPDATE_ROLLBACK_COMPLETE`.

## To cancel a stack update (AWS CLI)
<a name="using-cfn-stack-update-cancel-cli"></a>

Use the command [cancel-update-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/cancel-update-stack.html) to cancel an update. For more information, see [Cancel a stack update](service_code_examples.md#cancel-update-stack-sdk).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
