---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-root.html
---

# `/` (The root directory)
<a name="filesystem-root"></a>

 By default, AL2023 images are configured with a writable `/`, allowing privileged users to create new files and directories.

 It is possible to configure `systemd` services to use a different path or image to appear as `/` for that service, as well as place access restrictions on any path.

**Note**
 It is best practice for `systemd` services to be configured to restrict what the service has access to. This can include using the `ReadOnlyPaths=/` directive which makes `/` read only for that service.
 For more information on using `systemd` to restrict what access a service has to the system, see the `systemd.exec(5)` man page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
