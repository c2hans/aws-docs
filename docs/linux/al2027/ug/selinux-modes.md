---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/selinux-modes.html
---

# Setting SELinux modes for AL2027
<a name="selinux-modes"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Security-Enhanced Linux (SELinux) is a collection of kernel features and user-space utilities that provide a strong, flexible mandatory access control (MAC) implementation. By default, SELinux is `enabled` and set to `enforcing` mode for AL2027. In `enforcing` mode, SELinux actively enforces the loaded security policy on the entire system.

SELinux provides an enhanced mechanism to enforce the separation of information based on confidentiality and integrity requirements. This separation of information reduces threats of tampering and bypassing of application security mechanisms. It also confines damage caused by malicious or flawed applications.

SELinux includes a set of sample security policy configuration files that are designed to meet everyday security goals.

For more information about SELinux features and functionality, see [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/toc.md) and [Policy Languages](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/policy_languages.md) on the GitHub website.

**Topics**
+ [Default SELinux status and modes for AL2027](default-SELinux-modes-states.md)
+ [Change to `permissive` mode](permissive-mode.md)
+ [Option to disable SELinux for AL2027](disable-option-selinux.md)
