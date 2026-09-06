---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/fips-mode.html
---

# Enable FIPS Mode on AL2027
<a name="fips-mode"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This section explains how to enable Federal Information Processing Standards (FIPS) on AL2027. For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)

**Note**
This section documents how to enable FIPS mode in AL2027, it does not cover the certification status of AL2027 cryptographic modules.

**Prerequisites**
+ An existing AL2027 Amazon EC2 instance with access to the internet to download required packages.
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager.

**Important**
ED25519 SSH user keys are not supported in FIPS mode. If you launched your Amazon EC2 instance using an ED25519 SSH key pair, you must generate new keys using another algorithm (such as RSA or ECDSA) or you may lose access to your instance after enabling FIPS mode. For more information see [Create key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*.

**Note**
AL2027 no longer provides the `fips-mode-setup` command-line utility. FIPS mode only needs to be enabled in the Linux kernel, and after rebooting the system-wide cryptographic FIPS policy will be automatically enabled via the `fips-crypto-policies` dracut module or the systemd `fips-crypto-policy-overlay` service.

**Enable FIPS Mode**

1. Connect to your AL2027 instance using SSH or AWS Systems Manager.

1. Ensure the system is up to date. For more information, see [Manage package and operating system updates in AL2027](manage-updates.md).

1. Ensure the `crypto-policies` utilities are installed and up-to-date.

   ```
   sudo dnf -y install crypto-policies crypto-policies-scripts
   ```

1. Enable FIPS mode by running the following command:

   ```
   sudo /sbin/grubby --update-kernel=ALL --args="fips=1"
   ```

1. Reboot the instance using the following command.

   ```
   sudo reboot
   ```

1. To verify that the Linux kernel is in FIPS mode, reconnect to your instance and run the following command:

   ```
   cat /proc/sys/crypto/fips_enabled
   ```

   An output of `1` means that the kernel is running FIPS mode.

1. To verify that the system-wide cryptographic policies are set to `FIPS`:

   ```
   update-crypto-policies --show
   ```

   The following output shows the FIPS crypto policy is enabled:

   ```
   FIPS
   ```
