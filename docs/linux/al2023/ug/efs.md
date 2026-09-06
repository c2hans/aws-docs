---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/efs.html
---

# Using Amazon Elastic File System on AL2023
<a name="efs"></a>

Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. Because Amazon EFS has a simple web services interface, you can create and configure file systems quickly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations.

Amazon EFS supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol, so the applications and tools that you use today work seamlessly with Amazon EFS. Multiple compute instances, including Amazon EC2, Amazon ECS, and AWS Lambda, can access an Amazon EFS file system at the same time. Therefore, an EFS file system can provide a common data source for workloads and applications that are running on more than one compute instance or server.

## Installing `amazon-efs-utils` on AL2023
<a name="efs-utils"></a>

 The `amazon-efs-utils` package is available in the AL2023 repositories to be installed and used to access Amazon EFS file systems.

**Install the `amazon-efs-utils` package on AL2023**
+ Install `amazon-efs-utils` using the following command.

  ```
  $ dnf -y install amazon-efs-utils
  ```

## Mounting an Amazon EFS file system on AL2023
<a name="mount-efs"></a>

 After `amazon-efs-utils` is installed, you can mount an Amazon EFS file system on your AL2023 instance.

**Mount an Amazon EFS file system on AL2023**
+ To mount using the file system id, use the following command.

  ```
  sudo mount -t efs {{file-system-id}} {{efs-mount-point}}/
  ```

 You can also mount the file system so that data in transit is encrypted using TLS, or by using the DNS name or mount target IP instead of the file system id. For more information, see [Mounting on Amazon Linux instances using the EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-ec2-linux.html).
