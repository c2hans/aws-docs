---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/ssh-host-key.html
---

# SSH server default configuration changes
<a name="ssh-host-key"></a>

For the AL2023 AMI, we changed the types of `sshd` host keys that we generate with the release. We also dropped some legacy key types to avoid generating them at launch time. Clients must support the `rsa-sha2-256` and `rsa-sha2-512` protocols or `ssh-ed25519` with use of an `ed25519` key. By default, `ssh-rsa` signatures are disabled.

Additionally, AL2023 configuration settings in the default `sshd_config` file contain `UseDNS=no`. This new setting means that DNS impairments are less likely to block your ability to establish `ssh` sessions with your instances. The tradeoff is that the `from={{hostname.domain}},{{hostname.domain}}` line entries in your `authorized_keys` files won't be resolved. Because `sshd` no longer attempts to resolve the DNS names, each comma separated `{{hostname.domain}}` value must be translated to a corresponding IP address.

For more information, see [Default SSH server configuration](ssh-host-keys-disabled.md).
