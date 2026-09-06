---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html
---

# Enable FIPS Mode on AL2023
<a name="fips-mode"></a>

This section explains how to enable Federal Information Processing Standards (FIPS) on AL2023. For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)

**Note**
This section documents how to enable FIPS mode in AL2023, it doesn't cover the certification status of AL2023 cryptographic modules.

**Prerequisites**
+ An existing AL2023 (AL2023.2 or higher) Amazon EC2 instance with access to the internet to download required packages. For more information about launching an AL2023 Amazon EC2 instance, see [Launching AL2023 using the Amazon EC2 console](ec2.md#launch-from-ec2-console).
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager. For more information, see [Connecting to AL2023 instances](connecting-to-instances.md).

**Important**
ED25519 SSH user keys aren't supported in FIPS mode. If you launched your Amazon EC2 instance using an ED25519 SSH key pair, you must generate new keys using another algorithm (such as RSA) or you may lose access to your instance after enabling FIPS mode. For more information see [Create key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*.

**Enable FIPS Mode**

1. Connect to your AL2023 instance using SSH or AWS Systems Manager.

1. Ensure the system is up to date. For more information, see [Manage package and operating system updates in AL2023](managing-repos-os-updates.md).

1. Ensure the `crypto-policies` utilities are installed and up-to-date.

   ```
   sudo dnf -y install crypto-policies crypto-policies-scripts
   ```

1. Enable FIPS mode by running the following command. This will enable FIPS mode system-wide for the modules listed in the [AL2023 FAQ](https://aws.amazon.com/linux/amazon-linux-2023/faqs/)

   ```
   sudo fips-mode-setup --enable
   ```

1. Reboot the instance using the following command.

   ```
   sudo reboot
   ```

1. To verify that FIPS mode is enabled, reconnect to your instance and run the following command.

   ```
   sudo fips-mode-setup --check
   ```

   The following example output shows FIPS mode is enabled:

   ```
   FIPS mode is enabled.
   ```
