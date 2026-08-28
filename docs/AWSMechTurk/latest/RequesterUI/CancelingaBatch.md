---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/CancelingaBatch.html
---

# Cancel a batch
<a name="CancelingaBatch"></a>

If the batch you published isn't working the way you'd like, you can cancel it.

**To cancel a batch**

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/), choose the **Manage** tab and then choose **Results**.

1. Under **Manage Batches**, choose the arrow next to **Batches in progress**.

1. Choose **Cancel** on the batch you want to delete.

1. In the **Cancel Batch** dialog box, choose **Yes**.

It can take several minutes to cancel a batch. All Workers who accepted assignments before you deleted the batch can continue working on them. The batch won't be completely deleted until all assignments accepted by Workers have been returned, submitted, or abandoned.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
