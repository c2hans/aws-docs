---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create-delete-edit-summary.html
---

# Summary of actions
<a name="multiplex-create-delete-edit-summary"></a>

The following table summarizes the create, edit, and delete capabilities for the MediaLive multiplex, program, and channel.

| Item | Action | Note |
| --- | --- | --- |
| Multiplex | Create |  |
|  | Edit | The multiplex can be idle or running. The channels can be all idle, or all running, or a combination or idle and running.<br />Exception: To change the **Max Video Buffer Delay** field, the multiplex must be idle. |
|  | Delete | The multiplex must be idle, and must not have any associated programs. |
| Program | Create | The multiplex for the program can be idle or running.  |
|  | Edit | The multiplex for this program can be idle or running. The channel for this program can be idle or running. |
|  | Delete | The multiplex for this program can be idle or running. The program can't have any associated channel. |
| Channel | Create | The multiplex for this channel can be idle or running. The program for the channel must be empty. |
|  | Edit | The channel must be idle. The multiplex for this channel can be idle or running.  |
|  | Delete | The channel must be idle. The channel can still be attached to a program. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
