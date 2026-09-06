---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/fips-openssl-swap-provider.html
---

# Swap OpenSSL FIPS providers on AL2023
<a name="fips-openssl-swap-provider"></a>

This section explains how to switch between the `latest` and `certified` OpenSSL FIPS providers on AL2023.

For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)
+ [FedRAMP Policy for Cryptographic Module Selection and Use](https://www.fedramp.gov/rev5/fips/)

**Important**
On AL2023.7 and higher, the default OpenSSL FIPS provider is the `openssl-fips-provider-latest` package, which receives regular bugfix and security updates.
The instructions below are only for customers who want to pin to the `openssl-fips-provider-certified` package. This version of the FIPS provider will match the checksum on the NIST certificate, and may not have the latest updates.
See the [AL2023 FAQ](https://aws.amazon.com/linux/amazon-linux-2023/faqs/) for more information about FIPS certified modules and package versions.

**Prerequisites**
+ An existing AL2023 (AL2023.7 or higher) Amazon EC2 instance with access to the internet to download required packages. For more information about launching an AL2023 Amazon EC2 instance, see [Launching AL2023 using the Amazon EC2 console](ec2.md#launch-from-ec2-console).
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager. For more information, see [Connecting to AL2023 instances](connecting-to-instances.md).
+ To enable FIPS mode on AL2023, follow the instructions at [Enable FIPS Mode on AL2023](fips-mode.md).

**Switch between `openssl-fips-provider-latest` and `openssl-fips-provider-certified`**

1. Use `dnf` to switch the OpenSSL FIPS provider:

   ```
   sudo dnf -y swap openssl-fips-provider-latest openssl-fips-provider-certified
   ```

1. Check that you are using the certified OpenSSL FIPS provider. With AL2023 in FIPS mode, run the following command:

   ```
   openssl list -providers
   ```

   You should see the following output:

   ```
   Providers:
     base
       name: OpenSSL Base Provider
       version: 3.2.2
       status: active
     default
       name: OpenSSL Default Provider
       version: 3.2.2
       status: active
     fips
       name: Amazon Linux 2023 - OpenSSL FIPS Provider
       version: 3.0.8-d694bfa693b76001
       status: active
   ```
