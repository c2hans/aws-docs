---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/cloud-init.html
---

# Customized cloud-init
<a name="cloud-init"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The cloud-init package is an open-source application that bootstraps Linux images in a cloud computing environment. AL2027 includes cloud-init 26.1. For more information, see the [cloud-init documentation](https://docs.cloud-init.io/en/26.1/) on the cloud-init website.

AL2027 contains a customized version of cloud-init. With cloud-init, you can specify what occurs to your instance at boot time.

When you launch an instance, you can use the user-data fields to pass actions to cloud-init. This means that you can use common AMIs for many use cases and configure them dynamically when you start an instance. AL2027 also uses cloud-init to configure the `ec2-user` account.

AL2027 uses the cloud-init actions in `/etc/cloud/cloud.cfg.d` and `/etc/cloud/cloud.cfg`. You can create your own cloud-init action files in the `/etc/cloud/cloud.cfg.d` directory. Cloud-init reads all the files in this directory in lexicographical order. Later files overwrite values in earlier files. When cloud-init launches an instance, the cloud-init package does the following configuration tasks:
+ Sets the default locale
+ Sets the hostname
+ Parses and handles user-data
+ Generates host private SSH keys
+ Adds a user's public SSH keys to `.ssh/authorized_keys` for easy login and administration
+ Prepares the repositories for package management
+ Handles package actions that are defined in user-data
+ Runs user scripts that are in user-data
+ Mounts instance store volumes, if applicable
  + Instance store volumes that support TRIM aren't formatted when an instance launches. Before you can mount instance store volumes, you must partition and format them.

    For more information about TRIM support, see [Instance store volume TRIM support](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport) in the *Amazon EC2 User Guide*.
  + When you launch your instances, you can use the `disk_setup` module to partition and format your instance store volumes.

    For more information about the module, see [Disk Setup](https://docs.cloud-init.io/en/26.1/reference/modules.html#disk-setup) on the cloud-init website.
  + You can use the `mounts` module to mount instance store volumes by device name. On AL2027 instances, instance store volumes are exposed as NVMe block devices. For example, the following cloud-config directive mounts the instance store volume at `/dev/nvme1n1` to `/mnt`:

    ```
    #cloud-config
    mounts:
     - [ /dev/nvme1n1, /mnt ]
    ```

    The device name and enumeration order for instance store volumes can vary by instance type. For more information about controlling mounts, see [Mounts](https://docs.cloud-init.io/en/26.1/reference/modules.html#mounts) on the cloud-init website.

For more information about cloud-init user-data formats, see [Configuration formats](https://docs.cloud-init.io/en/26.1/explanation/format/index.html) on the cloud-init website.
