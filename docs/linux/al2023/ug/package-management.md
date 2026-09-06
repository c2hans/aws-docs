---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/package-management.html
---

# Package management tool
<a name="package-management"></a>

The default software package management tool in AL2023 is DNF. DNF is the successor to YUM, the package management tool in AL2.

DNF is similar to YUM in its usage. Many DNF commands and command options are the same as YUM commands. In a Command Line Interface (CLI) command, in most cases `dnf` replaces `yum`.

For example, for the following AL2 `yum` commands:

```
$ sudo yum install packagename
$ sudo yum search packagename
$ sudo yum remove packagename
```

In AL2023, they become the following commands:

```
$ sudo dnf install packagename
$ sudo dnf search packagename
$ sudo dnf remove packagename
```

In AL2023 the `yum` command is still available, but as a pointer to the `dnf` command. So, when the `yum` command is used in the shell or in a script, all commands and options are the same as the DNF CLI. For more information about the differences between the YUM CLI and the DNF CLI, see [Changes in DNF CLI compared to YUM](https://dnf.readthedocs.io/en/latest/cli_vs_yum.html)﻿.

For a complete reference of commands and options for the `dnf` command, refer to the man page `man dnf`. For more information, see ﻿[DNF Command Reference](https://dnf.readthedocs.io/en/latest/command_ref.html).
