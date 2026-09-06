---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/fips-openssl-swap-provider.html
---

# Swap OpenSSL FIPS providers on AL2027
<a name="fips-openssl-swap-provider"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This section explains how to switch between the `latest` and `certified` OpenSSL FIPS providers on AL2027.

For more information about FIPS, see:
+ [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/)
+ [Compliance FAQs: Federal Information Processing Standards](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips)
+ [FedRAMP Policy for Cryptographic Module Selection and Use](https://www.fedramp.gov/rev5/fips/)

**Important**
On AL2027 the default OpenSSL FIPS provider is the `openssl-fips-provider-latest` package, which receives regular bugfix and security updates.
The instructions below are only for customers who want to pin to the `openssl-fips-provider-certified` package. This version of the FIPS provider will match the checksum on the NIST certificate, and may not have the latest updates.
See the [AL2027 FAQ](https://aws.amazon.com/linux/amazon-linux-2023/faqs/) for more information about FIPS certified modules and package versions.

**Note**
The initial version of the `openssl-fips-provider-certified` package on AL2027 contains the certified FIPS provider from AL2023 ([certificate \#5438](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5438)). See also: [Amazon Linux 2023 FAQs](https://aws.amazon.com/linux/amazon-linux-2023/faqs/)

**Prerequisites**
+ An existing AL2027 Amazon EC2 instance with access to the internet to download required packages.
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager.
+ To enable FIPS mode on AL2027, follow the instructions at [Enable FIPS Mode on AL2027](fips-mode.md).

**Switch between `openssl-fips-provider-latest` and `openssl-fips-provider-certified`**

1. Use `dnf` to switch the OpenSSL FIPS provider:

   ```
   sudo dnf -y swap openssl-fips-provider-latest openssl-fips-provider-certified
   ```

1. Check that you are using the certified OpenSSL FIPS provider. With AL2027 in FIPS mode, run the following command:

   ```
   openssl list -providers
   ```

   You should see the following output:

   ```
   Providers:
     base
       name: OpenSSL Base Provider
       version: 3.5.7
       status: active
     default
       name: OpenSSL Default Provider
       version: 3.5.7
       status: active
     fips
       name: Amazon Linux 2023 - OpenSSL FIPS Provider
       version: 3.2.2-799901ad7ab41d45
       status: active
   ```
