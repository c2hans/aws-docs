---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/ssh-config.html
---

# Default SSH server configuration
<a name="ssh-config"></a>

If you have SSH clients from several years ago, you might see an error when you connect to an instance. If the error tells you there's no matching host key type found, update your SSH host key to troubleshoot this issue.

AL2027 includes OpenSSH 9.9 (up from 8.7 in AL2023).

**Hardened server defaults**

AL2027 ships hardened OpenSSH server defaults in the `/etc/ssh/sshd_config.d/10-amazon-hardening.conf` file, which disables root login, X11 forwarding, Kerberos authentication, and Active Directory login by default.

**Default disabling of `ssh-rsa` signatures**

AL2027 includes a default configuration that disables the legacy `ssh-rsa` host key algorithm and generates a reduced set of host keys. Clients must support the `ssh-ed25519` or the `ecdsa-sha2-nistp256` host key algorithm.

AL2027 also requires RSA keys to be at least 2048 bits.

The default configuration accepts any of these key exchange algorithms:
+ `mlkem768x25519-sha256`
+ `mlkem768nistp256-sha256`
+ `mlkem1024nistp384-sha384`
+ `curve25519-sha256`
+ `curve25519-sha256@libssh.org`
+ `ecdh-sha2-nistp256`
+ `ecdh-sha2-nistp384`
+ `ecdh-sha2-nistp521`
+ `diffie-hellman-group-exchange-sha256`
+ `diffie-hellman-group14-sha256`
+ `diffie-hellman-group16-sha512`
+ `diffie-hellman-group18-sha512`

The first three algorithms in this list are the NIST-standardized Module-Lattice Key Encapsulation Mechanism (ML-KEM) hybrid methods. AL2027 adds these post-quantum key exchange methods and prefers them ahead of the classical algorithms.

By default, AL2027 generates `ed25519` and `ECDSA` host keys. Clients support either the `ssh-ed25519` or the `ecdsa-sha2-nistp256` host key algorithm. When you connect by SSH to an instance, you must use a client that supports a compatible algorithm, such as `ssh-ed25519` or `ecdsa-sha2-nistp256`. If you need to use other key types, override the list of generated keys with a `cloud-config` fragment in user-data.

In the following example, `cloud-config` generates a `rsa` host key with the `ecdsa` and `ed25519` keys.

```
#cloud-config
 ssh_genkeytypes:
 - ed25519
 - ecdsa
 - rsa
```

If you use an RSA key pair for public key authentication, your SSH client must support a `rsa-sha2-256` or `rsa-sha2-512` signature. If you're using an incompatible client and can't upgrade, re-enable `ssh-rsa` support on your instance. To re-enable `ssh-rsa` support, activate the `LEGACY` system crypto policy using the following commands.

```
$ sudo dnf install crypto-policies-scripts
$ sudo update-crypto-policies --set LEGACY
```

DSA keys are **disabled by default**. If you have existing DSA host keys or client keys, you must migrate to a supported key type (RSA, ECDSA, or Ed25519) before upgrading to AL2027.

For more information about managing host keys, see [Module reference: SSH](https://docs.cloud-init.io/en/26.1/reference/modules.html#ssh) on the cloud-init website.
