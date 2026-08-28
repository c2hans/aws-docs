---
source_url: https://docs.aws.amazon.com/linux/al2/ug/fips-mode.html
---

# Enable FIPS Mode on AL2
<a name="fips-mode"></a>

This section explains how to enable Federal Information Processing Standards (FIPS) on AL2. For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)

**Prerequisites**
+ An existing AL2 Amazon EC2 instance with access to the internet to download required packages. For more information about launching an AL2 Amazon EC2 instance, see [AL2 on Amazon EC2](ec2.md).
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager. .

**Important**
ED25519 SSH user keys aren't supported in FIPS mode. If you launched your Amazon EC2 instance using an ED25519 SSH key pair, you must generate new keys using another algorithm (such as RSA) or you may lose access to your instance after enabling FIPS mode. For more information see [Create key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*.

**Enable FIPS Mode**

1. Connect to your AL2 instance using SSH or AWS Systems Manager.

1. Ensure the system is up to date. For more information, see [Package repository](ec2.md#package-repository).

1. Install and enable the `dracut-fips` module by running the following commmands.

   ```
   sudo yum -y install dracut-fips
   sudo dracut -f
   ```

1. Enable FIPS mode on the Linux kernel command-line using the following command. This will enable FIPS mode system-wide for the modules listed in the [AL2 FAQ](https://aws.amazon.com/amazon-linux-2/faqs/)

   ```
   sudo /sbin/grubby --update-kernel=ALL --args="fips=1"
   ```

1. Reboot your AL2 instance.

   ```
   sudo reboot
   ```

1. To verify that FIPS mode is enabled, reconnect to your instance and run the following command.

   ```
   sysctl crypto.fips_enabled
   ```

   You should see the following output:

   ```
   crypto.fips_enabled = 1
   ```

   You can also verify that OpenSSH is in FIPS mode by running the following command:

   ```
   ssh localhost 2>&1 | grep FIPS
   ```

   You should see the following output:

   ```
   FIPS mode initialized
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
