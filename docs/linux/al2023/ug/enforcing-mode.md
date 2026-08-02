---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/enforcing-mode.html
---

# Change to `enforcing` mode
<a name="enforcing-mode"></a>

When you run SELinux in `enforcing` mode, the SELinux utility is `enforcing` the configured policy. SELinux governs the capabilities of select applications by allowing or denying access based on the policy’s rules.

To find the current SELinux mode, run the `getenforce` command.

```
getenforce
Permissive
```

## Edit config file to enable `enforcing` mode
<a name="config-file-enforcing"></a>

To change the mode to `enforcing`, use the following steps.

1. Edit the `/etc/selinux/config` file to change to `enforcing` mode. The `SELINUX` setting should look like the following example.

   ```
   SELINUX=enforcing
   ```

1. Restart your system to complete the change to `enforcing` mode.

   ```
   $ sudo reboot
   ```

On the next boot, SELinux relabels all files and directories in the system. SELinux also adds the SELinux context for files and directories that were created when SELinux was `disabled`.

After changing to `enforcing` mode, SELinux might deny some actions because of incorrect or missing SELinux policy rules. You can view the actions that SELinux denies with the following command.

```
$ sudo ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent
```

## Use cloud-init to enable `enforcing` mode
<a name="cloud-init-enforcing"></a>

As an alternative, when you launch your instance, pass the following `cloud-config` as user-data to enable `enforcing` mode.

```
#cloud-config
selinux:
  mode: enforcing
```

By default, this setting causes the instance to reboot. For greater stability, we recommend rebooting your instance. However, if you prefer, you can skip the reboot by providing the following `cloud-config`.

```
#cloud-config
selinux:
  mode: enforcing
  selinux_no_reboot: 1
```
