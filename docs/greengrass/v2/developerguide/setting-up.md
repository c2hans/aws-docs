---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html
---

# Setting up AWS IoT Greengrass core devices
<a name="setting-up"></a>

Complete the tasks in this section to install, configure, and run the AWS IoT Greengrass Core software.

**Note**
This section describes advanced installation and configuration of the AWS IoT Greengrass Core software. These steps do not apply to nucleus lite.If you're a first-time user of AWS IoT Greengrass V2, we recommend that you first complete the [getting started tutorial](getting-started.md) to set up a core device and explore the features of AWS IoT Greengrass.

**Topics**
+ [Supported platforms](#supported-platforms)
+ [Device requirements](#device-requirements)
+ [Lambda function requirements](#greengrass-v2-lambda-requirements)
+ [Set up an AWS account](#set-up-aws-account)
+ [Install the AWS IoT Greengrass Core software](install-greengrass-core-v2.md)
+ [Run the AWS IoT Greengrass Core software](run-greengrass-core-v2.md)
+ [Run AWS IoT Greengrass Core software in a Docker container](run-greengrass-docker.md)
+ [Configure the AWS IoT Greengrass Core software](configure-greengrass-core-v2.md)
+ [Update the AWS IoT Greengrass Core software (OTA)](update-greengrass-core-v2.md)
+ [Uninstall the AWS IoT Greengrass Core software](uninstall-greengrass-core-v2.md)

## Supported platforms
<a name="supported-platforms"></a>
+ [Greengrass nucleus supported platforms](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html)
+ [Greengrass nucleus lite supported platforms](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)

## Device requirements
<a name="device-requirements"></a>
+ [Greengrass nucleus device requirements](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html)
+ [Greengrass nucleus lite device requirements](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-lite-component.html)

## Lambda function requirements
<a name="greengrass-v2-lambda-requirements"></a>

**Important**
Greengrass Lambda functions are currently not supported by Greengrass nucleus lite.

Your device must meet the following requirements to run Lambda functions:
+ A Linux-based operating system.
+ Your device must have the `mkfifo` shell command.
+ Your device must run the programming language libraries that a Lambda function requires. You must install the required libraries on the device and add them to the `PATH` environment variable. Greengrass supports all Lambda supported versions of Python, Node.js, and Java runtimes. Greengrass doesn't apply any additional restrictions on deprecated Lambda runtime versions. For more information about AWS IoT Greengrass support for Lambda runtimes, see [Run AWS Lambda functions](run-lambda-functions.md).
+ To run containerized Lambda functions, your device must meet the following requirements:
  + Linux kernel version 4.4 or later.
  + The kernel must support [cgroups](https://en.wikipedia.org/wiki/Cgroups) v1, and you must enable and mount the following cgroups:
    + The *memory* cgroup for AWS IoT Greengrass to set the memory limit for containerized Lambda functions.
    + The *devices* cgroup for containerized Lambda functions to access system devices or volumes.

    The AWS IoT Greengrass Core software doesn't support cgroups v2.

    To meet this requirement, boot the device with the following Linux kernel parameters.

    ```
    cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
    ```
**Tip**
On a Raspberry Pi, edit the `/boot/cmdline.txt` file to set the device's kernel parameters.
  + You must enable the following Linux kernel configurations on the device:
    + Namespace:
      + `CONFIG_IPC_NS`
      + `CONFIG_UTS_NS`
      + `CONFIG_USER_NS`
      + `CONFIG_PID_NS`
    + Cgroups:
      + `CONFIG_CGROUP_DEVICE`
      + `CONFIG_CGROUPS`
      + `CONFIG_MEMCG`
    + Others:
      + `CONFIG_POSIX_MQUEUE`
      + `CONFIG_OVERLAY_FS`
      + `CONFIG_HAVE_ARCH_SECCOMP_FILTER`
      + `CONFIG_SECCOMP_FILTER`
      + `CONFIG_KEYS`
      + `CONFIG_SECCOMP`
      + `CONFIG_SHMEM`
**Tip**
Check the documentation for your Linux distribution to learn how to verify and set Linux kernel parameters. You can also use AWS IoT Device Tester for AWS IoT Greengrass to verify that your device meets these requirements. For more information, see [Using AWS IoT Device Tester for AWS IoT Greengrass V2](device-tester-for-greengrass-ug.md).

## Set up an AWS account
<a name="set-up-aws-account"></a>
