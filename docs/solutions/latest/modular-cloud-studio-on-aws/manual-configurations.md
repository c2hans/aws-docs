---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/manual-configurations.html
---

# Step 6: Manual configurations
<a name="manual-configurations"></a>

Complete the following manual configurations based on your storage module deployment and workstation operating system. Choose the appropriate configuration that matches your setup:

## Configure FSx for Windows File Server on Windows workstations
<a name="configure-fsx-for-windows-file-server-on-windows-workstations"></a>

Use this configuration when you have deployed the FSx for Windows File Server storage module and are using Windows-based workstations.

1. Follow the instructions in [Mapping a file share on an Amazon EC2 Windows instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-share-windows.html) to mount the Amazon FSx for Windows File Server file system on Windows workstations.

## Configure FSx for Windows File Server on Linux workstations
<a name="configure-fsx-for-windows-file-server-on-linux-workstations"></a>

Use this configuration when you have deployed the FSx for Windows File Server storage module and are using Linux-based workstations.

1. Follow the instructions in [Manually join an Amazon EC2 Linux instance to your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance.html).

1. Follow the instructions in [Mounting a file share on an Amazon EC2 Linux instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-shares-linux.html) to mount the Amazon FSx for Windows File Server file system on Linux workstations.

## Configure FSx for Lustre on Linux workstations
<a name="configure-fsx-for-lustre-on-linux-workstations"></a>

Use this configuration when you have deployed the FSx for Lustre storage module and are using Linux-based workstations.

1. Follow the instructions in [Manually join an Amazon EC2 Linux instance to your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance.html).

1. Follow the instructions in [Installing the Lustre client](https://docs.aws.amazon.com/fsx/latest/LustreGuide/install-lustre-client.html#lustre-client-rhel) to install the Lustre client on Linux workstations.

1. Follow the instructions in [Mounting from an Amazon Electic Compute Cloud instance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-ec2-instance.html) to mount the Amazon FSx for Lustre file system on Linux workstations.

1. If using a data repository, follow [Using data repositories with Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html) and [POSIX metadata support](https://docs.aws.amazon.com/fsx/latest/LustreGuide/posix-metadata-support.html) to customize access and permissions to the Lustre file system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
