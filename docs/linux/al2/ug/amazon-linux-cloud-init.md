---
source_url: https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-cloud-init.html
---

# Using cloud-init on AL2
<a name="amazon-linux-cloud-init"></a>

The cloud-init package is an open-source application built by Canonical that is used to bootstrap Linux images in a cloud computing environment, such as Amazon EC2. Amazon Linux contains a customized version of cloud-init. This allows you to specify actions that should happen to your instance at boot time. You can pass desired actions to cloud-init through the user data fields when launching an instance. This means you can use common AMIs for many use cases and configure them dynamically at startup. Amazon Linux also uses cloud-init to perform initial configuration of the ec2-user account.

 For more information, see the [cloud-init documentation](http://cloudinit.readthedocs.org/en/latest/).

Amazon Linux uses the cloud-init actions found in `/etc/cloud/cloud.cfg.d` and `/etc/cloud/cloud.cfg`. You can create your own cloud-init action files in `/etc/cloud/cloud.cfg.d`. All files in this directory are read by cloud-init. They are read in lexical order, and later files overwrite values in earlier files.

The cloud-init package performs these (and other) common configuration tasks for instances at boot:
+ Set the default locale.
+ Set the hostname.
+ Parse and handle user data.
+ Generate host private SSH keys.
+ Add a user's public SSH keys to `.ssh/authorized_keys` for easy login and administration.
+ Prepare the repositories for package management.
+ Handle package actions defined in user data.
+ Run user scripts found in user data.
+ Mount instance store volumes, if applicable.
  + By default, the `ephemeral0` instance store volume is mounted at `/media/ephemeral0` if it is present and contains a valid file system; otherwise, it is not mounted.
  + By default, any swap volumes associated with the instance are mounted (only for `m1.small` and `c1.medium` instance types).
  + You can override the default instance store volume mount with the following cloud-init directive:

    ```
    #cloud-config
    mounts:
    - [ ephemeral0 ]
    ```

    For more control over mounts, see [Mounts](http://cloudinit.readthedocs.io/en/latest/topics/modules.html#mounts) in the cloud-init documentation.
  + Instance store volumes that support TRIM are not formatted when an instance launches, so you must partition and format them before you can mount them. For more information, see [Instance store volume TRIM support](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#InstanceStoreTrimSupport). You can use the `disk_setup` module to partition and format your instance store volumes at boot. For more information, see [Disk Setup](http://cloudinit.readthedocs.io/en/latest/topics/modules.html#disk-setup) in the cloud-init documentation.

## Supported user data formats
<a name="supported-user-data-formats"></a>

The cloud-init package supports user data handling of a variety of formats:
+ Gzip
  + If user data is gzip compressed, cloud-init decompresses the data and handles it appropriately.
+ MIME multipart
  + Using a MIME multipart file, you can specify more than one type of data. For example, you could specify both a user data script and a cloud config type. Each part of the multipart file can be handled by cloud-init if it is one of the supported formats.
+ Base64 decoding
  +  If user data is base64-encoded, cloud-init determines if it can understand the decoded data as one of the supported types. If it understands the decoded data, it decodes the data and handles it appropriately. If not, it returns the base64 data intact.
+ User data script
  + Begins with `#!` or `Content-Type: text/x-shellscript`.
  + The script is run by `/etc/init.d/cloud-init-user-scripts` during the first boot cycle. This occurs late in the boot process (after the initial configuration actions are performed).
+ Include file
  + Begins with `#include` or `Content-Type: text/x-include-url`.
  + This content is an include file. The file contains a list of URLs, one per line. Each of the URLs is read, and their content passed through this same set of rules. The content read from the URL can be gzip compressed, MIME-multi-part, or plaintext.
+ Cloud config data
  + Begins with `#cloud-config` or `Content-Type: text/cloud-config`.
  + This content is cloud config data.
+ Upstart job (not supported on AL2)
  + Begins with `#upstart-job` or `Content-Type: text/upstart-job`.
  + This content is stored in a file in `/etc/init`, and upstart consumes the content as it does with other upstart jobs.
+ Cloud boothook
  + Begins with `#cloud-boothook` or `Content-Type: text/cloud-boothook`.
  + This content is boothook data. It is stored in a file under `/var/lib/cloud` and then runs immediately.
  +  This is the earliest *hook* available. There is no mechanism provided for running it only one time. The boothook must take care of this itself. It is provided with the instance ID in the environment variable `INSTANCE_ID`. Use this variable to provide a once-per-instance set of boothook data.
