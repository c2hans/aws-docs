---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-option-c.html
---

# Option C: Install a custom OS on an original AWS DeepRacer device
<a name="custom-car-option-c"></a>

If you own an original AWS DeepRacer device (Intel Atom-based), you can install a modern operating system using the developer bootloader shim. This option requires no hardware modifications, no soldering, and no additional purchases. The developer bootloader shim is based on the [open-source shim project](https://github.com/rhboot/shim) on the GitHub website.

The developer bootloader shim replaces the factory boot process and transfers control to your custom operating system. You can choose from three sub-options depending on your needs.

**Developer mode security implications**
Installing the developer bootloader shim places your device into developer mode, which disables the factory Secure Boot chain. In developer mode, the device boots only operating systems signed with certificates that you provide. We do not provide support for devices running in developer mode.

## Option C1: Install the community distribution
<a name="option-c1-install-the-community-distribution"></a>

The [AWS DeepRacer Community](https://github.com/aws-deepracer-community/deepracer-custom-car) on the GitHub website provides a ready-to-use Ubuntu 24.04 distribution with ROS2 Jazzy pre-configured for the original AWS DeepRacer hardware. This is the fastest path if you want a modern, fully compatible software stack.

To install the community distribution, follow the instructions in the [Installation section](https://github.com/aws-deepracer-community/deepracer-custom-car#installation) of the AWS DeepRacer Community custom car repository on the GitHub website.

## Option C2: Install a third-party distribution
<a name="option-c2-install-a-third-party-distribution"></a>

You can use the developer bootloader shim to install a third-party operating system (such as Ubuntu) on your AWS DeepRacer device.

To install a third-party distribution:

1. Download the [developer bootloader shim](https://s3.amazonaws.com/deepracer-public/shim/deepracer-developer-shim.zip).

1. Prepare the boot volume of the third-party OS.

1. Rename the original bootloader to `EFI/BOOT/GRUBX64.EFI`.

1. Replace the default `EFI/BOOT/BOOTX64.EFI` file with the developer bootloader shim.

1. Place your public signing certificate in DER (Distinguished Encoding Rules) format in the `EFI/DEVELOPER/certs/` directory.

1. Sign the OS kernel and bootloader with your private key.

1. Boot the device from the prepared volume.

For detailed instructions, refer to the `USAGE.md` file included in the developer bootloader shim download.

## Option C3: Build and install a custom OS
<a name="option-c3-build-and-install-a-custom-os"></a>

You can build and install a fully custom operating system on the original AWS DeepRacer device.

To build and install a custom OS:

1. Download the [developer bootloader shim](https://s3.amazonaws.com/deepracer-public/shim/deepracer-developer-shim.zip).

1. Create a boot volume with the following structure:

   ```
   EFI/
   ├── BOOT/
   │   ├── BOOTX64.EFI      (developer bootloader shim)
   │   └── GRUBX64.EFI      (your OS kernel or bootloader)
   └── DEVELOPER/
       └── certs/
           └── your-cert.der (your public signing certificate)
   ```

1. Place the developer bootloader shim as `EFI/BOOT/BOOTX64.EFI`.

1. Place your OS kernel or bootloader as `EFI/BOOT/GRUBX64.EFI`.

1. Place your public signing certificate in DER (Distinguished Encoding Rules) format in the `EFI/DEVELOPER/certs/` directory.

1. Sign your OS kernel with the corresponding private key.

1. Boot the device from the prepared volume.

For detailed instructions, refer to the `USAGE.md` file included in the developer bootloader shim download.

## Getting started
<a name="getting-started"></a>

To get started with any Option C sub-option:

1. Download the [developer bootloader shim](https://s3.amazonaws.com/deepracer-public/shim/deepracer-developer-shim.zip).

1. Extract the archive and review the `USAGE.md` file for detailed instructions specific to your chosen sub-option.

**Early boot sequence**
When the developer bootloader shim starts, it blinks "DEVELOPER MODE" in Morse code on the device LEDs. This sequence takes approximately 21 seconds. After the Morse code sequence completes, the shim checks for valid certificates in `/EFI/DEVELOPER/certs/`. If a valid signed operating system is found, the shim transfers control to it.

**Returning to original configuration**
To restore your device to its original factory configuration, follow the directions in the [Update and restore your vehicle](update-and-restore-vehicle.md) chapter.

For more information about the developer bootloader shim, see [Custom OS installation now available on AWS DeepRacer devices](https://aws.amazon.com/blogs/machine-learning/custom-os-installation-now-available-on-aws-deepracer-devices/) on the AWS Machine Learning Blog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
