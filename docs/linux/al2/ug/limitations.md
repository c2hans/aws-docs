---
source_url: https://docs.aws.amazon.com/linux/al2/ug/limitations.html
---

# AL2 Limitations
<a name="limitations"></a>

The following topics cover various limitations of AL2, and if they have been resolved in a newer version of Amazon Linux.

**Topics**
+ [`yum` cannot verify GPG signatures made with GPG subkeys](#rpm-gpg-subkeys)

## `yum` cannot verify GPG signatures made with GPG subkeys
<a name="rpm-gpg-subkeys"></a>

 The version of the `rpm` package manager in AL2 is from before `rpm` added support for verifying package signatures made with GPG subkeys. If you are creating packages to be compatible with AL2, you will need to ensure you use GPG signing keys which are compatible with the `rpm` which is part of AL2

 In order to ensure backwards compatibility for existing users, the version of `rpm` in AL2 receives only security backports.

 The version of `rpm` in AL2023 includes support for verifying package signatures made with GPG subkeys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
