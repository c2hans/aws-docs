---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/windows-ssh.html
---

# Creating SSH keys on Microsoft Windows
<a name="windows-ssh"></a>

Windows includes OpenSSH as a built-in feature, which you can use to generate SSH keys in the same format as on Linux or macOS. Alternatively, you can use third-party tools like PuTTY's key generator (PuTTYgen).

## Using Windows built-in OpenSSH
<a name="windows-openssh"></a>

Recent versions of Windows include OpenSSH by default. You can use the same `ssh-keygen` commands as described in the macOS/Linux section:

1. Open Windows PowerShell or Command Prompt.

1. Run one of the following commands based on the type of key you want to generate:
   + To generate an RSA 4096-bit key pair:

     ```
     ssh-keygen -t rsa -b 4096 -f {{key_name}}
     ```
   + To generate an ECDSA 521-bit key-pair:

     ```
     ssh-keygen -t ecdsa -b 521 -f {{key_name}}
     ```
   + To generate an ED25519 key pair:

     ```
     ssh-keygen -t ed25519 -f {{key_name}}
     ```

1. Follow the same steps as in the macOS/Linux section to upload your public key to AWS Transfer Family.

## Using PuTTYgen (third-party tool)
<a name="windows-puttygen"></a>

Some third-party SSH clients for Windows, such as PuTTY, use different key formats. PuTTY uses the `PPK` format for private keys. If you're using PuTTY or related tools like WinSCP, you can use PuTTYgen to create keys in this format.

**Note**
If you present WinSCP with a private key file not in `.ppk` format, that client offers to convert the key into `.ppk` format for you.

For a tutorial about creating SSH keys by using PuTTYgen, see the [SSH.com website](https://www.ssh.com/ssh/putty/windows/puttygen).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
