---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-issues.html
---

# Troubleshoot service-managed user issues
<a name="service-managed-issues"></a>

This section describes possible solutions for issues with service-managed users.

**Topics**
+ [Troubleshoot service-managed users](#transfer-service-managed-issues)

## Troubleshoot service-managed users
<a name="transfer-service-managed-issues"></a>

This section describes possible solutions for the following issues.

**Topics**
+ [Troubleshoot public key body too long](#pgp-keys)
+ [Troubleshoot failed to add SSH public key](#ssh2-public-keys)

### Troubleshoot public key body too long
<a name="pgp-keys"></a>

**Description**

When you try to create a service-managed user, you receive the following error:

```
Failed to create user (1 validation error detected:
'sshPublicKeyBody' failed to satisfy constraint: Member must have length less than or equal to 2048)
```

**Cause**

You might be entering a PGP key for the public key body, and AWS Transfer Family does not support PGP keys for service-managed users.

**Solution**

If the PGP key is RSA-based, you can convert it to PEM format. For example, Ubuntu provides a conversion tool here: [https://manpages.ubuntu.com/manpages/jammy/en/man1/openpgp2ssh.1.html](https://manpages.ubuntu.com/manpages/jammy/en/man1/openpgp2ssh.1.html)

### Troubleshoot failed to add SSH public key
<a name="ssh2-public-keys"></a>

**Description**

When you try to add a public key for a service-managed user, you receive the following error:

```
Failed to add SSH public key (Unsupported or invalid SSH public key format)
```

**Cause**

You might be attempting to import an SSH2-formatted public key, and AWS Transfer Family does not support SSH2-formatted public keys for service-managed users.

**Solution**

You need to convert the key into OpenSSH format. This process is described in [Converting an SSH2 key to SSH public key format](convert-ssh2-public-key.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
