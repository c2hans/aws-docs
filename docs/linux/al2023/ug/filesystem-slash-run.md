---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-run.html
---

# `/run` (runtime data)
<a name="filesystem-slash-run"></a>

 The `/run` directory is used by system packages to store small amounts of runtime data (such as socket files). It is a `tmpfs` file system, and is writable only by privileged programs.

 The `/run/log` directory can be used by system components to store logs in, either before being written out to `/var/log` or before the `/var/log` file system is available.

 The `/run/user/` path contains per-user runtime directories. By default, these will be individual `tmpfs` file systems mounted by `systemd` when the user logs in, and erased when the user is no longer logged in. As per the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/), these paths should not be referenced directly but rather via the `$XDG_RUNTIME_DIR` environment variable.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
