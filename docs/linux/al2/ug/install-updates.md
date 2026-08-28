---
source_url: https://docs.aws.amazon.com/linux/al2/ug/install-updates.html
---

# Update instance software on your AL2 instance
<a name="install-updates"></a>

It is important to keep software up to date. Packages in a Linux distribution are updated frequently to fix bugs, add features, and protect against security exploits. When you first launch and connect to an Amazon Linux instance, you might see a message asking you to update software packages for security purposes. This section shows how to update an entire system, or just a single package.

This information applies to AL2. For information about AL2023, see [Manage packages and operating system updates in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html) in the *Amazon Linux 2023 User Guide*.

For information about changes and updates to AL2, see [AL2 release notes](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2.html).

For information about changes and updates to AL2023, see [AL2023 release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes.html).

**Important**
If you launched an EC2 instance that uses an Amazon Linux 2 AMI into an IPv6-only subnet, you must connect to the instance and run `sudo amazon-linux-https disable`. This lets your AL2 instance connect to the yum repository in S3 over IPv6 using the http patch service.

**To update all packages on an AL2 instance**

1. (Optional) Start a **screen** session in your shell window. Sometimes you might experience a network interruption that can disconnect the SSH connection to your instance. If this happens during a long software update, it can leave the instance in a recoverable, although confused state. A **screen** session allows you to continue running the update even if your connection is interrupted, and you can reconnect to the session later without problems.

   1. Execute the **screen** command to begin the session.

      ```
      [ec2-user ~]$ screen
      ```

   1. If your session is disconnected, log back into your instance and list the available screens.

      ```
      [ec2-user ~]$ screen -ls
      There is a screen on:
      	{{17793}}.pts-0.ip-12-34-56-78	(Detached)
      1 Socket in /var/run/screen/S-ec2-user.
      ```

   1. Reconnect to the screen using the **screen -r** command and the process ID from the previous command.

      ```
      [ec2-user ~]$ screen -r {{17793}}
      ```

   1. When you are finished using **screen**, use the **exit** command to close the session.

      ```
      [ec2-user ~]$ exit
      [screen is terminating]
      ```

1. Run the **yum update** command. Optionally, you can add the `--security` flag to apply only security updates.

   ```
   [ec2-user ~]$ sudo yum update
   ```

1. Review the packages listed, enter **y**, and press Enter to accept the updates. Updating all of the packages on a system can take several minutes. The **yum** output shows the status of the update while it is running.

1. (Optional) [Reboot your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html) to ensure that you are using the latest packages and libraries from your update; kernel updates are not loaded until a reboot occurs. Updates to any `glibc` libraries should also be followed by a reboot. For updates to packages that control services, it might be sufficient to restart the services to pick up the updates, but a system reboot ensures that all previous package and library updates are complete.

**To update a single package on an AL2 instance**

Use this procedure to update a single package (and its dependencies) and not the entire system.

1. Run the **yum update** command with the name of the package to update.

   ```
   [ec2-user ~]$ sudo yum update {{openssl}}
   ```

1. Review the package information listed, enter **y**, and press Enter to accept the update or updates. Sometimes there will be more than one package listed if there are package dependencies that must be resolved. The **yum** output shows the status of the update while it is running.

1. (Optional) [Reboot your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html) to ensure that you are using the latest packages and libraries from your update; kernel updates are not loaded until a reboot occurs. Updates to any `glibc` libraries should also be followed by a reboot. For updates to packages that control services, it might be sufficient to restart the services to pick up the updates, but a system reboot ensures that all previous package and library updates are complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
