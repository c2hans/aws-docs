---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/fips-mode-container.html
---

# Enable FIPS Mode in an AL2027 Container
<a name="fips-mode-container"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This section explains how to enable Federal Information Processing Standards (FIPS) in an AL2027 container. For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)

**Note**
This section documents how to enable FIPS mode in an AL2027 container. It does not cover the certification status of AL2027 cryptographic modules.

**Prerequisites**
+ An existing AL2027 Amazon EC2 instance with access to the internet to download required packages.
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager.

**Note**
AL2027 no longer provides the `fips-mode-setup` command-line utility. FIPS mode only needs to be enabled in the container host's Linux kernel.

**Enable FIPS Mode in an AL2027 Container**

1. FIPS mode must first be enabled on the AL2027 container Host. Follow the instructions at [Enable FIPS Mode on AL2027](fips-mode.md) to enable FIPS mode on the Host.

1. Connect to your AL2027 container host instance using SSH or AWS Systems Manager.

1. FIPS mode will be automatically enabled in an AL2027 container if the AL2027 host is in FIPS mode and `/proc/sys/crypto/fips_enabled` is accessible from within the container. If the contents of `/proc/sys/crypto/fips_enabled` is `0` then FIPS is not enabled, and a value of `1` indicates that FIPS mode is enabled.

   You can verify that FIPS is enabled by running the following command on both the AL2027 host and container:

   ```
   cat /proc/sys/crypto/fips_enabled
   ```

1. Next, enable the FIPS crypto-policies within the container. There are several ways to accomplish this, described in the options below. Use the option that works best for your environment.

   1. Enable the FIPS crypto-policies manually within the container using the `update-crypto-policies` command:

      ```
      # Run these commands inside the container
      dnf install -y crypto-policies-scripts
      update-crypto-policies --set FIPS
      ```

   1. Create `bind` mounts within the AL2027 container - **note:** this option may require running the container with additional privileges to allow bind mounts (i.e. `docker run --cap-add=SYS_ADMIN ...`):

      ```
      # Run these commands inside the container
      mount --bind /usr/share/crypto-policies/back-ends/FIPS /etc/crypto-policies/back-ends
      echo "FIPS" > /usr/share/crypto-policies/default-fips-config
      mount --bind /usr/share/crypto-policies/default-fips-config /etc/crypto-policies/config
      ```

   1. It is also possible to create a bind mount so that the AL2027 container matches the AL2027 host's crypto-policies. The following is only provided as an example. This configuration could cause issues if there are incompatible differences in the crypto-policies and package versions between the container and host:

      ```
      sudo docker pull amazonlinux:2027
      sudo docker run --mount type=bind,readonly,src=/etc/crypto-policies,dst=/etc/crypto-policies -it amazonlinux:2027
      ```

1. After performing the steps above you can again verify that FIPS is enabled in the container with the following commands:

   ```
   $ cat /etc/crypto-policies/config
   FIPS

   $ cat /proc/sys/crypto/fips_enabled
   1
   ```
