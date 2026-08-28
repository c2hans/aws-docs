---
source_url: https://docs.aws.amazon.com/efs/latest/ug/mounting-access-points.html
---

# Mounting with EFS access points
<a name="mounting-access-points"></a>

You can mount an EFS file system using an EFS access point only by using the EFS mount helper.

**Note**
You must configure one or more mount targets for your file system when mounting a file system using EFS access points.

When you mount a file system using an access point, the mount command includes the `access-point-id` and the `tls` mount option in addition to the regular mount options. An example is shown following.

```
$ sudo mount -t efs -o tls,accesspoint={{access-point-id}} {{file-system-id}} {{efs-mount-point}}
```

To automatically mount a file system using an access point, add the following line to the `/etc/fstab` file on the EC2 instance.

```
{{file-system-id}} {{efs-mount-point}} efs _netdev,tls,accesspoint={{access-point-id}} 0 0
```

For more information about EFS access points, see [Working with access points](efs-access-points.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
