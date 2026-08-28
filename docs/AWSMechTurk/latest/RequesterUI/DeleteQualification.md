---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/DeleteQualification.html
---

# Delete qualification types
<a name="DeleteQualification"></a>

The following procedure shows you how to delete qualification types.

**To delete a qualification type**

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/), choose the **Manage** tab and then choose **Qualification Types**.

1. On the **Qualification Types** page, choose the **X** next to the qualification type you want to delete.

1. Choose **Dispose** to confirm the deletion.

There is a short delay before the new qualification type is removed from the list. You can refresh your browser to update the list.

When you delete a qualification type, it is removed from all of your Workers and HIT templates. The deleted qualification type is not removed from HITs that Workers are working on.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
