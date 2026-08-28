---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/disable-option-selinux.html
---

# Option to disable SELinux for AL2023
<a name="disable-option-selinux"></a>

When you disable SELinux, SELinux policy isn't loaded or enforced and Access Vector Cache (AVC) messages aren't logged. You lose all benefits of running SELinux.

Instead of disabling SELinux, we recommend using `permissive` mode. It costs only a little more to run in `permissive` mode than it does to disable SELinux completely. Transitioning from `permissive` mode to `enforcing` mode requires much less of a configuration adjustment than transitioning back to `enforcing` mode after disabling SELinux. You can label files, and the system can track and log actions that the active policy might have denied.

## Change SELinux to `permissive` mode
<a name="change-to-permissive"></a>

When you run SELinux in `permissive` mode, SELinux policy isn’t enforced. In `permissive` mode, SELinux logs AVC messages but doesn’t deny operations. You can use these AVC messages for troubleshooting, debugging, and SELinux policy improvements.

To change SELinux to permissive mode, use the following steps.

1. Edit the `/etc/selinux/config` file to change to `permissive` mode. The `SELINUX` value should look like the following example.

   ```
   SELINUX=permissive
   ```

1. Restart your system to complete the change to `permissive` mode.

   ```
   sudo reboot
   ```

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

For more information about SELinux, see the [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/toc.md) and [SELinux configuration](http://selinuxproject.org/page/Guide/Mode#SELinux_Config).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
