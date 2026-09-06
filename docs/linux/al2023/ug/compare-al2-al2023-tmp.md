---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-al2-al2023-tmp.html
---

# `/tmp` is now `tmpfs`
<a name="compare-al2-al2023-tmp"></a>

 Amazon Linux 2023 introduces changes to how `/tmp` behaves when compared to Amazon Linux 2. The default configuration for AL2 was that both `/tmp` and `/var/tmp` were on the root file system. Amazon Linux 2023 defaults to using `tmpfs` for `/tmp` with a limit of 50% of RAM and a maximum of one million inodes. These changes bring Amazon Linux in line with the behavior of other Linux distributions.

 For full details of the file system layout of AL2023, see [`/tmp`](filesystem-slash-tmp.md) and [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) in the [Filesystem Layout](filesystem.md) section.
