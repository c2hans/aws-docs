---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/security-features.html
---

# Security updates and features
<a name="security-features"></a>

AL2023 provides many security updates and solutions.

**Topics**
+ [Manage updates](#manage-updates)
+ [Security in the cloud](#cloud-security)
+ [SELinux modes](#setting-selinux)
+ [Compliance program](#compliance-program)
+ [SSH server default](#ssh-server-default)
+ [Major features of OpenSSL 3](#openssl-3)

## Manage updates
<a name="manage-updates"></a>

Apply security updates using DNF and repository versions. For more information, see [Manage package and operating system updates in AL2023](managing-repos-os-updates.md).

## Security in the cloud
<a name="cloud-security"></a>

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud. For more information, see [Security and Compliance in Amazon Linux 2023](security.md).

## SELinux modes
<a name="setting-selinux"></a>

By default, SELinux is enabled and set to permissive mode in AL2023. In permissive mode, permission denials are logged but not enforced.

The SELinux policies define permissions for users, processes, programs, files, and devices. With SELinux, you can choose one of two policies. The policies are targeted or multi-level security (MLS).

For more information about SELinux modes and policy, see [Setting SELinux modes for AL2023](selinux-modes.md) and [ the SELinux Project Wiki](http://selinuxproject.org/page/Main_Page).

## Compliance program
<a name="compliance-program"></a>

Independent auditors assess the security and compliance of AL2023 along with many AWS compliance programs.

## SSH server default
<a name="ssh-server-default"></a>

AL2023 includes OpenSSH 8.7. OpenSSH 8.7 by default disables the `ssh-rsa` key exchange algorithm. For more information, see [Default SSH server configuration](ssh-host-keys-disabled.md).

## Major features of OpenSSL 3
<a name="openssl-3"></a>
+ The Certificate Management Protocol (CMP, RFC 4210) includes both CRMF (RFC 4211) and HTTP transfer (RFC 6712).
+ A HTTP or HTTPS client in libcrypto supports GET and POST actions, redirection, plain and ASN.1-encoded content, proxies, and timeouts.
+ The EVP\_KDF works with Key Derivation Functions.
+ The EVP\_MAC API works with MACs.
+ Linux Kernel TLS support.

For more information, see the [OpenSSL migration guide](https://www.openssl.org/docs/man3.0/man7/migration_guide.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
