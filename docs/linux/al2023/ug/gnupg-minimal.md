---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/gnupg-minimal.html
---

# GNU Privacy Guard (GNUPG)
<a name="gnupg-minimal"></a>

 AL2023 separates out minimal and complete functionality for the `gnupg2` package into `gnupg2-minimal` and `gnupg2-full` packages. By default, only the `gnupg2-minimal` package is installed. This provides the minimal functionality required to verify the digital signatures on `rpm` packages.

 For more functionality from `gnupg2`, such as the ability to download keys from a key server, ensure that the `gnupg2-full` package is installed. Run the following command to swap `gnupg2-minimal` for `gnupg2-full`.

```
$ dnf swap gnupg2-minimal gnupg2-full
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
