---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-root.html
---

# `/root` (root user home directory)
<a name="filesystem-slash-root"></a>

 The home directory of the root user is the `/root` directory, purposefully separate from [`/home` (User home directories)](filesystem-slash-home.md) so that it is present in the event that [`/home` (User home directories)](filesystem-slash-home.md) is on a file system which is not available.

 The best practice for configuring `systemd` services is the same for `/root` as it is for [`/home` (User home directories)](filesystem-slash-home.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
