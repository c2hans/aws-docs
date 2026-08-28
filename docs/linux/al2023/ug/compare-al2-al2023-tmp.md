---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-al2-al2023-tmp.html
---

# `/tmp` is now `tmpfs`
<a name="compare-al2-al2023-tmp"></a>

 Amazon Linux 2023 introduces changes to how `/tmp` behaves when compared to Amazon Linux 2. The default configuration for AL2 was that both `/tmp` and `/var/tmp` were on the root file system. Amazon Linux 2023 defaults to using `tmpfs` for `/tmp` with a limit of 50% of RAM and a maximum of one million inodes. These changes bring Amazon Linux in line with the behavior of other Linux distributions.

 For full details of the file system layout of AL2023, see [`/tmp`](filesystem-slash-tmp.md) and [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) in the [Filesystem Layout](filesystem.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
