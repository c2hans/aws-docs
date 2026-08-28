---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/sshkeygen.html
---

# Generate SSH keys for service-managed users
<a name="sshkeygen"></a>

You can set up your server to authenticate users using the service managed authentication method, where usernames and SSH keys are stored within the service. The user's public SSH key is uploaded to the server as a user's property. This key is used by the server as part of a standard key-based authentication process. Each user can have multiple public SSH keys on file with an individual server. For limits on number of keys that can be stored per user, see [AWS Transfer Family endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transfer-service.html) in the *Amazon Web Services General Reference*.

As an alternative to the service managed authentication method, you can authenticate users using a custom identity provider, or AWS Directory Service for Microsoft Active Directory. For more information, see [Working with custom identity providers](custom-idp-intro.md) or [Using AWS Directory Service for Microsoft Active Directory](directory-services-users.md).

A server can only authenticate users using one method (service managed, directory service, or custom identity provider), and that method cannot be changed after the server is created.

**Topics**
+ [Creating SSH keys on macOS, Linux, or Unix](macOS-linux-unix-ssh.md)
+ [Creating SSH keys on Microsoft Windows](windows-ssh.md)
+ [Converting an SSH2 key to SSH public key format](convert-ssh2-public-key.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
