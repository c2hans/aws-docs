---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/default-SELinux-modes-states.html
---

# Default SELinux status and modes for AL2023
<a name="default-SELinux-modes-states"></a>

For AL2023, SELinux by default is `enabled` and set to `permissive` mode. In `permissive` mode, permission denials are logged but not enforced.

The **getenforce** or **sestatus** commands tell you the current SELinux status, policy, and mode.

With the default status set to `enabled` and `permissive`, the **getenforce** command returns `permissive`.

The **sestatus** command returns the SELinux status and the current SELinux policy as shown in the following example:

```
$ sestatus
SELinux status:                 enabled
  SELinuxfs mount:                /sys/fs/selinux
  SELinux root directory:         /etc/selinux
  Loaded policy name:             targeted
  Current mode:                   permissive
  Mode from config file:          permissive
  Policy MLS status:              enabled
  Policy deny_unknown status:     allowed
  Memory protection checking:     actual (secure)
  Max kernel policy version:      33
```

When you run SELinux in `permissive` mode, users might label files incorrectly. When you run SELinux in the `disabled` status, files aren't labeled. Both incorrect or unlabeled files can cause problems when you change to `enforcing` mode.

SELinux automatically relabels files to avoid this problem. SELinux prevents labeling problems with automatic relabeling when you change the status to `enabled`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
