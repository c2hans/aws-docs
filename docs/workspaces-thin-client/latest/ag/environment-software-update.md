---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-software-update.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Updating environment software
<a name="environment-software-update"></a>

WorkSpaces Thin Client is an AWS End User Computing service that provides users access to virtual desktops. These virtual desktops are periodically updated with new software sets. To update environment software, do the following:

1. Select the software set from the list in **Available software updates**. For a list of software sets, refer to [WorkSpaces Thin Client environment software sets](environment-software-sets.md).

1. Select the **Install** button.

1. Select **Environments** at the top of the page.

1. Select the environment to update from the list in the **Environments** section.

1. Select when to update the environment in the **Schedule the update** by choosing one of the following:
   + **Update software now** - Starts the update of the environment software on all registered devices.
**Note**
Updating software now may interrupt any active user sessions.
   + **Update software during each environments maintenance window** - Updates the environment software during the scheduled maintenance window for the environment.

1. Check the box to authorize the update. This box must be checked for the software to update.

1. Select the **Install** button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
