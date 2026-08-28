---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/entering-environment-details.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Step 1: Enter your environment details
<a name="entering-environment-details"></a>

1. Enter a name for your environment in the **Environment details** field.

1. To set up automatic software patches, check the box for **Always keep software up-to-date**.
**Note**
If automatic software updates is not enabled, the devices registered to this environment won't receive software updates until you manually push the update or when the software reaches its expiration and the system forces an update.
Also, the devices Software Set version is determined by the system. This version may not be the most recent one.

1. Select when you want to schedule the maintenance window for your environment.
   + **Apply system wide maintenance window** - Automatically updates the environment software at a determined time each week.
   + **Apply custom maintenance window** - Set a day and time when you want the environment software to update each week.

1. Select a virtual desktop service.
   + [Amazon WorkSpaces](virtual-service-providers.md#setting-up-ws)
   + [Amazon WorkSpaces Secure Browser](virtual-service-providers.md#setting-up-wsw)
   + [WorkSpaces Applications](virtual-service-providers.md#setting-up-as)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
