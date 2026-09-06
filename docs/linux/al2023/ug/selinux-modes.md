---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/selinux-modes.html
---

# Setting SELinux modes for AL2023
<a name="selinux-modes"></a>

By default, Security Enhanced Linux (SELinux) is `enabled` and set to `permissive` mode for AL2023. In permissive mode, permission denials are logged but not enforced. SELinux is a collection of kernel features and utilities to provide a strong, flexible, mandatory access control (MAC) architecture to the major subsystems of the kernel.

SELinux provides an enhanced mechanism to enforce the separation of information based on confidentiality and integrity requirements. This separation of information reduces threats of tampering and bypassing of application security mechanisms. It also confines damage that can be caused by malicious or flawed applications.

SELinux includes a set of sample security policy configuration files that's designed to meet everyday security goals.

For more information about SELinux features and functionality, see [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/toc.md) and [Policy Languages"](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/policy_languages.md).

**Topics**
+ [Default SELinux status and modes for AL2023](default-SELinux-modes-states.md)
+ [Change to `enforcing` mode](enforcing-mode.md)
+ [Option to disable SELinux for AL2023](disable-option-selinux.md)
