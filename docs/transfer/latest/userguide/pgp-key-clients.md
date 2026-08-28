---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/pgp-key-clients.html
---

# Supported PGP clients
<a name="pgp-key-clients"></a>

The following clients have been tested with Transfer Family and can be used to generate PGP keys, and to encrypt files that you intend to decrypt with a workflow.
+ **Gpg4win \+ Kleopatra**.
**Note**
When you select **Sign / Encrypt Files**, make sure to clear the selection for **Sign as**: we do not currently support signing for encrypted files.

![The Kleopatra options for signing and encrypting files. The option for Sign as is cleared, and the option for Encrypt for me is selected.](http://docs.aws.amazon.com/transfer/latest/userguide/images/workflows-step-decrypt-kleopatra.png)

If you sign the encrypted file and attempt to upload it to a Transfer Family server with a decryption workflow, you receive the following error:

  ```
  Encrypted file with signed message unsupported
  ```
+ Major **GnuPG** versions: 2.4, 2.3, 2.2, 2.0, and 1.4.

Note that other PGP clients might work as well, but only the clients mentioned here have been tested with Transfer Family.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
