---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-wsl-on-ec2-windows-instance.html
---

# Install Windows Subsystem for Linux on your EC2 Windows instance
<a name="install-wsl-on-ec2-windows-instance"></a>

The Windows Subsystem for Linux (WSL) is a feature of Microsoft Windows. By installing WSL on your EC2 Windows instance, you can run native Linux tools directly on your Windows instance.

There are two versions of Windows Subsystem for Linux (WSL): WSL 1 and WSL 2. For more information, see [Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-us/windows/wsl/) on the Microsoft website.

**Requirements**
+ The operating system must be Windows Server 2019 or later.
+ You can only install WSL 1 on virtualized Windows instances (the instance size is not `.metal` or does not support nested virtualization).
+ You can install either WSL 1 or WSL 2 on instances that support nested virtualization and have the `NestedVirtualization` CPU Option enabled.
+ You can install either WSL 1 or WSL 2 on bare metal instances (the instance size is `.metal`). Bare metal instances provide the required support for nested virtualization by default.

For more information about nested virtualization for EC2, see [Use nested virtualization to run hypervisors in Amazon EC2 instances](amazon-ec2-nested-virtualization.md).

## Install WSL on your Windows instance
<a name="install-wsl-steps"></a>

**To install WSL 1**

1. Install WSL. The process that you'll use depends on the version of Windows Server running on the instance.
   + **Windows Server 2022 and later** - Run the following standard installation command on your EC2 instance.

     ```
     wsl --install --enable-wsl1 --no-launch
     ```
   + **Windows Server 2019** - Enable WSL and then install WSL as described in [Install WSL on previous versions of Windows Server](https://learn.microsoft.com/en-us/windows/wsl/install-on-server#install-wsl-on-previous-versions-of-windows-server) on the Microsoft website.

1. Restart your EC2 instance.

   ```
   shutdown -r -t 20
   ```

1. To configure WSL to use WSL 1, run the following command on your instance. This step is required for virtualized instances (the instance size is not `.metal` or not configured for nested virtualization).

   ```
   wsl --set-default-version 1
   ```

1. Install the default distribution.

   ```
   wsl --install
   ```

**To install WSL 2 (.metal or instances with nested virtualization enabled)**
Run the following standard installation command on your EC2 instance. By default, WSL 2 is installed.

```
wsl --install
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
