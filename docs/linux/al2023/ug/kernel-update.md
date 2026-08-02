---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html
---

# Updating the Linux Kernel on AL2023
<a name="kernel-update"></a>

**Topics**
+ [Linux Kernel Versions on AL2023](#al2023-kernels)
+ [Updating AL2023 to a Newer Kernel Version](#kernelup)
+ [AL2023 kernels - Frequently Asked Questions](#al2023-kernel-faq)

## Linux Kernel Versions on AL2023
<a name="al2023-kernels"></a>

AL2023 regularly includes new kernel versions based on Long-Term Support (LTS) versions of the Linux kernel.

AL2023 was originally released in March 2023 with kernel 6.1.

In April 2025, AL2023 added support for Linux kernel 6.12. This kernel added new features including EEVDF scheduling, FUSE passthrough I/O support, a new Futex API, and improvements in eBPF. Kernel 6.12 also allows a userspace program to secure itself at runtime using user-space shadow stacks and memory sealing.

In March 2026, AL2023 added support for Linux kernel 6.18. The updated kernel 6.18 brings additional improvements in processor support, virtualization, security, and performance. Notable features include improved IOMMU capabilities across architectures and Attack Vector Controls for managing CPU vulnerability mitigations. Performance enhancements come through cryptography optimizations with faster FSCRYPT operations, memory management improvements, and the introduction of Sheaves as a new opt-in, per-CPU array-based caching layer.

## Updating AL2023 to a Newer Kernel Version
<a name="kernelup"></a>

Starting in June 2026, AL2023 will update the default kernel annually. The [`al2023-ami-kernel-default`](ec2.md#launch-via-aws-cli) set of AMIs will be updated to the latest LTS kernel, so that newly launched instances will automatically come up with the new kernel version — this is the simplest way to stay current with the latest security fixes and performance improvements.

If you prefer to choose a specific kernel version, you can run AL2023 with kernel 6.12 or 6.18 either by selecting an AMI with the desired kernel pre-installed or by upgrading an existing AL2023 EC2 instance.

### Running an AL2023 AMI with a specific kernel version
<a name="kernelup-ami"></a>

You may select to run an AL2023 AMI with a specific kernel pre-installed through the AWS Console or by querying SSM for specific parameters. The SSM keys to query start with `/aws/service/ami-amazon-linux-latest/` followed by one of

#### For kernel 6.12
<a name="kernel6.12-ami"></a>
+ `al2023-ami-kernel-6.12-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-6.12-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-6.12-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-6.12-x86_64` for x86\_64 architecture (minimal AMI)

#### For kernel 6.18
<a name="kernel6.18-ami"></a>
+ `al2023-ami-kernel-6.18-arm64` for arm64 architecture
+ `al2023-ami-minimal-kernel-6.18-arm64` for arm64 architecture (minimal AMI)
+ `al2023-ami-kernel-6.18-x86_64` for x86\_64 architecture
+ `al2023-ami-minimal-kernel-6.18-x86_64` for x86\_64 architecture (minimal AMI)

Please see [Launching AL2023 using the SSM parameter and AWS CLI](ec2.md#launch-via-aws-cli) for details on selecting AL2023 AMIs.

### Updating an AL2023 instance to a newer kernel
<a name="kernel-ipu"></a>

You can in-place upgrade a running AL2023 instance to kernel 6.12 or 6.18 with the following steps:

1. Detect current kernel and set target version:

   ```
   # Automatically detect current kernel version BEFORE upgrade
   $ CURRENT_KERNEL=$(uname -r)
   $ SOURCE_VERSION=""

   $ if [[ $CURRENT_KERNEL == *"6.12"* ]]; then
       SOURCE_VERSION="6.12"
   else
       SOURCE_VERSION=""
   fi

   # Save the source version to a persistent location for use after reboot
   $ echo "${SOURCE_VERSION}" | sudo tee /var/lib/source_kernel_version > /dev/null
   ```

   ```
   # Set your target version (change this to your desired kernel: 6.12 or 6.18)
   $ TARGET_VERSION="6.12"
   ```

   ```
   $ echo "Current kernel: ${SOURCE_VERSION:-6.1}"
   $ echo "Upgrading to kernel ${TARGET_VERSION}"
   ```

1. Install the target kernel package:

   ```
   $ sudo dnf install -y kernel${TARGET_VERSION}
   ```

1. Get the latest version of the target kernel package:

   ```
   $ version=$(rpm -q --qf '%{version}-%{release}.%{arch}\n' kernel${TARGET_VERSION} | sort -V | tail -1)
   ```

1. Make the new kernel your default kernel:

   ```
   $ sudo grubby --set-default "/boot/vmlinuz-$version"
   ```

1. Reboot your system:

   ```
   $ sudo reboot
   ```

1. Uninstall the previous kernel:

   ```
   # Read the source kernel version from the saved file
   $ SOURCE_VERSION=$(sudo cat /var/lib/source_kernel_version)

   # Uninstall the source kernel
   $ sudo dnf remove -y kernel${SOURCE_VERSION}
   ```

1. Replace extra kernel packages with their target kernel equivalents:

   ```
   # Set your target version (change this to your desired kernel: 6.12 or 6.18)
   $ TARGET_VERSION="6.12"
   ```

   ```
   $ for pkg in bpftool kernel-debuginfo kernel-debuginfo-common kernel-headers \
               kernel-modules-extra-common perf python3-perf; do
     case "$pkg" in
       kernel-*)
         src="kernel${SOURCE_VERSION}${pkg#kernel}"
         tgt="kernel${TARGET_VERSION}${pkg#kernel}" ;;
       *)
         src="${pkg}${SOURCE_VERSION}"
         tgt="${pkg}${TARGET_VERSION}" ;;
     esac
     rpm -q "$src" && sudo dnf -y swap "$src" "$tgt"
   done

   # kernel-tools and kernel-tools-devel must be removed and reinstalled
   # together due to version dependency requirements
   $ if rpm -q "kernel${SOURCE_VERSION}-tools"; then
     sudo dnf -y remove kernel${SOURCE_VERSION}-tools kernel${SOURCE_VERSION}-tools-devel
     sudo dnf -y install kernel${TARGET_VERSION}-tools kernel${TARGET_VERSION}-tools-devel
   fi
   ```

1. (Optional) Uninstall kernel-devel for previous kernel version:

   ```
   $ rpm -q kernel${SOURCE_VERSION}-devel && sudo dnf remove -y kernel${SOURCE_VERSION}-devel
   ```

### Downgrading to an earlier kernel version
<a name="kernel-downgrade"></a>

If at any point in time you need to downgrade back to an earlier kernel version, use the following steps:

1. Detect current kernel and set target version:

   ```
   # Automatically detect current kernel version BEFORE downgrade
   $ CURRENT_KERNEL=$(uname -r)
   $ SOURCE_VERSION=""

   $ if [[ $CURRENT_KERNEL == *"6.12"* ]]; then
       SOURCE_VERSION="6.12"
   elif [[ $CURRENT_KERNEL == *"6.18"* ]]; then
       SOURCE_VERSION="6.18"
   fi

   # Save the source version to a persistent location for use after reboot
   $ echo "${SOURCE_VERSION}" | sudo tee /var/lib/source_kernel_version > /dev/null
   ```

   ```
   # Set your target version (change this to your desired kernel)
   # Use "" for kernel 6.1, "6.12" for kernel 6.12
   $ TARGET_VERSION=""
   ```

   ```
   $ echo "Downgrading from kernel ${SOURCE_VERSION:-6.1} to kernel ${TARGET_VERSION:-6.1}"
   ```

1. Replace extra kernel packages with their target kernel equivalents:

   ```
   $ for pkg in bpftool kernel-debuginfo kernel-debuginfo-common kernel-headers \
               kernel-modules-extra-common python3-perf; do
     case "$pkg" in
       kernel-*)
         src="kernel${SOURCE_VERSION}${pkg#kernel}"
         tgt="kernel${TARGET_VERSION}${pkg#kernel}" ;;
       *)
         src="${pkg}${SOURCE_VERSION}"
         tgt="${pkg}${TARGET_VERSION}" ;;
     esac
     rpm -q "$src" && sudo dnf -y swap "$src" "$tgt"
   done

   # perf requires --allowerasing due to libtraceevent conflicts
   $ rpm -q "perf${SOURCE_VERSION}" && sudo dnf -y swap "perf${SOURCE_VERSION}" "perf${TARGET_VERSION}" --allowerasing

   # kernel-tools and kernel-tools-devel must be removed and reinstalled
   # together due to version dependency requirements
   $ if rpm -q "kernel${SOURCE_VERSION}-tools"; then
     sudo dnf -y remove kernel${SOURCE_VERSION}-tools kernel${SOURCE_VERSION}-tools-devel
     sudo dnf -y install kernel${TARGET_VERSION}-tools kernel${TARGET_VERSION}-tools-devel
   fi
   ```

1. Install the target kernel package:

   ```
   $ sudo dnf install -y kernel${TARGET_VERSION}
   ```

1. Get the latest version of the target kernel package:

   ```
   $ version=$(rpm -q --qf '%{version}-%{release}.%{arch}\n' kernel${TARGET_VERSION} | sort -V | tail -1)
   ```

1. Make the target kernel your default kernel:

   ```
   $ sudo grubby --set-default "/boot/vmlinuz-$version"
   ```

1. Reboot your system:

   ```
   $ sudo reboot
   ```

1. Uninstall the source kernel:

   ```
   # Read the source kernel version from the saved file
   $ SOURCE_VERSION=$(sudo cat /var/lib/source_kernel_version)

   # Uninstall the source kernel
   $ sudo dnf remove -y kernel${SOURCE_VERSION}
   ```

## AL2023 kernels - Frequently Asked Questions
<a name="al2023-kernel-faq"></a>

### 1. Do I need to reboot after a kernel update?
<a name="w2aac39c19b9b3"></a>

Every change to the running kernel requires a reboot.

### 2. How do I keep kernels up-to-date across multiple instances?
<a name="w2aac39c19b9b5"></a>

Amazon Linux does not provide facilities to manage fleets of instances. We recommend you patch large fleets using tools like [AWS Systems Manager](https://aws.amazon.com/systems-manager/).

### 3. How do I check which kernel version I am running right now?
<a name="w2aac39c19b9b7"></a>

Execute this command on your AL2023 instance:

```
$ uname -r
```

### 4. Which kernel does AL2023 recommend me to use?
<a name="w2aac39c19b9b9"></a>

It is recommended to upgrade to latest AL2023 kernel 6.18 while all the other AL2023 kernels are still supported. Customers are recommended to test their workloads before they upgrade.

### 5. Will my existing applications work with any AL2023 kernel?
<a name="w2aac39c19b9c11"></a>

AL2023 supports a newer kernel (6.12 or 6.18) the same way as kernel 6.1. Applications will work and improvements are happening under the hood. Customers should in any case test their specific workloads before switching to a newer kernel.

### 6. How do I install kernel headers, development packages, and extra modules for kernel 6.12 or 6.18?
<a name="w2aac39c19b9c13"></a>

Please run:

```
$ version=$(uname -r | grep -oP '^\d+\.\d+')
$ sudo dnf install -y kernel${version}-modules-extra-$(uname -r) kernel${version}-headers-$(uname -r) kernel${version}-devel-$(uname -r)
```

### 7. How long kernel 6.12 and 6.18 will be supported?
<a name="w2aac39c19b9c15"></a>

Kernel 6.12 and 6.18 will be supported until the planned end of life of Amazon Linux 2023, which is 2029-06-30.
