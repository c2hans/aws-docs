---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/efs.html
---

# Using Amazon Elastic File System on AL2027
<a name="efs"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

With Amazon Elastic File System (Amazon EFS), you can share file data using serverless, fully elastic storage. You don't need to provision or manage storage capacity and performance. Amazon EFS scales on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. Because Amazon EFS has a simple web services interface, you can create and configure file systems quickly and easily.

With Amazon EFS, you can use the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol. The applications and tools that you already use work seamlessly with Amazon EFS. Multiple compute instances, including Amazon EC2, Amazon ECS, and AWS Lambda, can access an Amazon EFS file system at the same time. Therefore, an Amazon EFS file system can provide a common data source for workloads and applications. These workloads can run on more than one compute instance or server.

## Installing `amazon-efs-utils` on AL2027
<a name="efs-utils"></a>

The `amazon-efs-utils` package is available in the AL2027 repositories.

**Install the `amazon-efs-utils` package on AL2027**
+ Install `amazon-efs-utils` using the following command.

  ```
  $ dnf -y install amazon-efs-utils
  ```

## Mounting an Amazon EFS file system on AL2027
<a name="mount-efs"></a>

After you install `amazon-efs-utils`, you can mount an Amazon EFS file system on your AL2027 instance.

**Mount an Amazon EFS file system on AL2027**
+ To mount using the file system ID, use the following command.

  ```
  sudo mount -t efs {{file-system-id}} {{efs-mount-point}}/
  ```

You can also mount the file system with TLS to encrypt data in transit. Alternatively, use the DNS name or mount target IP instead of the file system ID. For more information, see [Mounting on Amazon Linux instances using the EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-ec2-linux.html).
