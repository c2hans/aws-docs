---
source_url: https://docs.aws.amazon.com/efs/latest/ug/nfs-automount-efs.html
---

# Enabling automatic mounting on EC2 Linux or Mac instances using NFS
<a name="nfs-automount-efs"></a>

Using NFS without the EFS mount helper to update the Amazon EC2 `/etc/fstab` file, for EC2 Linux and Mac instances.

**To update the `/etc/fstab` file on your EC2 instance**

1. Connect to your EC2 instance. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*.

1. Open the `/etc/fstab` file in an editor.

1. To automatically mount a file system using NFS instead of the EFS mount helper, add the following line to the `/etc/fstab` file.
   + Replace {{file\_system\_id}} with the ID of the file system you are mounting.
   + Replace {{aws-region}} with the AWS Region that the file system in, such as `us-east-1`.
   + Replace {{mount\_point}} with the file system's mount point.

   ```
   {{file_system_id}}.efs.{{aws-region}}.amazonaws.com:/ {{mount_point}} nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0
   ```

The line of code you added to the `/etc/fstab` file does the following.

| Field | Description |
| --- | --- |
| `{{file-system-id}}:/` | The ID for your EFS file system. You can get this ID from the console or programmatically from the CLI or an AWS SDK. |
| `{{efs-mount-point}}` | The mount point for the EFS file system on your EC2 instance. |
| `nfs4` | Specifies the file system type. |
| `mount options` | The comma-separated list of mount options for the file system:[See the AWS documentation website for more details](http://docs.aws.amazon.com/efs/latest/ug/nfs-automount-efs.html) |
| `0` | Specifies the `dump` value; `0` tells the `dump` utility to not back up the file system. |
| `0` | Tells the `fsck` utility to not run at start-up. |
