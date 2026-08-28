---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/fixing-windows-cursor-issues.html
---

# Fixing cursor issues on Windows
<a name="fixing-windows-cursor-issues"></a>

With Amazon DCV servers running on Windows Server 2016 or Windows 10 and later, the mouse cursor always appears as an arrow. This happens even when pausing on text entry fields or single-click navigation items. This could happen if there is no physical mouse attached to the server, or if there is no mouse device listed in Device Manager.

**To resolve the issue**

1. Open Control Panel, and choose **Ease of Access Center**.

1. Choose **Make the mouse easier to use**.

1. Select **Turn on Mouse Keys**.

1. Choose **Apply**, **OK**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
