---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/manage-layouts-security-profiles.html
---

# Security profiles needed to manage layouts
<a name="manage-layouts-security-profiles"></a>

Access to Manage layouts is controlled by the same Profile explorer permissions described in [Enable Profile explorer](enabling-profile-explorer.md). The following permissions determine what a user can do:
+ **Profile explorer - View**: Required to open Profile explorer and view the currently active default layout.
+ **Profile explorer - Edit**: Required to see and open the **Manage layouts** button, access the **Profile layouts** page, and use the **Delete** and **Make default** actions on that page. This permission is also required, along with **Profile explorer - Create**, to see the layout editor toolbar (**Edit tabs**, **Add widget**, and **Save layout**).
+ **Profile explorer - Create**: Required to see and choose the **Create layout** button on the **Profile layouts** page.

**Note**
There's no separate permission for deleting a layout or setting a layout as default—both actions are controlled by **Profile explorer - Edit**.

For instructions on assigning these permissions, see [Enable administrators to define a layout](enabling-profile-explorer.md#enable-administrators-define-layout).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
