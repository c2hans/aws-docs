---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/permissive-mode.html
---

# Change to `permissive` mode
<a name="permissive-mode"></a>

When you run SELinux in `permissive` mode, SELinux policy isn't enforced. In `permissive` mode, SELinux logs AVC messages but doesn't deny operations. You can use these AVC messages for troubleshooting, debugging, and SELinux policy improvements.

To find the current SELinux mode, run the `getenforce` command.

```
getenforce
Enforcing
```

## Editing the config file to enable `permissive` mode
<a name="config-file-permissive"></a>

To change the mode to `permissive`, use the following steps.

1. Edit the `/etc/selinux/config` file to change to `permissive` mode. The `SELINUX` value should look like the following example.

   ```
   SELINUX=permissive
   ```

1. Restart your system to complete the change to `permissive` mode.

   ```
   $ sudo reboot
   ```

## Using cloud-init to enable `permissive` mode
<a name="cloud-init-permissive"></a>

As an alternative, when you launch your instance, pass the following `cloud-config` as user-data to enable `permissive` mode.

```
#cloud-config
selinux:
  mode: permissive
```

By default, this setting causes the instance to reboot. For greater stability, we recommend rebooting your instance. However, if you prefer, you can skip the reboot by providing the following `cloud-config`.

```
#cloud-config
selinux:
  mode: permissive
  selinux_no_reboot: 1
```
