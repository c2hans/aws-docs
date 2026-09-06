---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/crypto-policies-pq.html
---

# Post-Quantum Cryptography (PQC) on AL2027
<a name="crypto-policies-pq"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The system-wide cryptographic policies on AL2027 enable post-quantum cryptography (PQC) by default. Most users will not need to change this default configuration.

AL2027 includes the following updated libraries and applications with PQC support:
+ **OpenSSH** enables Post-Quantum Cryptography (PQC) key exchange by default.
+ **OpenSSL 3.5** added support for the ML-KEM hybrid key exchange algorithm, and ML-DSA (ML-DSA-44, ML-DSA-65, and ML-DSA-87) and SLH-DSA signature algorithms.
+ **GnuTLS 3.8.10** supports ML-KEM hybrid key exchange algorithms and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.
+ **NSS 3.124** supports the ML-KEM hybrid key exchange algorithm and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.

For more information about Post-Quantum Cryptography on AWS, see [AWS Cloud Security > Post-Quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/)

## How to disable Post-Quantum Cryptography (PQC) on AL2027
<a name="al2027-nopq"></a>

In some cases users may need to disable the use of post-quantum cryptography. The system-wide cryptographic policies provides the `NO-PQ` subpolicy to accomplish this. After applying the `NO-PQ` subpolicy, hybrid post-quantum key exchange using the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) and post-quantum digital signatures using the Module-Lattice-Based Digital Signature Standard (ML-DSA) will no longer be enabled in the LEGACY, DEFAULT, FUTURE, or FIPS cryptographic policies.

**Prerequisites**
+ An existing AL2027 Amazon EC2 instance.
+ You must connect to your Amazon EC2 instance using SSH or AWS Systems Manager.

**Enable the `NO-PQ` subpolicy on AL2027**

1. Ensure that the latest `crypto-policies` and `crypto-policies-scripts` packages are installed:

   ```
   sudo dnf -y install crypto-policies-scripts
   sudo dnf -y update crypto-policies crypto-policies-scripts
   ```

1. Use the `update-crypto-policies` command to enable the `NO-PQ` subpolicy:

   ```
   sudo update-crypto-policies --set DEFAULT:NO-PQ
   ```

1. To check that you are using the `NO-PQ` subpolicy, run the following command:

   ```
   update-crypto-policies --show
   ```

   For example, if you are using the `DEFAULT` policy you should see the following output:

   ```
   DEFAULT:NO-PQ
   ```
