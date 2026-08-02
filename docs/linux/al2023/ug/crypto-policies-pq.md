---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/crypto-policies-pq.html
---

# Enable Post-Quantum Cryptography (PQC) on AL2023
<a name="crypto-policies-pq"></a>

The system-wide cryptographic policies on AL2023 now supports post-quantum cryptography (PQC) via a new `PQ` subpolicy. After applying the PQ subpolicy, hybrid post-quantum key exchange using the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) and post-quantum digital signatures using the Module-Lattice-Based Digital Signature Standard (ML-DSA) will be enabled in the LEGACY, DEFAULT, FUTURE, or FIPS cryptographic policies.

AL2023 includes the following updated libraries with PQC support:
+ OpenSSL 3.5 added support for the ML-KEM hybrid key exchange algorithm, and ML-DSA (ML-DSA-44, ML-DSA-65, and ML-DSA-87) and SLH-DSA signature algorithms.
+ GnuTLS 3.8.10 supports ML-KEM hybrid key exchange algorithms and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.
+ NSS 3.112 introduced support for the ML-KEM hybrid key exchange algorithm and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.

**Note**
OpenSSH on AL2023 does not currently support ML-KEM hybrid key exchange algorithms.

For more information about Post-Quantum Cryptography on AWS, see:
+ [AWS Cloud Security > Post-Quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/)

**Prerequisites**
+ An existing AL2023 (AL2023.12 or higher) Amazon EC2 instance. For more information about launching an AL2023 Amazon EC2 instance, see [Launching AL2023 using the Amazon EC2 console](ec2.md#launch-from-ec2-console).
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager. For more information, see [Connecting to AL2023 instances](connecting-to-instances.md).

**Enable the `PQ` subpolicy on AL2023**

1. Ensure that the latest `crypto-policies` and `crypto-policies-scripts` packages are installed:

   ```
   sudo dnf -y install crypto-policies-scripts
   sudo dnf -y update crypto-policies crypto-policies-scripts
   ```

1. Use the `update-crypto-policies` command to enable the PQ subpolicy:

   ```
   sudo update-crypto-policies --set DEFAULT:PQ
   ```

1. It is also possible to apply the PQ subpolicy to other policies, such as the `LEGACY` or `FIPS` policies, for example:

   ```
   sudo update-crypto-policies --set FIPS:PQ
   ```

1. To check that you are using the `PQ` subpolicy, run the following command:

   ```
   update-crypto-policies --show
   ```

   For example, if you are using the `DEFAULT` policy you should see the following output:

   ```
   DEFAULT:PQ
   ```
