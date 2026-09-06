---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/package-management-migration.html
---

# Migrating to DNF5
<a name="package-management-migration"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 replaces DNF (version 4) with DNF5. The `dnf` and `yum` commands run DNF5. AL2027 does not include DNF (version 4), and you cannot install it. AL2027 ships a compatibility layer for the common DNF (version 4) spellings. Most commands and scripts written for AL2023 run unchanged. This page lists what that layer covers, the changes that can break scripts and tools, and the steps to move.

**Topics**
+ [What does not change](#package-management-migration-unchanged)
+ [Command changes](#package-management-migration-commands)
+ [Automatic updates](#package-management-migration-automatic)
+ [Changes that can break scripts and tools](#package-management-migration-breaking)
+ [Python API](#package-management-migration-python-api)
+ [Plugins](#package-management-migration-plugins)
+ [Steps to move](#package-management-migration-steps)

## What does not change
<a name="package-management-migration-unchanged"></a>

The following AL2023 package management behaviors are unchanged in AL2027:
+ The configuration carries over. Repository definitions stay in `/etc/yum.repos.d/`, and settings you add to `/etc/dnf/dnf.conf` apply as before. The Amazon Linux defaults moved to a vendor file, so `/etc/dnf/dnf.conf` starts empty.
+ The update model is the same: versioned repositories, a locked `releasever`, and `dnf upgrade --releasever` to move between release versions. For more information, see [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md).
+ Installed-package queries with `rpm`, such as `rpm -q` and `rpm -ql`, work unchanged.
+ The AL2023 package manager configuration defaults carry over, including package signature checking being on by default and unreachable repositories being skipped rather than failing the command.

## Command changes
<a name="package-management-migration-commands"></a>

The following DNF (version 4) spellings keep working through the compatibility layer. Adopt the native DNF5 spelling when you update a script.

| DNF (version 4) command | Native DNF5 command |
| --- | --- |
| dnf erase | dnf remove |
| dnf localinstall | dnf install |
| dnf groupinstall, dnf groupremove, dnf grouplist | dnf group install, dnf group remove, dnf group list |
| dnf list installed | dnf list --installed |
| dnf whatprovides | dnf provides |
| dnf deplist | dnf repoquery --providers-of=requires |
| dnf updateinfo list | dnf advisory list |
| dnf repolist enabled | dnf repolist --enabled |
| dnf history userinstalled | dnf repoquery --userinstalled |
| dnf update-minimal | dnf upgrade-minimal |

Group names keep working. AL2027 resolves group specs by display name in addition to the group ID, so `dnf group install "Development Tools"` and `dnf install "@Development Tools"` work. The match is case-sensitive. Spell the name exactly as `dnf group list` shows it.

AL2027 also includes the `yum-utils` command-line tools, such as `repoquery` and `yumdownloader`. They run the equivalent DNF5 commands. For the full compatibility surface, see [Compatibility with AL2023 commands](package-management.md#package-management-compatibility).

## Automatic updates
<a name="package-management-migration-automatic"></a>

The `dnf5-plugin-automatic` package replaces the `dnf-automatic` tool from AL2023. Installing the `dnf-automatic` package name resolves to it, and the AL2023 timer spelling still works:

```
sudo dnf install dnf-automatic
sudo systemctl enable --now dnf-automatic.timer
```

Both the `dnf-automatic.timer` and `dnf5-automatic.timer` units run `dnf5 automatic`. Configure it in `/etc/dnf/automatic.conf`. The packaged defaults are documented in `/usr/share/dnf5/dnf5-plugins/automatic.conf`. If you carry an AL2023 `automatic.conf`, review it against the packaged defaults. DNF5 added options and removed others.

## Changes that can break scripts and tools
<a name="package-management-migration-breaking"></a>

The following changes in AL2027 can break existing scripts and tools:
+ The DNF (version 4) Python API (`python3-dnf`, imported as `import dnf`) is not available. This is the largest change. See [Python API](#package-management-migration-python-api).
+ DNF (version 4) plugins do not load. See [Plugins](#package-management-migration-plugins).
+ The package is named `dnf5`. `rpm -q dnf` reports that `dnf` is not installed. Query `dnf5` instead.
+ DNF5 has changed most exit codes from DNF (version 4). For example, a command line that DNF5 cannot parse exits with code 2, whereas DNF (version 4) returned 1 for many of these errors. If your scripts or automation check for specific exit code values, they might get unexpected results. We recommend that you treat any non-zero exit code as failure instead of testing for a specific value.
+ `dnf history` requires a subcommand and exits with an error without one. Use `dnf history list`.
+ Group name matching is case-sensitive in `dnf group install`, `dnf group remove`, `dnf group upgrade`, and `@name` specs on `dnf install`. For example, `"Development Tools"` matches and `"development tools"` does not. DNF (version 4) matched both forms. Group IDs avoid this, for example, `dnf group install development`. The `dnf group list` output shows the ID for every group, and `dnf group list` and `dnf group info` still accept name variants in any case.
+ Output text changed in places. Do not parse human-readable output. Many commands support the `--json` option, for example, `dnf advisory list --json`, `dnf repolist --json`, and `dnf list --installed --json`. When you use a custom `--queryformat`, end the format string with `\n`. DNF5 does not add the newline.
+ DNF5 logs to `/var/log/dnf5.log`. It does not write to `/var/log/dnf.log` or `/var/log/dnf.librepo.log`. Update log collection tools that read them.
+ AL2027 does not provide module streams, and the `dnf module` commands are not included.
+ A small set of DNF (version 4) commands was removed without a replacement, such as `dnf shell` and `dnf alias`. They fail with a clear error message rather than changing behavior silently.
+ `yum-config-manager --add-repo` accepts repository definition (`.repo`) files. To add a repository from a plain URL, use `dnf config-manager addrepo --id=myrepo --set=baseurl=URL` or point `--from-repofile` at a `.repo` file.

## Python API
<a name="package-management-migration-python-api"></a>

The DNF (version 4) Python API is not available in AL2027. Port scripts that use `import dnf` to the DNF5 Python bindings in the `python3-libdnf5` package. For more information, see the [DNF5 API documentation](https://dnf5.readthedocs.io/en/latest/api/index.html) on the dnf5.readthedocs.io website.

For many scripts, calling the command line and reading JSON output is the smaller change: `dnf advisory list --json`, `dnf repolist --json`, or `dnf repoquery --queryformat json`.

Configuration management tools that use the DNF (version 4) Python API are affected the same way. For Ansible, install `python3-libdnf5` on the managed node and use the `dnf5` module that comes with `ansible-core`. Both packages are in the AL2027 repositories.

## Plugins
<a name="package-management-migration-plugins"></a>

DNF (version 4) plugins do not load in DNF5. The plugin interface changed.

**Important**
A plugin that is not ported stops working silently. Commands run, exit with code 0, and print no error message while the plugin's features are missing. Check for the features you rely on.

DNF5 command plugins are configured under `/etc/dnf/dnf5-plugins` and library plugins under `/etc/dnf/libdnf5-plugins`. The `/etc/dnf/plugins` path remains as a symbolic link, so tools that write there keep working, but configuration written for DNF (version 4) plugins has no effect.

The Amazon Linux plugin commands from AL2023 are provided as native DNF5 plugins, including `dnf check-release-update` and `dnf supportinfo`.

If you maintain your own DNF (version 4) plugin, port it to the DNF5 plugin interface. The development headers ship in the `dnf5-devel` and `libdnf5-devel` packages. The upstream [Tutorial: Writing Plugins](https://dnf5.readthedocs.io/en/latest/tutorial/plugins/index.html) on the dnf5.readthedocs.io website walks through both plugin types: DNF5 command plugins and libdnf5 library plugins.

## Steps to move
<a name="package-management-migration-steps"></a>

To move your scripts and tools from AL2023 to AL2027, complete the following steps:

1. Launch the latest AL2027 preview AMI and run your scripts, tools, and services as they are. Most run unchanged. Compare the results with the same run on AL2023. For launch instructions, see [AL2027 on Amazon EC2](ec2.md).

1. Add `-y` to commands that must not prompt.

1. Treat error exit codes as zero or non-zero, not as exact values.

1. Replace output text parsing with `--json` output.

1. End custom `--queryformat` strings with `\n`.

1. Prefer group IDs in `dnf group` commands. Group names also work, but the name form is case-sensitive and names can change. IDs stay stable.

1. Point log collection at `/var/log/dnf5.log`.

1. Port code that uses `import dnf` to `python3-libdnf5`, or call the command line and read JSON output.

1. Port your own DNF (version 4) plugins to the DNF5 plugin interface.

1. Confirm the result. Run `dnf --version` and check that it reports `dnf5`.

1. If a command behaves differently than expected, see [Changes that can break scripts and tools](#package-management-migration-breaking).
