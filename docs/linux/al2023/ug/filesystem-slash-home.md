---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-home.html
---

# `/home` (User home directories)
<a name="filesystem-slash-home"></a>

 Normal users have their home directories under `/home`, but software should always look for the per-user `$HOME` environment variable rather than relying on a pattern such as `/home/$USER`.

 By default, AL2023 images have `/home` on the root file system, but software should not rely on this. It is perfectly valid for the OS to be configured for `/home` to be a separate file system, which is mounted later during boot, or only after a user authenticates to the system.

 The root user home directory is not in `/home` but rather is [`/root` (root user home directory)](filesystem-slash-root.md) so that it is available in the event that the `/home` file system cannot be mounted.

**Note**
 It is best practice for `systemd` services which do not need write access to `/home` to be configured with the `ProtectHome=read-only` directive. With this option, `/home`, `/root`, and `/run/user` are made read-only for the service.
 It is also best practice for services that do not need any access to `/home` to be configured with the `ProtectHome=tmpfs` directive, which will run the service in a sandbox where `/home`, `/root`, and `/run/user` are empty read-only `tmpfs` file systems.
 For more information on using `systemd` to restrict what access a service has to the system, see the `systemd.exec(5)` man page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
