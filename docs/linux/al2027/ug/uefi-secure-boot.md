---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/uefi-secure-boot.html
---

# UEFI Secure Boot on AL2027
<a name="uefi-secure-boot"></a>

AL2027 supports UEFI Secure Boot. You must use AL2027 with Amazon EC2 instances that support both UEFI and UEFI Secure Boot. For more information, see [Requirements to launch an Amazon EC2 instance in UEFI boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instance-boot-mode.html) in the *Amazon EC2 User Guide*.

With UEFI Secure Boot enabled, AL2027 instances accept only kernel-level code, including the Linux kernel and modules, that is signed by Amazon. This makes sure that your instance runs only kernel-level code signed by AWS.

 For more information about Amazon EC2 instances and UEFI Secure Boot, see [UEFI Secure Boot for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the *Amazon EC2 User Guide*.

**Prerequisites**
+ You must be using an AMI with AL2027.
+ The instance type must support UEFI Secure Boot, as described earlier.

## Enable UEFI Secure Boot on AL2027
<a name="enablement"></a>

Standard AL2027 AMIs incorporate a bootloader and a kernel signed by our keys. You can enable UEFI Secure Boot in one of two ways: by enrolling an existing instance, or by creating an AMI with UEFI Secure Boot pre-enabled using a registered image from a snapshot. UEFI Secure Boot isn't enabled by default on the standard AL2027 AMIs.

The boot mode of AL2027 AMIs is set to `uefi-preferred` which makes sure that instances launched with these AMIs will use the UEFI firmware, if the instance type supports UEFI. If the instance type doesn't support UEFI, the instance is launched with Legacy BIOS firmware. When an instance launches in Legacy BIOS mode, UEFI Secure Boot isn't enforced.

For more information about AMI boot modes on Amazon EC2 instances, see [Instance launch behavior with Amazon EC2 boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Enable UEFI Secure Boot on AL2027](#enablement)
+ [Enrollment of an existing instance](#enrollment-existing-instance)
+ [Register image from snapshot](#secure-boot-amis)
+ [Revocation updates](#revocation-updates)
+ [How UEFI Secure Boot works on AL2027](#shim-use)
+ [Enrolling your own keys](#enrolling-own-keys)

## Enrollment of an existing instance
<a name="enrollment-existing-instance"></a>

To enroll an existing instance, populate the specific UEFI firmware variables with a set of keys that enable the firmware to verify the bootloader and the bootloader to verify the kernel on the next boot.

1. AL2027 provides a tool to simplify the enrollment process. Run the following command to provision the instance with the necessary set of keys and certificates.

   ```
   sudo amazon-linux-sb enroll
   ```

1. Run the following command to reboot the instance. After the instance is rebooted, UEFI Secure Boot will be enabled.

   ```
   sudo reboot
   ```

**Note**
AL2027 AMIs currently don't enable Nitro Trusted Platform Module (NitroTPM) by default with `BootMode` set to `uefi-preferred`. If you need NitroTPM in addition to UEFI Secure Boot, use the information in the following section.

## Register image from snapshot
<a name="secure-boot-amis"></a>

When registering an AMI from a snapshot of an Amazon EBS root volume using the Amazon EC2 `register-image` API, you can provision the AMI with a binary blob that contains the state of the UEFI variable store. By providing the AL2027 `UefiData`, you enable UEFI Secure Boot and don't need to follow the steps in the previous section.

AL2027 provides a pre-built binary blob that can be used directly on Amazon EC2 instances. The binary blob is located in `/usr/share/amazon-linux-sb-keys/uefi.vars` on a running instance. The `amazon-linux-sb-keys` RPM package provides this blob, relevant keys, and the dbx. This is installed by default on AL2027 AMIs.

**Note**
To make sure that you are using the latest version of keys and revocations, use the blob from the same release of AL2027 that you use to create the AMI.

If you would like to add custom binary blobs, use the keys in `/usr/share/amazon-linux-sb-keys`. Find more information about creating and using binary blobs at [Create a binary blob containing a pre-filled variable store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami-with-uefi-secure-boot.html#uefi-secure-boot-optionB) in the *Amazon EC2 User Guide*.

When registering an image, we recommend using the `BootMode` parameter of the [`RegisterImage`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html) API set to `uefi` instead of `uefi-preferred`. This allows you to enable NitroTPM by setting the `TpmSupport` parameter to `v2.0`. Also, setting `BootMode` to `uefi` prevents boot on BIOS instances, thus making sure that UEFI Secure Boot can't be disabled by accident when switching to an instance type that doesn't support UEFI.

For more information about NitroTPM, see [NitroTPM for Amazon EC2 instances ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide*.

## Revocation updates
<a name="revocation-updates"></a>

It may be necessary for AL2027 to distribute a new version of the bootloader `grub2` or the Linux kernel signed with updated keys. In that case, the old key may need to be revoked to prevent the chance of allowing exploitable bugs from previous versions of the bootloader to bypass the UEFI Secure Boot verification process.

Package updates to the `grub2` or `kernel` packages always automatically update the list of revocations into the UEFI variable store of the running instance. This means that with UEFI Secure Boot enabled, you might no longer be able to run the old version of a package after installing a security update for the package.

## How UEFI Secure Boot works on AL2027
<a name="shim-use"></a>

Unlike other Linux distributions, AL2027 doesn't provide an additional component, called a shim, to act as the first stage bootloader. On distributions that use a shim, the shim (generally signed with Microsoft keys) loads the `grub2` bootloader and uses its own code to verify the Linux kernel. The shim also maintains its own set of keys and revocations in the Machine Owner Key (MOK) database, which is located in the UEFI variable store and controlled with the `mokutil` tool. For the full explanation of how shim and MOK work with other distributions, see the linked Amazon EC2 guide topic.

AL2027 doesn't provide a shim. Because the AMI owner controls the UEFI variables, this intermediary step isn't needed. Adding it would adversely affect launch and boot times. Also, we chose not to include trust for any vendor keys by default, to reduce the chance that undesired binaries could run. As always, you can include binaries if you choose to do so.

With AL2027, UEFI directly loads and verifies our `grub2` bootloader. The `grub2` bootloader was modified to use UEFI to verify the Linux kernel after loading it. As a result, UEFI verifies the Linux kernel using the same certificates in the normal UEFI `db` variable (authorized key database). It tests the kernel against the same `dbx` variable (revocations database) used for the bootloader and other UEFI binaries. Because we provide our own PK and KEK keys, which control access to the `db` and `dbx` databases, we can distribute signed updates and revocations as needed without an intermediary such as the shim.

For more information about UEFI Secure Boot, see [How UEFI Secure Boot works with Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-uefi-secure-boot-works.html) in the *Amazon EC2 User Guide*.

## Enrolling your own keys
<a name="enrolling-own-keys"></a>

As documented in the previous section, AL2027 does not require a `shim` for UEFI Secure Boot on Amazon EC2. When you're reading documentation for other Linux distributions, you may find documentation for managing the Machine Owner Key (MOK) database using `mokutil`, which is not present on AL2027. The `shim` and MOK environments work around some limitations of key enrollment in UEFI Firmware that aren't applicable to how Amazon EC2 implements UEFI Secure Boot. With Amazon EC2 there are mechanisms to easily directly manipulate the keys in the UEFI variable store.

If you want to enroll your own keys, you can do so either by manipulating the variable store within an existing instance (see [ Add keys to the variable store from within the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami-with-uefi-secure-boot.html#uefi-secure-boot-optionA)) or by constructing a binary blob that's prefilled (see [ Create a binary blob containing a pre-filled variable store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami-with-uefi-secure-boot.html#uefi-secure-boot-optionB)).
