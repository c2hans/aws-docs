---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security-features.html
---

# Security updates and features

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 includes several security enhancements over AL2023. For the compile-time hardening flags applied to all packages, see [Compile-time hardening](compile-time-hardening.md).

**Topics**
+ [SELinux enforcing by default](#setting-selinux)
+ [Post-Quantum Cryptography (PQC) by Default](#post-quantum-cryptography)
+ [SSH server default](#ssh-server-default)
+ [Supply chain protection for package managers](#supply-chain-protection)
+ [Restricted ptrace scope by default](#ptrace-scope-default)
+ [`/var/tmp` mounted noexec by default](#var-tmp-noexec)
+ [Manage updates](#security-manage-updates)
+ [Security in the cloud](#cloud-security)

## SELinux enforcing by default
<a name="setting-selinux"></a>

The SELinux mandatory access control policies define permissions for users, processes, programs, files, and devices.

By default, SELinux is enabled and set to `enforcing` mode in AL2027. This is in contrast with `permissive` mode (default in AL2023) where permission denials are logged but not enforced.

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

## Supply chain protection for package managers
<a name="supply-chain-protection"></a>

AL2027 ships default configurations, known as dependency cooldowns, that delay the installation of recently published packages through *npm* and *pip*. Dependency cooldowns give the security community time to detect and remove malicious packages before they reach your systems.
+ **npm**: `min-release-age=1` is set in the system-wide npm configuration file `/etc/npmrc`, so `npm install` skips package versions published less than one day ago. To override, use `--min-release-age=0` or set the option in a project-level `.npmrc`. For details, see [Security best practices](nodejs-security.md).
+ **pip**: `uploaded-prior-to = P1D` is set in `/etc/pip.conf`, so `pip install` skips package versions published less than one day ago. To override, use `--uploaded-prior-to=P0D` or edit `/etc/pip.conf` directly.

For more information, see [Secure your npm and pip package updates in Amazon Linux](https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/) on the AWS Security Blog.

## Restricted ptrace scope by default
<a name="ptrace-scope-default"></a>

AL2027 restricts the scope of `ptrace` to the descendants of a process. The Yama sysctl `kernel.yama.ptrace_scope` defaults to `1`, so a process can attach only to its descendants, that is, its child processes and their children. Attaching to an unrelated process owned by the same user, or reading `/proc/{{PID}}/mem` of such a process, requires the `CAP_SYS_PTRACE` capability. The restriction limits the ability of a compromised process to read credentials and other secrets from the memory of other processes that run as the same user.

Debuggers and tracers that start the target process themselves, such as `gdb ./program` or `strace ./program`, work without changes. To attach to a process that is already running, you can run the debugger as `root`, or you can lower the ptrace scope on development and debugging instances. For the steps, see [Attach a debugger to a running process](#ptrace-scope-lower).

### Attach a debugger to a running process
<a name="ptrace-scope-lower"></a>

If you have `sudo` access, the simplest option is to run the debugger as `root`, for example `sudo gdb -p {{PID}}`. The following procedure instead lowers the ptrace scope for all users of the instance. Use it on development and debugging instances only.

**To lower the ptrace scope**

1. Check the current value.

   ```
   $ sysctl kernel.yama.ptrace_scope
   ```

   A value of `1` means that the default restriction is in place.

1. Install the opt-in package `elfutils-yama-ptrace-enable`. The package sets `kernel.yama.ptrace_scope` to `0`, and the setting persists across reboots.

   ```
   $ sudo dnf install elfutils-yama-ptrace-enable
   ```

1. Verify that the value is now `0`.

   ```
   $ sysctl kernel.yama.ptrace_scope
   ```

To lower the scope only until the next reboot, run `sudo sysctl -w kernel.yama.ptrace_scope=0` instead of installing the package. To restore the default, remove the package with `sudo dnf remove elfutils-yama-ptrace-enable` and reboot the instance.

## `/var/tmp` mounted noexec by default
<a name="var-tmp-noexec"></a>

AL2027 mounts `/var/tmp` with the `noexec` option. The `var-tmp.mount` systemd unit, provided by the `amazon-mount-config` package, bind-mounts `/var/tmp` read-write with execution disabled at boot. The option prevents an attacker from running dropped binaries from a world-writable location that persists across reboots. Inside containers, systemd skips the unit.

The option blocks the direct execution of files, including binaries and scripts that rely on a `#!` line. You can still run a script that is stored in `/var/tmp` by passing it to an interpreter.

If your programs build or unpack executables into `/var/tmp`, set `$TMPDIR` to a directory that allows execution, for example a directory in your home directory. If your workload must execute files from `/var/tmp`, you can allow execution. For the steps, see [Allow execution in `/var/tmp`](#var-tmp-exec).

To check the current mount options, run `findmnt /var/tmp`. For the layout of temporary directories, see [`/var/tmp` (larger temporary files)](filesystem-slash-var.md#filesystem-slash-var-tmp).

### Allow execution in `/var/tmp`
<a name="var-tmp-exec"></a>

**To allow execution in `/var/tmp`**

1. Mask the mount unit so that it does not mount `/var/tmp` with `noexec` at the next boot.

   ```
   $ sudo systemctl mask --now var-tmp.mount
   ```

1. Remount `/var/tmp` for the current boot.

   ```
   $ sudo mount -o remount,rw,exec,suid,dev /var/tmp
   ```

   The command uses the following mount options:
   + `rw`: keeps the directory writable. Without `rw`, the bind mount becomes read-only.
   + `exec`: allows you to run binaries from the directory.
   + `suid`: keeps set-user-ID and set-group-ID bits in effect.
   + `dev`: keeps device files in the directory usable.

1. Verify the mount options.

   ```
   $ findmnt /var/tmp
   ```

To restore the default, run `sudo systemctl unmask var-tmp.mount` and reboot the instance.

## Manage updates
<a name="security-manage-updates"></a>

Apply security updates using DNF and repository versions. For more information, see [Manage package and operating system updates in AL2027](manage-updates.md).

## Security in the cloud
<a name="cloud-security"></a>

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud. For more information, see [Security and Compliance in AL2027](security.md).
