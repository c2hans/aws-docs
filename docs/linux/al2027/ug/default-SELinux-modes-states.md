---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/default-SELinux-modes-states.html
---

# Default SELinux status and modes for AL2027
<a name="default-SELinux-modes-states"></a>

For AL2027, SELinux is `enabled` and set to `enforcing` mode by default. In `enforcing` mode, SELinux actively enforces the loaded security policy on the entire system.

To find the current SELinux status, policy, and mode, run the **getenforce** or **sestatus** command.

With the default status set to `enabled` and `enforcing`, the **getenforce** command returns `Enforcing`.

The **sestatus** command returns the SELinux status and the current SELinux policy as shown in the following example:

```
$ sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      35
```

When you run SELinux in `permissive` mode, you might label files incorrectly. When SELinux is `disabled`, files aren't labeled. Both incorrectly labeled and unlabeled files can cause problems in `enforcing` mode.

SELinux automatically relabels files to avoid this problem. SELinux prevents labeling problems with automatic relabeling when you change the status to `enabled`.
