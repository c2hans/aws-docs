---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/cloud-init.html
---

# Customized cloud-init
<a name="cloud-init"></a>

The cloud-init package is an open-source application that bootstraps Linux images in a cloud computing environment. For more information, see [cloud-init Documentation](https://cloudinit.readthedocs.io/en/22.2.2/).

AL2023 contains a customized version of cloud-init. With cloud-init, you can specify what occurs to your instance at boot time.

When you launch an instance, you can use the user-data fields to pass actions to cloud-init. This means that you can use common Amazon Machine Images (AMIs) for many use cases and configure them dynamically when you start an instance. AL2023 also uses cloud-init to configure the `ec2-user` account.

AL2023 uses the cloud-init actions in `/etc/cloud/cloud.cfg.d` and `/etc/cloud/cloud.cfg`. You can create your own cloud-init action files in the `/etc/cloud/cloud.cfg.d` directory. Cloud-init reads all the files in this directory in lexicographical order. Later files overwrite values in earlier files. When cloud-init launches an instance, the cloud-init package does the following configuration tasks:
+ Sets the default locale
+ Sets the hostname
+ Parses and handles user-data
+ Generates host private SSH keys
+ Adds a user's public SSH keys to `.ssh/authorized_keys` for easy login and administration
+ Prepares the repositories for package management
+ Handles package actions that are defined in user-data
+ Runs user scripts that are in user-data
+ Mounts instance store volumes, if applicable
  + By default, if the `ephemeral0` instance store volume is present and contains a valid file system, the instance store volume is mounted at `/media/ephemeral0`. Otherwise, it's not mounted.
  + By default, for the `m1.small` and `c1.medium` instance types, all swap volumes that are associated with the instance are mounted.
  + You can override the default instance store volume mount with the following cloud-init directive:

    ```
    #cloud-config
    mounts:
    - [ ephemeral0 ]
    ```

    For more control over mounts, see [Mounts](https://cloudinit.readthedocs.io/en/22.2.2/topics/modules.html#mounts) in the cloud-init documentation.
  + When an instance launches, instance store volumes that support TRIM aren't formatted. Before you can mount instance store volumes, you must partition and format instance store volumes.

    For more information, see [Instance store volume TRIM support](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport) in the *Amazon EC2 User Guide*.
  +  When you launch your instances, you can use the `disk_setup` module to partition and format your instance store volumes.

    For more information, see [Disk Setup](https://cloudinit.readthedocs.io/en/22.2.2/topics/modules.html#disk-setup) in the cloud-init documentation.

For information about using cloud-init with SELinux, see [Use cloud-init to enable `enforcing` mode](enforcing-mode.md#cloud-init-enforcing).

For information about cloud-init user-data formats, see [User-Data Formats](https://cloudinit.readthedocs.io/en/22.2.2/topics/format.html#format) in the cloud-init documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
