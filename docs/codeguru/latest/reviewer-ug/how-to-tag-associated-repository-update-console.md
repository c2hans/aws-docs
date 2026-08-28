---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update-console.html
---

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Add or update tags for a CodeGuru Reviewer associated repository (console)
<a name="how-to-tag-associated-repository-update-console"></a>

You can use the CodeGuru Reviewer console to update, add, or remove the tags associated with a CodeGuru Reviewer associated repository. Using the console, you can also change the name of the key, which is equivalent to removing the current tag and adding a different one with the new name and the same value.

**To add or update tags for an associated repository**

1. Open the Amazon CodeGuru Reviewer console at [https://console.aws.amazon.com/codeguru/reviewer/](https://console.aws.amazon.com/codeguru/reviewer/).

1. In the navigation pane, choose **Repositories**.

1. Do one of the following:
   + Choose the association ID of the associated repository where you want to view tags, then choose **Manage tags**.
   + Choose the radio button next to the associated repository where you want to view tags, then choose **Manage tags**.

1. Enter new values in **key** and **value** to edit tags. Choose **Remove** next to a tag to remove it. Choose **Add new tag** to add a new tag.

1. Choose **Save changes** when you are finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
