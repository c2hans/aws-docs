---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/manage-test-sets.html
---

# Manage test sets
<a name="manage-test-sets"></a>

You can download, update, and delete test sets from the test set window. Or you can use the list of available test sets to edit or manually annotate your test set file. Then, upload it again to retry validation, due to errors or other input issues.

**To download the test set file from test set record:**

1. Select the name of the test set from the list of test sets.

1. In the test set record window, select the **Download** button on the right side of the screen in the **Test Inputs** section.

1. if there are any validation error details at the top of the window regarding the test set, select the **Download** button. The file will be saved to your Downloads folder. You can fix the validation errors in the test set from the error messages in the test set CSV file. Find the error identified in the validation step, fix the line or remove it, and upload the file to retry the validation step.

1. if you successfully download the test set, a green banner messages will appear.

**To download a test set from the list of test sets:**

1. From the list of test sets, select the radio button next to the test set item you want to download.

1. From the Action menu at the top right, choose **Download**.

1. A green banner message will indicate if you successfully have downloaded the test set. The file will be saved to your Downloads folder.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
