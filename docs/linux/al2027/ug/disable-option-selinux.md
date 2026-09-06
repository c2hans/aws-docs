---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/disable-option-selinux.html
---

# Option to disable SELinux for AL2027
<a name="disable-option-selinux"></a>

When you disable SELinux, SELinux policy isn't loaded or enforced and Access Vector Cache (AVC) messages aren't logged. You lose all benefits of running SELinux.

Instead of disabling SELinux, we recommend using `permissive` mode. It costs only a little more to run in `permissive` mode than it does to disable SELinux completely. Transitioning from `permissive` mode to `enforcing` mode requires much less configuration than transitioning back to `enforcing` mode after disabling SELinux. You can label files, and the system can track and log actions that the active policy might have denied.

For information about how to change to `permissive` mode, see [Change to `permissive` mode](permissive-mode.md).

## Disable SELinux
<a name="disable-selinux"></a>

When you disable SELinux, SELinux policy isn't loaded or enforced, and AVC messages aren't logged. You lose all benefits of running SELinux.

To disable SELinux, use the following steps.

1. Ensure that the `grubby` package is installed.

   ```
   rpm -q grubby
   grubby-{{version}}
   ```

1. Configure your bootloader to add `selinux=0` to the kernel command line.

   ```
   sudo grubby --update-kernel ALL --args selinux=0
   ```

1. Restart your system.

   ```
   sudo reboot
   ```

1. Run the `getenforce ` command to confirm that SELinux is `Disabled`.

   ```
   $ getenforce
   Disabled
   ```

For more information about SELinux, see the [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/toc.md) and [SELinux modes](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/modes.md), both on the GitHub website.
