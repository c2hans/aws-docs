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
