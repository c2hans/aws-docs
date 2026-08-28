---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/review-settings.html
---

# Launching a web portal with Amazon WorkSpaces Secure Browser
<a name="review-settings"></a>

When you are finished configuring your web portal, you can follow these steps to launch it.

1. On the **Step 5: Review and launch** page, review the settings you selected for your web portal. You can choose **Edit** to changes settings within a given section. You can also change these settings later on from the **Web portals** tab of the console.

1. When you're done, choose **Launch web portal**.

1. To view the status of your web portal, choose **Web portals**, choose your portal, and then choose **View details**.

   A web portal has one of the following statuses:
   + **Incomplete** - The web portal's configuration is missing required identity provider settings.
   + **Pending** - The web portal is applying changes to its settings.
   + **Active** - The web portal is ready and available for use.

1. Wait up to 15 minutes for your portal to become **Active**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
