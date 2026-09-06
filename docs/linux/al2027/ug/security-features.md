---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security-features.html
---

# Security updates and features
<a name="security-features"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 includes several security enhancements over AL2023

**Topics**
+ [SELinux enforcing by default](#setting-selinux)
+ [Post-Quantum Cryptography (PQC) by Default](#post-quantum-cryptography)
+ [SSH server default](#ssh-server-default)
+ [Manage updates](#security-manage-updates)
+ [Security in the cloud](#cloud-security)

## SELinux enforcing by default
<a name="setting-selinux"></a>

The SELinux mandatory access control policies define permissions for users, processes, programs, files, and devices.

By default, SELinux is enabled and set to `enforcing` mode in AL2027. This means that SELinux security policy is fully enforced, in contrast with permissive mode (default in AL2023) where permission denials are logged but not enforced.

For more information about SELinux modes and policy, see [Setting SELinux modes for AL2027](selinux-modes.md) and [the SELinux Project](https://selinuxproject.github.io/).

## Post-Quantum Cryptography (PQC) by Default
<a name="post-quantum-cryptography"></a>

The system-wide cryptographic policies on AL2027 now enables post-quantum cryptography (PQC) by default.
+ **OpenSSH** enables Post-Quantum Cryptography (PQC) key exchange by default.
+ **OpenSSL 3.5** added support for the ML-KEM hybrid key exchange algorithm, and ML-DSA (ML-DSA-44, ML-DSA-65, and ML-DSA-87) and SLH-DSA signature algorithms.
+ **GnuTLS 3.8.10** supports ML-KEM hybrid key exchange algorithms and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.
+ **NSS 3.124** supports the ML-KEM hybrid key exchange algorithm and ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications.

For more information about Post-Quantum Cryptography on AWS, see: [AWS Cloud Security > Post-Quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/)

## SSH server default
<a name="ssh-server-default"></a>

AL2027 includes **OpenSSH 9.9p1**.
+ Post-Quantum Cryptography (PQC) key exchange is enabled by default
+ Additional default configurations have been added to `/etc/ssh/sshd_config.d/10-amazon-hardening.conf`
+ DSA signature algorithm support is no longer available. If you have existing DSA host keys or client keys, you must migrate to a supported key type (RSA, ECDSA, or Ed25519) before upgrading to AL2027.
+ RSA keys <2048 bits are not allowed by default

For more information, see [Default SSH server configuration](ssh-config.md).

## Manage updates
<a name="security-manage-updates"></a>

Apply security updates using DNF and repository versions. For more information, see [Manage package and operating system updates in AL2027](manage-updates.md).

## Security in the cloud
<a name="cloud-security"></a>

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud. For more information, see [Security and Compliance in AL2027](security.md).
