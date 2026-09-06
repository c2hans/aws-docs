---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/selinux.html
---

# SELinux
<a name="selinux"></a>

In AL2027, SELinux is set to **enforcing** mode by default. This is a change from AL2023, which used permissive mode by default. For more information about the default status and modes, see [Default SELinux status and modes for AL2027](default-SELinux-modes-states.md).

In enforcing mode, SELinux actively enforces the loaded security policy on the entire system. Applications that relied on permissive behavior might need policy adjustments when you migrate to AL2027. To relax enforcement while you make those adjustments, you can change to permissive mode. For more information, see [Change to `permissive` mode](permissive-mode.md).

To change the SELinux mode or disable SELinux completely, see [Option to disable SELinux](disable-option-selinux.md).
